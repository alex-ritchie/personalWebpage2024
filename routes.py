from app import app
from flask import render_template, request, flash, redirect, url_for

@app.route('/')
def home():
    # Landing page with key information
    return render_template('index.html', job_title=app.config['JOB_TITLE'])

@app.route('/about')
def about():
    # Pass detailed summary and skills to the about page
    return render_template(
        'about.html',
        detailed_summary=(
            "Alexander M. Ritchie is a machine learning expert with over 7 years of experience spanning academia, "
            "industry, and community-driven initiatives. His research covers a wide range of ML topics, from "
            "statistical learning and generative models to fairness and optimization. Alex has extensive experience "
            "in deep learning, nonparametric statistics, and applications of ML in public health, such as leading "
            "air quality monitoring projects to fight environmental injustice."
        ),
        skills=app.config['SKILLS']
    )

@app.route('/projects')
def projects():
    # Pass project descriptions to the projects page
    projects_list = [
        {
            'title': 'Bio-Inspired ML for Neuromorphic Hardware',
            'description': 'Leveraged neuroscience insights to co-design ML algorithms and systems to work with neuromorphic chips.'
        },
        {
            'title': 'Air Quality Monitoring Project (McLouth Waterfront Alliance)',
            'description': 'Developed a real-time sensor network to monitor air pollution in Metro Detroit, preventing landfill expansion.'
        },
        {
            'title': 'Transformer-based Speaker Identification (Amazon)',
            'description': 'Developed a self-attention-based speaker ID model, which increased system accuracy for Alexa devices.'
        }
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/publications')
def publications():
    # Pass a list of publications to the publications page
    publications_list = [
        {
            'title': 'Online Platforms and the Fair Exposure Problem Under Homophily',
            'conference': '37th AAAI Conference on Artificial Intelligence, 2023'
        },
        {
            'title': 'Consistent Estimation of Identifiable Nonparametric Mixture Models from Grouped Observations',
            'conference': 'Advances in Neural Information Processing Systems (NeurIPS), 2020'
        },
        {
            'title': 'Supervised PCA: A Multiobjective Approach',
            'conference': 'arXiv preprint, 2020'
        }
    ]
    return render_template('publications.html', publications=publications_list)

@app.route('/blog')
def blog():
    # Placeholder for future blog posts
    blog_posts = [
        {
            'title': 'Fairness in Machine Learning: What We Can Do Better',
            'excerpt': 'A deep dive into the current state of fairness in ML, and ways we can improve inclusivity and ethical AI.',
            'date': 'March 2023'
        },
        {
            'title': 'Understanding Generative Models',
            'excerpt': 'An introduction to generative models and how they have changed the landscape of AI.',
            'date': 'February 2023'
        }
    ]
    return render_template('blog.html', blog_posts=blog_posts)

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
