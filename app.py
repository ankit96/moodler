__author__ = 'ankit'

import os
from flask import Flask,request, redirect, Response
from moodle import main
import requests
import json
import re
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/moodle', methods=['post'])
def moodler():

    text = request.values.get('text')
    data = main(str(text))
    return Response(str(data),content_type="text/plain; charset=utf-8" )

@app.route('/')
def hello():
    return redirect('https://github.com/ankit96/moodler')


if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
