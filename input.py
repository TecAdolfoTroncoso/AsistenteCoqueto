!pip install --upgrade revChatGPT
!pip install revChatGPT
!pip show revChatGPT

from revChatGPT.V1 import Chatbot
import sys

chatbot = Chatbot(config={
     "access_token": "",
    "model": "gpt-3.5-turbo-16k",
})

#Se envia la personalidad por unica vez
def ask_chatgpt(personality, message, first_interaction=False):
    print("Chatbot:")
    prev_text = ""
    full_context = personality if first_interaction else ""

    try:
        for data in chatbot.ask(full_context + message, language="es", timeout=10):
            response = data["message"][len(prev_text):]
            print(response, end="", flush=True)
            prev_text = data["message"]
    except Exception as e:
        print(f"Ocurrió un error: {e}")

with open('personalidad.txt', 'r') as file:
    personality = file.read()

message = input("User: ")

if message.lower() in ["salir", "adiós"]:
    sys.exit()

print("\n")
ask_chatgpt(personality, message, first_interaction=True)

while True:
    print("\n")
    message = input("User: ")

    if message.lower() in ["salir", "adiós"]:
        break

    print("\n")
    ask_chatgpt(personality, message)
