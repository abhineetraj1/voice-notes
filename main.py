from time import sleep
from tkinter import*
from tkinter import simpledialog
from tkinter import messagebox as msg
import pyttsx3
import speech_recognition as sr
import os
import shutil
import datetime
import socket

def listen(duration):
	t= sr.Recognizer()
	with sr.Microphone() as source:
		text = t.record(source, duration=duration)
		try:
			return t.recognize_google(text)
		except:
			return "Didn't heard perfectly!"

def ssk():
		text = listen(5)
		e.insert(END, text)
		sh.place(x=2332,y=2322)
		e.place(x=10,y=10)

def write_text():
	if (socket.gethostbyname(socket.gethostname()) == "127.0.0.1"):
		msg.showerror("App","Your device is not connected to internet")
	else:
		e.place(x=10000,y=10000)
		sh.place(x=30,y=20)
		t.after(1000, ssk)

def speak():
	pyttsx3.speak(e.get("1.0",END).replace("\n",""))

def save():
	p = simpledialog.askstring("Save","Enter filename.")
	if (p+".txt" in os.listdir()):
		pyttsx3.speak("File with this name already exists")
		msg.showerror("Error","File with this name already exists")
	else:
		open(p+".txt","a").write(e.get("1.0",END))
		pyttsx3.speak("File saved successfully.")
		msg.showinfo("Success","File saved successfully")

t= Tk()
t.geometry("300x300")
t.title("Speech processing app")
Label(background="yellow", width=100, height=1000).place(x=0,y=0)
Button(text="Activate Microphone", command =write_text).place(x=10,y=180)
Button(text="Speak", width=5, command=speak).place(x=10,y=220)
Button(text="Save", width=5, command=save).place(x=140,y=180)
sh = Label(text="Say something!",font=("Arial",25) ,background="yellow")
e=Text(bd=4, height=8, width=32)
e.place(x=10,y=10)
t.mainloop()