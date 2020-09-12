import PyPDF2

# Using pythons built-in open() method to read binary pdf file
pdfFile = open('meetingminutes1.pdf', 'rb')

# Parse binary to reader object using PyPDF2 module
reader = PyPDF2.PdfFileReader(pdfFile)
print('The PDF file has ' + str(reader.numPages) + ' pages')

# Using getPage() method to extract a specific page and store in page object
page = reader.getPage(0)
print(page.extractText())

# Using for loop to print entire document
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

pdfFile.close()
