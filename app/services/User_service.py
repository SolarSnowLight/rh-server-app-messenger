import os
import datetime
from ..repository import Users_repository
from flask import jsonify


def create_user(user_data):
    print('pre try')
    try:
        print('rty')
        name = user_data.name
        avatar = user_data.avatar
        token = str(os.urandom(32))
        status = True
        time_connected = datetime.datetime.now()

        print('registr')
        Users_repository.create(name=name, avatar=avatar, token=token, status=status, time_connected=time_connected)

        return jsonify({'message': f'user {name} created'})
    except Exception as e:
        return jsonify({'message': 'error'})


def get_users_list():
    try:
        return Users_repository.get_users_list()
    except Exception as e:
        return jsonify({'message': 'error'})


def get_current_user(name):
    try:
        user = Users_repository.get_current_user(name=name)

        return jsonify({
            "id": user.uuid,
            "name": user.name,
            "avatar": user.avatar,
            "status": user.status
        })
    except Exception as e:
        return jsonify({'message': 'error'})


def update_user(user_data, name):
    try:
        return Users_repository.update_user(user_data=user_data, name=name)
    except Exception as e:
        return jsonify({'message': 'error'})


def delete_user(name):
    try:
        return Users_repository.delete_user(name=name)
    except Exception as e:
        return jsonify({'message': 'error'})