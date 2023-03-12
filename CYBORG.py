#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install SpeechRecognition')


# In[2]:


get_ipython().system('pip install pyttsx3')


# In[3]:


get_ipython().system('pip install wikipedia')


# In[4]:


get_ipython().system('pip install PyAutoGUI')


# In[5]:


get_ipython().system('pip install winshell')


# In[6]:


get_ipython().system('pip install pyjokes')


# In[7]:


get_ipython().system('pip install appopener')


# In[8]:


get_ipython().system('pip install PyAudio')


# In[9]:


import speech_recognition as sr
import pyttsx3
import time
import datetime
import calendar
import wikipedia
import webbrowser
import os
import requests
import json
import pyautogui
import sys
import cv2
import tkinter as tk
import psutil
import winshell
import pyjokes


# In[10]:


from AppOpener import run
from urllib.request import urlopen
# Used for wheather
from bs4 import BeautifulSoup
# Used to take screenshot
from tkinter.filedialog import *


# In[11]:


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate',250)
# print(voices[0].id)
# print(voices[1].id)


# In[12]:


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# In[13]:


def engine_listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = True
        r.pause_threshold = 1
        r.operation_timeout = 1
        print('\n')
        print("Listening...")
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-US").lower()
        print(f"User: {query}")
        return query
    
    except:
        print("Please repeat that one")
        engine_listen()


# In[14]:


def wish_master():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am cyborg. Sir, how can I help you")


# ### FUNCTIONS RELATED TO WIDGETS

# In[15]:


# This function uses datetime module to tell the date.

def date():
    now = datetime.datetime.now()
    date = datetime.datetime.today()

    day = calendar.day_name[date.weekday()]
    date = now.day
    month = now.month
    year = now.year

    months = ["January","February","March","April","May","June","July","August","September","October","November","December",]

    ordinals = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st",]
    
    print(f"Cyborg: {day}-{ordinals[date - 1]}-{months[month - 1]}-{year}")
    speak("The current date is")
    speak(day)
    speak(ordinals[date - 1])
    speak(months[month - 1])
    speak(year)   


# In[16]:


# This function uses datetime module to tell the time.

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is\n")
    print(f"Cyborg: {time}")
    speak(time)


# In[17]:


# This function uses json and urlopen modules to tell your current location.

def location_finder():
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)
    print(f"Cyborg: Sir, you are currently in {data['city']} city and country {data['country']}")
    speak(f"Sir, you are currently in {data['city']} city and country {data['country']}")
    # print(data) all the attributes that you will get with data variable


# In[18]:


# This function uses json, urlopen and beautifulsoap modules to tell weather of your current city.

def weather_forcast():
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)
    city = data["city"]
    # city = "Delhi"
    # city = "New York"
    # city = "London"
    # city = "France"
    # city = "Hong Kong"
    # city = "Dubai"

    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # printing all data
    print(f"Cyborg: Sir you are currently in {city}")
    speak(f"Sir you are currently in {city}")
    print(f"Cyborg: Temperature is {temp}")
    speak(f"Here Temperature is {temp}")
    print(f"Cyborg: Sky Description is {sky}")
    speak(f"And Sky Description: is {sky}")


# In[19]:


# def google_maps():


# ### FUNCTIONS RELATED TO WEBBROWSER OR SEARCH

# In[20]:


# This function uses os module to open chrome.

def open_chrome():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    os.startfile(chrome_path)


# In[21]:


# This function uses webbrowser module to open google and it is going to ask for what should i search on google.

def open_google():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    tabUrl = "http://google.com/search?q="
    print("Cyborg: Sir, what should i search on google ?")
    speak("Sir, what should i search on google ?") 
    search = engine_listen()
    webbrowser.get(chrome_path).open(tabUrl+search)


# In[22]:


# This function is going to search anything for you accoding to your request in google.

def search_on_google():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    tabUrl = "http://google.com/search?q="
    print("Cyborg: Sir, i am unable to recognize please repeat that one ?")
    speak("Sir, i am unable to recognize please repeat that one ?")
    search = engine_listen()
    webbrowser.get(chrome_path).open(tabUrl+search)


# In[23]:


# This function uses wikipedia module to search in wikipedia.

def search_in_wikipedia():
    query = engine_listen()
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print("Cyborg: According to Wikipedia\n")
    speak("According to Wikipedia")
    print(f"Cyborg: {results}")
    speak(results)


# In[24]:


# This function uses requests and json module to fetch information from newsapi.org using api key.

