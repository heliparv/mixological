```mermaid
classDiagram
    class Recipes{
        id : int
        name : varchar
        directions : varchar
        user_id : int
    } 
    class Ingredients{
        name : varchar
        quantity : varchar
        recipe_id : int
    }
    class Ratings{
        user_id : int
        recipe_id : int
        rating : int
    }
    class Users{
        user_id : int
        username : varchar
        password : varchar
    }
    Recipes -- Users
    Recipes -- Ingredients
    Recipes -- Ratings
    Users -- Ratings
```
