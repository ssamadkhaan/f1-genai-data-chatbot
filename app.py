import streamlit as st
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

drivers = pd.read_csv("data/drivers.csv")
constructors = pd.read_csv("data/constructors.csv")
races = pd.read_csv("data/races.csv")


st.title("🏎️ F1 GenAI Chatbot")

question = st.text_input(
    "Ask an F1 Question"
)

if question:

    prompt = f"""
    You are an F1 expert.

    Question:
    {question}

    Drivers Dataset:
    {drivers.head(20)}

    Constructors Dataset:
    {constructors.head(20)}

    Races Dataset:
    {races.head(20)}

    Answer professionally.
    """

    response = model.generate_content(
        prompt
    )

    st.write(response.text)