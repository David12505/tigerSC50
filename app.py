from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymysql://team_tiger:tiger@localhost:3306/year_book'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    profile_picture = db.Column(db.String(120))
    preferences = db.Column(db.String(120))
    quote = db.Column(db.Text())

    ## Relations
    comments = db.relationship('Comment',backref='user'))
    likes = db.relationship('Like',backref='user'))
    messages = db.relationship('Message',backref='user'))
​
    def __init__(self, email, username, password, first_name, last_name, profile_picture, preferences, quote):
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture = profile_picture
        self.preferences = preferences
        self.quote = quote 
        
​
​
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poster_id = db.Column (db.Integer)
    reciever_id = db.Column(db.Integer)
    comment = db.Column(db.Text())
​    user_id = db.Column(db.Integer, db.ForeingKey('user.id'))
​
    def __init__(self,poster_id,reciever_id,comment,):
        self.poster_id = poster_id
        self.reciever_id = reciever_id
        self.comment = comment
​
        self.user = user 
​
​
class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeingKey('user.id'))​

    def __init__(self,comment_id,user_id):
        self.comment_id = comment_id
        self.user_id = user_id

        self.user = user 
​
## class Message(db.Model) ##
  ## id = db.Column(db.Integer, primary_key=True)
  ## messanger_id = db.Column(db.Integer)
  ## reciever_id = db.Column(db.Integer)
  ## menssage = db.Column(db.Text())
​  ## user_id = db.Column(db.Integer, db.ForeingKey('user.id'))


@app.route('/')
def home():
  return render_template( "index.html" )


@app.route('/Sign out')
def signin():
  return render_template( "signin.html" )


@app.route('/add_comment')
def addcomment():
  return render_template( "add_comment.html" )


@app.route('/submit_comment', methods=["POST"])
def submitcomment():
  commentTitle = request.form['comment_title']
  commentBody = request.form['comment_body']


if __name__ == "__main__":
    app.run()