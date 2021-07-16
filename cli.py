"""Provides the CLI functions via Click"""
import click
from iss import current_location, initialize_loc, \
    known_cities, add_city, passing_time, find_city

@click.group()
def ISS():
    pass

@ISS.command()
def init():
    """Initialise the First known cities
    """
    response = initialize_loc()
    if response:
        click.echo("File initialized")
    else:     
        click.echo("File has already been initialized")
    

@ISS.command()
def now():
    """Show the ISS current location
    """
    current = current_location()
    click.echo(current)


@ISS.command()
def knowncities():
    """ show list of known cities
    """
    cities = known_cities()
    if cities:
        for city in cities:
            click.echo(f"{city[0]} ----- {city[1]} ----- {city[2]}")
    else:
        click.echo("Run 'init' to get default files")
        

@ISS.command()
@click.argument('city')
@click.argument('lat', type=float)
@click.argument('lon', type=float)
def addcity(city, lat, lon):
    """Add A city to the list of cities 
    """
    response = add_city(city, lat, lon)

    if response:
        click.echo(f"{city.upper()} has been added to list of cities")
    else:
        click.echo("Run the 'init' command first")


@ISS.command()
@click.option("--city", help="Name of a city in known files")
@click.option('--coordinates', '--coors', nargs=2, type=float)
def whenat(city, coordinates):
    """show when the ISS will be at
    city or coordinates: lat and lon

    Arguments:
    city --- Name of a city in the known locations.
    coordinates -- A tuple of the latitude and longitude
    """
    if city and coordinates:
        click.echo(f"showing when ISS will be in '{coordinates}'")
        response = passing_time(coordinates)
        click.echo(response)
    elif city:
        coors = find_city(city)
        if coors: click.echo(passing_time(coors))
        else: click.echo(f"'{city}' is not a known city")
    else:
        response = passing_time(coordinates)
        click.echo(response)
    


if __name__ == '__main__':
    ISS()

    
    
