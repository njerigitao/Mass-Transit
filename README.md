# Mass-Transit
### Mass Transit Management System
This is a command-line application for managing mass transit routes, stops, and schedules using SQLite. The application allows users to create, view, delete, and find routes, stops, and schedules.

## Features
Create, view, delete, and find routes.
Create, view, delete, and find stops.
Create, view, delete, and find schedules.
# Prerequisites
Python 3
pipenv
## Installation
Clone the repository or download the project files to your local machine.

Open your terminal and navigate to the project directory:

cd path/to/Mass-Transit
Install the required dependencies and activate the virtual environment:
pipenv install sqlite3 click
pipenv shell

### Project Structure
Mass-Transit/
├── Pipfile
├── Pipfile.lock
├── app.py
├── database/
│   ├── connection.py
│   └── setup.py
├── models/
│   ├── route.py
│   ├── stop.py
│   └── schedule.py
└── cli/
    └── main.py
## Running the Project
Ensure you're in the Mass-Transit directory.

Activate the virtual environment:

pipenv shell
Run the application:
python app.py
You should see the CLI options and be able to create routes, stops, and schedules.

