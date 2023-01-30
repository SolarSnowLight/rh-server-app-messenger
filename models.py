import datetime
import uuid

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):

    at_created = Column(DateTime, default=datetime.datetime.now())
    at_modified = Column(DateTime, auto_now=True)

    is_active = Column(Boolean, default=True)

    class Meta:
        abstract = True


class Users(Base):

    __tablename__ = 'users'
    __tableargs__ = {
        'comment': 'Список пользователей'
    }

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(128), comment='Имя пользователя')
    avatar = Column(String(128), comment='Аватар')
    token = Column(String(128), comment='Токен пользователя')
    time_connected = Column(DateTime(timezone=True), comment='Время подключения')
    status = Column(Boolean())

    def __repr__(self):
        return f'{self.uuid} {self.name} {self.avatar}'


class Chats(Base):

    __tablename__ = 'chats'
    __tableargs__ = {
        'comment': 'Список чатов'
    }

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id1 = Column(
        Integer, ForeignKey(
            'users.uuid'
        )
    )

    user_id2 = Column(
        Integer, ForeignKey(
            'users.uuid'
        )
    )

    def __repr__(self):
        return f'{self.user_id1} {self.user_id2} '


class Messages(Base):

    __tablename__ = 'messages'
    __tableargs__ = {
        'comment': 'Сообщения пользователей'
    }
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    chat_id = Column(
        Integer, ForeignKey(
            'chats.uuid'
        )
    )

    user_id = Column(
        Integer, ForeignKey(
            'chats.user_id2'
        )
    )

    def __repr__(self):
        return f'{self.chat_id} {self.user_id}'
