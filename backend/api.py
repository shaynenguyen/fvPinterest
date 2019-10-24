from flask import Blueprint, abort, jsonify
from .models import Images
from .database import session

api = Blueprint('api',__name__)

@api.route('/')
def index():
    response = {
        'message':'Hello World'
    }
    return jsonify(response)

@api.route('/images')
def images():
    data = []
    images = session.query(Images).all()
    
    for i_ in images:
        tempoClass = ''
        if i_.width > i_.height:
            tempoClass = 'grid-item--width2'
        data.append({
            'id':           i_.index,
            'name':         i_.name,
            'width':        i_.width,
            'height':       i_.height,
            'class':        tempoClass
        })
    print("LIST: ", len(images))

    return jsonify(data)