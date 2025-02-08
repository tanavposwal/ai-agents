from langchain_google_genai import GoogleGenerativeAI
from constants import GOOGLE_API_KEY
import streamlit as st


llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY, temperature=0.6
)
st.title("LangChain Demo")

input_text = st.text_input("Search the topic u want")

if input_text:
    st.write(llm.predict(input_text))
