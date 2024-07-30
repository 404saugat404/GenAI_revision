import streamlit as st
from mcq.quiz.logger import logging
from mcq.quiz.utils import read_file, get_table_data
import json
import traceback
from langchain.callbacks import get_openai_callback
from mcq.quiz.mcq_main import final_chain

from dotenv import load_dotenv


#loading json file:
with open('/home/saugat/Desktop/GenAI/mcq_generation_using_genAI/RESPONSE.json', "r") as file:
    RESPONSE_JSON=json.load(file)

st.title('MCQ GENERATOR')

#CREATING FORM USING st.form

with st.form('user input'):
    file_upload=st.file_uploader("upload your file here: ")

    mcq_count=st.number_input("input number of mcq you want: ", min_value=3, max_value=20)

    topic=st.text_input("input the topic on which you want to generate mcq: " , max_chars=20)

    difficulty=st.text_input('input the difficulty level: ', max_chars=20,placeholder="simple" )

    button=st.form_submit_button('click to submit: ')



