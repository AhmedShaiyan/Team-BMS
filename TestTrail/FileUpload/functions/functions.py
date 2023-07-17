import openai
from pdfminer.high_level import extract_text
import json
import psycopg2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from FileUpload.models import Document
import environ

env = environ.Env()
environ.Env.read_env()

with open('FileUpload/functions/OpenAI.txt') as f:
    openai.api_key = f.read().strip()

def identify_skills():
    lastFile = Document.objects.last()
    lastFilePath = lastFile.filepath
    text = extract_text('media/'+str(lastFilePath))

    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role':'system','content':"Return a python list of the top 10 skills identified in the following resume, summarising them in up to 3 words each: " + text}],
        max_tokens = 1000,
        n = 3,
        stop = None,
        temperature = 0.3,
    )
    
    output = completion['choices'][0]['message']['content']

    return output

def connect_to_database():
    connection = psycopg2.connect(
        database=env('DBNAME'),
        user=env('DBUSER'),
        password=env('DBPASS'),
        host=env('DBHOST'),
        port=env('DBPORT')
    )