import pyttsx3
import pygame

pygame.mixer.init()
counter = 0
def onStart(name):
   print ('starting', name)
def onWord():
   
   counter += 1
   print ('word', counter)
   
def onEnd(name, completed):
   print ('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
