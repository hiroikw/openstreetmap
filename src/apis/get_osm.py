import numpy as np
import requests

from flask_restful import Resource, reqparse, abort

from osmread import parse_file, Node

from flask import jsonify

from src.database import get_db

class GetOsmAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    super(GetOsmAPI, self).__init__()
  def get(self):
    url = 'https://www.google.com/maps/search/?api=1&query='
    min_destance=9999999
    db = get_db('osm')
    # coll ~= db.samples
    #テストとして京都府庁の緯度経度を使用（緯度: 35.020956 経度: 135.755574)
    shortest=1000000000   
    dest_lon = 135.755574
    dest_lat = 35.020956
    coll = db['sample']
    data = coll.find({'tags.shop':'convenience'})
    for one in data:
      lon = one['lon']
      lat = one['lat']
      ra=6378.140  # equatorial radius (km)
      rb=6356.755  # polar radius (km)
      F=(ra-rb)/ra # flattening of the earth
      rad_lat_a=np.radians(dest_lat)
      rad_lon_a=np.radians(dest_lon)
      rad_lat_b=np.radians(lat)
      rad_lon_b=np.radians(lon)
      pa=np.arctan(rb/ra*np.tan(rad_lat_a))
      pb=np.arctan(rb/ra*np.tan(rad_lat_b))
      xx=np.arccos(np.sin(pa)*np.sin(pb)+np.cos(pa)*np.cos(pb)*np.cos(rad_lon_a-rad_lon_b))
      c1=(np.sin(xx)-xx)*(np.sin(pa)+np.sin(pb))**2/np.cos(xx/2)**2
      c2=(np.sin(xx)+xx)*(np.sin(pa)-np.sin(pb))**2/np.sin(xx/2)**2
      dr=F/8*(c1-c2)
      rho=ra*(xx+dr)
      distance = rho
      if(distance<min_destance):
        min_destance = distance
        min_lon = lon
        min_lat = lat
    url = url + str(min_lat) + ',' + str(min_lon)
    return jsonify({
      str(min_lat) + ',' + str(min_lon):url
    })

