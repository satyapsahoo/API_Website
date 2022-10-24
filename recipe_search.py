import requests

API_KEY = "abcde"
API_HOST = "abcde"


class RecipeSearch:

    def __init__(self):
        self.query_data = dict()

    def search_recipe(self, recipe_name):
        url = f"https://recipesapi2.p.rapidapi.com/recipes/{recipe_name}"

        querystring = {
            "recipe_name": recipe_name,
            "maxRecipes": "2"
        }

        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }

        query_response = requests.request("GET", url, headers=headers, params=querystring)
        self.query_data = query_response.json()
