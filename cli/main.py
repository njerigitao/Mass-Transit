import click
from models.route import Route
from models.stop import Stop
from models.schedule import Schedule
from database.setup import create_tables

@click.group()
def cli():
    pass

@click.command()
def menu():
    while True:
        click.echo("\n1. Manage Routes\n2. Manage Stops\n3. Manage Schedules\n4. Exit")
        choice = click.prompt("Choose an option", type=int)
        if choice == 1:
            manage_routes()
        elif choice == 2:
            manage_stops()
        elif choice == 3:
            manage_schedules()
        elif choice == 4:
            break
        else:
            click.echo("Invalid choice. Please try again.")

def manage_routes():
    while True:
        click.echo("\n1. Create Route\n2. Delete Route\n3. View All Routes\n4. Find Route by ID\n5. Back to Main Menu")
        choice = click.prompt("Choose an option", type=int)
        if choice == 1:
            create_route()
        elif choice == 2:
            delete_route()
        elif choice == 3:
            view_all_routes()
        elif choice == 4:
            find_route_by_id()
        elif choice == 5:
            break
        else:
            click.echo("Invalid choice. Please try again.")

def manage_stops():
    while True:
        click.echo("\n1. Create Stop\n2. Delete Stop\n3. View All Stops\n4. Find Stop by ID\n5. Back to Main Menu")
        choice = click.prompt("Choose an option", type=int)
        if choice == 1:
            create_stop()
        elif choice == 2:
            delete_stop()
        elif choice == 3:
            view_all_stops()
        elif choice == 4:
            find_stop_by_id()
        elif choice == 5:
            break
        else:
            click.echo("Invalid choice. Please try again.")

def manage_schedules():
    while True:
        click.echo("\n1. Create Schedule\n2. Delete Schedule\n3. View All Schedules\n4. Find Schedule by ID\n5. Back to Main Menu")
        choice = click.prompt("Choose an option", type=int)
        if choice == 1:
            create_schedule()
        elif choice == 2:
            delete_schedule()
        elif choice == 3:
            view_all_schedules()
        elif choice == 4:
            find_schedule_by_id()
        elif choice == 5:
            break
        else:
            click.echo("Invalid choice. Please try again.")

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
@click.option('--route_id', prompt='Route ID', help='The ID of the route to delete.', type=int)
def delete_route(route_id):
    route = Route.get_by_id(route_id)
    if route:
        route.delete()
        click.echo(f'Route with ID {route_id} deleted.')
    else:
        click.echo('Route not found.')

@click.command()
def view_all_routes():
    routes = Route.get_all()
    if routes:
        for route in routes:
            click.echo(f'ID: {route.id}, Name: {route.name}, Start: {route.start_location}, End: {route.end_location}')
    else:
        click.echo('No routes found.')

@click.command()
@click.option('--route_id', prompt='Route ID', help='The ID of the route to find.', type=int)
def find_route_by_id(route_id):
    route = Route.get_by_id(route_id)
    if route:
        click.echo(f'ID: {route.id}, Name: {route.name}, Start: {route.start_location}, End: {route.end_location}')
    else:
        click.echo('Route not found.')

@click.command()
@click.option('--name', prompt='Stop name', help='The name of the stop.')
@click.option('--location', prompt='Location', help='The location of the stop.')
def create_stop(name, location):
    stop = Stop(name, location)
    stop.save()
    click.echo(f'Stop {stop.name} created with ID {stop.id}')

@click.command()
@click.option('--stop_id', prompt='Stop ID', help='The ID of the stop to delete.', type=int)
def delete_stop(stop_id):
    stop = Stop.get_by_id(stop_id)
    if stop:
        stop.delete()
        click.echo(f'Stop with ID {stop_id} deleted.')
    else:
        click.echo('Stop not found.')

@click.command()
def view_all_stops():
    stops = Stop.get_all()
    if stops:
        for stop in stops:
            click.echo(f'ID: {stop.id}, Name: {stop.name}, Location: {stop.location}')
    else:
        click.echo('No stops found.')

@click.command()
@click.option('--stop_id', prompt='Stop ID', help='The ID of the stop to find.', type=int)
def find_stop_by_id(stop_id):
    stop = Stop.get_by_id(stop_id)
    if stop:
        click.echo(f'ID: {stop.id}, Name: {stop.name}, Location: {stop.location}')
    else:
        click.echo('Stop not found.')

@click.command()
@click.option('--route_id', prompt='Route ID', help='The ID of the route.', type=int)
@click.option('--stop_id', prompt='Stop ID', help='The ID of the stop.', type=int)
@click.option('--arrival', prompt='Arrival time', help='The arrival time at the stop.')
@click.option('--departure', prompt='Departure time', help='The departure time from the stop.')
def create_schedule(route_id, stop_id, arrival, departure):
    schedule = Schedule(route_id, stop_id, arrival, departure)
    schedule.save()
    click.echo(f'Schedule created with ID {schedule.id}')

@click.command()
@click.option('--schedule_id', prompt='Schedule ID', help='The ID of the schedule to delete.', type=int)
def delete_schedule(schedule_id):
    schedule = Schedule.get_by_id(schedule_id)
    if schedule:
        schedule.delete()
        click.echo(f'Schedule with ID {schedule_id} deleted.')
    else:
        click.echo('Schedule not found.')

@click.command()
def view_all_schedules():
    schedules = Schedule.get_all()
    if schedules:
        for schedule in schedules:
            click.echo(f'ID: {schedule.id}, Route ID: {schedule.route_id}, Stop ID: {schedule.stop_id}, Arrival: {schedule.arrival_time}, Departure: {schedule.departure_time}')
    else:
        click.echo('No schedules found.')

@click.command()
@click.option('--schedule_id', prompt='Schedule ID', help='The ID of the schedule to find.', type=int)
def find_schedule_by_id(schedule_id):
    schedule = Schedule.get_by_id(schedule_id)
    if schedule:
        click.echo(f'ID: {schedule.id}, Route ID: {schedule.route_id}, Stop ID: {schedule.stop_id}, Arrival: {schedule.arrival_time}, Departure: {schedule.departure_time}')
    else:
        click.echo('Schedule not found.')

cli.add_command(menu)
cli.add_command(create_route)
cli.add_command(delete_route)
cli.add_command(view_all_routes)
cli.add_command(find_route_by_id)
cli.add_command(create_stop)
cli.add_command(delete_stop)
cli.add_command(view_all_stops)
cli.add_command(find_stop_by_id)
cli.add_command(create_schedule)
cli.add_command(delete_schedule)
cli.add_command(view_all_schedules)
cli.add_command(find_schedule_by_id)

if __name__ == '__main__':
    create_tables()
    cli()