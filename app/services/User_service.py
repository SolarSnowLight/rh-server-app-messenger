import os
import datetime
from ..repository import Users_repository
from flask import jsonify


def create_user(user_data):
    try:
        name = user_data.name
        token = str(os.urandom(32))
        status = True
        time_connected = datetime.datetime.now()

        Users_repository.create(name=name, token=token, status=status, time_connected=time_connected)

        return jsonify({'message': f'user {name} created'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def get_users_list():
    try:
        users = []

        for user in Users_repository.get_users_list():
            users.append(
                {   
                    "id": user.id,
                    'uuid': user.uuid,
                    'name': user.name,
                    'status': user.status
                }
            )

        return jsonify(users)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def get_current_user(user_id):
    try:
        user = Users_repository.get_current_user(user_id=user_id)

        return jsonify({
            "id": user.id,
            "uuid": user.uuid,
            "name": user.name,
            "status": user.status
        })
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def update_user(user_data, user_id):
    try:
        return Users_repository.update_user(user_data=user_data, user_id=user_id)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def delete_user(user_id):
    try:
        return Users_repository.delete_user(user_id=user_id)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})