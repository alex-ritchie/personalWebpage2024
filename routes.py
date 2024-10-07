# routes.py
from app import app
from flask import render_template
from flask import request, flash, redirect

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/publications')
def publications():
    return render_template('publications.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Implement email sending logic here or save to database
        # For now, we'll just flash a message

        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')
