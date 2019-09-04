from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.database import get_db

class SampleAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    super(SampleAPI, self).__init__()
  
  def get(self):
    print("hogehoge")
    # db = get_db('sample')
    # coll = db['samplecollection']
    # result = coll.insert({"name":"hoge","bla":"huga"})
    # print(coll.find_one())
    return jsonify({
      "message": "Hello!!"
    })
