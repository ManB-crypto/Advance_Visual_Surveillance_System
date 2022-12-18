from flask import Flask, g, redirect, render_template, request, session, url_for, Response
import os
import cv2
from appy import *
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []
users.append(User(id=1, username='manb', password='123'))
users.append(User(id=2, username='sus', password='secret'))
users.append(User(id=3, username='abidin', password='222'))

app = Flask(__name__)
app.secret_key = 'only1willknow'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')








@app.route('/video')
def vid():
    return render_template('video.html')

@app.route('/videoa')
def vida():
    os.system("play beep.mp3")
    return render_template('video.html')


@app.route('/beuty')
def beuty():
    return render_template('navbar.html')

@app.route('/instruct')
def instruct():
    return render_template('instruct.html')


@app.route('/vid')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)


@app.route('/obon')
def obon():
    os.system('python pp.py')

    return render_template('objectbutton.html')


@app.route('/oboff')
def oboff():
    os.system('pkill -f pp.py')
    return render_template('objectbutton.html')


@app.route('/mmon')
def mmon():
    os.system('python mm.py')

    return render_template('movebutton.html')


@app.route('/mmoff')
def mmoff():
    os.system('pkill -f mm.py')
    return render_template('movebutton.html')



@app.route('/kil')
def kill():
    os.system('pkill -f appy.py')
    return render_template('video.html')