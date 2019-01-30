from docx import Document
document = Document()

document.add_paragraph('Add some text')
document.save('book test.docx')