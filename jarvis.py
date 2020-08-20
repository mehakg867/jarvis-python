import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os                      



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishus():
   hour= int(datetime.datetime.now().hour)
   #print(hour) 

   if hour>=0 and hour<12:
       speak("good morning")
   elif hour>= 12 and hour<18:
        speak("good afternoon")
   else:
        speak("good evening")
   speak("hello..! I am jarvis. please tell how can i help you my owner") 
       

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print (" listening.....")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("recognizing..") 
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        # print("e")
        print("say that again....")
        return "None"

    return query 

if __name__ == "__main__":
   wishus()
   while True:
      query = takecommand().lower()

      if "wikipedia" in query:
          speak("searching in wikipedia")
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query,sentences=2)
          speak("according to wikipedia")
          speak(results)


      elif "open youtube" in query:
          webbrowser.open("youtube.com")

      elif "open google" in query:
          webbrowser.open("google.com")  

      elif "open facebook" in query:
          webbrowser.open("facebook.com")
        
      elif "time" in query:
          timenow = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"sir, the thime is {timenow}")

      elif "open code" in query:
        codepath = "C:\\Users\\91892\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
        os.startfile(codepath) 

      elif "quit" in query:
           exit()


