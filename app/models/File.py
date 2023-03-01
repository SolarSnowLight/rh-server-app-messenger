from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app import db
from app.models.Chat import Chats
from app.models.User import Users


class Messages(db.Model):

    __tablename__ = 'files'
    __tableargs__ = {
        'comment': 'файлы пользователей'
    }

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    uuid = db.Column(
        # UUID(as_uuid=True),
        # primary_key=True,
        db.String(36),
        default=uuid.uuid4
    )
    chat_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'chats.id'
        )
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'users.id'
        )
    )
    file_url = db.Column(
        db.String
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

    # ссылка на таблицу "chats" для чата, к которому
    # принадлежит файл
    chat = db.relationship("Chats", foreign_keys=[chat_id])

    # ссылка на таблицу "users" для отправителя файла
    user = db.relationship("Users", foreign_keys=[user_id])

    def __repr__(self):
        return f'{self.chat_id} {self.user_id}'
