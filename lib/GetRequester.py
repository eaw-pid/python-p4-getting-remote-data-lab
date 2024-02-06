import requests
import json

##Building a generic GETRequester Class
class GetRequester:

# Takes a URL on initialization 
    def __init__(self, url):
        self.url = url

# This method send a GET request to the URL passed in on initialization and
        #returns the body of the response
    def get_response_body(self):
        response = requests.get(self.url)

        return response.content

# This method uses the get_response_body to send a request, then return a Python list or 
    # dictionary made up of data converted from teh response of that request 
    def load_json(self):
        return json.loads(self.get_response_body())

        