from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ip = db.Column(db.String(20))
    psk = db.Column(db.String(128))
    check_date = db.Column(db.DateTime)

    def __init__(self, name, ip, psk, check_date=None):
        self.name = name
        self.ip = ip
        if check_date is None:
            check_date = datetime.utcnow()
        self.check_date = check_date
        self.psk = psk


@app.route('/', methods=['POST'])
def index():
    key = request.form['key']
    user = User.query.filter_by(psk=key).first()

    if user is None:
        abort(401)

    user.ip = request.remote_addr
    user.check_date = datetime.utcnow()

    db.session.commit()

    return "OK"
