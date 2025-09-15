import argparse


###------------------------------------------------------###
# code for extra arguments on command line

parser = argparse.ArgumentParser()
parser.add_argument("Start", type = str, required = True, help = "Name of departing city.")
parser.add_argument("End", type = str, required = True, help = "Name of arriving city.")
args = parser.parse_args()

starting_city = args.start 
ending_city = args.end

city_coordinates = "coordinates.txt"
city_distances = "map.txt"

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
    dictionary = {}

    with open(file, "r") as f:
        for line in f:
            og_city, value = line.strip().split("-")
            dictionary[og_city] = {}

            for i in value.split(","):
                neighbor_city, distance = i.split("(")
                distance = float(distance.strip(")"))
                dictionary[og_city][neighbor_city] = distance
                
    # should return dict, {city: {neighbor:distance}}
    return dictionary
    pass

###------------------------------------------------------###
## Haversine formula to calculate straight line distance
# Status: Not started

def haversine_formula(start, end):

    #radius of the earth (miles)
    radius = 3958.8 

    # should return a float
    pass

###------------------------------------------------------###
## Actual A* algorithm, will find the optimal path to the destination city
# Status: Not Started

# print(read_coordinates(city_coordinates))
print(parse_map(city_distances))
