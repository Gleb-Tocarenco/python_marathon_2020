from datetime import date, datetime

from flask import Flask
from flask import request
from flask import render_template

from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!!!"


@app.route('/second-route')
def second_route():
    return 'Second route'

@app.route('/user/<name>/<last_name>/')
def show_profile_username(name, last_name):
    return f'Hello {escape(name)}, {escape(last_name)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/search/')
def show_query_params():
    searchword = request.args.get('key')
    return f'You are looking for {searchword}'


@app.route('/date/')
def date_route():
    now = datetime.now()
    return f'In Chisinau time is {now}'


@app.route('/template')
def tempalte_route():
    user = {'username': 'Gleb'}
    posts = [
        {
            'author': {'username': 'Vasile'},
            'body': 'Beautiful day in Chisinau!'
        },
        {
            'author': {'username': 'Ion'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', **{'title': 'My title', 'user': user, 'posts': posts})
