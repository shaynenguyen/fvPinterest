from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        'message':'Hello World'
    }
    return render_template('index.html',title='Welcome ',data = data)


if __name__ ==  '__main__':
    # Remove the next line when in production
    app.config['DEBUG'] = True 
    app.run(host='0.0.0.0', port=5000)