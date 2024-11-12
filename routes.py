from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('sections/about.html')

@app.route('/about')
def about():
    return render_template('sections/about.html')

# @app.route('/projects')
# def projects():
#     return render_template('sections/projects.html')

@app.route('/publications')
def publications():
    return render_template('sections/publications.html')

# @app.route('/blog')
# def blog():
#     return render_template('sections/blog.html')

@app.route('/contact')
def contact():
    return render_template('sections/contact.html')
