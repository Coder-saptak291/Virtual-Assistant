# from email.mime import audio
import pyttsx3
import datetime
# import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def jarvisbol(kotha):
    engine.say(kotha)
    engine.runAndWait()

def greetkor():
    h = int(datetime.datetime.now().hour)

    if h>=0 and h<12:
        jarvisbol("Good Morning Sir!")
    if h>=12 and h<16:
        jarvisbol("Good Afternoon Sir!")
    if h>=16 and h<24:
        jarvisbol("Good Evening Sir!")
    jarvisbol("How Can I Help you sir")
    

def request():
    query = ""
    query = input("Sir please tell me your query \n")
    # print(query)
    while True:
        query.lower()
        if "wikipedia" in query.lower():
            jarvisbol("Searching Wikipedia")
            query = query.replace("wikipedia","")
            webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
            request()
        elif "open youtube" in query.lower():
            jarvisbol("opening youtube")
            # query = query.replace("wikipedia","")
            webbrowser.open("https://m.youtube.com/")
            request()
        elif "open code" in query.lower():
            coder_thikana = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(coder_thikana)
            request()
        elif "open powerpoint" in query.lower():
            p_thikana = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(p_thikana)
            request()
        elif "open word" in query.lower():
            w_thikana = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(w_thikana)
            request()
        elif "open google" in query.lower():
            webbrowser.open("https://www.google.com/")
            request()
        elif "open notepad++" in query.lower():
            n_thikana = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(n_thikana)
            request()
        elif "open q-basic" in query.lower():
            q_thikana = "C:\\Users\\tapas\\Downloads\\qb64_2021-11-07-03-00-00_4d85302_win-x86\\qb64\\qb64.exe"
            os.startfile(q_thikana)
            request()
        elif "open idle" in query.lower():
            i_thikana = "C:\\Program Files\\Python310\\Lib\\idlelib\\idle.pyw"
            os.startfile(i_thikana)
            request()
        elif "open scratch" in query.lower():
            s_thikana = "C:\\Program Files (x86)\\Scratch 3\\Scratch 3.exe"
            os.startfile(s_thikana)
            request()
        elif "open bluej" in query.lower():
            j_thikana = "C:\\Program Files\\BlueJ\\BlueJ.exe"
            os.startfile(j_thikana)
            request()
        elif "open onenote" in query.lower():
            on_thikana = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(on_thikana)
            request()

        elif "open github" in query.lower():
            webbrowser.open("https://www.github.com/")
            request()
        elif "play songs" in query.lower():
            webbrowser.open("https://coder-saptak291.github.io/Song-Website/")
            request()
        elif "open wavepad" in query.lower():
            wp_thikana = "C:\\Program Files (x86)\\NCH Software\\WavePad\\wavepad.exe"
            os.startfile(wp_thikana)
            request()
        elif "open audacity" in query.lower():
            ac_thikana = "C:\\Program Files\\Audacity\\Audacity.exe"
            os.startfile(ac_thikana)
            request()
        elif "shutdown" in query.lower():
            os.system("shutdown /s /t 1")
        elif "restart" in query.lower():
            os.system("shutdown /r /t 1")
        elif "logout" in query.lower():
            os.system("shutdown -l")
            
        else:
            jarvisbol("Sir please enter correctly")
            print("Sir please enter correctly")
        
        

            
        

greetkor()
request()
