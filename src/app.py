from flask import Flask, jsonify, request
from flask_restful import Api

from src.apis.sample import SampleAPI
from src.apis.hoge import HogeAPI
from src.apis.fuga import FugaAPI
from src.apis.osm import OsmAPI
from src.apis.get_osm import GetOsmAPI

def create_app():
  app = Flask(__name__)
  app.config['JSON_AS_ASCII'] = False

  api = Api(app)

  api.add_resource(SampleAPI, '/sample')
  api.add_resource(HogeAPI, '/hoge')
  api.add_resource(FugaAPI,'/fuga')
  api.add_resource(OsmAPI, '/osm')
  api.add_resource(GetOsmAPI, '/getosm')

  return app

app = create_app()
