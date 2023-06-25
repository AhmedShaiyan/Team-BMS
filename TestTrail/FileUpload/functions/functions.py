import openai
from pdfminer.high_level import extract_text
import json
from FileUpload.models import Document

with open('FileUpload/functions/OpenAI.txt') as f:
    openai.api_key = f.read().strip()

def identify_skills():
    lastFile = Document.objects.last()
    lastFilePath = lastFile.filepath
    text = extract_text('media/'+str(lastFilePath))

    completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role':'system','content':"Return a python list of the skills identified in the following resume: " + text}],
        max_tokens = 1000,
        n = 3,
        stop = None,
        temperature = 0.3,
    )
    
    output = completion['choices'][0]['message']['content']

    return output