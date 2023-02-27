from ..repository import Messages_repository
from flask import jsonify


def create_message(message_data):
    try:
        return jsonify({'message': f'{Messages_repository.create(message_data=message_data)}'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def get_messages_list():
    try:
        messages_list = Messages_repository.get_messages_list()

        messages = []

        for message in messages_list:
            messages.append(
                {   
                    'id': message.uuid,
                    'chat_id': message.chat_id,
                    'user_id': message.user_id,
                    'message': message.message
                }
            )

        return jsonify(messages)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def get_current_message(message_id):
    try:
        message = Messages_repository.get_current_message(message_id=message_id)

        return jsonify({
            "id": message.uuid,
            "chat_id": message.chat_id,
            "user_id": message.user_id,
            'message': message.message
        })
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def update_message(message_data, message_id):
    try:
        return Messages_repository.update_message(message_data=message_data, message_id=message_id)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def delete_message(message_id):
    try:
        return Messages_repository.delete_message(message_id=message_id)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})