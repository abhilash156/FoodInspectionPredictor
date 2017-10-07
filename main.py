import sys
import json
from flask import Flask, render_template, request
from watson_developer_cloud import ToneAnalyzerV3

app = Flask(__name__)

user = {
    "url": "https://gateway.watsonplatform.net/tone-analyzer/api",
    "username": "c8fe566d-2e12-442c-98bf-6586750f9389",
    "password": "GLlc2TbzFqvD"
}


@app.route('/', methods=['GET'])
def home():
    return "Hello World!"


@app.route('/baymax', methods=['GET'])
def baymax():
    return "<h1>Hello, I am Baymax!</h1>"


@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    return "<h1>Addition : " + str(a + b) + "</h1>"


@app.route('/square', methods=['GET'])
def get_square():
    return render_template('square.html')


@app.route('/square', methods=['POST'])
def post_square():
    result = int(request.values['x']) ** 2
    return render_template('square.html', result)


@app.route('/tone', methods=['GET'])
def get_tone():
    return render_template('square.html')


@app.route('/tone', methods=['POST'])
def post_tone():
    # from IPython import embed; embed()
    version = '2016-05-17'
    text = request.values['text']
    tone = ToneAnalyzerV3(username=user.username, password=user.password, version=version)
    doc = tone.tone(text)

    tones = doc['document_tone']['tone_categories'][0]['tones']
    return render_template('tone.html', tones)


app.run(host='0.0.0.0', port=3156, debug=True)
