import pyttsx3

while True:
    data=input("Enter the text you want to convert:\n")
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()
    