import speech_recognition as sr

def speech_recognizer():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        task = r.recognize_google(audio, language='en-in')
        print("You said: " + task)

    except Exception as e:
        print(e)
        print("Sorry couldn't get you, try again...'")