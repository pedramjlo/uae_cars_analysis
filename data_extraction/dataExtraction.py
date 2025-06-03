from wikidata.client import Client
import requests

import os 
from dotenv import load_dotenv

load_dotenv()



class DataExtraction:
    def __init__(self):
        pass

    def get_country_from_serpapi(self, brand, api_key=os.getenv('API_KEY')):
    
        url = "https://serpapi.com/search.json"
        params = {
            "q": brand,
            "api_key": api_key
        }
        response = requests.get(url, params=params)

        if response:
            return response
        else:
            return "failed to get repsponse"


    
ex = DataExtraction()
print(ex.get_country_from_serpapi(brand="bmw"))