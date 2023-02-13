# Flask template 
from flask import Flask, request
import telegram
import os

app = Flask(__name__)
TOKEN=os.environ["TOKEN"]
bot = telegram.Bot(token=TOKEN)

WEBHOOK_URL = 'https://7a3a-84-54-76-136.eu.ngrok.io/'

@app.route('/')
def home():
    return '<h1>Flask template</h1>'

@app.route('/set', methods=['GET'])
def set_webhook():
    bot.setWebhook(WEBHOOK_URL)
    print(bot.getWebhookInfo())
    return 'Webhook set'

@app.route('/api', methods=['POST'])
def bot_app():
    bot.sendMessage(chat_id=chat_id, text='Hello World')
    print("Message sent")
    return {'ok': True}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)