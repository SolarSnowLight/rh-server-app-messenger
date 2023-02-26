from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from app import app, socketio
from flask_pydantic import validate
from ..services import Chat_service
from ..pydantic_models.Chats import CreateChat, UpdateChat


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


@app.route('/chat/create', methods=['POST'])
@validate()
def create_chat(body: CreateChat):
    return Chat_service.create_chat(chat_data=body)


@app.route('/chat/all', methods=['GET'])
def get_all_chats():
    return Chat_service.get_chats_list()


@app.route('/chat/<chat_id>/info', methods=['GET'])
def get_current_chat(chat_id: str):
    return Chat_service.get_current_chat(chat_id=chat_id)


@app.route('/chat/<chat_id>/update', methods=['PUT'])
@validate()
def update_chat(chat_id: str, body: UpdateChat):
    return Chat_service.update_chat(chat_data=body, chat_id=chat_id)


@app.route('/chat/<chat_id>/delete', methods=['DELETE'])
@validate()
def delete_chat(chat_id: str):
    return Chat_service.delete_chat(chat_id=chat_id)


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
