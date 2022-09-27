from aiohttp import web
from fpdf import FPDF
from PyPDF2 import PdfFileReader
import os


async def form(request):
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", "B", 140)
    for i in range(0,20):
        pdf.cell(0, 150, "Hello World!", ln=True, align='C')
    i = int(lastFile()) + 1
    pdf.output(str(i) + ".pdf") 
    return web.Response(text="Ficheiro criado!")

async def getFiles(request):
    files=''
    for i in os.listdir():
        if i.endswith('.pdf'):
            files += i + ", "
    return web.Response(text=files)

def lastFile():
    files = []
    for i in os.listdir():
            if i.endswith('.pdf'):
                files.append(i)
    return files[-1].replace('.pdf', '')   

from aiohttp import web
from aiohttp import streamer
@streamer
async def file_sender(writer, file_path=None):
    """
    This function will read large file chunk by chunk and send it through HTTP
    without reading them into memory
    """
    with open(file_path, 'rb') as f:
        chunk = f.read(2 ** 16)
        while chunk:
            await writer.write(chunk)
            chunk = f.read(2 ** 16)

async def showFile(request):
    file_name = request.match_info['demofile2.txt']  # Could be a HUGE file
    headers = {
        "Content-disposition": "attachment; filename={file_name}".format(file_name=file_name)
    }

    file_path = os.path.join('data', file_name)

    if not os.path.exists(file_path):
        return web.Response(
            body='File <{file_name}> does not exist'.format(file_name=file_name),
            status=404
        )

    return web.Response(
        body=file_sender(file_path=file_path),
        headers=headers
    )

app = web.Application()

app.add_routes([web.get('/criar', form), web.get('/files', getFiles), web.get('/file', showFile), web.get('/file/{file_name}', showFile)])

web.run_app(app)