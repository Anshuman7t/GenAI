import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from mcqgenerator.MCQGenrator import generate_evaluate_chain
from mcqgenerator.logger import logging

#loading json file
with open('Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)


#creating a title for the app
st.title("MCQs Creator Application with LangChain 🦜⛓️")