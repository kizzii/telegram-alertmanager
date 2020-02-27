# Telegram-Alertmanager

This is an API for allowing Alert Manager from Prometheus send messages to Telegram

Require:
  - [prom/alertmanager:v0.20.0](https://hub.docker.com/r/prom/alertmanager)
  - [Telgram Bot](https://core.telegram.org/bots)
 
# How to use this image

**via docker run**
```bash
docker run -d -name my-telegram-alertmanager -p 8000:80 \
-e DEFAULT_BOT_TOKEN=<telegram_bot_token> \
-e DEFAULT_CHAT_ID=<chat_id> \
kizzii/telegram-alertmanager:latest
```

**via docker-compose**
 
 ```yaml
version: "3.5"
services:
  telegram-alertmanger:
    image: kizzii/tlegram-alertmanger:latest
    container_name: telgram.alertmanger
    hostname: telegram-alertmanger
    environment:
      DEFAULT_BOT_TOKEN: <TELEGRAM DEFAULT BOT TOKEN>
      DEFAULT_CHAT_ID: <TELEGRAM DEFAULT CHAT ID>
    ports:
      - "8000:80"
    # Optional if you want use more one bot and more chat room
    # volumes:
    #  - "<path to your cofig.yaml>:/var/www/html/config.yaml"
```
 Start container by `docker-compose up`
 
 #### Note:
 You must spicify either `config.yaml` or `DEFAULT_BOT_TOKEN`, `DEFAULT_CHAT_ID`
 
 
# Example configuration

You can create config.yaml to use more than one bot and chat room
**config.yaml**
```yaml
example:
  bot_token: <telegram_bot_token>
  chat_id: <telegram_chat_id>
example2:
  bot_token: <telegram_bot_token2>
  chat_id: <telegram_chat_id2>
  ...
```
Then mount this file to container 



# Telegram Bot Token and Chat ID
You need to Create Telegram Bot then you can get Bot Token and Chat ID 
[https://core.telegram.org/bots](https://core.telegram.org/bots)

