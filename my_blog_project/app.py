
from flask import Flask, render_template, abort

app = Flask(__name__)

# SAMPLE BLOG ARTICLES

posts = [

    {
        "id": 1,
        "slug": "future-of-technology",
        "title": "The Future of Technology",
        "category": "Technology",
        "author": "My Blog Team",
        "date": "10 November 2026",
        "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1000",
        "excerpt": "Exploring how modern technology is transforming our everyday lives.",
        "content": """
Technology continues to transform the way people live,
work and communicate.

From artificial intelligence to mobile applications,
digital innovation is creating new opportunities across
different industries.

As technology continues to advance, individuals and
businesses must learn to adapt to new developments.

The future will bring more opportunities for creativity,
innovation and global connection.
"""
    },

    {
        "id": 2,
        "slug": "building-better-habits",
        "title": "Building Better Daily Habits",
        "category": "Lifestyle",
        "author": "My Blog Team",
        "date": "10 November 2026",
        "image": "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=1000",
        "excerpt": "Small positive changes can make a meaningful difference in life.",
        "content": """
Good habits play an important role in personal development.

Simple actions such as reading, exercising, planning
your day and learning something new can improve your
daily routine.

Consistency is more important than making huge changes
all at once.

Start with small steps and gradually build a routine
that supports your goals.
"""
    },

    {
        "id": 3,
        "slug": "importance-of-learning",
        "title": "Why Lifelong Learning Matters",
        "category": "Education",
        "author": "My Blog Team",
        "date": "10 November 2026",
        "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?w=1000",
        "excerpt": "Learning new things helps us grow personally and professionally.",
        "content": """
Education does not end when someone leaves school.

The world continues to change, and people need to
develop new knowledge and skills throughout their lives.

Reading books, taking online courses, attending workshops
and learning from other people are all valuable ways
to continue learning.

Lifelong learning creates opportunities for growth
and personal achievement.
"""
    }

]


# HOMEPAGE

@app.route("/")
def home():

    return render_template(
        "index.html",
        posts=posts
    )


# INDIVIDUAL ARTICLE PAGE

@app.route("/article/<slug>")
def article(slug):

    selected_post = next(
        (post for post in posts if post["slug"] == slug),
        None
    )

    if selected_post is None:
        abort(404)

    return render_template(
        "article.html",
        post=selected_post
    )


# ABOUT PAGE

@app.route("/about")
def about():

    return """
    <h1>About My Blog</h1>
    <p>A creative space for ideas, knowledge and stories.</p>
    <a href="/">Return Home</a>
    """


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
