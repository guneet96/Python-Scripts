import urllib
import json

base_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = raw_input('Enter the address for its co-ordinates - ')
if len(address) < 1:
	print 'Please enter something...'
url = base_url + urllib.urlencode({'sensor': 'false', 'address': address})
print 'Retrieving...', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved :', len(data), 'characters'
try:
	js = json.loads(str(data))
except:
	js = None
if js['status'] != 'OK':
	print '------Failed To Retrieve------'
	print data
#print json.dumps(js, indent = 4)

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print 'Latitude  : ',lat
print 'Longitude : ',lng
location = js["results"][0]["formatted_address"]
print location
