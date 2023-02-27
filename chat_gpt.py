# creating a Telegram bot to communicate with the OpenAI neural network

# pip install pyTelegramBotAPI
# pip install openai

import telebot
import openai
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = API_KEY

@bot.message_handler(content_types=["text"])
def handle_text(message):
    logging.info(f'Received message: {message.text}')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    logging.info(f'Sending response: {response.choices[0].text}')
    bot.send_message(message.chat.id, response.choices[0].text)

bot.polling()
