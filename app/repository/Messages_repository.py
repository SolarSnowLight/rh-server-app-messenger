from app import db
from ..models.Messages import Messages
from ..models.Chat import Chats


def create(message_data):
    chat = db.session.query(Chats).filter(Chats.id==message_data.chat_id).first()
    if int(message_data.user_id) == int(chat.user_id1) or int(message_data.user_id) == int(chat.user_id2):
        msg = Messages(chat_id=message_data.chat_id, user_id=message_data.user_id, message=message_data.message)
        db.session.add(msg)
        db.session.commit()

        return f'message saved'
    else:
        return f'user {message_data.user_id} not in chat'


def get_messages_list():
    messages = Messages.query.all()
    return messages


def get_current_message(message_id):
    message = db.session.query(Messages).filter(Messages.id==message_id).first()
    return message


def update_message(message_data, message_id):
    msg = db.session.query(Messages).filter(Messages.id==message_id).first()
    msg.chat_id = message_data.chat_id
    msg.user_id = message_data.user_id
    msg.message = message_data.message

    db.session.commit()
    return f'message updated'


def delete_message(message_id):
    message = Messages.query.filter_by(id=message_id).delete()
    db.session.commit()

    return f'message with id {message_id} deleted'