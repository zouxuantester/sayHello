from sayhello import app, db
from flask import render_template, redirect, url_for, flash
from sayhello.forms import MessageForm
from sayhello.models import Message


@app.route('/', methods=['POST', 'GET'])
def index():
    # return "<h1>Say Hello to the world</h1>"
    messages = Message.query.order_by(Message.create_time.desc()).all()
    form = MessageForm()
    # post 请求验证表单后提交数据
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('哇，你的信息已经被全世界接收！！！')
        return redirect(url_for('index'))
    # Get请求直接返回index页面
    return render_template('index.html', form=form, messages=messages)
