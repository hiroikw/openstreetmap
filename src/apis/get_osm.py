import numpy as np
import requests

from math import sin, cos, sqrt, atan2, radians

from flask_restful import Resource, reqparse, abort

from osmread import parse_file, Node

from flask import jsonify

from src.database import get_db

class GetOsmAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('lat',required=True)
    self.reqparse.add_argument('lon',required=True)
    super(GetOsmAPI, self).__init__()
  
  def get(self):
    def cal_rho(lon_a,lat_a,lon_b,lat_b):
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
      return rho

    args = self.reqparse.parse_args()
    lat_a = args.lat  #データ受け取り
    lon_a = args.lon  #データ受け取り
    
    # print(args.lat, args.lon)
    url = 'https://www.google.com/maps/search/?api=1&query='
    db = get_db('osm')
    min_distance=9999999
    # coll ~= db.samples
    #テストとして京都府庁の緯度経度を使用（緯度: 35.020956 経度: 135.75556)  
    # lon_a =35.043399
    # lat_a =135.733959
    coll = db['sample']
    data = coll.find({'tags.shop':'convenience'})
    for one in data:
      lon_b = one['lon']
      lat_b = one['lat']
      rho = cal_rho(float(lon_a), float(lat_a), float(lon_b), float(lat_b))
      distance = rho
      if(distance < min_distance):
        min_distance = distance
        min_lon = lon_b
        min_lat = lat_b
    return jsonify({
      "lon":str(min_lon),"lat":(min_lat),"url":url + str(min_lat) + ',' + str(min_lon)
    })

