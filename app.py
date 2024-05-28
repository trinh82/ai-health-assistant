# Import libraries
import streamlit as st
from  phi.assistant import Assistant 
from phi.llm.ollama import Ollama

# create an UI interface
st.title("AI Health Assistant")
st.caption("Chat with your AI assistant about health and fitness-related topics.")

# create and initialize the AI assistant
assistant = Assistant(
    llm = Ollama(model="llama2:latest"),
    description="You are an AI assistant. You help people with their health and fitness goals.",
    markdown=True,
    debug_mode=True
)

# Chat with Research papers
query = st.text_input("Enter your question:",type="default")
if query:
    response = assistant.run(query,stream=False)
    st.write(response)