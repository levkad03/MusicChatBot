import streamlit as st

from src.agent import agent

st.set_page_config(page_title="🎵 MusicBot", page_icon="🎶")
st.title("🎶 MusicBot – Ask Me Anything About Music")


# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
user_input = st.chat_input("Ask about an artist, lyrics, or song history...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Run LangChain agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = agent.run(user_input)
            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
