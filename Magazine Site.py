from flask import Flask, render_template

app = Flask(__name__)

articles = [
    {
        'id': 1,
        'title': 'Future of Social Media',
        category': 'Technology',
        'content': 'Social media is constantly evolving...'
    }
    {
        'id': 2,
        'title': "Fashion Trends in 2026",
        "category': 'Lifestyle',"
        'content': 'The fashion industry is embracing sustainability...'
    }   
    {
        'id': 3,
        'title': 'Entrepreneurship in the Digital Age',
        'category': 'Business',
        'content': 'Building digital startups is becoming more accessible...'
    }
    {
        'id': 4,
        'title': 'The Rise of Remote Work',
        'category': 'Work',
        'content': 'Remote work is reshaping the traditional office environment...'
    }
]

@app.route("/")
def home():
    return render_template('home.html', articles=articles)

    @app.route("/article/<int:article_id>")
def article(article_id):
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        return render_template('article.html', article=article)

if __name__ == "__main__":    app.run(debug=True)

