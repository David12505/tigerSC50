from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://team_tiger:tiger@localhost:3306/year_book'
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
    comments = db.relationship('Comment',backref='user')
    likes = db.relationship('Like',backref='user')
    messages = db.relationship('Message', backref='user')


    def __init__(self, email, username, password, first_name, last_name, profile_picture, preferences, quote):
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.profile_picture = profile_picture
        self.preferences = preferences
        self.quote = quote 
        


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poster_name = db.Column(db.String(120))
    reciever_id = db.Column(db.Integer)
    comment = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,poster_name,reciever_id,comment,):
        self.poster_name = poster_name
        self.reciever_id = reciever_id
        self.comment = comment

        #self.user = user

allComments = {
  1: {
    'poster_name' : "manuel",
    'receiver_id' : 4,
    'comment' : "very interesting"
  }
}

  
  
class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,comment_id,user_id):
        self.comment_id = comment_id
        self.user_id = user_id

        #self.user = user 


## class Message(db.Model) ##
  ## id = db.Column(db.Integer, primary_key=True)
  ## messanger_id = db.Column(db.Integer)
  ## reciever_id = db.Column(db.Integer)
  ## menssage = db.Column(db.Text())
  ## user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@app.route('/')
def home():
  return render_template( "signin.html" )


@app.route('/submit_signin', methods=["GET", "POST"])
def login():
    error = None
    UsernameO = request.form.get('Username')
    PasswordO =  request.form.get('Password')
    if request.method == 'POST':
        if UsernameO != 'user' or PasswordO != 'user':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect('/index.html')
    return render_template('index.html', error=error)


@app.route('/all_comments.html')
def showcomments():
  return render_template( "all_comments.html", comments = allComments )


@app.route('/add_comment.html')
def addcomment():
  return render_template( "add_comment.html" )


@app.route('/submit_comment', methods=["POST"])
def submitComment():
  posterName = request.form['poster_name']
  commentBody = request.form['comment']

  next_id = list( allComments.keys() )[-1] + 1

  allComments[next_id] = {  
    'poster_name' : posterName,
    'comment' : commentBody
  }

  return render_template('/all_comments.html')


@app.route('/Sign out')
def signin():
  return render_template( "signin.html" )


if __name__ == "__main__":
    app.run()







