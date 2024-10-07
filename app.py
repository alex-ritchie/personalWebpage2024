from flask import Flask
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

@app.context_processor
def inject_now():
    return {'current_year': datetime.utcnow().year}

@app.context_processor
def inject_personal_info():
    return {
        'your_name': Config.YOUR_NAME,
        'job_title': Config.JOB_TITLE,
        'email': Config.EMAIL,
        'github_url': Config.GITHUB_URL,
        'linkedin_url': Config.LINKEDIN_URL,
        # Add other variables as needed
    }

# Configuration can be added here if needed

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
