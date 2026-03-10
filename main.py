from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT

document = Document()
header = document.add_table(3,3)
header.alignment = WD_TABLE_ALIGNMENT

document.add_heading("Teste 1: Título Centralizado", 0)


document.save("neo.docx")