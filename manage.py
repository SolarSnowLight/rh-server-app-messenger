from flask_script import Manager
from app import app, socketio
from flask_migrate import Migrate

manager = Manager(app)


@manager.command
def runserver():
    if __name__ == '__main__':
        socketio.run(app)


if __name__ == "__main__":
    manager.run()
