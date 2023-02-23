## Mixological
A small app to save and find recipes for cocktails and moctails

This is a studies project for [the University of Helsinki course Database Application](https://studies.helsinki.fi/courses/cu/hy-CU-118025659-2021-08-01)

### Project status
The project is in the "merry" situation that I have not for the life of me been able to run the database in this project or any other database app on my computer (even the ones that were previously working), but have not had the time to come to campus and ask IT or course assistants so... :)


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


### Description of desired features
#### Core features
- Users can log in
- Users can save, edit and delete recipes for coctails and mocktails
- Users can view an alphabetized list of recipes
- Users can search recipes by name
- Users can search recipes by ingredients

#### Nice to have features
- Users can rate recipes
- Users can view a list of recipes ranked by rating
- Recipes can be flagges as coctail or moctail
- Users can view a list of only coctails or only mocktails
- Users can make a recipe public
- Users can view public recipes
- Users can review public recipes, but can not edit or remove them
- Admins can remove and edit public recipes, or set them as private to the original poster
- Public recipes have an average rating
- User can view a list of recipes containing their own and public recipes
    - This list can be alphabetized or ranked by average rating
