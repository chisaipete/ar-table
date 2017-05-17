import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = True
SECRET_KEY = 'i-love-magic-beans'
OAUTH_CREDENTIALS = {
    'twitter': {
        'id': '58bWCkDctbLCxYtqVTWycSVqv',
        'secret': 'nt8dondH3nb1EFtt8hIntMkpUEfDnNVBZQvfJzSU50uny5ZYWb',
    },
}
