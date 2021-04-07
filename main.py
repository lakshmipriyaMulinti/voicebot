import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk (text):
   engine.say(text)

   engine.runAndWait()
def take_command():
 try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener .listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'john' in command:
            talk('Hey this is john how can i help you priya')

            print(command)
 except:
    pass
 return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play', '')
        talk('yes madam priya Iam playing a song for you'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
       time = datetime.datetime.now().strftime("%I:%M %A")
       print(time)
       talk('madam priya The current is'+ time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,4)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_jokes())
        talk(pyjokes.get_jokes())
    else:
        talk('could you tell the command again  .')
while True:
    run_alexa()

run_alexa()
