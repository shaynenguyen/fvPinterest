from flask import Blueprint, abort, jsonify, request
from .models import Images
from .database import session
from .config import SQL_COUNT

api = Blueprint('api',__name__)

@api.route('/')
def index():
    response = {
        'message':'Hello World'
    }
    return jsonify(response)

@api.route('/countTotalImanges')
def countTImages():
    images = session.query(Images).all()
    
    return jsonify(len(images))


@api.route('/getImages')
def images():
    data = []
    
    # Check start point to query
    if request.args.get('start') is not None:
        # https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
        sPoint = int(request.args.get('start'))
        ePoint = sPoint + SQL_COUNT
        images = session.query(Images).filter()[sPoint:ePoint]
    else:
        images = session.query(Images).all()   
    
    for i_ in images:
        data.append({
            'id':           i_.index,
            'name':         i_.name,
            'url':          i_.url,
            'width':        i_.width,
            'height':       i_.height
        })

    return jsonify(data)
