from docx import Document
from docx.shared import Inches

document = Document()

# Setor de Margin do espaçamento da folha

section = document.sections[0]
section.top_margin = Cm(2)
section.bottom_margin = Cm(2)
section.left_margin = Cm(2.5)
section.right_margin = Cm(2.5)

# Setor de Margin do espaçamento da folha


document.save("neo1.docx")