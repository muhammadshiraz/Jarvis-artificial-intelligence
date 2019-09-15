import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_Greeting():
    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12:
        speak("Good Morning! Hi sir how are you I am Jarvis Sir Please tell me how I may help you")

    elif 12 <= currentTime.hour < 18:
        speak("Good Afternoon! Hi sir how are you I am Jarvis Sir Please tell me how I may help you")
    else:
        speak("Good Evening!")
        speak("Hi sir how are you I am Jarvis Sir Please tell me how I may help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-pk')
            print(f"User said: {query}\n")

        except Exception as e:
             #print(e)
            print("Say that again")
            return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    time_Greeting()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'G:\\Desktop Assets\\note5\\WhatsApp\\Media\\WhatsApp Video'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Muhammad Shiraz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'what is your name' in query:
            speak("Sir My name is Jarvis")

        elif 'where are you from' in query:
            speak("I'm originally from Seoul, South Korea, but I live in Gumi-si.")

        elif 'goodbye' in query:
                speak("GoodBye Sir! Take Care")
                quit();

        elif 'email to friend' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "friendemail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend shiraz. I am not able to send this email")




