#!/usr/bin/env python

# MAC 2017-04-24 15:47:39

import json
import sys
import geoip2.database

class Response:
  
  def __init__(self):
    self.success = True
    self.error = None
    self.results = []
    
    
  def set_error(self, e):
    self.success = False
    pass
  
  
  def add_result(self, ip=None, lat=0, lon=0):
    self.results.append({ 
      "ip": ip, 
      "lat": lat, 
      "lon": lon 
    })
  
  
  def to_json(self):
    print self
    return json.dumps({
      "success": self.success,
      "error": self.error,
      "result": self.results
    }, sys.stdout)
    

print "Content-Type: application/json"

ip_file = r"./ips.txt"
reader = geoip2.database.Reader(r"GeoLite2-City_20170404/GeoLite2-City.mmdb")
resp = Response()
try:
  with open(ip_file) as ip_lines:
    for line in ip_lines:
      try:
        test_ip = line.strip("\n")
        ip = reader.city(test_ip)
        resp.add_result(ip=test_ip, lat=ip.location.latitude, lon=ip.location.longitude)
      except geoip2.errors.AddressNotFoundError:
        pass # ignore this IP
  
    body = resp.to_json()
    print "Status: 200 OK"
    print "Content-Length: %d" % len(body)
    print ""
    print body     
except BaseException as e:
  resp.set_error(e)
  print "Status: 500 Internal Server Error"
  print ""
  print "{ \"success\": false, \"error\": \"%s\" }" % str(e)