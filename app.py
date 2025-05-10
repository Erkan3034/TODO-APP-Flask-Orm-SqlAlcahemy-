from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase , Mapped, mapped_column

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users/Win11/Desktop/ToDoApp/todo.db'
db = SQLAlchemy(app)

class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True) # Auto-incrementing primary key
    title = db.Column(db.String(80), nullable=False) # Title of the task
    """    description = db.Column(db.String(200), nullable=True) # Description of the task
    completed = db.Column(db.Boolean, default=False) # Completion status of the task
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) # Timestamp of task creation
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) # Timestamp of last update
    """
    completed = db.Column(db.Boolean) # Completion status of the task

if __name__ == '__main__':
    # Create the database and tables
    db.create_all()
    app.run(debug=True)


