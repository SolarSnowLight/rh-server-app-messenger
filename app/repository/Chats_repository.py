from app import db
from app import Chat, User

def create_chat(chat_data):
    # try:
    user1 = db.session.query(User.Users).filter(User.Users.uuid==chat_data.user_id1).first()
    user2 = db.session.query(User.Users).filter(User.Users.uuid==chat_data.user_id2).first()
    chat = Chat.Chats(user_id1=chat_data.user_id1, user_id2=chat_data.user_id2)

    db.session.add(chat)
            
    db.session.commit()

    return f'new chat created'
    # except Exception as e:
    #     print(e)

    # return f'new chat created'


def get_chats_list():
    # try:
    chats = Chat.Chats.query.all()
    return chats
    # except Exception as e:
    #     print(e)


def get_current_chat(chat_id):
    chat = db.session.query(Chat.Chats).filter(Chat.Chats.uuid==chat_id).first()
    return chat


def update_chat(chat_data, chat_id):
    chat = db.session.query(Chat.Chats).filter(Chat.Chats.uuid==chat_id).first()
    
    chat.user_id1 = chat_data.user_id1
    chat.user_id2 = chat_data.user_id2

    db.session.commit()

    return f'chat with id {chat_id} updated'


def delete_chat(chat_id):
    chat = Chat.Chats.query.filter_by(uuid=chat_id).delete()
    db.session.commit()

    return f'chat with id {chat_id} deleted'
