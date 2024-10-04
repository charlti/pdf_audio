import tkinter
from tkinter import filedialog
from PyPDF4 import PdfFileReader
import pyttsx3
import sys

# Si on a besoin de print le texte extrait du pdf
sys.stdout.reconfigure(encoding='utf-8')

# pdf_path = input("Entre le chemin vers ton fichier pdf / Enter the path to your pdf file : ")
langage = input("Selectionne la langue du texte [fr/en] / Select the langage of the text [fr/en]")
pdf_path = "Bug_bounty.pdf"

def chose_langage(langage):
    voices = speak.getProperty('voices')
    if langage == 'en':
        speak.setProperty('voice', voices[1].id)


def extract_info(pdf_path):

    with open(pdf_path, "rb") as file:
        pdf = PdfFileReader(file)
        informations = pdf.getDocumentInfo()
        pages_nb = pdf.getNumPages()
        from_page = pdf.getPage(28)
        text = from_page.extractText()
        text = text.replace('\n', '')   
        text = text.replace("™", "'")
        text = text.replace("˜", "fi")

    print(f"Informations for {pdf_path}\n")
    print(f"Author : {informations.author}")
    print(f"Title : {informations.title}")
    print(f"Number of pages : {pages_nb}")
    print(text)
    return text


if __name__ ==  "__main__":
    
    speak = pyttsx3.init()
    chose_langage(langage)
    speak.setProperty('rate', 165)

    extracted_text = extract_info(pdf_path)
    speak.say(extracted_text)
    speak.runAndWait()


