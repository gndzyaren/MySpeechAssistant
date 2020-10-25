import smtplib
import ec as ec
import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import googlesearch
import wikipedia
import webbrowser
import os
import time
import subprocess
#import ecapture as ec
import wolframalpha
import json
import requests
from selenium import webdriver

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Hi Guys!This is YG AI Assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)


def welcome():
    speak("Welcome Sir!")
    speak("The current time is: ")
    time()
    speak("The current day is: ")
    date()
    hour = int(datetime.datetime.now().hour)
    if (hour >= 6 and hour < 12):
        speak("Good morning Sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon Sir!")
    elif (hour >= 18 and hour <= 24):
        speak("Good evening Sir!")
    else:
        speak("Good night Sir!")

    speak("AI Assistant is running on your service."
          "Please give some instructions to do for you")


def takeInstructions():
    read = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        read.pause_threshold = 1  # listen the audio for 1 second
        audio = read.listen(source)

    try:
        print("Recognizing...")
        query = read.recognize_google(audio)
        print(query)
    except Exception as e:
        print("e")
        speak("Please repeat your instruction again...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.echo()
    server.starttls()
    server.login("Senderemail@gmail.com", 'Password')
    server.sendmail("Senderemail@gmail.com", to, content)
    server.close()


# Rearrange the lighton and lightoff
def lighton():
    driver = webdriver.Chrome('"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe')
    driver.get("https://http://www.google.com")
    elem1 = driver.find_element_by_id("S1off")
    elem1.click()


def lightoff():
    driver = webdriver.Chrome('"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe')
    driver.get("https://http://www.google.com")
    elem1 = driver.find_element_by_id("S1on")
    elem1.click()

welcome()
takeInstructions()

if __name__ == '__main__':

    while True:
        speak("Talk to me")
        speak("How can I help you?")
        statement = takeInstructions().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "see you" in statement \
                or "okay bye" in statement or "stop" in statement\
                or "shut up" in statement:
            speak('YG AI Assistant is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak("Searching Wikipedia...")
            statement = statement.replace("Wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("Oops,Wikipedia thought as ")
            speak(results)
        elif 'open google' in statement or "Google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(7)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open now")
            time.sleep(7)
        elif 'open gmail' in statement or "Gmail" in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(7)
        elif 'open stackoverlflow' in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Stackoverflow is open now")
            time.sleep(7)
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.reuters.com/")
            speak('News headers are here.You can select any topic that yo want to read.')
            time.sleep(6)
        elif 'open camera' in statement or 'take a photo' in statement:
            speak("Say cheese")
            ec.capture(0,"camera","img.jpg")
        elif 'search' in statement:
            statement = statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(7)
        elif 'ask' in statement:
            speak("I know something from my master.I improved for helping the people to doing the commands for them")
            speak("My owner Yaren, still improving me,Thanks to her")
            question =takeInstructions()
            app_id ="YG-12345"
            client = wolframalpha.Client(app_id)
            result = client.query(question)
            answer = next(result.results).text
            speak(answer)
        elif "log off" in statement or "sign out" in statement:
            speak("See you soon.I want to take a nap for a while.")
            subprocess.call(["shutdown","/l"])
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeInstructions()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
        else:
            speak("There is no valid instrucitons yet.")

time.sleep(7)

