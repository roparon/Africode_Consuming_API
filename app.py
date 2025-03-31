from flask import Flask, render_template
import requests

app = Flask(__name__)

BASE_URL = 'https://jsonplaceholder.typicode.com/'

@app.route('/')
def index():
    response = requests.get(f'{BASE_URL}/users')
    users = response.json()
    return render_template('index.html', users=users)

@app.route('/posts', methods=['GET'])
def get_posts():
    response = requests.get(f'{BASE_URL}/posts')
    posts = response.json()
    return render_template('posts.html', posts=posts)

@app.route('/comments', methods=['GET'])
def get_comments():
    response = requests.get(f'{BASE_URL}/comments')
    comments = response.json()
    return render_template('comments.html', comments=comments)

@app.route('/photos', methods=['GET'])
def get_photos():
    response = requests.get(f'{BASE_URL}/photos')
    photos = response.json()
    return render_template('photos.html', photos=photos)

@app.route('/todos', methods=['GET'])
def get_todos():
    response = requests.get(f'{BASE_URL}/todos')
    todos = response.json()
    return render_template('todos.html', todos=todos)

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get(f'{BASE_URL}/users')
    users = response.json()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
