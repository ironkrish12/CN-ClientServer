import socket
import pyttsx3 as tts#pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import passw
import os
import smtplib
from googletrans import Translator
'''
What is pyttsx3?
A python library that will help us to convert text-to-speech. In short, it is a text-to-speech library.
It works in offline mode, and it is compatible with Python 2 as well as Python 3.'''
choice = 1#defined as global variable with default value 1

def generateMP3():#generates an mp3
            print("choice 0")
            mp3FileName = 'myAudio.mp3'

            engine = tts.init()

            engine.save_to_file(
        '''mail to Sangamesh''', 
            mp3FileName
            ) 
            engine.runAndWait()

            return mp3FileName

def speech_to_text():#Convert speech to text
    
    engine = sr.Recognizer()

    # 4) read mp3 file
    mp3FileName = generateMP3()
    with sr.AudioFile(mp3FileName) as source:
            print('File is being analyzed...')
            audio = engine.record(source)

    # 5) Extract and print text
    try:
            text = engine.recognize_google(audio)
            print(f'Text: {text}')
            txtFile = open('textFromMp3.txt', 'a')
            txtFile.writelines(text)
            #query = text
            # 
            return text
    except:
            print('Something gone very wrong...')

def sendEmail(to, content):#Sends Email. Don't forget to switch 'Less secure apps access to email account' ON
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('124003212@sastra.ac.in', passw.passqw)
    server.sendmail('124003212@sastra.ac.in', to, content)
    server.close()

def speak(audio):#As the name suggests, it speaks the text given as argument
        engine.say(audio)
        engine.runAndWait()

def wishMe():#Wishes the user once they choose voice command
            hour = int(datetime.datetime.now().hour)

            if hour>=0 and hour<12:
                speak("Good Morning!")

            elif hour>=12 and hour<18:
                speak("Good Afternoon!")

            else: 
                speak("Good Evening!")

            speak("I am Quixle Sir. Please tell me how may I help you")
            c.send(bytes('start','utf-8'))

def work(query):#does the string matching and proceeds accordingly
    print("IN WORKKKKKK")
    print(query)
    app = query.split()
    
    print(app)
    if 'Wikipedia' in query:
            c.send(bytes('stop','utf-8'))
            print('wiki')
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            print(query)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            c.send(bytes('start','utf-8'))

    elif app[1]=='YouTube' or  app[1]=='youtube':
            c.send(bytes('stop','utf-8'))
            print("Opening....youtube")
            webbrowser.open("youtube.com")
            print("opened")
            c.send(bytes('start','utf-8'))

    elif  app[1] == 'Google' or app[1]== 'google':
            c.send(bytes('stop','utf-8'))
            print("Opening....google")
            webbrowser.open("google.com")
            print("opened")
            c.send(bytes('start','utf-8'))
            

    elif 'open stackoverflow' in query:
            c.send(bytes('stop','utf-8'))
            print("Opening....")
            webbrowser.open("stackoverflow.com")
            print("opened")
            c.send(bytes('start','utf-8'))
            
    # elif 'play music' in query:
    elif app[1]== 'music':
            c.send(bytes('stop','utf-8'))
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

   
    
    elif app[0]=='tamil' and app[1]=='mail' or app[0]=='Tamil' and app[1]=='mail' in query:
        print('inside tamil email')
        # get choice from user
        # if user choice is 0: normal 
        # elif userchoice is 1 : copy till to=1233jk        ,translate content ,copy the rest
        c.send(bytes('stop','utf-8'))
        speak("What should I say?")
        c.send(bytes('start','utf-8'))
        content = c.recv(1024)
        if type(content)==bytes:
         content=content.decode()
        to = "sangameshdavey@gmail.com"
        #translate the content
        translator = Translator()
        result = translator.translate(content, src='en', dest='ta')
        #result = str(result)
        print(result.text)
        # sendEmail(to, (result))
        print(type(result.text))
        content=result.text
        content = content.encode('utf-8')
        print(type(content)) 
        sendEmail(to, content)
        speak("Email has been sent!")
        
    elif app[0]=='simple' and app[1]=='mail' or app[0]=='Simple' and app[1]=='mail' in query:
        print('inside general mail')
        c.send(bytes('stop','utf-8'))
        speak("What should I say?")
        c.send(bytes('start','utf-8'))
        content = c.recv(1024)
        print(content)
        print(type(content))
        to = "ironkrish12@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")
           

    elif app[0]=='exit' and app[1]=='exit' in query:
            speak("Bye panel!")
            c.send(bytes('stop','utf-8'))#new code
            
       
n = 0
query=''
engine = tts.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
'''
What is sapi5?
1)Microsoft developed speech API.
2)Helps in synthesis and recognition of voice.
What Is VoiceId?
Voice id Helps us to select different voices.
voice[0].id is Male voice 
voice[1].id is Female voice
'''
engine.setProperty('voice', voices[0].id)
s = socket.socket()
print("Socket created!")

s.bind(('localhost',9999))#localhost is IP, 9999 is port number,we bind socket with port number

s.listen(5)#5 clients

print("Waiting for connection")
while True:
    c, addr= s.accept()#If we want the server,gives client socket 'c' and address
    print("Connected with ",addr)
    
    
    fromClient = c.recv(1024)
    print(fromClient)
    if type(fromClient)==bytes:
        fromClient=int(fromClient.decode('utf-8'))
        print(fromClient)
        choice = int(fromClient)
   
    if(choice == 0):  

        query=speech_to_text()
        app1 = ''.join(query)
        query = str(app1)
        app = query.split()
        print('entered choice 0')
        print(query)
        work(query)
       
    elif(choice==1):
        # query = c.recv(1024)#to recv query
        # if type(query)==bytes:
        #     query=query.decode()
        #     print(query)
            # Logic for executing tasks based on query
            
            wishMe()
            c.send(bytes('stop','utf-8'))
            print('the choice is 1')
            query = c.recv(2048)
            if type(query)==bytes:
                query=query.decode()
            work(query)
            c.send(bytes('start','utf-8'))
        
        # elif 'open code' in query:
        #     codePath = ""C:\Users\ironk\AppData\Local\Programs\Microsoft VS Code\Code.exe""
        #     os.startfile(codePath)