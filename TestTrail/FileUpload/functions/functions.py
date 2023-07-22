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


    return connection

def retrieve_job_listings(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT job, skills FROM joblistings")
    job_listings = cursor.fetchall()
    cursor.close()
    return job_listings

def calculate_cosine_similarity(skills, job_listings):
    skill_set = set(skills)
    similarities = []
    
    for job_title, job_skills in job_listings:
        job_skill_set = set(job_skills)
        common_skills = skill_set.intersection(job_skill_set)
        
        # Calculate the cosine similarity
        similarity = len(common_skills) / (np.sqrt(len(skill_set)) * np.sqrt(len(job_skill_set)))
        similarities.append((job_title, similarity))
    
    return similarities
