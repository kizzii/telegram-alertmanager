from flask import Flask
from flask import request
from datetime import datetime
import telegram
import yaml
import os


app = Flask(__name__)

def get_configuration_from_file():
    with open(r'config.yaml') as file:
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
    result = ""
    for alert in data['alerts']:
        messege = ""
        messege += 'Status: ' + alert['status'] + '\n'
        messege += 'Name: ' + alert['labels']['alertname'] + ' ['+ alert['labels']['severity'] + ']' + '\n'
        messege += 'Description: ' + alert['annotations']['description'] + '\n'
        start_at = datetime.strptime(alert['startsAt'][:-4], "%Y-%m-%dT%H:%M:%S.%f")
        messege += 'Starts at: ' + start_at.strftime('%d-%m-%Y %H:%M') + '\n'
        if alert['status'] == 'resolved':
            ends_at = datetime.strptime(alert['endsAt'][:-4], "%Y-%m-%dT%H:%M:%S.%f")
            messege += 'Ends at: ' + ends_at.strftime('%d-%m-%Y %H:%M') + '\n'
        result += messege
    return result

def send_message(bot_token, chat_id, message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

@app.route('/<path:text>', methods=['GET', 'POST'])
def root(text):
    data = request.get_json()
    message = parse_data(data)
    config = get_configuration()
    bot_token = config[text]['bot_token']
    chat_id = config[text]['chat_id']
    send_message(bot_token, chat_id, message)
    return message
