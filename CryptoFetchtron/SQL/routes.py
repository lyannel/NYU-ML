from SQL import SQL
from flask import render_template



@SQL.route('/')
@SQL.route('/index')
def index():
    user = {'What do you call a pile of cats?': 'A Meow-Tain'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
