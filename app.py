__author__='ankit'

import os
from flask import Flask, request, Response, redirect
from moodle import main

app = Flask(__name__)


@app.route('/moodle',methods=['post'])
def moodle():
	data=main()
	

