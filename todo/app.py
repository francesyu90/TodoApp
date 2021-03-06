from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://beijiayu@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(), nullable = False)
    completed = db.Column(db.Boolean, nullable = False, default = False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

@app.route('/')
def index():
    return render_template(
        'index.html', 
        data = Todo.query.all()
    )