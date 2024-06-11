from database.setup import create_tables
from cli.main import cli

def main():
    create_tables()
    cli()

if __name__ == "__main__":
    main()