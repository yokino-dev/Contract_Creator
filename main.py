from docx import Document
from docx.shared import Inches

document = Document()


document.add_heading("Titulo Centralizado", 0)
p = document.add_paragraph("Teste de Paragrafo: 1")

p.add_run("Teste de Paragrafo: 2").italic = True
document.add_picture("goku.png", width=Inches(1.25))

document.save("neo.docx")