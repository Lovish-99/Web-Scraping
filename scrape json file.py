import urllib.request,urllib.parse,urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 :
        break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')

    try:
        js = json.loads(str(data))
    except:
        js = 'None'


    place = js['results'][0]['place_id']
    print ('The place ID is:',place)

