from datetime import datetime
from flask import Flask, render_template, request, make_response, redirect, abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('Qual o seu nome?', validators= [DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return render_template('user.html',
                           name=name,
                           prontuario=prontuario,
                           instituicao=instituicao);

@app.route('/contextorequisicao/<name>')
def contextorequisicao(name):
    user_agent = request.headers.get('User-Agent');
    remote_addr = request.remote_addr;
    remote_host = request.host;
    return render_template('contexto.html',
                           name=name,
                           user_agent=user_agent,
                           remote_addr=remote_addr,
                           remote_host=remote_host);

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
