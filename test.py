url='https://api.telegram.org/bot1747040677:AAHl1HmMIQktFbiZ7sUJdkgXj3pCCg7iThk/'
import requests
import json
import os
from flask import Flask
from flask import request
from flask import Response
app=Flask(__name__)

def get_all_updates():
    response=requests.get(url+'getUpdates')
    return response.json()
def get_last_updats(allupdates):
    return allupdates['result'][-1]
def get_chat_id(update):
    return update['message']['chat']['id']
def send_message(chat_id,text):
    senddata={'chat_id' : chat_id, 'text' :text}
    response = requests.post(url+'sendMessage',senddata)
    return response

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        msg=request.get_json()
        chat_id=get_chat_id(msg)
        text=msg['message'].get('text','')
        if text == '/start':
            send_message(chat_id,'Welcom!')
        elif text=='':
            pass
        return Response('ok', status=200)
    else:
        return ""
def write_json(data,filename="math.json"):
    with open(filename,'w') as target:
        json.dump(data,target,indent=4,ensure_ascii=False)
def read_json(filename="math.json"):
    with open(filename,'r') as target:
        data=json.load(target)
    return data

app.run(debug=True)
