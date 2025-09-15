import argparse
from math import radians

###------------------------------------------------------###
# code for extra arguments on command line

parser = argparse.ArgumentParser()
parser.add_argument("Start", type = str, help = "Name of departing city.")
parser.add_argument("End", type = str, help = "Name of arriving city.")
args = parser.parse_args()

starting_city = args.Start 
ending_city = args.End

###------------------------------------------------------###
## Parsing in text from coordinates.txt
# Status: Done?

def read_coordinates(file):
    dictionary = {}

    with open(file, "r") as f:
        # looks through entire file
        for line in f:

            key, value = line.strip().split(":")
            lat, lon = value.strip("()").split(",")
            dictionary[key] = (float(lat), float(lon))

    # should return dict, {city: (latitude, longitude)}
    return dictionary
    pass

###------------------------------------------------------###
## Parsing in text from map.txt
# Status: Done?

def parse_map(file):
    map = {}

    with open(file, "r") as f:
        for line in f:
            og_city, value = line.strip().split("-")
            map[og_city] = {}

            for i in value.split(","):
                neighbor_city, distance = i.split("(")
                distance = float(distance.strip(")"))
                map[og_city][neighbor_city] = distance

    # should return dict, {city: {neighbor:distance}}
    return map
    pass

###------------------------------------------------------###
## Haversine formula to calculate straight line distance
# Status: Not started

def haversine_formula(start, end):

    lat1, lon1 = start
    lat2, lon2 = end

    print(f"Degrees - {start}: ({lat1}, {lon1}), {end}: {lat2},{lon2}")

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    print(f"Radians - {start}: ({lat1}, {lon1}), {end}: {lat2},{lon2}")

    #radius of the earth (miles)
    radius = 3958.8 

    # should return a float
    pass

###------------------------------------------------------###
## Actual A* algorithm, will find the optimal path to the destination city
# Status: Not Started

city_coordinates = read_coordinates("coordinates.txt")
city_distances = parse_map("map.txt")


haversine_formula(starting_city, ending_city)
# print(read_coordinates(city_coordinates))
# print(parse_map(city_distances))
