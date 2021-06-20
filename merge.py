# https://realpython.com/creating-modifying-pdf/#using-the-pdffilewriter-class
# https://pythonhosted.org/PyPDF2/PdfFileMerger.html
# https://automatetheboringstuff.com/chapter13/

# pip install PyPDF2

# Append (concatenate) vs. Merge
# .append() - add pdf 2 to end of pdf 1
# .merge() - instert pdf 2 at specific location of pdf 1
# merge a select page(s) from one into another

from PyPDF2 import PdfFileMerger
from os import path, listdir

##################
##### Append #####
##################

# Step 1: Create PdfFileMerger Object
pdf_merger = PdfFileMerger()

# Step 2: append pdf's to merger
pdf_merger.append('pdf_1.pdf')
pdf_merger.append('pdf_2.pdf')

# Step 3: Write to File
# from os import path
# save to new folder so we are not merging our new merges
with open(path.abspath('merged_pdfs/append_1_2.pdf'), 'wb') as append_pdf:
    pdf_merger.write(append_pdf)

# Appending many pdfs
# from os import listdir
# get all pdf files in folder
# create new PdfFileMerger or overwrite
pdf_merger2 = PdfFileMerger()

files = [f for f in listdir('.') if path.isfile(f) and f.endswith('.pdf')]

for pdf in all_pdfs:
    pdf_merger2.append(pdf)

with open(path.abspath('merged_pdfs/append_all.pdf'), 'wb') as append_all_pdfs:
    pdf_merger2.write(append_all_pdfs)


#################
##### Merge #####
#################

# Step 1: Create PdfFileMerger Object
pdf_merger3 = PdfFileMerger()

# Step 2: Add pdf
pdf_merger3.append('pdf_1.pdf')

# Step 3: indicate index position of where to
# to insert the other pdf (Index position will
# will be the index position of first page of 2nd pdf)
# the entire 2nd pdf will be inserted and then the rest
# of the firstr pdf will be inserted
pdf_merger3.merge(2, 'pdf_2.pdf')

# Step 4: Write to PDF
with open(path.abspath('merged_pdfs/merge.pdf'), 'wb') as merge_pdfs:
    pdf_merger3.write(merge_pdfs)

#### Merge a portion of 1 pdf with another ####
pdf_merger4 = PdfFileMerger()
pdf_merger4.append('pdf_1.pdf')
pdf_merger4.merge(2, 'pdf_3.pdf', pages=(2,3)) # start, stop, step

with open(path.abspath('merged_pdfs/merge_slice_of.pdf'), 'wb') as merge_slice_of_pdfs:
    pdf_merger4.write(merge_slice_of_pdfs)
