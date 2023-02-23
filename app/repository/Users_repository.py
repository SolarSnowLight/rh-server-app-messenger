from ..models.User import db
from ..models.User import Users

def create(name, avatar, token, status, time_connected):
    try:
        user = Users(name=name, avatar=avatar, token=token, time_connected=time_connected, status=status)
        db.session.add(user)
        db.session.commit()

        return f'user {name} created'
    except Exception as e:
        print(e)


def get_users_list():
    users = []

    for user in Users.query.all():
        users.append(
            {   
                'id': user.uuid,
                'name': user.name,
                'avatar': user.avatar,
                'status': user.status
            }
        )

    return users


def get_current_user(name):
    user = db.session.query(Users).filter(Users.name==name).first()
    return user


def update_user(user_data, name):
    user = db.session.query(Users).filter(Users.name==name).first()
    user.name = user_data.name
    user.avatar = user_data.avatar
    # user.status = user_data.status

    db.session.commit()
    return f'user {name} updated'


def delete_user(name):
    user = Users.query.filter_by(name=name).delete()
    db.session.commit()

    return f'user with name {name} deleted'