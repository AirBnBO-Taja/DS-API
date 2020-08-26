from flask import Flask, request

"""
Henry's work for BW_U3
"""


app = Flask(__name__)

@app.route('/')
def root():
    """ This is the base view"""
    return 'Henry Gultom'


@app.route('/json')

def nine():
    return 'Test - Henry'

@app.route('/joni/<name>')
def name(name):
    return" my name is <name>" + name

