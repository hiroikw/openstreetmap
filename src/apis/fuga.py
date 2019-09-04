import random
from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.database import get_db

class FugaAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    super(FugaAPI, self).__init__()
  
  def get(self):
    print("fugafuga")
    num = random.random()
    print(num)

    # db = get_db('sample')
    # coll = db['samplecollection']
    # result = coll.insert({"name":"hoge","bla":"huga"})
    # print(coll.find_one())
    return jsonify({
      "message": "fugafuga"
    })
