## Mixological
A small app to save and find recipes for cocktails and moctails

This is a studies project for [the University of Helsinki course Database Application](https://studies.helsinki.fi/courses/cu/hy-CU-118025659-2021-08-01)

### Project status
The project can only be tested locally.
The project could be more refined, but it basically functional. There might be a second release with better visuals and refinements, if I somehow have time and energy before the deadline.

### Description of features
- Users can register, log in and log out
- Users can create, edit and delete recipes for coctails and mocktails
- Users can view an alphabetized list of recipes
- Users can rate recipes, change their rating, view their rating, and view an average rating

### Possible future features
- users can delete a recipe
- users can filter recipe list by cocktail/mocktail status
- Users can search recipes by name
- Users can search recipes by ingredients
- Users can view a list of recipes ranked by their rating
- Users can view a list of recipes ranked by average rating
- recipes can only be edited or deleted by the original author or admin

### How to test project

#### First time set up
The project is currently not online, it can be tested locally by downloading the source code and following these instructions.

PostgreSQL needs to be downloaded. It can be downloaded with [this script](https://github.com/hy-tsoha/local-pg) or [directly from the PostgreSQL web page](https://www.postgresql.org/download/).

Navigate to the app root folder on your terminal

In the app root folder create a file called ".env" with the following contents
```bash
DATABASE_URL="postgresql:///user"
SECRET_KEY ="key"
```
here "user" is your username in the system and key is a token you can create for example with the following commands in a terminal
```bash
python3
>>> import secrets
>>> secrets.token_hex(16)
```

Create a virtual environment
```bash
python3 -m venv venv
```

Activate the virtual environment
```bash
source venv/bin/activate
```

Install project dependencies with the following command
```bash
pip install -r requirements.txt
```

Have your database running in the backgroud. If you used the download script written for this course and linked above, you can do so by opening a new terminal that you keep open after entering the command 
```bash
start-pg.sh
```

Return to the terminal with your virtual environment and get the database schema with
```bash
psql < schema.sql
```

If you want to test the app with some pre-initiated recipes and ratings by other users, you can add data to the database by running a scrip with
```bash
psql < add_data.sql
```

Run app
```bash
flask run
```

Enter the app by navigating to  http://127.0.0.1:5000 on your browser

You can exit the project by closing the browser window, using "control+C" in your terminal and deactivating the virtual environment with
```bash
deactivate
```

#### Using project after first time set up
Activate database in the background, for example by using
```bash
start-pg.sh
```

In a new terminal window activate the virtual environment
```bash
source venv/bin/activate
```

Run app
```bash
flask run
```

#### Dropping tables
If you want to drop the tables in this project from the database, you can do so in your virtual environment with the command
```bash
psql < drop.sql
```
NOTE! If you have databases with the same names as in this project but for use in other projects, this will drop those databases.
