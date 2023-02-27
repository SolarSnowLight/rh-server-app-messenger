from app import db
from app import Chat, User

def create_chat(chat_data):
    user1 = db.session.query(User.Users).filter(User.Users.id==chat_data.user_id1).first()
    user2 = db.session.query(User.Users).filter(User.Users.id==chat_data.user_id2).first()
    chat = Chat.Chats(user_id1=user1.id, user_id2=user2.id)

    db.session.add(chat)
    db.session.commit()

    return f'new chat created'


def get_chats_list():
    chats = Chat.Chats.query.all()
    return chats


def get_current_chat(chat_id):
    chat = db.session.query(Chat.Chats).filter(Chat.Chats.id==chat_id).first()
    return chat


def update_chat(chat_data, chat_id):
    chat = db.session.query(Chat.Chats).filter(Chat.Chats.id==chat_id).first()
    
    chat.user_id1 = chat_data.user_id1
    chat.user_id2 = chat_data.user_id2

    db.session.commit()

    return f'chat with id {chat_id} updated'


def delete_chat(chat_id):
    chat = Chat.Chats.query.filter_by(id=chat_id).delete()
    db.session.commit()

    return f'chat with id {chat_id} deleted'
