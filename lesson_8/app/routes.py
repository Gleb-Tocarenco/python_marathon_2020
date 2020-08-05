from flask import render_template, flash, redirect, url_for
from flask import request
from app import app
from app import db
from app.forms import LoginForm, PostForm
#...
from app.models import User, Post

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', title='Home', users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
           form.username.data, form.remember_me.data))
        return redirect(url_for('.index'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/posts/<int:user_id>/')
def posts(user_id):
    user = User.query.get(user_id)
    posts = Post.query.filter_by(user_id=user_id)
    return render_template('posts.html', user=user, posts=posts)


@app.route('/posts/<int:user_id>/add/', methods=['GET', 'POST'])
def add_post(user_id):
    user = User.query.get(user_id)
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, author=user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts', user_id=user.id))
    return render_template('post_form.html', user=user, form=form, header='Add new post for')



@app.route('/posts/<int:user_id>/edit/<int:post_id>/', methods=['GET', 'POST'])
def edit_post(user_id, post_id):
    user = User.query.get(user_id)
    post = Post.query.get(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('posts', user_id=user.id))
    if request.method == 'GET':
        form.body.data = post.body
    return render_template('post_form.html', user=user, form=form, header='Edit post for user')
    

@app.route('/posts/<int:user_id>/delete/<int:post_id>')
def delete_post(user_id, post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts', user_id=user_id))