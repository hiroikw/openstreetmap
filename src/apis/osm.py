import random

from flask_restful import Resource, reqparse, abort

from osmread import parse_file, Node

from os.path import join, dirname, realpath

from flask import jsonify

from src.database import get_db

class OsmAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    super(OsmAPI, self).__init__()
  
  def get(self):
    file_path = join(dirname(realpath(__file__)), '../files/kansai-latest.osm.pbf')
    # print(file_path)
    shop_count = 0
    for entity in parse_file(file_path):
      if shop_count < 10:
        if isinstance(entity, Node) and 'shop' in entity.tags:
          shop_count += 1
          print(entity)
          # データベースに追加
          # ~~~~~~
    print(shop_count)

    return jsonify({
      "message": "OSM"
    })
