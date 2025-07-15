import requests
import os

def send_telegram_message(message: str, chat_id: str, bot_token: str):
    """
    Envía un mensaje a un chat de Telegram usando la API de Telegram.
    
    :param message: El mensaje a enviar.
    :param chat_id: El ID del chat donde se enviará el mensaje.
    :param bot_token: El token del bot de Telegram.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("Mensaje enviado correctamente.")
    else:
        print(f"Error al enviar mensaje: {response.status_code} - {response.text}")

canal = os.getenv('CANAL')
mensaje = os.getenv('MENSAJE')
token = os.getenv('TOKEN')

# Ejemplo de uso
send_telegram_message(mensaje, canal, token)
