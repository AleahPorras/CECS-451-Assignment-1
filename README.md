1. Implement an optimal route finder program using A* algorithm.

    i. Find coordinates.txt and map.txt. Figure 1 is attached for your information.

    ii. coordinates.txt stores the latitude and longitude of each city.
City:(Latitude,Longitude)

    iii. map.txt stores actual distances between connected cities in California. We assume
each city is connected with limited number of nearby cities.
City-NearbyCity1(Distance),NearbyCity2(Distance),...

    iv. You can compute the straight line distance between two cities using the Haversine
formula.

    - You need to convert latitude and longitude to radian. (radian = π
180 degree)
    - Let φ1, φ2 be the latitude of point 1 and latitude of point 2
and λ1, λ2 be the longitude of point 1 and longitude of point 2.
    - The straight line distance d is defined by ..., where r is the radius of the earth. Use r = 3, 958.8 mile.

    v. The program should be able to
    - parse coordinates.txt and map.txt
    - take a departing city and an arriving city as input arguments (an interactive
style is not acceptable).

    - output an optimal route from the departing city to the arriving city.

    vi. Please follow the output format below.

    python a-star.py SanFrancisco LongBeach <br>
    From city: SanFrancisco <br>
    To city: LongBeach <br>
    Best Route: SanFrancisco - SanJose - Fresno - LosAngeles - LongBeach <br>
    Total distance: 442.50 mi <br>

    vii. Submit a-star.py file.