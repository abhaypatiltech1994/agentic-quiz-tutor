import os
from dotenv import load_dotenv
from typing import Annotated, TypedDict
#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
import streamlit as st

from tools import get_question, check_answer

load_dotenv()

# --- Step 5a: Turn our plain functions into LangChain "tools" ---
@tool
def get_question_tool(topic: str = "") -> str:
    """Fetch a new quiz question. Optionally pass a topic keyword like 'Azure' or 'DI'."""
    return get_question(topic)

@tool
def check_answer_tool(user_answer: str) -> str:
    """Check the user's submitted answer against the last question asked."""
    return check_answer(user_answer)

tools = [get_question_tool, check_answer_tool]

# --- Step 5b: Define the graph's "state" ---
class State(TypedDict):
    messages: Annotated[list, add_messages]

# --- Step 5c: Set up the LLM and bind tools to it ---
groq_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
llm = ChatGroq(model="openai/gpt-oss-20b", groq_api_key=groq_key)

llm_with_tools = llm.bind_tools(tools)

# --- Step 5d: Define the "brain" node ---
def chatbot_node(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# --- Step 5e: Build the graph ---
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot_node)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.set_entry_point("chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")

graph = graph_builder.compile()

# --- Step 5f: Simple command-line chat loop ---
if __name__ == "__main__":
    print("Quiz Tutor Agent ready. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
        print("Agent:", result["messages"][-1].content, "\n")