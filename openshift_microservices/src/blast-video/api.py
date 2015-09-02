import os

from flask import Flask
from flask_restful import Resource, Api

from db import Redis

app = Flask(__name__)
api = Api(app)

class BlastVideo(Resource):

    def __init__(self):
        self._db = Redis('localhost', '6379')

    def get(self, tag):
        items = []
        for obj in self._db.get(tag):
            items.append({'url': obj.decode('utf-8')})
        return {'items': items}


api.add_resource(BlastVideo, '/blast/api/v1.0/video/<string:tag>')

if __name__ == '__main__':
    app.run(debug=os.getenv('BLAST_DEBUG')=='True')