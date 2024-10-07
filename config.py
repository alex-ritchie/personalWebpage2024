# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    YOUR_NAME = 'Alex Ritchie'
    JOB_TITLE = 'AI Engineer'
    EMAIL = 'alex.ritchie.ml@gmail.com'
    GITHUB_URL = 'https://github.com/alex-ritchie'
    LINKEDIN_URL = 'https://linkedin.com/in/alexander-ritchie'
    # Add other personal info as needed
