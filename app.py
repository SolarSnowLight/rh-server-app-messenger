from app import app, db, socketio

app.app_context().push()
db.create_all()
socketio.run(app)