def news(): 
    api_key = "c3f46981c1bc40f3a20007de84314822"
    
    speak("Sir please select a country from the list given below")
    country = ["India","United States","Japan","China","United Kingdom","australia"]
    for i in range(len(country)):
        print(country[i])
    
    query = str(engine_listen())
    
    if "india" in query:
        main_url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="+api_key
            
    elif "united states" in query or "u s" in query:
         main_url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="+api_key
            
    elif "japan" in query:
        main_url = "https://newsapi.org/v2/top-headlines?country=jp&category=business&apiKey="+api_key
            
    elif "china" in query:
        main_url = "https://newsapi.org/v2/top-headlines?country=cn&category=business&apiKey="+api_key
        
    elif "united kingdom" in query or "u k" in query:
        main_url = "https://newsapi.org/v2/top-headlines?country=uk&category=business&apiKey="+api_key
            
    elif "australia" in query:
        main_url = "https://newsapi.org/v2/top-headlines?country=au&category=business&apiKey="+api_key
            
    else:
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        tabUrl = "http://google.com/search?q=" 
        search = "top 10 treding news from around the world"
        webbrowser.get(chrome_path).open(tabUrl+search)
        
    news = requests.get(main_url).json()
    article = news["articles"]
    news_article = []
    
    for arti in article:
        news_article.append(arti["title"])
        
    for i in range(10):
        print(i+1,news_article[i])


# In[25]:


# This function uses webbrowser and AppOpener module to open social media platforms whether you have that app installed or not.

def social_media_app_opener():
    query = engine_listen()
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    if query is not None:
        if 'whatsapp' in query:
            speak("Opening Whatsapp")
            run("whatsapp")
            webbrowser.get(chrome_path).open("web.whatsapp.com")

        elif 'youtube' in query:
            speak("Opening Youtube")
            run("youtube")
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'facebook' in query:
            speak("Opening Facebook")
            run("facebook")
            webbrowser.get(chrome_path).open("facebook.com")

        elif 'instagram' in query:
            speak("Opening Instagram")
            run("instagram")
            webbrowser.get(chrome_path).open("instagram.com")

        elif 'twitter' in query:
            speak("Opening Twitter")
            run("twitter")
            webbrowser.get(chrome_path).open("twitter.com")

        elif 'snapchat' in query:
            speak("Opening Snapchat")
            run("snapchat")
            webbrowser.get(chrome_path).open("snapchat.com")

        elif 'linkedin' in query:
            speak("Opening Linkedin")
            run("linkedin")
            webbrowser.get(chrome_path).open("linkedin.com")

        elif 'telegram' in query:
            speak("Opening Telegram")
            run("telegram")
            webbrowser.get(chrome_path).open("web.telegram.org")

        elif 'reddit' in query:
            speak("Opening Reddit")
            run("reddit")
            webbrowser.get(chrome_path).open("reddit.com")

        elif 'discord' in query:
            speak("Opening Discord")
            run("discord")
            webbrowser.get(chrome_path).open("discord.com")

        elif 'gmail' in query or 'email' in query:
            speak("Opening Email")
            run("email")
            webbrowser.get(chrome_path).open("mail.google.com")


# In[26]:


# This function uses time and requests module to calculate the internet speed.

def internet_speed():
    # Make a request to a popular website
    start = time.time()
    r = requests.get('http://www.google.com')
    end = time.time()
    elapsed = end - start

    # Calculate the download speed in megabits per second
    download_speed = len(r.content) / elapsed / (1024 * 1024)

    # Make a request to a file hosting service
    start = time.time()
    r = requests.post('http://example.com/upload', data=b'x' * (1024 * 1024))
    end = time.time()
    elapsed = end - start

    # Calculate the upload speed in megabits per second
    upload_speed = len(r.content) / elapsed / (1024 * 1024)

    # Measure the internet speed
    download_speed, upload_speed = measure_internet_speed()

    # Print the speeds
    print(f'Cyborg: Download speed: {download_speed:.2f} Mbps')
    speak(f'Download speed: {download_speed:.2f} M b p s')
    print(f'Cyborg: Upload speed: {upload_speed:.2f} Mbps')
    speak(f'Upload speed: {upload_speed:.2f} M b p s')


# ### FUNCTIONS RELATED TO OPERATING SYSTEM

# In[27]:


# This function uses psutil module to check battery sensors to fetch battery information like how much battery do we have.

def system_power():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    print(f"Cyborg: Sir we have {percentage} percent battery")
    speak(f"Sir we have {percentage} percent battery")
    if percentage >=75:
        speak("We have enough power to continue our work.")
    elif percentage >=40 and  percentage <75:
        speak("We should connect our system to the charger.")
    elif percentage >=15 and  percentage <40:
        speak("We don't have enough power to work please connect to the charger.")
    elif percentage <=15:
        speak("We don't have enough power to run this system .Please connect to the charger. The system will shut down very soon.")


# In[28]:


# This function uses os module to perform basic os functions like shutdown,restart and sleep

