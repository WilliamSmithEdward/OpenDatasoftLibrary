import requests
import json

import opendatasoft_library as ods
from statistics import mean

from typing import List

class Universities:
    data = {}
    def first(this):
        u = University()
        u.data = this.data[0]
        return u
    def get_university_object_list(this):
        li: List[University] = []
        for x in this.data:
            u = University()
            u.data = x
            li.append(u)
        return li

class University:
    data = {}
    def name(this):
        return str(this.data["name"])
    def address(this):
        return str(this.data["address"])
    def city(this):
        return str(this.data["city"])
    def county(this):
        return str(this.data["county"])
    def state_two_letter_code(this):
        return str(this.data["state"])
    def state_full(this):
        return ods.states.abbrev_to_us_state()[this.data["state"]]
    def latitude(this):
        return str(this.data["latitude"])
    def longitude(this):
        return str(this.data["longitude"])

def query_universities_by_partial_name(name):
    
    response = requests.get(f"https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/us-colleges-and-universities/records?where=name%20like%20%22{ods.urlify(name)}%22&limit=20").content
    data = json.loads(response)
    
    u = Universities()
    u.data = data["results"]
    
    return u