from fastapi import FastAPI
from fastapi.responses import FileResponse
from fpdf import FPDF
from nacl.signing import SigningKey
import os
import shutil
import time

app = FastAPI()
signing_key = SigningKey.generate()

# Eliminar ficheiros .pdf
@app.on_event("startup")
def start_up():
    for i in os.listdir():
        if i.endswith('.pdf'):
            os.remove(i)

@app.get("/create/{word}")
def createFile(word: str):
    signed = signing_key.sign(bytes(word, 'utf-8'))
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", "B", 140)
    for i in range(0,20):
        pdf.cell(0, 150, str(signed), ln=True, align='C')
    i = int(lastFile()) + 1
    pdf.output(str(i) + ".pdf")
    return "Ficheiro criado com sucesso!"

@app.get("/createdouble/{word}/{pages}")
def createFile(word: str, pages: int):
    signed = signing_key.sign(bytes(word, 'utf-8'))
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", "B", 140)
    for i in range(0, pages):
        pdf.cell(0, 150, str(signed), ln=True, align='C')
    i = int(lastFile()) + 1
    pdf.output(str(i) + ".pdf")
    return "Ficheiro criado com sucesso!"

# procura id do ultimo ficheiro adicionado
def lastFile():
    files = []
    for i in os.listdir():
        if i.endswith('.pdf'):
            files.append(int(i.replace('.pdf', '')))
    files.sort()
    if files == []:
        return 0
    else:
        return files[-1]

@app.get("/files")
def getFiles():
    files=[]
    for i in os.listdir():
        if i.endswith('.pdf'):
            files.append(i)
    return files

@app.get("/file/{name}")
def sendFile(name: str):
    return FileResponse(name)
    
