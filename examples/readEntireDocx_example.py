import docx

# This function returns the full text of a docx in a single string
def getText(filename):
    doc = docx.Document(filename)
    # Create blank string
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('demo.docx'))
