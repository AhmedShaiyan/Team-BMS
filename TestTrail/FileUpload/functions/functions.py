import openai
from pdfminer.high_level import extract_text
import json
import psycopg2
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix, coo_matrix
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
        messages = [{'role':'system','content':"Return a Python list of the top 10 skills identified in the following resume, summarising them in up to 3 words each: " + text}],
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

def fetchjoblistings():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute('SELECT * FROM joblistings;')
    temp_list = cur.fetchall()
    cur.close()

    df = pd.DataFrame(temp_list,columns=('job','skills'))
    
    return df

def calculate_cosine_similarity():
    
    df = fetchjoblistings()
    
    #change to append skill output to end
    df.loc[len(df)] = ['Test',"['Detail-oriented', 'Six Sigma Black Belt', 'Manufacturing internships', 'Efficiency improvement', 'Cost reduction', 'Setup reduction', 'Kanban implementation', 'Mechanical engineering', 'MATLAB, AutoCAD, SolidWorks', 'CNC, Lathes']"]
    
    tv = TfidfVectorizer()
    tfidf_matrix = tv.fit_transform(df['skills'])

    A_sparse = csr_matrix(tfidf_matrix)
    similarities_sparse = cosine_similarity(A_sparse, dense_output = True)
    table_len = len(similarities_sparse)
    similarity_list = []

    for i in range(len(similarities_sparse[table_len-1])):
        similarity_list.append(similarities_sparse[table_len-1][i])
    
    del similarity_list[-1]
    sim_list_copy = similarity_list.copy()

    index_list = []

    for j in range(5):
        i = sim_list_copy.index(max(sim_list_copy))
        index_list.append(i)
        del sim_list_copy[i]

    job_rec = []

    for item in index_list:
        job_rec.append(df['job'][item])

    return job_rec

