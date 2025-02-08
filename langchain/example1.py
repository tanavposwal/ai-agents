from langchain_google_genai import GoogleGenerativeAI
from constants import GOOGLE_API_KEY
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY, temperature=0.6
)
st.title("Celeb Search")

person_memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")
dob_memory = ConversationBufferMemory(input_key="person", memory_key="chat_history")
events_memory = ConversationBufferMemory(
    input_key="dob", memory_key="discription_history"
)

# prompt template
first_input_prompt = PromptTemplate(
    input_variables=["name"],
    template="Tell, me about celebrity {name} in paragraph and all majors details",
)

chain = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key="person",
    memory=person_memory,
)

second_input_prompt = PromptTemplate(
    input_variables=["person"],
    template="when was {person} born?",
)

chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key="dob",
    memory=dob_memory,
)

third_input_prompt = PromptTemplate(
    input_variables=["dob"],
    template="Mention 5 major events that happened aroudn {dob} in the world?",
)

chain3 = LLMChain(
    llm=llm,
    prompt=third_input_prompt,
    verbose=True,
    output_key="events",
    memory=events_memory,
)

parentchain = SequentialChain(
    chains=[chain, chain2, chain3],
    verbose=True,
    input_variables=["name"],
    output_variables=["person", "dob", "events"],
)

input_text = st.text_input("Search the topic u want")

if input_text:
    st.write(parentchain({"name": input_text}))

    with st.expander("Person Name"):
        st.info(person_memory.buffer)

    with st.expander("Major Events"):
        st.info(events_memory.buffer)
