from flask import render_template,url_for,request,flash,redirect
from flask_login import login_user,login_required,logout_user,current_user
from ..models import User
from . import auth
from .forms import LoginForm,RegistrationForm
from .. import db

@auth.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data.lower()).first()
        if user is not None and form.password.data == '123456':
            login_user(user,form.remember_me.data)
            flash('登录成功')
            #根据github上的flasky文档修改内容
            next = request.args.get('next')
            if next is None or not next.startwith('/'):
                next = url_for('main.index')
            return redirect(next)
            #原书上内容// return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效的用户名或密码')
    return render_template('auth/login.html',form = form)

@auth.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功，现在你可以用此邮箱登录')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出登录...')
    return redirect(url_for('main.index'))