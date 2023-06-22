!pip install --upgrade revChatGPT
!pip install revChatGPT
!pip show revChatGPT
!pip install googlesearch-python
!pip install beautifulsoup4 requests

from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "access_token": "", #Ingresa tu acces token
    "model": "gpt-3.5-turbo-16k",
})
# Se envia la personalidad junto con lo que ingresa el usuario
def ask_chatgpt(personality, context, message):
    print("Chatbot:")
    prev_text = ""
    
    full_context = personality + context

    # Enviar mensaje a la API
    for data in chatbot.ask(full_context + message, language="es"):
        response = data["message"][len(prev_text):]
        print(response, end="", flush=True)
        prev_text = data["message"]

    return context

# Leer el contenido del archivo de personalidad
with open('personalidad.txt', 'r') as file:
    personality = file.read()

context = ""
message = input("User: ")
print("\n")

# Enviar la personalidad solo una vez al inicio
context = ask_chatgpt(personality, context, message)
context += message + "\nChatbot: "

while True:
    print("\n")
    message = input("User: ")
    print("\n")
    context = ask_chatgpt(personality, context, message)
    context += message + "\nChatbot: "
