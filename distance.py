from moon_utils import random_sample, pick_country
from cfg import csv_path
from geopy.distance import geodesic


def find_shortest(cities_location):
    n = len(cities_location)
    print(cities_location)
    distance_min = 0
    distance_min_city = cities_location[0]
    for h in range(1, n):
        distance_min = distance_min + geodesic(cities_location[0], cities_location[h]).km
    for i in cities_location:
        cities_rest = cities_location.copy()
        cities_rest.remove(i)
        distance = 0
        for e in range(n - 1):
            distance = distance + geodesic(i, cities_rest[e]).km
        print("Sum of distance for ", i, "is: ", distance, 'km')
        if distance < distance_min:
            distance_min = distance
            distance_min_city = i
    return [distance_min_city, distance_min]


if __name__ == '__main__':
    m = 5
    n = 6
    countries_name = pick_country(m)
    for i in countries_name:
        print("-"*100, "\nCOUNTRY: ", str(i))
        fs = find_shortest(random_sample(i, csv_path, n))
        print("-" * 50, "\nThe local distribution center for ", str(i)," should be set at ", fs[0], ", which has a sum of distance: ",
              fs[1], "km")
    print("-"*100)
