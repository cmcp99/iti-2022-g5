from fastapi import FastAPI
from fastapi.responses import FileResponse
from fpdf import FPDF
from nacl.signing import SigningKey
import os
import time

""" mkdir /mnt/mountedshare
mount -t drvfs '\\servername\sharename' /mnt/mountedshare """

#linux /mnt/mountedshare/
#windows //192.168.1.36/Servidor/

dir = '//192.168.6.211/Servidor/' 
app = FastAPI()
signing_key = SigningKey.generate()

# Eliminar ficheiros .pdf ao iniciar o servidor
@app.on_event("startup")
def start_up():
    for i in os.listdir(dir):
        if i.endswith('.pdf'):
            os.remove(dir + i)

#MUDAR PARA POST
@app.get("/create/{word}")
def createFile(word: str):
    a = time.time()
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", "B", 45)
    while pdf.page_no() != 100:
        signed = signing_key.sign(bytes(word, 'utf-8'))
        pdf.cell(80, 10, str(signed), ln=True, align='C')
    b = time.time()
    print('Tempo para preencher PDF: ', b-a)
    c = time.time()
    i = int(lastFile()) + 1
    pdf.output(dir + str(i) + ".pdf")
    d = time.time()
    print('Tempo para escrita no disco: ', d-c)
    return "Ficheiro criado com sucesso!"

@app.post("/createn/{word}/{pages}")
def createFile(word: str, pages: int):
    a = time.time()
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", "B", 45)
    while pdf.page_no() != pages:
        signed = signing_key.sign(bytes(word, 'utf-8'))
        pdf.cell(80, 10, str(signed), ln=True, align='C')
    b = time.time()
    print('Tempo para preencher PDF: ', b-a)
    c = time.time()
    i = int(lastFile()) + 1
    pdf.output(dir + str(i) + ".pdf")
    d = time.time()
    print('Tempo para escrita no disco: ', d-c)
    return "Ficheiro criado com sucesso!"

# procura id do ultimo ficheiro adicionado
def lastFile():
    files = []
    for i in os.listdir(dir):
        if i.endswith('.pdf'):
            files.append(int(i.replace('.pdf', '')))
    files.sort()
    if files == []:
        return 0
    else:
        return files[-1]

@app.get("/files")
def getFiles():
    a = time.time()
    files=[]
    for i in os.listdir(dir):
        if i.endswith('.pdf'):
            files.append(i)
    b = time.time()
    print('Tempo de acesso a todos os ficheiros no disco: ', b-a)
    return files

@app.get("/file/{name}")
def sendFile(name: str):
    a = time.time()
    b = FileResponse(dir + name)
    c = time.time()
    print('Tempo de leitura do ficheiro no disco: ', c-a)
    return b
    
