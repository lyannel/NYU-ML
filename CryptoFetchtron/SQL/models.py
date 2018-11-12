from SQL import db


class price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q = db.Column(db.Integer)
    p =db.Column(db.Integer)
    date=db.Column(db.Integer)
    cid = db.Column(db.Integer, db.ForeignKey('cryptodata.id'),nullable=False)

    def __repr__(self):
        return '<Price {}>'.format(self.p)


class cryptodata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coin = db.Column(db.String(120), index=True, unique=True)
    # oprice = db.relationship('price', backref=db.backref('cryptodata', lazy ="joined"), lazy='dynamic')
    prices = db.relationship('price', backref='cryptodata', lazy='dynamic')
    # aprice = db.relationship('price', backref=db.backref('cryptodata', lazy ="joined"), lazy='dynamic')
    # aprice = db.relationship('price', backref='coin', lazy='dynamic')

    def __repr__(self):
        return '<cryptodata {}>'.format(self.coin)
