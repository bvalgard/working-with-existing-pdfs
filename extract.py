from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import re

# Create pdf file reader object
pdf = PdfFileReader('lorem.pdf')

# TWO STEPS TO EXTRACT TEXT 
# Step 1: Grab the Page(s)
page_1_object = pdf.getPage(0)

# Step 2: Extract Text
page_1_text = page_1_object.extractText()

# Combine the text from all the pages and save as txt file
with Path('lorem_text.txt').open(mode='w') as output_file:
    text = ''
    for page in pdf.pages:
        text += page.extractText()
    output_file.write(text)

# Where's Waldo?
waldo_pages = []
for page in pdf.pages:
    page_num = page['/StructParents'] # if yo uwant to see the actual page number +1
    page_text = page.extractText()

    if 'Waldo' in page_text: # page_text.find('Waldo') for index position of Waldo
        waldo_pages.append(page_num)

# Save Waldo pages to pdf

# create PdfFileReader object
input_pdf = PdfFileReader('lorem.pdf')

# create PdfFilerWriter object
pdf_writer = PdfFileWriter()

# Get the Text from Pages with Waldo
for page in waldo_pages:
    page_object = input_pdf.getPage(page)
    pdf_writer.addPage(page_object)

# Save Pages as PDF
with Path('waldo_pages.pdf').open(mode='wb') as output_file_2:
    pdf_writer.write(output_file_2)

# Where's Waldo - Get Sentence & Page Number
pages_sentences = []
for page in pdf.pages:
    page_num = page['/StructParents'] # if yo uwant to see the actual page number +1
    page_text = page.extractText()

    if 'Waldo' in page_text: # page_text.find('Waldo') for index position of Waldo
        sentence_list = ['page ' + str(page_num) + ': ' + sentence.replace('\n', '') for sentence in re.split('\.\W+|\?\W+|\!\W+', page_text) if 'Waldo' in sentence][0]
        pages_sentences.append(sentence_list)

text = '\n'.join(pages_sentences)

# cannot create new pdf from scratch (could use fpdf2 if need pdf)
with Path('waldo_sentences_pages.text').open(mode='w') as output_file_3:
    output_file_3.write(text)