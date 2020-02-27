from flask import Flask
from flask import request
from datetime import datetime
import telegram
import yaml
import os
import json
import sys


app = Flask(__name__)

config_path = "config/config.yaml"

def get_configuration_from_file():
    with open(config_path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data

def get_configuration_from_env():
    token = os.getenv('DEFAULT_BOT_TOKEN')
    chat_id = os.getenv('DEFAULT_CHAT_ID')
    data = dict()
    data['default'] = {'bot_token': token, 'chat_id': chat_id}
    return data

def get_configuration():
    try:
        config = get_configuration_from_file()
    except:
        config = get_configuration_from_env()
    return config

def parse_data(data):
    result = []
    try:
        for alert in data['alerts']:
            messege = ""
            messege += 'Status: ' + alert['status'] + '\n'
            messege += 'Name: ' + alert['labels']['alertname'] + ' ['+ alert['labels']['severity'] + ']' + '\n'
            messege += 'Description: ' + alert['annotations']['description']
            result.append(messege)
    except KeyError as err:
        app.logger.error(f"Data : {data}")
        raise err
    return result

def send_message(bot_token, chat_id, message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

@app.route('/<path:text>', methods=['GET', 'POST'])
def root(text):
    data = request.get_json()
    messeges = parse_data(data)
    config = get_configuration()
    bot_token = config[text]['bot_token']
    chat_id = config[text]['chat_id']
    for i in messeges:
        send_message(bot_token, chat_id, i)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
