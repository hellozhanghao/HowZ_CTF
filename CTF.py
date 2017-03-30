#!/usr/bin/env python3
# Kopi-CTF Challenge
# HowZ: Yujia, Hao, Su, Xiongyi

from flask import Flask, render_template,request,redirect,make_response,session
import sqlite3
import os
import hashlib

app = Flask(__name__)

def hash(data):
    """ Wrapper around sha224 """
    return hashlib.sha224(data.replace('\n','').encode('ascii')).hexdigest()

@app.route('/')
def main():
    return render_template('main.html')
        
@app.route('/search')
def search():
    term = request.args.get('term')
    return render_template('main.html',error="Search not implemented yet. Could not find "+term)

@app.route('/ping', methods=['POST'])
def ping():
    cmd = 'ping -c 1 '+ request.form['target']
    stream = os.popen(cmd)
    rval = stream.read()
    return render_template('main.html', error3=rval)

if __name__ == '__main__':
    app.config.update(SESSION_COOKIE_HTTPONLY=False)
    app.run(debug=True)
