import click
from database.setup import create_tables
from models.route import Route

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    create_tables()
    click.echo('Initialized the database')

if __name__ == '__main__':
    cli()