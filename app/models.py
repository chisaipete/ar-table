from hashlib import md5
from app import db, lm, UserMixin

# friends = db.Table('friends',
#     db.Column('requested_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('accepted_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('accepted', db.Boolean, default=False),
# )

#TODO: add connections to form a "party"

#TODO: add permissions roles association for "DM" or "Player" in a campaign

#TODO: add association to have multiple social_ids per user

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    # friends = db.relationship(
    #     'User', 
    #     secondary=friends, 
    #     primaryjoin=(friends.c.requested_id == id),
    #     secondaryjoin=(friends.c.accepted_id == id),
    #     backref=db.backref('friends', lazy='dynamic'),
    #     lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def avatar(self, size):
        if self.email:
            return 'http://www.gravatar.com/avatar/%s?d=retro&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)
        else:
            return 'http://www.gravatar.com/avatar/%s?d=retro&s=%d' % (md5(self.nickname.encode('utf-8')).hexdigest(), size)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
