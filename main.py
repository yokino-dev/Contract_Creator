from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT

document = Document()


document.add_heading("Titulo Centralizado", 0)
p = document.add_paragraph("Teste de Paragrafo: 1    ")

p.add_run("Teste de Paragrafo: 2").italic = True


document.save("neo.docx")