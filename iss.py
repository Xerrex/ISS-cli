"""Defines operations with the ISS API"""
import requests
import csv
import os

def current_location():
    """ Get ISS Current location data
    """
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    return response.json()


def passing_time(coordiantes):
    """Show when ISS with be at the specified coordinates
    
    Arguments:
    coordiantes -- the latitude and longitude of a place
    """
    url = "http://api.open-notify.org/iss-pass.json"
    coors = {
        "lat":coordiantes[0],
        "lon":coordiantes[1]
    }

    response = requests.get(url, params=coors)
    return response.json()


def initialize_loc():
    """Setups default locations
    """
    locs = [
        ['CITY', 'LATITUDE', 'LONGITUDE'], 
        ['NAIROBI', '-1.2921', '36.8219'], 
        ['MOMBASA', '-4.0435', '39.6682'], 
        ['KISUMU', '-0.0917', '34.7680'], 
        ['THIKA', '-1.0388', '37.0834'], 
        ['BUSIA', '0.4608', '34.1115'], 
        ['KAMPALA', '0.3476', '32.5825'], 
        ['DAR-ES-SALAM', '-6.7924', '39.2083']
    ]

    if not os.path.exists('cities.txt'):
        with open('cities.txt', mode='w') as cities_file:
            city_writer = csv.writer(cities_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for loc in locs:
                city_writer.writerow(loc)
        return True
        
    else:
        return None


def known_cities():
    """Show a list of known cities and coordinates
    
    returns dictionary with cities as keys 
    and list of it coordinates FileNotFoundError
    """
    if not os.path.exists('cities.txt'):
        return None
    else:
        with open('cities.txt', mode='r') as cities_file:
            csv_reader = csv.reader(cities_file, delimiter=',')
            locations = 0
            locs=[]
            for row in csv_reader:
                if locations == 0:
                    # print(", ".join(row))
                    locations += 1
                    locs.append(row)
                else:
                    if row: locs.append(row)
                    #print(", ".join(row))
                    locations+= 1

            if locations <=1:
                return None
            return locs


def add_city(city, lat, lon):
    """Add a new city to list of known cities

    Arguments:
    city -- name of the location
    lat -- latitude value of a city
    lon -- longitude value of a city
    """
    if not os.path.exists('cities.txt'):
        return None
    else:
        with open('cities.txt', mode='a') as cities_file:
            city_writer = csv.writer(cities_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            city_writer.writerow([city.upper(), lat, lon])
        return True


def find_city(name):
    """finds a city from in known cities
    
    Parameters
    ----------
    name : [String]
        [the name of a city to find]
    """
    cities = known_cities()
    for city in cities:
        if name.upper() in city[0]:
            return (city[1], city[2])
    return None
    

