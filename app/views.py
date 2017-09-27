from app import app
from flask import render_template, request, redirect, url_for
from app.models import Todo, TodoForm
import datetime


@app.route('/')  # home page
def index():
    form = TodoForm()
    # create TodoForm object
    todos = Todo.objects.order_by('status', '-time')
    # get all to-dos
    return render_template('index.html', todos=todos, form=form)
    # use template to render data
    # old version: return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST', ])
def add():
    form = TodoForm(request.form)
    # create TodoForm object for validation
    if form.validate_on_submit():
        # if validate
        content = form.content.data
        # get the content
        # old version: content = request.form.get("content")
        todo = Todo(content=content, time=datetime.datetime.now())
        # create a new to-do
        todo.save()
        # save the new to-do
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/do/<string:todo_id>')
def do(todo_id):
    form = TodoForm()
    # create TodoForm object
    todo = Todo.objects.get_or_404(id=todo_id)
    # get to-do by its id
    todo.status = 1
    # set its status to 1 (finished)
    todo.save()
    return redirect(url_for('index'))


@app.route('/undo/<string:todo_id>')
def undo(todo_id):
    form = TodoForm()
    # create TodoForm object
    todo = Todo.objects.get_or_404(id=todo_id)
    # get to-do by its id
    todo.status = 0
    # set its status to 0 (unfinished)
    todo.save()
    return redirect(url_for('index'))


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = TodoForm()
    # create TodoForm object
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    # delete this to-do
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