def operating_system():
    if "shutdown" in query:
        print("Sir, Do you wish to shutdown your computer say yes or no ?")
        speak("Sir, Do you wish to shutdown your computer say yes or no ?")
        if "yes" in query:
            speak("Shutting down your computer")
            os.system("shutdown /s /t 1")
        else:
            exit()
    
    elif "restart" in query:
        os.system("shutdown /r /t 1")

    elif "sleep" in query:
        os.system("shutdown -l")


# In[29]:


# This function uses pyautogui and tkinter module to take screenshots

def screenshot():
    root = tk.Tk()

    window = tk.Canvas(root, width = 300, height = 50)
    window.pack()

    def take_ss():
        screen_shot = pyautogui.screenshot() 
        save_path = asksaveasfilename()
        screen_shot.save(save_path+".jpg")
        
    speak("Sir, dont forget to close the window after saving your file")
    
    button = tk.Button(root,text="Screenshot", font=('Aerial 11 bold'), background="black", foreground="white", command=take_ss)
    button.pack(pady=20)
    window.create_window(150,25,window=button)
   
    root.mainloop() 


# In[30]:


# This function uses AppOpener module to open in-built operating system apps.

def operating_system_app():
    if "calculator" in query:
        speak("Opening Calculator")
        run("calculator")
    elif "excel" in query:
        speak("Opening Excel")
        run("excel")
    elif "vlc" in query:
        speak("Opening vlc media player")
        run("vlc media player")
    elif "notepad" in query:
        speak("Opening Notepad")
        run("notepad")
    elif "word" in query:
        speak("Opening word")
        run("word")
    elif "task manager" in query:
        speak("Opening Task manager")
        run("task manager")
    elif "command prompt" in query:
        speak("Opening command prompt")
        run("command prompt")
    elif "paint" in query:
        speak("Opening Paint")
        run("paint")


# In[31]:


# This function uses winshell module to empty recycle bin.

def empty_recycle_bin():
    winshell.recycle_bin().empty(
        confirm = True, show_progress = False, sound = True
    )
    speak("Deleted all the files that are there in the recycle bin")


# ### FUNCTIONS RELATED TO CAMERA

# In[32]:


# This function uses cv2 module to open camera.

def open_camera():
    print("Cyborg: Opening camera")
    speak("Opening camera")
    print("Cyborg: Sir press q to close the camera")
    speak("Sir press q to close the camera")
    webcam = cv2.VideoCapture(0)  
    
    while True:
        ret, frame = webcam.read()      
        cv2.imshow('webcam', frame)
        
        key = cv2.waitKey(1)
        if key == ord("q"):
            print("Cyborg: Closing camera")
            speak("Closing camera")
            break
            
    webcam.release()
    cv2.destroyAllWindows()


# In[33]:


# This function uses cv2 module to open camera and take a picture.

def photo_capture():
    print("Cyborg: Opening camera")
    speak("Opening camera")
    print("Cyborg: Press space bar to take a picture")
    speak("Press space bar to take a picture")
    print("Cyborg: Press q to close the camera")
    speak("Press q to close the camera")
    webcam = cv2.VideoCapture(0)
    image_counter = 0
    
    while True:
        ret,frame = webcam.read()
        cv2.imshow("webcam",frame)
        
        key = cv2.waitKey(1)
        if key == 32:
            image_name = "image_{}.png".format(image_counter)
            cv2.imwrite(image_name , frame)
            image_counter+=1
            
        elif key == ord("q"):
            print("Cyborg: Closing camera")
            speak("Closing camera")
            break
    webcam.release()
    cv2.destroyAllWindows()


# In[34]:


# This function uses cv2 module to open camera and record a video.

def video_recorder():
    print("Cyborg: Opening camera")
    speak("Opening camera")
    print("Cyborg: Press r to record the video")
    speak("Press r to record the video")
    print("Cyborg: Press q to close the camera")
    speak("Press q to close the camera")
    webcam = cv2.VideoCapture(0) 
    
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter("recording.mp4", fourcc, 30.0, (1280,720))
    recording = False
    
    while True:
        ret, frame = webcam.read()     
        
        if ret:
            cv2.imshow('Webcam', frame)
            if recording:
                writer.write(frame)
        
        key = cv2.waitKey(1)
        if key == ord("q"):
            print("Cyborg: Saving your file")
            speak("Saving your file")
            print("Cyborg: Closing camera")
            speak("Closing camera")
            break
            
        elif key == ord("r"):
            recording = not recording
            print("Cyborg: Recording has been started")
            speak("Recording has been started")
            
    webcam.release()
    writer.release()
    cv2.destroyAllWindows()


# ### OTHERS

# In[35]:


# def email_sender():


# In[36]:


# def music_player():


# In[37]:


# def set_alarm():


# In[38]:


# This function uses pyjokes module to find out some jokes

def jokes():
    jokes = pyjokes.get_joke()
    speak(jokes)


