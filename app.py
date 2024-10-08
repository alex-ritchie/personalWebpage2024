from flask import Flask, render_template, request, flash, redirect
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

@app.context_processor
def inject_personal_info():
    return {
        'your_name': Config.YOUR_NAME,
        'job_title': Config.JOB_TITLE,
        'email': Config.EMAIL,
        'github_url': Config.GITHUB_URL,
        'linkedin_url': Config.LINKEDIN_URL,
        'skills': Config.SKILLS,
        'current_year': datetime.utcnow().year,
        # Add other variables as needed
    }

# Import routes from a separate routes file
from routes import *

# # Contact route
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')

#         # Implement email sending logic here or save to database
#         flash('Thank you for your message! I will get back to you soon.', 'success')
#         return redirect('/contact')
#     return render_template('contact.html')

if __name__ == '__main__':
    # Print all registered routes for debugging
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)
