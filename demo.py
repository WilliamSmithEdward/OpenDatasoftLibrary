import opendatasoft_library as ods

def main():
    uni = ods.query_universities.query_universities_by_partial_name("Harvard").get_university_object_list()[0]
    print(uni.name().title())
    print(uni.address().title())
    city = uni.city().title()
    state = uni.state_full().title()
    print(f"City: {city}, State: {state}")
    city_obj = ods.query_city_demographics_by_name(city, state)
    print(f"Total population for {city}, {state}: {city_obj.get_sum_of_total_population()}")

if __name__ == "__main__":
    main()