# ### ALL THE TASKS THAT THIS ASSISTANT CAN PERFORM

# In[39]:


# This is the task execution function. 
# This function combines all the above task into one using if else and respond to the user based on their query.   

def cyborg():
    wish_master()
    while True:
        query = engine_listen()
        if query is not None:
            if "date" in query and "time" in query:
                date()
                time()
            elif "date" in query:
                date()   
            elif "time" in query:
                time()
            elif "location" in query or "where are we" in query or "where we are" in query:
                location_finder()
            elif "weather" in query or "climate" in query or "temperature" in query:
                weather_forcast()
                
            
            elif "search" in query:
                search_on_google()
            elif "wikipedia" in query:
                search_in_wikipedia()  
            elif "news" in query:
                news()
            elif "internet speed" in query:
                internet_speed()
                    
            
            elif "battery" in query or "power" in query:
                system_power()
            elif "shutdown" in query or "restart" in query or "sleep" in query:
                operating_system()
            elif "volume" in query or "mute" in query or "unmute" in query:
                if "up" in query or "increase" in query:
                    pyautogui.press("volumeup")
                elif "down" in query or "decrease" in query:
                    pyautogui.press("volumedown")
                elif "mute" in query:
                    pyautogui.press("volumemute")
                elif "unmute" in query:
                    pyautogui.press("volumeunmute")     
            elif "screenshot" in query:
                screenshot()
                speak("Thanks for closing the window")
            elif "recycle bin" in query:
                empty_recycle_bin()
                
            
            elif "photo" in query or "capture" in query or "picture" in query:
                photo_capture()
            elif "record" in query or "video record" in query:
                video_recorder()
            elif "close camera" in query:
                webcam.release()
                cv2.destroyAllWindows()
                
                
            elif "open" in query:
                if "camera" in query:
                    open_camera()
                elif "whatsapp" in query or "youtube" in query or "facebook" in query or "instagram" in query or "telegram" in query or "twitter" in query or "snapchat" in query or "linkedin" in query or "reddit" in query or "discord" in query or "email" in query or "gmail" in query:
                    social_media_app_opener()
                elif "calculator" in query or "excel" in query or "vlc" in query or "notepad" in query or "word" in query or "task manager" in query or "command prompt" in query or "paint" in query:
                    operating_system_app()
                elif "chrome" in query:
                    open_chrome() 
                elif "google" in query:
                    open_google()
                
                    
            elif "open spotify" in query or "play music" in query or "music" in query or "songs" in query:
                music_player()
                
            elif "joke" in query or "jokes" in query:
                jokes()

                
            elif "who are you" in query or "what can you do" in query or "define yourself" in query or "your name" in query:
                speak("Hi sir my name is cyborg and i am a virtual sidekick")
            elif "created you" in query or "made you" in query or "build you" in query:
                speak("I am a computer program built by a human being")
            elif "your purpose" in query or "why do you exist" in query:
                speak("To take over this world and to wipe out the entire human civilization")
            elif "how are you" in query:
                speak("Sir i am good. what about you")
            elif "fine" in query or "good" in query:
                speak("It's good to know that you are fine")


# In[41]:


if __name__ == "__main__":
    while True:
        permission = engine_listen()
        if permission is not None:
            if "wake up" in permission or "hey" in permission or "cyborg" in permission  or "hello" in permission:
                cyborg()
            elif "goodbye" in permission or "sleep" in permission or "bye" in permission or "stop" in permission:
                print("Good bye sir, have a nice day .")
                speak("Good bye sir, have a nice day .")    
                sys.exit()


# In[33]:


# LIST OF FUNCTIONS

# WIDGETS
# 1 DATE 
# 2 TIME 
# 3 LOCATION FINDER
# 4 FIND A PLACE IN GOOGLE MAP X
# 5 WEATHER FORCAST 

# WEBROWSER
# 6 OPEN CHROME 
# 7 OPEN GOOGLE AND SEARCH ON GOOGLE
# 8 SEARCH IN WIKIPEDIA
# 9 NEWS
# 10 SOCIAL MEDIA APP/WEB OPENER
# 11 INTERNET SPEED 

# OPERATING SYSTEM
# 12 OPERATING SYSTEM APPS
# 13 SYSTEM POWER OR BATTERY POWER
# 14 OPERATING SYSTEM / SHUTDOWN,RESTART,SLEEP
# 15 SYSTEM VOLUME 
# 16 SCREENSHOT
# 17 EMPTY RECYCLE BIN

# CAMERA
# 18 OPEN CAMERA
# 19 PHOTO CAPTURE
# 20 VIDEO RECORDER 
# 21 CLOSE CAMERA

# OTHERS
# 22 SEND EMAILS X
# 23 PLAY MUSIC X
# 24 SET ALARM X
# 25 TELL A JOKE 
# 26 PERSONAL QUESTIONS

