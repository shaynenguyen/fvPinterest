from flask import Flask, render_template, jsonify, send_from_directory
from flask_cors import CORS
from random import *
import requests
from backend.api import api


app = Flask(__name__,
            static_url_path='',
            static_folder   = 'dist/static',
            template_folder = 'dist/')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(api, url_prefix='/api')

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


# @app.route('/<path:filename>')
# def send_file(filename):
#     return send_from_directory('/dist/static', filename)
    

@app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')               # url /books will fail into here
def index():    
    # if app.debug:
    #     return requests.get('http://localhost:8080/{}'.format(path)).text
    # return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
# https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532