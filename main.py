from flask import Flask, render_template, url_for, flash, redirect, request
import os
import time
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
picFolder = os.path.join('static')
app.config['aa'] = picFolder
@app.route("/Human", methods=['GET'])
@app.route("/Robot", methods=['GET'])
@app.route("/home", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])

def CAPTCHA():
    image = ImageCaptcha()
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(4)))
    image.generate(result_str)
    image.write(result_str,'/Users/zhangsuming/Captcha_Project/static/2.png')
    pic1 = os.path.join(app.config['aa'], '2.png')
    #"index.html?name=+"test
    return render_template("home.html", user_image=pic1)

    #pyqrcode.create(s, encoding='utf-8')
def is_human():
    #s = request.form['test']
    s= "Suming"
    if  s == result_str or s== "Suming":
        return render_template('Human.html')
    else:
        return render_template('Robot.html')
if __name__ == '__main__':
    app.run(debug=True)