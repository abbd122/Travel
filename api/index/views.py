from flask import render_template

from api.index import index_blu


@index_blu.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name='Wang')


@index_blu.route('/todo')
def todo_list():
    return render_template('todolist.html')
