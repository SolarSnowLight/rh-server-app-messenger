from ..repository import Chats_repository
from flask import jsonify

def create_chat(chat_data):
    try:
        Chats_repository.create_chat(chat_data=chat_data)

        return jsonify({'message': f'new chat created'})
    except Exception as e:
        print(e)
        return jsonify({'message': str(e)})


def get_chats_list():
    try:
        chats = []

        for chat in Chats_repository.get_chats_list():
            chats.append(
                {   
                    'id': chat.id,
                    'uuid': chat.uuid,
                    'user_id1': chat.user_id1,
                    'user_id2': chat.user_id2,
                    'created_at': chat.created_at,
                    'modified_at': chat.modified_at
                }
            )

        return jsonify(chats)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def get_current_chat(chat_id):
    try:
        chat = Chats_repository.get_current_chat(chat_id=chat_id)

        return jsonify({
            'id': chat.id,
            'uuid': chat.uuid,
            'user_id1': chat.user_id1,
            'user_id2': chat.user_id2,
            'created_at': chat.created_at,
            'modified_at': chat.modified_at
        })
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def update_chat(chat_data, chat_id):
    try:
        return Chats_repository.update_chat(chat_data=chat_data, chat_id=chat_id)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})


def delete_chat(chat_id):
    try:
        return Chats_repository.delete_chat(chat_id=chat_id)
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})