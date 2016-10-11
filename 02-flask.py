#tutorial 

from flask import Flask, url_for, render_template
from jinja2 import Markup

app = Flask(__name__)
import datetime

@app.route('/')
def index():
    url = url_for('hello_named', name='Petr', count= 10)
    return '<a href="{}">Pozdrav mne!</a>'.format(url)

@app.route('/sablona/<name>/')
def hello(name):
    return render_template("text.html",
                            name=name) # TODO musi byt adresar template

@app.route('/sablona/')
def hello_bez_jmena():
    kus_html = Markup("<h2>Kapka</h2>")
    now=datetime.datetime.now()
    return render_template("text.html",
                           now = now,
                           kus_html=kus_html)

@app.route('/hello/<name>/<int:count>/') #ve spicatych zavorkach bere jako argument
def hello_named(name,count):
    result = ''
    for i in range(count):
        result += 'Hello {}!'.format(name)
    return result

@app.template_filter('time')
def human_time(t):
    return t.strftime("%Y")

'''
string
int
float
path - muze obsahovat i lomitka
'''

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, port = 5000)
