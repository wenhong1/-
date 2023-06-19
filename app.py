from flask import Flask,render_template
from flask import url_for,redirect,request
import hashlib
import json
import random
from urllib import parse
import urllib.request as urllib_request



app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('translate'))

@app.route('/translate',methods=['GET','POST'])
def translate():
    if request.method == 'POST':
        if 'clear' in request.form:
            return render_template('translation.html')

        inpt1 = request.form['input']
        source_lang = request.form.get('source_language', 'zh')  # 默认为'zh'
        target_lang = request.form.get('target_language', 'wyw')  # 默认为'wyw'
        outpt = translate_Word(inpt1)
        outpt1 = translate_Word(source_lang, target_lang)
        return render_template('translation.html', inpt=inpt1, outpt=outpt,outpt1=outpt1)

    return render_template('translation.html')

if __name__ == '__main__':
    app.run()
