from fastapi import FastAPI
from fastapi.responses import FileResponse
from fpdf import FPDF
import os

app = FastAPI()

@app.get("/create")
def createFile():
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", "B", 140)
    for i in range(0,20):
        pdf.cell(0, 150, "Hello World!", ln=True, align='C')
    i = int(lastFile()) + 1
    pdf.output(str(i) + ".pdf") 
    return "Ficheiro criado com sucesso!"

# procura id do ultimo ficheiro adicionado
def lastFile():
    files = []
    for i in os.listdir():
            if i.endswith('.pdf'):
                files.append(i)
    return files[-1].replace('.pdf', '')

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
