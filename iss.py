"""Defines operations with the ISS API"""
import requests
import csv

def iss_current_loc():
    """ Get ISS Current location data
    """
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    return response.json()


def iss_passing_time(lat, lon):
    """Show when ISS with be at the specified coordinates
    
    Arguments:
    lat -- The latitude value of a location
    lon -- The longitude value of a location
    """
    url = "http://api.open-notify.org/iss-pass.json"
    coordinates = {
        "lat":lat,
        "lon":lon
    }

    response = requests.get(url, params=coordinates)
    return response.json()


def known_cities():
    """Show a list of known cities and coordinates
    
    returns dictionary with cities as keys 
    and list of it coordinates
    """
    with open('cities.txt', mode='r') as cities_file:
        if cities_file is None:
            print("file does not exist")
        csv_reader = csv.reader(cities_file, delimiter=',')
        locations = 0
        for row in csv_reader:
            if locations == 0:
                print(row)
                locations += 1
            else:
                print(", ".join(row))
                locations+= 1

        if locations <=1:
            print("Add locations")
        print(f'\n{locations} Known locations exist')


def add_city(city, lat, lon):
    """Add a new city to list of known cities

    Arguments:
    city -- name of the location
    lat -- latitude value of a city
    lon -- longitude value of a city
    """
    with open('cities.txt', mode='a') as cities_file:
        city_writer = csv.writer(cities_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        city_writer.writerow([city, lat, lon])

