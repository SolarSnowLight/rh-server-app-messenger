from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func

db = SQLAlchemy()


class Chats(db.Model):

    __tablename__ = 'chats'
    __tableargs__ = {
        'comment': 'Список чатов'
    }

    uuid = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
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

    def __repr__(self):
        return f'{self.user_id1} {self.user_id2} '