from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from app import db
from app.models.User import Users


class Chats(db.Model):

    __tablename__ = 'chats'
    __tableargs__ = {
        'comment': 'Список чатов'
    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    uuid = db.Column(
        # UUID(as_uuid=True),
        # primary_key=True,
        db.String(36),
        default=uuid.uuid4,
        nullable=False,
        unique=True
    )
    user_id1 = db.Column(
        db.Integer,
        db.ForeignKey(
            'users.id'
        )
    )
    user_id2 = db.Column(
        db.Integer,
        db.ForeignKey(
            'users.id'
        )
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

    # ссылка на таблицу "users" для получателя
    user1 = db.relationship("Users", foreign_keys=[user_id1])

    # ссылка на таблицу "users" для отправителя
    user2 = db.relationship("Users", foreign_keys=[user_id2])

    def __repr__(self):
        return f'{self.uuid}'
