from PyPDF2 import PdfFileReader
import openai

with open('functions/OpenAI.txt') as f:
    openai.api_key = f.read().strip()

def read_file(file):
    with open(file, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()

        return information