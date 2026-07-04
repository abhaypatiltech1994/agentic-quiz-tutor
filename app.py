import streamlit as st
from langchain_core.messages import HumanMessage
from agent import graph

st.title("🧠 Agentic Quiz Tutor")
st.caption("Built with LangGraph + Groq — the agent decides which tool to call")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask for a quiz question, or submit your answer...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
    reply = result["messages"][-1].content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)