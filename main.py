# pip install pyttsx3 - textToSpeech package
# pip install PyPDF2  - read pdf package

import pyttsx3
import PyPDF2
book = open('audio.pdf', 'rb')
readBook = PyPDF2.PdfFileReader(book)
pages = readBook.numPages
print(pages)

speaker = pyttsx3.init()
page = readBook.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()


# code for page number 7 to end
# speaker = pyttsx3.init()
# for num in range(7, pages):
#     page = pdfReader.getPage(num)
#     text = page.extractText()
#     speaker.say(text)
#     speaker.runAndWait()