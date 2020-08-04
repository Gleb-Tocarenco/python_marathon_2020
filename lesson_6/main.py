import io
import csv

from datetime import date, datetime

from flask import Flask
from flask import request
from flask import render_template, flash, redirect, url_for
from flask import make_response
from flask_json import FlaskJSON, json_response, as_json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from markupsafe import escape

from config import Config
from forms import LoginForm


app = Flask(__name__)
app.config.from_object(Config)
FlaskJSON(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import User, Post

@app.route('/')
@app.route('/index-url')
def index():
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
           form.username.data, form.remember_me.data))
        return redirect(url_for('.index'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/json-reponse')
@as_json
def json_route():
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
    return posts


@app.route('/download')
def download():
    io_file = io.StringIO()
    csv_writer = csv.writer(io_file)

    csv_list = [
        ['id', 'name', 'email'],
        ['1', 'Vasie', 'vasile@gmail.com'],
        ['2', 'Ion', 'ion@gmail.com']
    ]
    csv_writer.writerows(csv_list)
    output = make_response(io_file.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=fisier_csv.csv"
    output.headers["Content-type"] = "text/csv"
    return output


@app.route('/users')
@as_json
def list_users():
    users = User.query.all()
    data = []
    for user in users:
        data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })
    return data

@app.route('/posts/<int:user_id>')
@as_json
def list_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id)
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'body': post.body,
            'timestamp': post.timestamp
        })
    return data