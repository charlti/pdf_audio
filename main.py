from PyPDF4 import PdfFileReader
import pyttsx3

def chose_langage(langage):
    voices = speak.getProperty('voices')
    if langage == 'en':
        speak.setProperty('voice', voices[1].id)

def extract_info(pdf_path):

    with open(pdf_path, "rb") as file:
        pdf = PdfFileReader(file)
        informations = pdf.getDocumentInfo()
        pages_nb = pdf.getNumPages()
        for i in range(page_start, page_stop+1):
            page = pdf.getPage(i)
            text = page.extractText()
            text = text.replace('\n', '')   
            text = text.replace("™", "'")
            text = text.replace("˜", "fi")
            pages_text.append(text)
        
    print(f"Informations for {pdf_path}\n")
    print(f"Author : {informations.author}")
    print(f"Title : {informations.title}")
    print(f"Number of pages : {pages_nb}")
    
if __name__ ==  "__main__":

    pdf_path = input("Entre le chemin vers ton fichier pdf : ")
    langage = input("Selectionne la langue du texte [fr/en] : ")
    page_start = int(input("Entre le numéro de la première page que tu souhaites lire : "))
    page_stop = int(input("Entre le numéro de la dernière page que tu souhaites lire : "))
    pages_text = []

    speak = pyttsx3.init()
    chose_langage(langage)
    speak.setProperty('rate', 165)
    extract_info(pdf_path)

    for page in pages_text:
        print(page + "\n")
        speak.say(page)
        speak.runAndWait()

        

