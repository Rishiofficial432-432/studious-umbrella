import speech_recognition as sr
import os
import webbrowser
import google.generativeai as genai
import datetime
import random
import numpy as np
import pyaudio

# Get API key from environment variable, fallback to 'YOUR_API_KEY' if not found
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", " your_api_key ")
if not GOOGLE_API_KEY:
    print("Error: Google API Key is missing. Please set the GOOGLE_API_KEY environment variable.")
    exit()
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"User: {query}\n Assistant: "
    try:
        response = model.generate_content(chatStr)
        response_text = response.text
        say(response_text)
        chatStr += f"{response_text}\n"
        return response_text
    except Exception as e:
         error_msg = f"Error: Could not get a response from the model: {e}"
         say(error_msg)
         return error_msg

def ai(prompt):
    text = f"Gemini response for Prompt: {prompt} \n *************************\n\n"
    try:
        response = model.generate_content(prompt)
        response_text = response.text
        text += response_text
        if not os.path.exists("Gemini"):
            os.mkdir("Gemini")

        # with open(f"Gemini/prompt- {random.randint(1, 2343434356)}", "w") as f:
        with open(f"Gemini/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
             f.write(text)
    except Exception as e:
        error_msg = f"Error: Could not get a response from the model: {e}"
        print(error_msg)
        say(error_msg)

def say(text):
    os.system(f'espeak "{text}"') #using espeak instead of say to work on chrome os flex


def takeCommand():
    r = sr.Recognizer()
    # If you know the index of your microphone use it, otherwise use default
    # You can get the device index with arecord -l
    # Example below: device_index = 1
    microphone_device_index = 0  # <---- Set this to the working index
    with sr.Microphone(device_index = microphone_device_index) as source:
        try:
            print("Listening...")
            audio = r.listen(source, timeout = 5)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return ""
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    # Setting the PA_ALSA_PLUGHW environment variable before initialization
    os.environ['PA_ALSA_PLUGHW'] = '1'
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        query = takeCommand()
        if not query:
            continue
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "/home/your_username/Downloads/downfall-21371.mp3" # Change this to path on your Chrome OS Flex device
            os.system(f"xdg-open {musicPath}")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} bajke {min} minutes")

        elif "open facetime".lower() in query.lower():
             say("FacetTime not supported on Chrome OS Flex")
            #os.system(f"open /System/Applications/FaceTime.app")

        elif "open pass".lower() in query.lower():
           say("Passky not supported on Chrome OS Flex")
           #os.system(f"open /Applications/Passky.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
