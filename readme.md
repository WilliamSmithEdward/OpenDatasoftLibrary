# OpenDataSoft Python API Library
- Video Demo: https://www.youtube.com/watch?v=PH5YYO-oSvc
- Description: Python library to query against OpenDataSoft's US city demographics API.

## About

This project is a python library that can be used to query against OpenDataSoft's US city demographics API. The library structure is contained with the opendatasoft_library folder. References to each of the individual .py files are included in the __init__.py file. The requests library is used to query against the OpenDataSoft http API endpoints. The JSON library is then used to deserialized the expected return from the http call. The project currently support querying city & university information.

## Usage

Import the OpenDataSoft library into your project

```py
import opendatasoft_library as ods
```

Querying universities by name
```py
list = ods.query_universities_by_partial_name("Harvard").get_university_object_list()
```

Interacting with the list
```
print(list[0].name().title())
print(list[0].name().city())
print(list[0].name().state_full())
```

Querying a city by city and state name
```py
city = query_city_demographics_by_name("Cambridge", "Massachusetts")
```

Interacting with the city data object
```
print(city.get_sum_of_total_population())
print(city.get_average_household_size())
```

## Example

```py
import opendatasoft_library as ods

def main():
    harvard_official_name = get_harvard_official_name()
    harvard_city = get_harvard_city()
    harvard_state = get_harvard_state()
    harvard_city_demographics = get_harvard_demographics_object(harvard_city, harvard_state)
    harvard_city_median_age = harvard_city_demographics.get_median_age()
    print(f"{harvard_official_name} is located in the city of {harvard_city} which has a median age of {harvard_city_median_age}.")

def get_harvard_official_name():
    return ods.query_universities_by_partial_name("Harvard").get_university_object_list()[0].name().title()

def get_harvard_city():
    return ods.query_universities_by_partial_name("Harvard").get_university_object_list()[0].city().title()

def get_harvard_state():
    return ods.query_universities_by_partial_name("Harvard").get_university_object_list()[0].state_full()

def get_harvard_demographics_object(city, state):
    return ods.query_city_demographics_by_name(city, state)
```