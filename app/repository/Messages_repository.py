from app import db
from ..models.Messages import Messages

def create(message_data):
    msg = Messages(chat_id=message_data.chat_id, user_id=message_data.user_id, message=message_data.message)
    db.session.add(msg)
    db.session.commit()

    return f'message saved'


def get_messages_list():
    messages = Messages.query.all()
    return messages


def get_current_message(message_id):
    message = db.session.query(Messages).filter(Messages.uuid==message_id).first()
    return message


def update_message(message_data, message_id):
    msg = db.session.query(Messages).filter(Messages.uuid==message_id).first()
    msg.chat_id = message_data.chat_id
    msg.user_id = message_data.user_id
    msg.message = message_data.message

    db.session.commit()
    return f'message updated'


def delete_message(message_id):
    message = Messages.query.filter_by(uuid=message_id).delete()
    db.session.commit()

    return f'message with id {message_id} deleted'