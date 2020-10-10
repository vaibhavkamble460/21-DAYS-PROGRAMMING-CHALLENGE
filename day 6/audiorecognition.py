import pyttsx3
import speech_recognition as sr
def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold=0.7
        audio=r.listen(source)
        try:
            print('Rcognizing')
            Query=r.recognize_google(audio,language='en-in')
            print("the query is printed='",Query,"'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query
def speak(audio):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()

if __name__== '__main__':
    while True:
        command=take_command()
        if "exit" in command:
            speak("sure sir! as your wish,bai")
            print("sure sir!as your wish.bai")
            break
        if "insta" in command:
            speak("Best Python page")
            print("Best Python page")
        if "learn" in command:
            speak("copy assignment website is best to learn python")
            print("copy assignment website is best to learn python")
        if "code" in command:
            speak("you can get this code from copyassignment website")
            print("you can get this code from copyassignment website")