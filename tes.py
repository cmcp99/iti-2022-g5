from fpdf import FPDF

pdf = FPDF(orientation='L', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("helvetica", "B", 50)
while pdf.page_no() != 6:
    pdf.cell(80,10,'ola', ln=True)
pdf.output('test.pdf')