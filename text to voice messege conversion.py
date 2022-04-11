# text to voice messege conversion in python 
from gtts import gTTS
#https://gtts.readthedocs.io/en/latest/module.html#module-gtts.tts
from playsound import playsound
# for playsound module please try to avoid using 1.3.0 version (it didn't work for me)
# try the older 1.2.2 version
#The playsound module contains only one thing - the function (also named) playsound.
#It requires one argument - the path to the file with the sound you’d like to play. This may be a local file, or a URL

audio = 'samp_speech.mp3'
#language = 'en'
sp = gTTS(text = "Hello! This is Kaustav Dey. Nice to meet you, everyone.", lang = 'en', slow = False)
sp.save(audio)
playsound(audio)

