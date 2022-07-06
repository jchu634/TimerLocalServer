from flask import Flask, redirect, url_for, request, render_template, session

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')    
    return app