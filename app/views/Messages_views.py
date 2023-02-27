from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
from ..pydantic_models.Messages import CreateMessage, UpdateMessage
from flask_pydantic import validate
from ..services import Message_service
from flask_sqlalchemy import SQLAlchemy
from app import app, socketio


@app.route('/messages/create', methods=['POST'])
@validate()
def create_message(body: CreateMessage):
    return Message_service.create_message(message_data=body)


@app.route('/messages/all', methods=['GET'])
def get_all_messages():
    return Message_service.get_messages_list()


@app.route('/messages/<message_id>/info', methods=['GET'])
def get_current_message(message_id: int):
    return Message_service.get_current_message(message_id=message_id)


@app.route('/messages/<message_id>/update', methods=['PUT'])
@validate()
def update_message(message_id: int, body: UpdateMessage):
    return Message_service.update_message(message_data=body, message_id=message_id)


@app.route('/messages/<message_id>/delete', methods=['DELETE'])
@validate()
def delete_message(message_id: int):
    return Message_service.delete_message(message_id=message_id)
