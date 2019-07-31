"""Provides the CLI functions via Click"""
import click
from iss import current_location, initialize_loc, \
    known_cities, add_city, passing_time

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
        click.echo(cities)
    else:
        click.echo("Run 'ISS init' to get default files or add a city.")


@ISS.command()
def whenat(city=None, coordinate=None):
    """show when the ISS will be at
    city or coordinates: lat and lon

    Arguments:
    city --- Name of a city in the known locationsself.
    coordinates -- A tuple of the latitude and longitude
    """
    if city:
        # find the city
        pass    
    response = passing_time(coordinate[0], coordinate[1])

    click.echo(response)
    

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
        click.echo("something has gone wrong ")



if __name__ == '__main__':
    ISS()

    
    
    
    
    