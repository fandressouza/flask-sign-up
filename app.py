from flask import Flask, render_template

app = Flask(__name__)

# Routes
from user import routes

@app.route('/')
def home():
    return render_template('index.html')