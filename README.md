# AI Playground

Hands-on experiments with AI agents, MCP (Model Context Protocol), and agentic frameworks.

[![Python](https://skillicons.dev/icons?i=py)](https://skillicons.dev)

---

## Projects

### MCP Multi-Server Agent (`mcp-tools/`)

A LangGraph ReAct agent that connects to **two MCP servers simultaneously using different transport protocols** — demonstrating real-world MCP client/server architecture.

```
User query
     │
     ▼
LangGraph ReAct Agent (Groq — qwen3-32b)
     │
     ├──── stdio transport ────▶ Math MCP Server (FastMCP)
     │                           add, multiply tools
     │
     └──── HTTP streamable ────▶ Weather MCP Server (FastMCP)
                                  get_weather tool
```

| Component | Detail |
|---|---|
| **Agent** | LangGraph ReAct loop — dynamically routes to the right tool |
| **LLM** | Groq `qwen/qwen3-32b` |
| **MCP transports** | `stdio` (subprocess) + `streamable-http` (HTTP) simultaneously |
| **MCP framework** | FastMCP for server definitions |
| **Tool discovery** | Agent fetches available tools from each server at startup |

**Why it matters:** MCP (Model Context Protocol) is the emerging standard for connecting AI agents to external tools and data sources. This project shows how to build both the client (agent) and the server (tool provider) side of an MCP integration.

```bash
cd mcp-tools
pip install -r requirements.txt
export GROQ_API_KEY=your_key
python client.py
```

---

### Tavily Search Agent (`tavily/`)

A conversational LangGraph agent that routes to **Tavily web search** when it needs real-time information — otherwise answers from LLM knowledge.

| Component | Detail |
|---|---|
| **Agent** | LangGraph graph with conditional routing |
| **Search** | Tavily API (real-time web search) |
| **LLM** | OpenAI |

```bash
cd tavily
uv sync
export OPENAI_API_KEY=your_key TAVILY_API_KEY=your_key
python chatbot.py
```

---

## Skills Demonstrated

- **MCP architecture** — building both MCP clients and servers, multi-transport connections
- **LangGraph** — ReAct agent loop, conditional graph routing
- **Groq / OpenAI** — LLM integration
- **Agentic tool use** — dynamic tool discovery and invocation
