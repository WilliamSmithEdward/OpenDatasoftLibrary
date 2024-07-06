from project import *

def test_get_harvard_official_name():
    assert(get_harvard_official_name() == "Harvard University")
    
def test_get_harvard_city():
    assert(get_harvard_city() == "Cambridge")
    
def test_get_harvard_state():
    assert(get_harvard_state() == "Massachusetts")
    
def test_get_harvard_demographics_object():
    obj = get_harvard_demographics_object("Cambridge", "Massachusetts")
    assert(obj.get_median_age() > 0)
    assert(obj.get_sum_of_total_population() > 0)