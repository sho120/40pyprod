from tkinter.ttk import Style
import docx
from docx.oxml.ns import qn
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

doc = docx.Document(r'Chapter4\main12\certificate.docx')

style = doc.styles['Normal']
style.font.name = '나눔고딕'
style._element.rPr.rFonts.set(qn('w:eastAsia'),'나눔고딕')
style.font.size = docx.shred.Pt(12)
