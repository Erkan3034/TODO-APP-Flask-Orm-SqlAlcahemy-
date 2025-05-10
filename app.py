from flask import Flask, render_template, url_for,redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    complete = db.Column(db.Boolean)


#Main page
@app.route('/')
def index():
    todos = ToDo.query.all() # Fetch all todos from the database
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def addToDo():
    title = request.form.get('title')
    #complete = request.form.get('complete')
    new_todo = ToDo(title=title,complete=False)
    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def deleteToDo(todo_id):
    todo = ToDo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def completeToDo(todo_id):
    todo = ToDo.query.get(todo_id)
    todo.complete = not todo.complete # Toggle the complete status
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
