from flask_script import Manager
from app import Users_views, socketio
from flask_migrate import Migrate

from app.views.Users_views import socketio

manager = Manager(Users_views)


@manager.command
def runserver():
    if __name__ == '__main__':
        socketio.run(Users_views)


if __name__ == "__main__":
    manager.run()
