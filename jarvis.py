import gtts
import datetime
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import sys
import random
import playsound
import wolframalpha
import pyautogui
from time import sleep
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',190)

def speak(audio):
    print("   ")
    print(f":  {audio}") 
    print("   ")
    engine.say(audio)
    engine.runAndWait()

def open_chrome():
    url = 'www.google.com'

    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)

def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listenting....")
        r.pause_threshold= 1
        audio = r.listen(source,0,3)

    try:
        print(': Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f": {query}\n")
    
    except Exception as e:
     return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir!")
    elif hour>12 and hour<18:
        speak("good afternoon sir!")
    else:
        speak("good evening sir ")

def W(query):
    api_key = "AL6YEU-4GPYXP4K73"     
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)
    
    try:
        Answer = next(requested.results).text
        return Answer
    except:
        speak("An string value is not answerable .")

def TaskExe():
    wish()

    while True:
        query = TakeCommand()

        if "hello man" in query:
            speak("Hello Man")

        elif "take break" in query:
            
            speak("Ok Sir Call me anytime!")
            playsound(u'endUP.wav')
            break
        elif "take some rest" in query:
            
            speak("Ok Sir Call me anytime!")
            playsound(u'endUP.wav')
            break
        elif "jarvis take some rest" in query:
            
            speak("Ok Sir Call me anytime!")
            playsound(u'endUP.wav')
            break
        
        # elif "jarvis" in query or "Jarvis":
        #     speak("Yes Sir !")

        # elif "close the system" in query:
        #     speak("Have a nice day sir!")
        #     break
        
        elif "youtube search" in query:
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            speak("this is what I found on youtube!")
        
        elif "how are you" in query:
            speak("online and ready sir!")
        
        elif "how are you jarvis" in query:
            speak("online and ready sir !")

        elif "what is the weather" in query or "what is the temperature" in query or "what is the temperature outside" in query or "wheater" in query or "temprature" in query:
            speak("wait sir searching")
            temp = W('temeperature in mumbai')
            speak(temp)

        # elif "calculate" in query:
        #     cal = "what should i calculate"
        #     speak(cal)
        #     mn = Calculator(cal)
        #     speak(mn)
            
        elif "doubt" in query:
            speak("what is your doubt sir ?")
            x = TakeCommand().lower()
            sr = W(x)
            speak(sr)
        
        elif "task manager" in query:
            pyautogui.hotkey('ctrl', 'shift', 'esc')
        
        elif "task view" in query:
            pyautogui.hotkey('winleft', 'tab')
        
        elif "take screenshot" in query:
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")
        
        elif "snip" in query:
            pyautogui.hotkey('winleft', 'shift', 's')

        elif "close the app" in query:
            pyautogui.hotkey('alt','f4')

        elif "desktop" in query:
            pyautogui.hotkey("win","d")

        elif "setting" in query:
            pyautogui.hotkey('winleft', 'i')

        elif "new virtual desktop" in query:
            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif "chrome" in query:  # quit to end the program
            speak("opening the Chrome")
            open_chrome()
            
           
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)


        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('restarting in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")
        
        elif "who are you" in query:
            speak("I am Jarvis , Model name Mark 1 , created by Lalit Bharti")


        
        # elif "vs code" in query:
        #     speak('opening vs code....')
        #     vscode= 'C:\Users\my\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\\Visual Studio Code.exe'







if __name__=="__main__":
    # TaskExe()
    while True:
        permisssion = TakeCommand()
        if "wake up jarvis" in permisssion:
            playsound(u'sound.wav')
            TaskExe()
        elif "wake up" in permisssion:
            playsound(u'sound.wav')
            TaskExe()

            