from flask_restful import Resource, reqparse, abort

from flask import jsonify

from src.database import get_db

import numpy as np

class DistanceAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    super(DistanceAPI, self).__init__()
  
  def get(self):
    lat_a = 135.7696182
    lon_a = 34.9257634
    lat_b = 135.7531423
    lon_b = 35.0226632
    ra=6378.140  # equatorial radius (km)
    rb=6356.755  # polar radius (km)
    F=(ra-rb)/ra # flattening of the earth
    rad_lat_a=np.radians(lat_a)
    rad_lon_a=np.radians(lon_a)
    rad_lat_b=np.radians(lat_b)
    rad_lon_b=np.radians(lon_b)
    pa=np.arctan(rb/ra*np.tan(rad_lat_a))
    pb=np.arctan(rb/ra*np.tan(rad_lat_b))
    xx=np.arccos(np.sin(pa)*np.sin(pb)+np.cos(pa)*np.cos(pb)*np.cos(rad_lon_a-rad_lon_b))
    c1=(np.sin(xx)-xx)*(np.sin(pa)+np.sin(pb))**2/np.cos(xx/2)**2
    c2=(np.sin(xx)+xx)*(np.sin(pa)-np.sin(pb))**2/np.sin(xx/2)**2
    dr=F/8*(c1-c2)
    rho=ra*(xx+dr)
    # db = get_db('sample')
    # coll = db['samplecollection']
    # result = coll.insert({"name":"hoge","bla":"huga"})
    # print(coll.find_one())
    return jsonify({
      "message": rho
    })