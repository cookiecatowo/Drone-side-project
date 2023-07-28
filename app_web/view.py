from flask import Flask
from app_web import app

@app.route('/')
def hello():
    return 'Hello, World!'