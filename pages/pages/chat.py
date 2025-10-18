import streamlit as st

st.title("💬 Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message("user").write(msg)

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append(prompt)
    st.chat_message("user").write(prompt)
