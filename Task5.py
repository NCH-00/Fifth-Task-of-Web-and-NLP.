import speech_recognition as sr #library used to convert speech to text
from bidi.algorithm import get_display # used for reverse letters and connect them

r = sr.Recognizer() # create a recognizer object 
r.energy_threshold = 4000 
lan = "ar-AR" # for arabic language

#recored the sound from microphone and convert it to text
with sr.Microphone() as source:
 print("Speak now...")
 audio = r.listen(source)

try:
 text = r.recognize_google(audio, language=lan) #convert the sound to text using Google Speech Recognition API
 reversed_text = get_display(text[::-1]) # Reverse the text and apply bidi algorithm
 print("You said:", reversed_text)
except sr.UnknownValueError:
 print("Sorry, I could not understand your speech.")
except sr.RequestError as e:
 print("Could not request results from Google Speech Recognition service; {0}".format(e))
