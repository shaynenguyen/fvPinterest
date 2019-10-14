from flask import Blueprint, render_template, request

# App
app = Blueprint(
                    'app',
                    __name__,
                    template_folder     ='templates',
                    static_folder       ='static'
                )

@app.route("/")
def home():
    data = {
        'message':'Hello World'
    }
    return render_template('index.html',title='Welcome ',data = data)

@app.route("/masonry")
def mansonry():
    data = {
        'images': 'Yes all images',
        'source': 'mdboostrap.com',
        'addition': 'https://imagesloaded.desandro.com/',
        'imagest': 'cdn images'
    }

    return render_template('mansonry.html', title='Masonry - images options',data = data)