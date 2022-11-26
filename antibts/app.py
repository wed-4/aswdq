
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test-db.sqlite3'
db = SQLAlchemy(app)

class Member(db.Model):
  __tablename__ = 'member'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  role = db.Column(db.Text, nullable='true')
  price = db.Column(db.Integer)

@app.before_first_request
def init():
    db.create_all()

@app.route('/')
def hello():
  members = Member.query.all()
  return render_template('index.html', members=members)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
