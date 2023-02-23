from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
from ..pydantic_models.Users import CreateUser, UpdateUser
from flask_pydantic import validate
from ..services import User_service
from flask_sqlalchemy import SQLAlchemy
from app import app, socketio

# app = Flask(__name__)
# app.config.from_object('config.DevelopConfig')
# db = SQLAlchemy(app)

# Session(app)

# socketio = SocketIO(app, manage_session=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        username = request.form['username']
        room = request.form['room']
        session['username'] = username
        session['room'] = room
        return render_template('chat.html', session=session)
    elif session.get('username'):
        return render_template('chat.html', session=session)

    return redirect(url_for('index'))


@socketio.on('join', namespace='/chat')
def join(message):
    room = session.get('room')
    join_room(room)
    emit(
        'status',
        {'msg':  session.get('username') + ' has entered the room.'},
        room=room
    )


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    emit(
        'message',
        {'msg': session.get('username')
            + ' : '
            + message['msg']
         },
        room=room
    )


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit(
        'status',
        {'msg': username
            + ' has left the room.'
         },
        room=room
    )
    print('left!!!')


@app.route('/users/create', methods=['POST'])
@validate()
def create_user(body: CreateUser):
    print('data get')
    return User_service.create_user(user_data=body)


@app.route('/users/all', methods=['GET'])
def get_all_users():
    return User_service.get_users_list()


@app.route('/users/<name>/info', methods=['GET'])
def get_current_user(name: str):
    return User_service.get_current_user(name=name)


@app.route('/users/<name>/update', methods=['PUT'])
@validate()
def update_user(name: str, body: UpdateUser):
    return User_service.update_user(user_data=body, name=name)


@app.route('/users/<name>/delete', methods=['DELETE'])
@validate()
def delete_user(name: str):
    return User_service.delete_user(name=name)


# if __name__ == '__main__':
#     # db.init_app(app)
#     app.app_context().push()
#     db.create_all()
#     socketio.run(app)
