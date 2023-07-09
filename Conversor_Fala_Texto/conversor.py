"""Testando conversor de texto em voz"""
import pyttsx3

robo = pyttsx3.init()

msg_robo = input("Hello World.")

robo.say(msg_robo)

robo.runAndWait()
