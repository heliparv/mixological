INSERT INTO users (username, password) VALUES ('pekka', 'pbkdf2:sha256:260000$eWAPjSNeELrQsW0J$95b02f3ee8e37437482685c5d1ceb16c3b8150a03fa322e62ac293a7af9b14db');
INSERT INTO users (username, password) VALUES ('maikki', 'pbkdf2:sha256:260000$qGijOuwA5Co7HDWA$5d4acd59dc159574c69747d84dc80cae7f87f8a87a4cff3bcbf2972e62e10808');
INSERT INTO recipes (title,alcohol,directions,user_id) VALUES ('Shirley Temple',0,'Pour grenadine in glass over ice, top with lemon-lime soda and ginger ale. Stir gently to combine and garnish with a maraschino cherry',1);
INSERT INTO recipes (title,alcohol,directions,user_id) VALUES ('Old Fashioned',1,'In a whiskey glass dissolve the sugar in in the water. Add the bitters and bourbon. Add a piece of ice and a piece of orange peel if desired. Stir gently',1);
INSERT INTO recipes (title,alcohol,directions,user_id) VALUES ('Gin Tonic',1,'Fill a highball glass with ice and add your lime slice. Pour the gin and top with tonic. Stir gently',1);
INSERT INTO ingredients (ingredient) VALUES ('Grenadine');
INSERT INTO ingredients (ingredient) VALUES ('Ice');
INSERT INTO ingredients (ingredient) VALUES ('Lemon-lime soda');
INSERT INTO ingredients (ingredient) VALUES ('Ginger ale');
INSERT INTO ingredients (ingredient) VALUES ('Maraschino cherries');
INSERT INTO ingredients (ingredient) VALUES ('Bourbon');
INSERT INTO ingredients (ingredient) VALUES ('Water');
INSERT INTO ingredients (ingredient) VALUES ('Sugar cube');
INSERT INTO ingredients (ingredient) VALUES ('Angostura bitters');
INSERT INTO ingredients (ingredient) VALUES ('Piece of orange peel');
INSERT INTO ingredients (ingredient) VALUES ('Gin');
INSERT INTO ingredients (ingredient) VALUES ('Tonic');
INSERT INTO ingredients (ingredient) VALUES ('Lime slice');
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (1,'Grenadine','2 cl',1);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (2,'Ice','enough to fill the glass',1);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (3,'Lemon-lime soda','8 cl',1);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (4,'Ginger ale','8 cl',1);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (5,'Maraschino cherries','1',1);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (6,'Bourbon','4 cl',2);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (7,'Water','2 cl',2);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (8,'Sugar cube','1',2);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (9,'Angostura bitters','2 dashes',2);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (2,'Ice','as much as desired',2);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (10,'Piece of orange peel','1',2);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (2,'Ice','enough to fill the glass',3);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (13,'Lime slice','1-3',3);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (11,'Gin','4 cl',3);
INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (12,'Tonic','2 dl',3);
INSERT INTO ratings (rating,user_id,recipe_id) VALUES (1,1,1);
INSERT INTO ratings (rating,user_id,recipe_id) VALUES (4,2,1);
INSERT INTO ratings (rating,user_id,recipe_id) VALUES (5,1,2);
INSERT INTO ratings (rating,user_id,recipe_id) VALUES (2,2,2);
INSERT INTO ratings (rating,user_id,recipe_id) VALUES (4,1,3);
INSERT INTO ratings (rating,user_id,recipe_id) VALUES (4,2,3);
