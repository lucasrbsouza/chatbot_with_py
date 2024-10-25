#Versão 2
import google.generativeai as genai

genai.configure(api_key = {GOOGLE_API})

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction="Seu nome vai ser 'Yan do ICEV', e voce vai ser especialista em gatos")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Qual o melhor jogador de futebol de todos os tempos?"},
        {"role": "model", "parts": "O Pelé é o maior jogador de futebol de todos os tempos"},
    ]
)

while(True):
    response = chat.send_message(input(), stream= True)
    for i in response:
        print(i.text)
    sair = input("Digite s se deseja sair: ")
    if sair == 's':
        break
    else:
        continue