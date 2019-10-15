from flask import Flask, render_template, request
from applications.app import app

server = Flask(
            __name__,
            static_url_path =   '',
            static_folder   =   'static'
            )

server.register_blueprint(app, url_prefix='/')

# Server Start Here
if __name__ ==  '__main__':
    # Remove the next line when in production
    # app.config['DEBUG'] = True 
    server.run(host='0.0.0.0', port=5000,debug=True)