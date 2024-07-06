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

if __name__ == "__main__":
    main()