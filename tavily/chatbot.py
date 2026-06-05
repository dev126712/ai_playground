from dotenv import load_dotenv
import os
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

os.environ["OPENAI_API_KEY"]==os.getenv("OPENAI_API_KEY")
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OPENAI_API_KEY:\n")

os.environ["TAVILY_API_KEY"]==os.getenv("TAVILY_API_KEY")
if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("Tavily API key:\n")

class State(TypedDict):
    # Define messages (a list type, with the add_messages function used to append messages)
    messages: Annotated[list, add_messages]

tool_search = TavilySearch(
    max_results=5,
    topic="general",
)

tool_search = [tool_search]

llm = init_chat_model(model="gpt-5.4", model_provider="openai", temperature=0)

llm_with_tools = llm.bind_tools(tool_search)

# Define the chatbot function
def chatbot(state: State):
    # Invoke messages and return the result
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


# Create the graph
graph_builder = StateGraph(State)
# Add a node by specifying its name and the associated function or callable object
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tool_search))
# Add an edge from the start node to the chatbot node
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
# Compile the graph
graph = graph_builder.compile()

question = "Recommend the top 10 famous restaurants in New York"

# Stream the graph execution exactly like your original script
for event in graph.stream({"messages": [("user", question)]}, stream_mode="values"):
    event["messages"][-1].pretty_print()
