#!flask/bin/python

from app import app, socketio
# app.run(debug=False)
socketio.run(app)
