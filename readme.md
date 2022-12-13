# This is a custom ChatGPT bot that is kinda like Jarvis

this is a personal project I made thinking I could recreate Jarvis from Tony Starks AI. Of course it isn't exactly -or close- to Jarvis, but this gave me a better understanding about how difficult it is making a tool assistant AI.

Written in Python, libraries used were:
pyChatGPT - https://github.com/terry3041/pyChatGPT
SpeechRecognition - https://pypi.org/project/SpeechRecognition/
PYTTSX3 - https://pypi.org/project/pyttsx3/

There are 2 modes: chat and voice:
 -Chat
   - You can type in anything and it will respond in text. Typing "stop" will end the chat.
 - Voice
   - You can say anything and with SpeechRecognition it will turn your speech into text and then ask ChatGPT what you said and it will respond in a voice and text for hearing and visual output. You can also say things like "stop", "goodbye", "bye", "exit", "quit" to exit the program by voice, or just exiting out.
   
I want to add more functionality to it, since the ChatGPT only knows 2021 and past, so you can't ask it about the weather or what not, but I want to add kind of a term based questioning for common things. Like if you ask something and it contains the word "weather" it will reply with a different api like a weather api and completely forget about the chatgpt. I am hoping with more release the better I can make this.

## Links

Download Tool in EXE format - https://kxffie.itch.io/chatgpt-jarvis-assistant
Or you can make it yourself using the source code!
