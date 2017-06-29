import eventlet
eventlet.monkey_patch()

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from config import basedir
from flask_socketio import SocketIO
# from config import ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.

async_mode = 'eventlet'
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
socketio = SocketIO(app, async_mode=async_mode)

from app import views, models

# if not app.debug:
#     import logging
#     from logging.handlers import SMTPHandler
#     credentials = None
#     if MAIL_USERNAME or MAIL_PASSWORD:
#         credentials = (MAIL_USERNAME, MAIL_PASSWORD)
#     mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@'+MAIL_SERVER, ADMINS, 'ar-table-server failure', credentials)
#     mail_handler.setLevel(logging.ERROR)
#     app.logger.addHandler(mail_handler)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/ar-table-server.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('ar-table-server startup')
