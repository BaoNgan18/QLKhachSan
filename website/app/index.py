from flask import Flask, render_template, request, redirect
from app import app, login
import dao
from flask_login import login_user, logout_user


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


@app.route('/login', methods=['get', 'post'])
def user_login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user)

            next = request.args.get('next')
            return redirect('/' if next is None else next)

    return render_template('login.html')


@app.route('/register', methods=['get', 'post'])
def user_register():
    err_msg = None
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        avatar = request.form.get('avatar')

        if confirm.__eq__(password):
            try:
                dao.add_user(name= name, username=username, password= password, avatar= request.files.get('avatar'))
            except Exception as e:
                print(str(e))
                err_msg = "Failure"
            else:
                return redirect('/login')
        else:
            err_msg = 'Passwords do not match'

    return render_template('register.html', err_msg=err_msg)


@app.route('/logout', methods=['get'])
def logout():
    logout_user()
    return redirect('/login')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)