#!/usr/bin/env python

# MAC 2017-04-24 15:47:39

import sys
import geoip2.database


print "Content-Type: text/html"
print "<title>foo</title>"


#def main(ip_file):
  #reader = geoip2.database.Reader(r"GeoLite2-City_20170404/GeoLite2-City.mmdb")
  #with open(ip_file) as ip_lines:
    #for line in ip_lines:
      #try:
        #test_ip = line.strip("\n")
        #ip = reader.city(test_ip)
        #print "[%s] => %s, %s, %s, lat: %f, lon: %f" % (test_ip, ip.postal.code, ip.city.name, ip.country.name, ip.location.latitude, ip.location.longitude)
      #except geoip2.errors.AddressNotFoundError:
        #print "[!] could not find address for [%s]" % test_ip
        ##print line.strip("\n")


#if __name__ == "__main__":
  #main(sys.argv[1])
