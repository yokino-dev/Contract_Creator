from docx import Document

document = Document()

document.add_heading("Titulo Marinho da silva", 0)


document.save("neo.docx")