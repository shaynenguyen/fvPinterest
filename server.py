from flask import Flask, render_template, jsonify, send_from_directory
from flask_cors import CORS
from backend.api import api
import os

# Initialize
static_files_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dist')

server = Flask(__name__,
                template_folder='./dist',
                static_folder='./dist/static')

cors = CORS(server, resources={r"/api/*": {"origins": "*"}})
server.register_blueprint(api, url_prefix='/api')

@server.route('/<path:path>', methods=['GET'])
def send_static_file(path):
    return send_from_directory(static_files_dir, path)

@server.route('/hello')
def hello():
    data = [
        {'name': 'Alice', 'birth-year': 1986},
          {'name': 'Bob', 'birth-year': 1985}
        ]
    return jsonify(data)

@server.route('/')
def index():
    return send_from_directory(static_files_dir, 'index.html')


if __name__ == '__main__':
    server.run(host="127.0.0.1", port="5000")