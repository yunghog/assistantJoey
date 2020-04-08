import gtts
import speech_recognition as sr
import os
import time
import webbrowser
import smtplib
#user modules
import timeNow as t
import weather as w

r=sr.Recognizer()
mic=sr.Microphone()

def Talktome(audio):
	print(audio)
	tts = gtts.gTTS(text = audio , lang = 'en')
	tts.save('audio.mp3')
	os.system('audio.mp3')

Talktome('Joey is ready')

def myCommand():
	print('Listening...')
	with mic as source:
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source , duration = 1)
		audio=r.listen(source)
	try:
		command = r.recognize_google(audio)
		print('You said '+ command)
	except sr.UnknownValueError:
		assistant(myCommand())
	return command

def assistant(query):
	if 'who are you' in query:
		Talktome('Hey I am Joey Tribbiani. I am your assistant. Joey doesn\'t share food')
	if 'hello ' in query:
		Talktome('how you doin')
	if 'how is the weather' in query:
		query=query.split(' ')
		Talktome(w.tellWeather(query[-1]))
	if 'what is the time' in query:
		Talktome(t.tellTime())

while True:
	assistant(myCommand())
