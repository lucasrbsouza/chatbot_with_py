# Google Generative AI Chatbot com Python

Este projeto é um exemplo de chatbot em Python utilizando a biblioteca `google.generativeai`. O chatbot usa o modelo generativo "gemini-1.5-flash" da Google, configurado para se identificar como "Yan do ICEV", um especialista em gatos, e responder a perguntas do usuário em um loop de conversação.

## Pré-requisitos

Para rodar este projeto, você precisa de:

1. **Python**: Versão 3.7 ou superior.
2. **google.generativeai**: Biblioteca necessária para se conectar com o modelo da Google. Para instalá-la, execute o comando:
   ```bash
   pip install google-generativeai

# Configuração
No código, você deverá substituir {GOOGLE_API} pela sua chave de API do Google Generative AI. A configuração do modelo ocorre no trecho abaixo:
    genai.configure(api_key = {GOOGLE_API})

# Estrutura e Funcionamento
Configuração do Modelo: O modelo "gemini-1.5-flash" é configurado com uma instrução de sistema (system_instruction) para que o chatbot se chame "Yan do ICEV" e seja um especialista em gatos.

Histórico Inicial: Um breve histórico de conversação é inicializado, contendo uma pergunta ("Qual o melhor jogador de futebol de todos os tempos?") e uma resposta ("O Pelé é o maior jogador de futebol de todos os tempos"). Isso ajuda a contextualizar o modelo antes de iniciar o chat.

Loop de Conversação:

O código entra em um loop onde o usuário pode enviar mensagens para o chatbot.
A resposta é exibida no terminal em tempo real.
Ao final de cada interação, o usuário tem a opção de sair do loop digitando s.

# Exemplo de Interação

![image](https://github.com/user-attachments/assets/d977a9e4-a58d-4562-a509-9dcf34cb8c5d)

# Observação
Este é um exemplo simples de interação com o Google Generative AI. Para outros casos de uso, você pode ajustar o system_instruction para fornecer um contexto diferente ao chatbot.
