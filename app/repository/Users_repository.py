from app import db
from ..models.User import Users

def create(name, avatar, token, status, time_connected):
    user = Users(name=name, avatar=avatar, token=token, time_connected=time_connected, status=status)
    db.session.add(user)
    db.session.commit()

    return f'user {name} created'


def get_users_list():
    users = Users.query.all()
    return users


def get_current_user(user_id):
    user = db.session.query(Users).filter(Users.id==user_id).first()
    return user


def update_user(user_data, user_id):
    user = db.session.query(Users).filter(Users.id==user_id).first()
    user.name = user_data.name
    user.avatar = user_data.avatar

    db.session.commit()
    return f'user {user_id} updated'


def delete_user(user_id):
    user = Users.query.filter_by(id=user_id).delete()
    db.session.commit()

    return f'user with uuid {user_id} deleted'