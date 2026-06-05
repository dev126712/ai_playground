# Multi-Server MCP Agent with LangChain & Groq

This project demonstrates how to build an AI agent using LangChain, LangGraph, and ChatGroq that seamlessly communicates with multiple Model Context Protocol (MCP) servers. It highlights the use of two different MCP transport mechanisms simultaneously: standard input/output (`stdio`) and HTTP (`streamable-http`).

## Features

* **Multi-Server Integration**: Connects to multiple disparate MCP tool providers.
* **Math Server Transport**: Uses `stdio` (runs as a subprocess).
* **Weather Server Transport**: Uses HTTP (`streamable-http`).
* **Agentic Routing**: Utilizes a LangGraph ReAct agent powered by Groq (`qwen/qwen3-32b`) to dynamically decide which tools to call based on user queries.

## Project Structure

* `client.py`: The main LangGraph React agent client. It connects to the MCP servers, fetches their tools, and processes user queries.
* `mathserver.py`: A local MCP server (`FastMCP`) that provides basic mathematical operations (`add` and `multiply`).
* `weather.py`: A local MCP server (`FastMCP`) that provides mock weather information.
* `main.py`: A minimal entry point / sanity check script.
* `requirements.txt`: Python package dependencies.

## Prerequisites

* **Python 3.8+**
* **Groq API Key**: You need an active API key from Groq to power the LLM agent.

## Installation

1. Clone or download the project files into a directory.
2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
