from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func

db = SQLAlchemy()


class Messages(db.Model):

    __tablename__ = 'messages'
    __tableargs__ = {
        'comment': 'Сообщения пользователей'
    }

    uuid = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    chat_id = db.Column(
        UUID, db.ForeignKey(
            'chats.uuid'
        )
    )
    user_id = db.Column(
        UUID, db.ForeignKey(
            'chats.user_id2'
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

    def __repr__(self):
        return f'{self.chat_id} {self.user_id}'
