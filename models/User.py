from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func

db = SQLAlchemy()


class Users(db.Model):

    __tablename__ = 'users'
    __table_args__ = {
        'extend_existing': True
    }

    uuid = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )
    name = db.Column(
        db.String(128),
        comment='Имя пользователя',
        nullable=False
    )
    avatar = db.Column(
        db.String(128),
        comment='Аватар'
    )
    token = db.Column(
        db.String(128),
        comment='Токен пользователя',
        nullable=False
    )
    time_connected = db.Column(
        db.DateTime(timezone=True),
        comment='Время подключения',
        nullable=False
    )
    status = db.Column(
        db.Boolean(),
        nullable=False
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
        return f'{self.uuid} {self.name} {self.avatar}'
