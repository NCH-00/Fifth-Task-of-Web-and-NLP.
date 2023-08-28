from gtts import gTTS
from playsound import playsound

language = "ar" # Arabic language code 
text = "مرحبًا بك سٌعدت بلقائك، كيف يمكنني مساعدتك؟" # The desired text converted to speech

tts = gTTS(text, lang=language)
tts.save("output.mp3") #save the sound into the current directory

file_path = "output.mp3" # Path to play the MP3 file 
playsound(file_path)