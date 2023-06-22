import openai
from pdfminer.high_level import extract_text
import json

#with open('OpenAI.txt') as f:
#    openai.api_key = f.read().strip()

def read_file(file):
    with open(file, 'rb') as f:
        information = extract_text(f)

        return information

def identify_skills(information):
    response = openai.Completion.create(
        model = 'gpt-3.5-turbo',
        prompt = information,
        max_tokens = 50,
        n = 5,
        stop = None,
        temperature = 0.5,
    )

    skills = []
    for choice in response.choices:
        skills.append(choice.text.strip())
    
    return skills