#!/usr/bin/env python3
# Kopi-CTF Challenge
# HowZ: Yujia, Hao, Su, Xiongyi

from flask import Flask, render_template,request,redirect,make_response,session

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')
        
@app.route('/search')
def search():
    return render_template('main.html', error='haha, you think I have any function here?!')

if __name__ == '__main__':
    app.config.update(SESSION_COOKIE_HTTPONLY=False)
    app.run(debug=True)
