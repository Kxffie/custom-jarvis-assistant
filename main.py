from pyChatGPT import ChatGPT
import speech_recognition as sr
import os
import pyttsx3

os.system('cls' if os.name == 'nt' else 'clear')
print("Find your session ID at https://chat.openai.com/ and right click the page.\nClick inspect and where it says \"Elements, Console, Sources etc...\" go into Application and find \"__Secure-next-auth.session-token\" and copy the value.\n")
ID = input("Please input your Session Value: ")
function = input(
    "Would you like to use the chatbot or the voice assistant? (chat/voice) ")
os.system('cls' if os.name == 'nt' else 'clear')
print("Loading ChatGPT \"Jarvis\" Assistant...")
api = ChatGPT(ID)
engine = pyttsx3.init()
engine.setProperty('rate', 130)
os.system('cls' if os.name == 'nt' else 'clear')

stoppingWords = ["stop", "goodbye", "bye", "exit", "quit"]


def main():
    if function == "chat":
        print("Type 'stop' to exit the chatbot.")
        inp = input("Type something! > ")
        if inp == "stop":
            print("---------------\nGoodbye!\n---------------")
            input("Press any button to quit...")
            exit()
        else:
            response = api.send_message(inp)
            print(f"---------------\n{response['message']}\n---------------")

    else:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source)
            finalAudio = r.recognize_google(audio).lower()
            print(finalAudio)

            try:
                print(f"You said: {finalAudio}")

                if any(word in finalAudio.split() for word in stoppingWords):
                    print("---------------\nGoodbye!\n---------------")
                    engine.say("Goodbye!")
                    engine.runAndWait()
                    input("Press any button to quit...")
                    exit()
                else:
                    engine.say("Thinking of a response...")
                    engine.runAndWait()
                    response = api.send_message(finalAudio)
                    print(
                        f"---------------\n{response['message']}\n---------------")
                    engine.say(response["message"])
                    engine.runAndWait()

            except Exception as e:
                print(f"Error: {e}")


while True:
    main()
