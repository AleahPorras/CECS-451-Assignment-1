import argparse


###------------------------------------------------------###
# code for extra arguments on command line

# parser = argparse.ArgumentParser()
# parser.add_argument('Start', type = str, required = True, help = "Name of departing city.")
# parser.add_argument('End', type = str, required = True, help = "Name of arriving city.")
# args = parser.parse_args()

# # opening files

city_coordinates = open("coordinates.txt", "r")
city_distances = open("map.txt", "r")

###------------------------------------------------------###
## Parsing in text from coordinates.txt
# Status: Not Started

def read_coordinates(file):
    dictionary = {}

    with open(file, "r") as f:
        # looks through entire file
        for line in f:

            key, value = line.strip().split(':')
            lat, lon = value.strip("()").split(',')
            dictionary[key] = (float(lat), float(lon))

    # should return dict, {city: (latitude, longitude)}
    return dictionary
    pass

###------------------------------------------------------###
## Parsing in text from map.txt
# Status: Not Started

def parse_map(file):

    # should return dict, {city: {neighbor:distance}}
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

print(read_coordinates("coordinates.txt"))
