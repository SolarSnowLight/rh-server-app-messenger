from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object('config.DevelopConfig')
db = SQLAlchemy(app)
Session(app)
socketio = SocketIO(app, manage_session=False)

from app.models import Chat, User, Messages, File
from app.views import Users_views, Chat_views, Messages_views