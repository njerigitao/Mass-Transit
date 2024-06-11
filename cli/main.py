import click
from models.route import Route
from models.stop import Stop
from models.schedule import Schedule
from database.setup import create_tables

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', prompt='Route name', help='The name of the route.')
@click.option('--start', prompt='Start location', help='The start location of the route.')
@click.option('--end', prompt='End location', help='The end location of the route.')
def create_route(name, start, end):
    route = Route(name, start, end)
    route.save()
    click.echo(f'Route {route.name} created with ID {route.id}')

@click.command()
@click.option('--name', prompt='Stop name', help='The name of the stop.')
@click.option('--location', prompt='Location', help='The location of the stop.')
def create_stop(name, location):
    stop = Stop(name, location)
    stop.save()
    click.echo(f'Stop {stop.name} created with ID {stop.id}')

@click.command()
@click.option('--route_id', prompt='Route ID', help='The ID of the route.', type=int)
@click.option('--stop_id', prompt='Stop ID', help='The ID of the stop.', type=int)
@click.option('--arrival', prompt='Arrival time', help='The arrival time at the stop.')
@click.option('--departure', prompt='Departure time', help='The departure time from the stop.')
def create_schedule(route_id, stop_id, arrival, departure):
    schedule = Schedule(route_id, stop_id, arrival, departure)
    schedule.save()
    click.echo(f'Schedule created with ID {schedule.id}')

cli.add_command(create_route)
cli.add_command(create_stop)
cli.add_command(create_schedule)

if __name__ == '__main__':
    create_tables()
    cli()