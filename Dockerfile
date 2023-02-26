# Base image
FROM python:3.9-slim-buster

# Copying the code to the container
COPY . /github.com/cronnoss/chat-gpt-telegram-bot-py/
WORKDIR /github.com/cronnoss/chat-gpt-telegram-bot-py/

# Install dependencies
RUN apt-get update && apt-get install -y git && \
    pip install --no-cache-dir pyTelegramBotAPI openai

# Expose the port for the bot
EXPOSE 80

# Start the bot
CMD ["python3", "chat_gpt.py"]
