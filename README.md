## Mixological
A small app to save and find recipes for cocktails and moctails

This is a studies project for [the University of Helsinki course Database Application](https://studies.helsinki.fi/courses/cu/hy-CU-118025659-2021-08-01)

### How to test project
The project is currently not online, it can be tested locally by downloading the source code and doing the following:

Navigate to the app folder on your terminal

Create a virtual environment
```bash
python3 -m venv venv
```

Activate virtual environment
```bash
source venv/bin/activate
```

Install flask library
```bash
pip install flask
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

### Project status
The project is currently very much not close to functional, mostly due to issues scheduling time to work on it. Below are listed the features that the app hopefully has at some point soon. (:

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
