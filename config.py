import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = '<READ FROM oauth.cred>'

OAUTH_CREDENTIALS = {
    'twitter' : {
        'id' : '<READ FROM oauth.cred>',
        'secret' : '<READ FROM oauth.cred>',
    },
    'google' : {
        'id' : '<READ FROM oauth.cred>',
        'secret' : '<READ FROM oauth.cred>',
    },
    'facebook' : {
        'id' : '<READ FROM oauth.cred>',
        'secret' : '<READ FROM oauth.cred>',
    },
}

with open(os.path.join(basedir,'oauth.cred')) as fh:
    for line in fh.read().strip().split('\n'):
        if line:
            protocol, key, value = line.split()
            if protocol == 'flask':
                SECRET_KEY = value
            else:
                OAUTH_CREDENTIALS[protocol][key] = value

# MAIL_SERVER = 'localhost'
# MAIL_PORT = 2555
# MAIL_USERNAME = 'foo'
# MAIL_PASSWORD = None

# ADMINS = ['you@example.com']
