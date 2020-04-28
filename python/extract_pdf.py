import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

fileurl = 'C:/Users/Arley%20Ribeiro/Desktop/springer_ebooks.pdf.pdf'
filename = 'springer_ebooks.pdf.pdf' 

pdfFileObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
if text != "":
   text = text   
else:
   text = textract.process(fileurl, method='tesseract', language='eng')

text_rows = text.split('\n')
text_rows_length = len(text_rows)
loop_length = text_rows_length - 5
i = 0
while i < loop_length:
    number = i
    bookTitle = i + 1
    author = i + 2
    edition = i + 3
    openUrl = i + 4
    print(text_rows[number], text_rows[bookTitle], text_rows[author], text_rows[edition], text_rows[openUrl])
    i += 5