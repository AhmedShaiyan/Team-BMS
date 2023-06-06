from PyPDF2 import PdfFileReader

def read_file(file):
    with open(file, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()

        return information