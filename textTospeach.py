from tkinter import *
# from gtts import gTTS
import pyttsx3
from playsound import playsound 
from tkinter import messagebox 
import os
import pyaudio
import speech_recognition as sr 
import sounddevice as sd
import numpy as np
import wave
# import scipy.io.wavfile as wav

r = sr.Recognizer() 
root = Tk()
root.title("TextToSpeech Converter App")
root.geometry('650x100')
lbl = Label(root, text = "Enter your text ")
lbl.grid()
textBox = Entry(root, bd=0, width=80, bg="white")
textBox.grid(row=0, column=1)

def clicked():
    Message = textBox.get()
    engine = pyttsx3.init()
    engine.say(Message)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()

def convertAudio(path,lang):
    with sr.AudioFile(path) as source:
        print('Fetching File')
        audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable
        try:
            # using google speech recognition
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text)
            print(text)
    
        except:
            print('Sorry.. run again...')

def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "AudioOutput.wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print("Hey! Say somthing I'm recording....")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("I have recorded.....")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    convertAudio(WAVE_OUTPUT_FILENAME,'en-IN')

# def speechTotext():
#     with sr.Microphone() as source:
#         print("Say something!")
#         r.adjust_for_ambient_noise(source, duration=5)  
#         audio = r.listen(source)
#         print("audio")
#     # recognize speech using Sphinx
#     try:
#         print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#     except sr.UnknownValueError:
#         print("Sphinx could not understand audio")
#     except sr.RequestError as e:
#         print("Sphinx error; {0}".format(e))

# def SpeakText(command): 
      
#     # Initialize the engine 
#     engine = pyttsx3.init() 
#     engine.say(command)  
#     engine.runAndWait() 
      
#     # Loop infinitely for user to 
#     # speak 
  
#     while(1):     

#         try:
#             m = sr.Microphone.list_microphone_names()
#             # print(m) 
#             mic=sr.Microphone(device_index=0)
#             with mic as source2:
#                 print("hello")
#                 r.adjust_for_ambient_noise(source2, duration=0.2)  
#                 audio2 = r.listen(source2) 
#                 print("audio2")
#                 MyText = r.recognize_google(audio2) 
#                 MyText = MyText.lower() 
#                 print("Did you say "+MyText) 
#                 SpeakText(MyText) 
                
#         except sr.RequestError as e: 
#             print("Could not request results; {0}".format(e)) 
            
#         except sr.UnknownValueError: 
#             print("unknown error occured")
      

def reset():
    textBox.delete(0,END)

def cancel():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

btn = Button(root, text = "Reset" ,fg = "black", command=reset)
btn.grid(column=0, row=1)
btn = Button(root, text = "Convert" ,fg = "black", command=clicked)
btn.grid(column=1, row=1)
btn = Button(root, text = "Cancel" ,fg = "black", command=cancel)
btn.grid(column=2, row=1)
# speechTotext()
#SpeakText("welcome Minal")
record()
# root.mainloop()