# Base image
FROM python:3.9-slim-buster

# Copying the code to the container
COPY . /app
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y git && \
    pip install --no-cache-dir pyTelegramBotAPI openai

# Expose the port for the bot
EXPOSE 81

# Start the bot
CMD ["python", "chat_gpt.py"]
