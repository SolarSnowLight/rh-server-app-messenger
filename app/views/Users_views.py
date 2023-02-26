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


@app.route('/users/create', methods=['POST'])
@validate()
def create_user(body: CreateUser):
    return User_service.create_user(user_data=body)


@app.route('/users/all', methods=['GET'])
def get_all_users():
    return User_service.get_users_list()


@app.route('/users/<user_id>/info', methods=['GET'])
def get_current_user(user_id: str):
    return User_service.get_current_user(user_id=user_id)


@app.route('/users/<user_id>/update', methods=['PUT'])
@validate()
def update_user(user_id: str, body: UpdateUser):
    return User_service.update_user(user_data=body, user_id=user_id)


@app.route('/users/<user_id>/delete', methods=['DELETE'])
@validate()
def delete_user(user_id: str):
    return User_service.delete_user(user_id=user_id)


# if __name__ == '__main__':
#     # db.init_app(app)
#     app.app_context().push()
#     db.create_all()
#     socketio.run(app)
