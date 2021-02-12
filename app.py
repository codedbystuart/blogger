from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///arthenna.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(45), nullable=False, default='N/A')
    date_created = db.Column(db.DateTime, nullable=False, default=timezone.utc)

    def __repr__(self):
        """ This function always prints out content each time a document is created in the posts table """
        return 'Blog Post ' + str(self.id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    my_posts = []
    return render_template('posts.html', posts=my_posts)


if __name__ == '__main__':
    app.run(debug=True)
