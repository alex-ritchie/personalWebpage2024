# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    YOUR_NAME = 'Alex Ritchie'
    JOB_TITLE = 'AI Engineer'
    EMAIL = 'alex.ritchie.ml@gmail.com'
    GITHUB_URL = 'https://github.com/alex-ritchie'
    LINKEDIN_URL = 'https://linkedin.com/in/alexander-ritchie'

    SKILLS = [
        # Core Machine Learning Skills
        'Deep Learning',
        'Statistical Machine Learning',
        "Autoregressive Models",
        'Generative Models',
        'Transfer Learning',
        'Fairness in Machine Learning',
        'Explainable AI',
        'Low Precision Model Training',
        'Distributed Model Training',
        'Model Quantization',
        'Model Pruning and Sparsity',
        'Model Selection and Evaluation',
        'Nonparametric Methods',
        'A/B Testing and Experiment Design',
        
        # LLMs/Transformers
        'Large Language Models',
        'Prompt Engineering',
        'Local LLMs',
        'Transformer Architecture',
        'Encoder Only Architectures',
        'Encoder/Decoder Architectures',
        
        # Natural Language Processing
        'Parameter Efficient Fine Tuning',
        'Recurrent Architectures'
        'Text Classification',
        'Speech Recognition and Speaker Identification',

        # Data Analysis and Modeling
        'Exploratory Data Analysis',
        'Data Visualization',
        'Feature Engineering',
        'Statistical Modeling',
        'Hypothesis Testing',

        # Programming Languages
        'Python',
        'C++',
        'Bash',
        'Julia',
        'Matlab',

        # Python Libraries and Frameworks
        ## Model Training & Development
        'PyTorch',
        'Lightning',
        'wandb',
        'Tensorboard'
        'sklearn',
        'Keras',
        'NLTK',
        'XGBoost',
        'fastai',
        
        ## AI Inference / Prototyping / API Tools
        'Transformers',
        'LangChain',
        'Gradio', 
        
        ## Data Manipulation and Visualization
        'Pandas',
        'Dask', # Learning
        'Polars', # Learning
        'Geopandas', # Learning
        'PySpark', # Learning
        'Matplotlib',
        'Seaborn',
        'Plotly',
        'Altair',
        
        ## General Numerical  Computing
        'NumPy',
        'cuPy', # Learning
        'JAX', # Learning
        'SciPy',
        
        # Platforms, OS, and Other Tools
        'Docker',
        'Linux',
        'SQL',
        'Git',
        'SVN',
        'Excel',        
        'Flask',

        # # Cloud and Big Data Technologies
        # 'AWS Services (Sagemaker, Rekognition, DynamoDB, Glue, Kinesis)',
        # 'Big Data Processing',
        # 'Cloud Model Deployment',

        # Hardware/Systems Experience
        'Analog Electronics (Audio)',
        'Embedded Systems',
        'Digital Signal Processing (Audio)'
        'Firmware Development',
        'Soldering',
        'System Design and Control Logic',
        'Neuromorphic Hardware',

        # Professional and Soft Skills
        'Leadership and Team Management',
        'Technical Communication',
        'Public Speaking',
        'Critical Thinking and Problem Solving',
        'Time Management and Multitasking',
        'Conflict Resolution',
        'Self-Teaching',
        'Teaching',
        'Mentorship',
        'Decision Making',
        'Collaboration',
        'Research Design and Execution',
        'Project Management',
    ]
