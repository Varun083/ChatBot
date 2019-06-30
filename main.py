import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
active=False
order=[]
number=[]

message="Hello"
engine.say(message)
engine.runAndWait()
r = sr.Recognizer()


def takeOrder():
    with sr.Microphone() as source:
        audio = r.listen(source)
        input1 = r.recognize_google(audio)
        order.append(input1)
        print(order)
        engine.say("Give me the number")
        engine.runAndWait()
        with sr.Microphone() as source:
            audio = r.listen(source)
            input1 = r.recognize_google(audio)
            number.append(input1)
            print(number)



with sr.Microphone() as source:
    print("hi")
    audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        if (command == 'hello'):
            engine.say("Do you need any suggestions")
            engine.runAndWait()
            with sr.Microphone() as source:
                audio = r.listen(source)
                input = r.recognize_google(audio)
                if(input=='yes'):
                    print("Biryani, Choco lava cake")
                    engine.say("dO YOU WANT TO CHOOSE FROM THE BOVE ONES")
                    engine.runAndWait()
                    with sr.Microphone() as source:
                        print("dO YOU WANT TO CHOOSE FROM THE aBOVE ONES")

                        audio = r.listen(source)
                        input1=r.recognize_google(audio)
                        if(input1=='yes'):
                            print("Tell me the order")
                            engine.say("Tell me the order")
                            engine.runAndWait()
                            takeOrder()
                            t=True
                            while t:
                                print("Do you want more orders?")
                                engine.say("Do you want more orders?")
                                engine.runAndWait()
                                with sr.Microphone() as source:
                                    audio = r.listen(source)
                                    input1 = r.recognize_google(audio)
                                    if(input1=='yes'):
                                        takeOrder()
                                    elif(input1=='no'):
                                        print('thankyou')
                                        t=False



                        else:
                            print("Sorry")
                            engine.say("Sorry!")
                            engine.runAndWait()

    except sr.UnknownValueError:
        command = ""
