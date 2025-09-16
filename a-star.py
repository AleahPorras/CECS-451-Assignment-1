import argparse
import math
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
# Status: Done

def haversine_formula(start, end):

    #radius of the earth (miles)
    radius = 3958.8 

    lat1, lon1 = start
    lat2, lon2 = end

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    latitude_distance = math.sin((lat2 - lat1)/2) ** 2
    longitude_distance = math.sin((lon2 - lon1)/2) ** 2

    x = math.sqrt(latitude_distance + math.cos(lat1) * math.cos(lat2) * longitude_distance)
    y = math.asin(x)

    distance = 2 * radius * y

    return distance

###------------------------------------------------------###
## Actual A* algorithm, will find the optimal path to the destination city
# Status: Not Started

def a_search_algorithm(start, end):

    open_list = []
    closed_list = []

    starting_node = start
    ending_node = end

    open_list.append(starting_node)

    # loop through a non empty list
    while len(open_list) > 0:
        current_node = open_list[0]
        index = 0
        

    pass

city_coordinates = read_coordinates("coordinates.txt")
city_distances = parse_map("map.txt")


print(haversine_formula(city_coordinates[starting_city], city_coordinates[ending_city]))
# print(read_coordinates(city_coordinates))
# print(parse_map(city_distances))
