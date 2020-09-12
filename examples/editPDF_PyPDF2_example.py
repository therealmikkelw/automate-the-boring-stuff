import PyPDF2

# Using xxx for page level editing of PDF files
# Note that PyPDF2 module cannot write text to a pdf


# Using pythons built-in open() method to read binary pdf files
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

# Parse binary to reader object using PyPDF2 module
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

# Creating a writer object (a pdf file, still not stored on disk)
writer = PyPDF2.PdfFileWriter()

# Run through first pdf file, page by page, and add each page to the writer object
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

# Save writer object to disk (PDF file)
outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)

outputFile.close()
pdf1File.close()
pdf2File.close()
