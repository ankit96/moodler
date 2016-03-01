__author__ = 'ankit'

import os
from flask import Flask,request, redirect, Response
from moodle import main
from setuser import set,delete
import requests
import json
import re
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/moodle', methods=['post'])
def moodler():

    text = request.values.get('text')
    user_name = request.values.get('user_name')
    user_id = request.values.get('user_id')
    data = main(str(text))
    if 'Invalid' in data and 'down' in data:
        data =  "<@"+str(user_id)+'|'+str(user_name)+'>'+str(data)
        return  Response(str(data),content_type="text/plain; charset=utf-8" )
    else:
        data = "<@"+str(user_id)+'|'+str(user_name)+'>'+':Your upcoming submission deadlines'+'\n'+str(data)
        return Response(str(data),content_type="text/plain; charset=utf-8" )


@app.route('/setmoodle', methods=['post'])
def setmoodler():

    team_id = request.values.get('team_id')
    team_domain = request.values.get('team_domain')
    channel_id = request.values.get('channel_id')
    channel_name = request.values.get('channel_name')
    user_id = request.values.get('user_id')
    user_name = request.values.get('user_name')
    text = request.values.get('text')

    st=str(team_domain)+'%'+str(team_id)+'%'+str(channel_id)+'%'+str(channel_name)+'%'+str(user_id)+'%'+str(user_name)+'%'+str(text)

    data= set(str(st))

    return Response(str(data),content_type="text/plain; charset=utf-8" )


@app.route('/')
def hello():
    return redirect('https://github.com/ankit96/moodler')

@app.route('/deletemoodle', methods=['post'])
def dell():
    user_id = request.values.get('user_id')
    response = delete(user_id)
    return Response(str(response),content_type="text/plain; charset=utf-8" )


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)

