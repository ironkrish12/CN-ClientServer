import socket
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from os import path
from pydub import AudioSegment

n = 0


isSpeech=input("PLEASE ENTER 0 IF YOU WANT TO PASS AUDIO FILE ELSE ENTER 1 FOR VOICE COMMAND.")

def takeCommand():
    #It takes microphone input from the user and returns string output
    
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            #bin_result = ''.join(format(ord(x), '08b') for x in query)
            #print(bin_result)
            c.send(bytes(query,'utf-8'))
            print(query)

        except Exception as e:
            # print(e)
            print("Say that again please...")
            takeCommand()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
 


c = socket.socket()
c.connect(('localhost',9999))
c.send(bytes(isSpeech,'utf-8'))
print('sent')
#print(c.recv(1024))#print info recieved from server with max size 1024,will mention which type
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    '''sound = AudioSegment.from_mp3("transcript.mp3")
    sound.export("transcript.wav", format="wav")


    # transcribe audio file                                                         
    AUDIO_FILE = "transcript.wav"

    # use the audio file as the audio source                                        
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file                  

            #print("Transcription: " + r.recognize_google(audio)) '''
         
if(isSpeech == 0):
    print("Please save the audio file as 'myAudio.mp3' in the folder ''Trial1'' to proceed.")
elif(isSpeech == 1):
    print('taking speech input')
    
while True:
    query = c.recv(2048)
    if type(query)==bytes:
        query=query.decode()
        if query not in 'stop':
            takeCommand()