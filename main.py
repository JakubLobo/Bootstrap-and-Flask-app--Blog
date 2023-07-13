from flask import Flask, render_template
import requests

app = Flask(__name__)

# Importing blog from API
blog_url = 'https://api.npoint.io/a31f1aedde0d93361694'
response = requests.get(blog_url)
blog_data = response.json()


# Main page setup
@app.route('/')
def main_page():
    return render_template("index.html", posts=blog_data)


# About page setup
@app.route('/about')
def about_page():
    return render_template("about.html")


# Contact page setup
@app.route('/contact')
def contact_page():
    return render_template("contact.html")


# Posts page setup
@app.route('/post<num>')
def post_page(num):
    return render_template("post.html", post=blog_data[int(num) - 1])


# Running the page
if __name__ == '__main__':
    app.run(debug=True)