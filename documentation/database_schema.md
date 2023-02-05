```mermaid
classDiagram
    class Recipes{
        id : int
        title : text
        directions : text
        user_id : int
    } 
    class Ingredients{
        name : text
        quantity : text
        recipe_id : int
    }
    class Ratings{
        user_id : int
        recipe_id : int
        rating : int
    }
    class Users{
        user_id : int
        username : text
        password : text
    }
    Recipes -- Users
    Recipes -- Ingredients
    Recipes -- Ratings
    Users -- Ratings
```
