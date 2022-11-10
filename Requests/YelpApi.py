#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

#import modules
import requests
import json
import creds

#define business id

business_id = creds.client_id
my_location = creds.my_location

#Define API_KEY, Endpoint, and Header **information that we send along to Yelp in order to successfully request their data**
API_KEY = creds.api_key
ENDPOINT = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#Define the parameters
PARAMETERS = { 'term':'coffee',
              'term': 'tea',
              'term': 'cafes',
                'limit':'50',
                'radius': '12875', #8 miles
                'location': my_location } 

#Make a request to the yelp API
response = requests.get(url = ENDPOINT, params= PARAMETERS, headers = HEADERS)

#convert json string to a dictionary
business_data = response.json()

#create an empty list so we can add the biz names of the local cafes 
names = []

#iterate through key: business_data["businesses"] and collect value: biz["name"]   
for biz in business_data["businesses"]:
    name = biz["name"]
    names.append(biz["name"]) 
 


address = []
for biz in business_data["businesses"]:
    addr = ( biz["location"]["display_address"] )
    addr = (" ".join(str(x) for x in addr)) # add space between (street address) and (city, zip code)
    address.append(addr)

    
#with open('.\\Requests\\results.txt', 'w', encoding='utf-8') as f:
#    f.write(json.dumps(names))
#    f.close()
    
    