CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
);
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title TEXT,
    directions TEXT,
    user_id INTEGER REFERENCES users
);
CREATE TABLE contents (
    ingredient TEXT,
    quantity TEXT,
    recipe_id INTEGER REFERENCES recipes
);
CREATE TABLE ratings (
    rating INTEGER,
    user_id INTEGER REFERENCES users,
    recipe_id INTEGER REFERENCES 

)