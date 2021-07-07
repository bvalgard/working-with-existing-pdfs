# Resources
# https://pythonhosted.org/PyPDF2/PdfFileWriter.html
# https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_archives/PDFReference.pdf

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import RectangleObject
from os import path

pdf_writer = PdfFileWriter()
pdf_reader = PdfFileReader(open('append_all.pdf','rb'))

# get page dimensions
x1, y1, x2, y2 = pdf_reader.getPage(0).mediaBox
print(f'x1, x2: {x1, x2}\ny1, y2: {y1,y2}')

# add each page in pdf to pdf writer
num_of_pages = pdf_reader.getNumPages()

for page in range(num_of_pages):
    current_page = pdf_reader.getPage(page)
    pdf_writer.addPage(current_page)

# Add Link
pdf_writer.addLink(
    pagenum=0, # index of the page on which to place the link
    pagedest=8, # index of the page to which the link should go
    rect=RectangleObject([20,550,300,700]), # clickable area x1, y1, x2, y2 (starts bottom left corner)
    # border
    # fit 
)

with open(path.abspath('pdf_with_link.pdf'), 'wb') as link_pdf:
    pdf_writer.write(link_pdf)



