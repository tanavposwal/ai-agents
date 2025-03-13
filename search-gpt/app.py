import streamlit as st
from utils import apply_styles
from agent import search_agent

st.title("Deep search with Llama")

if st.button("💬 New Chat"):
    st.session_state.messages = []
    st.rerun()

apply_styles()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            msg = search_agent.run(prompt)
            response = st.markdown(
                msg.content,
                unsafe_allow_html=True,
            )
    st.session_state.messages.append({"role": "assistant", "content": response})
