```mermaid
classDiagram
    class Recipes{
        id : int
        title : text
        directions : text
        alcohol : int
        user_id : int
    } 
    class Ingredients{
        id : int
        ingredient : text
    }
    class Contents{
        ingredient_id : text
        quantity : text
        recipe_id : int
    }
    class Ratings{
        rating : int
        user_id : int
        recipe_id : int
    }
    class Users{
        user_id : int
        username : text
        password : text
    }
    Recipes -- Users
    Recipes -- Contents
    Recipes -- Ratings
    Users -- Ratings
    Contents -- Ingredients
```
