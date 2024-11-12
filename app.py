# app.py
from socket import gethostname
from flask import Flask
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
        'google_scholar_url': Config.GOOGLE_SCHOLAR_URL,
        'skills': Config.SKILLS,
        'current_year': datetime.utcnow().year,
        'publications': Config.PUBLICATIONS,
        'pronoun_3p': Config.PRONOUN_3P,
        'pronoun_3pp': Config.PRONOUN_3PP,
        # Add other variables as needed
    }

# Import routes from a separate routes file
from routes import *

if __name__ == '__main__':
    # Print all registered routes for debugging
    # for rule in app.url_map.iter_rules():
    #     print(rule)
    # app.run(debug=True)
    if 'liveconsole' not in gethostname():
        app.run()
    else:
        app.run(debug=True)