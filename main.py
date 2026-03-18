from docx import Document # classe principal para criação de Documento Word
from docx.shared import Pt, Cm # Unidade de medida como (PT = tamanho da fonte) Cm = (Tamanho das margens)
from docx.enum.text import WD_ALIGN_PARAGRAPH # Alinhamento de texto (Centro, esquerda, direita)

document = Document()

# Setor de Margin do espaçamento da folha

section = document.sections[0]
section.top_margin = Cm(2)
section.bottom_margin = Cm(2)
section.left_margin = Cm(2.5)
section.right_margin = Cm(2.5)

# Setor de Margin do espaçamento da folha


document.save("neo1.docx")