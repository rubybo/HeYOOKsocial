from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jfdkfkjsgjgrg'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    content = db.Column(db.Text, unique=True, nullable=False)
    author = db.Column(db.String(60), unique=True, nullable=False)


db.create_all()


@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return render_template('success.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/database', methods=['GET'])
def users():
    articles = Article.query.all()
    return render_template('database.html', articles=articles)


@app.route('/posts', methods=['GET', 'POST'])
def posts():
        return render_template('posts.html')


@app.route('/addposts', methods=['GET', 'POST'])
def addposts():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        article = Article(title=title, content=content, author=author)
        db.session.add(article)
        db.session.commit()
        return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)