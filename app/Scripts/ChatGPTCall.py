import sys
from openai import OpenAI
import os
from dotenv import load_dotenv


def ChatGPTCall(captionMessage):
    dotenv_path = "/home/admin/Escritorio/Lesser/.env"
    load_dotenv(dotenv_path)
    client = OpenAI(api_key=os.getenv("CHATGPT_API_KEY"),)

    chat_completion = client.chat.completions.create(messages=[
        {
            "role": "system",
            "content": "Estás hablando con un asistente de IA que puede resumir textos."
        },
        {
            "role": "user",
            "content": f"Por favor, hazme un resumen del siguiente texto para que lo entienda alguien sin contexto utilizando un lenguaje muy natural y poco analítico. No añadas nada más que el resumen: {captionMessage}"
        }
    ],
        model="gpt-3.5-turbo",)

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    captionMessage = sys.argv[1]
    resumen = ChatGPTCall(captionMessage)
    print(resumen)
