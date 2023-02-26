from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
# from ..models.User import Users
from app import db
from app.models.User import Users


# db = SQLAlchemy()


class Chats(db.Model):

    __tablename__ = 'chats'
    __tableargs__ = {
        'comment': 'Список чатов'
    }

    uuid = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True
    )
    user_id1 = db.Column(
        UUID, db.ForeignKey(
            'users.uuid'
        ),
        unique=True
    )
    user_id2 = db.Column(
        UUID, db.ForeignKey(
            'users.uuid'
        ),
        unique=True
    )
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )
    modified_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )

    user1 = db.relationship("Users", foreign_keys=[user_id1])
    user2 = db.relationship("Users", foreign_keys=[user_id2])

    # users = db.relationship('Users')

    def __repr__(self):
        return f'{self.uuid}'
    

# Base = declarative_base()

# class ChatsUsers(db.Model):
#     __tablename__ = 'chats_users'
#     __table_args__ = (PrimaryKeyConstraint('chat_id', 'user_id1', 'user_id2'),)
#     chat_id = db.Column(UUID, db.ForeignKey('chats.uuid'))
#     user_id1 = db.Column(UUID, db.ForeignKey('users.uuid'))
#     user_id2 = db.Column(UUID, db.ForeignKey('users.uuid'))


# chat_users = db.Table('chats_users',
#                     db.Column('chat_id', UUID, db.ForeignKey('chats.uuid')),
#                     db.Column('user_id1', UUID, db.ForeignKey('users.uuid')),
#                     db.Column('user_id2', UUID, db.ForeignKey('users.uuid'))
#                     )