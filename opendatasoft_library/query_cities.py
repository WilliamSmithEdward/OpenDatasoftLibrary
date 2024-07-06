import requests
import json

import opendatasoft_library as ods
from statistics import mean

class CityDemographics:
    data = {}
    def get_sum_of_male_population(self):
        return sum(x["male_population"] for x in self.data)
    def get_sum_of_female_population(self):
        return sum(x["female_population"] for x in self.data)
    def get_sum_of_total_population(self):
        return sum(x["total_population"] for x in self.data)
    def get_median_age(self):
        return mean(x["median_age"] for x in self.data)
    def get_average_household_size(self):
        return mean(x["average_household_size"] for x in self.data)

def query_city_demographics_by_name(city, state):
    
    response = requests.get(f"https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/us-cities-demographics/records?where=city%3D%22{ods.urlify(city)}%22%20and%20state%3D%22{ods.urlify(state)}%22&limit=20").content
    data = json.loads(response)
    
    cd = CityDemographics()
    cd.data = data["results"]
    
    return cd