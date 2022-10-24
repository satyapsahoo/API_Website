from dish import Dish
from recipe_search import RecipeSearch
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import RecipeName
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "q1w2e3r4"
Bootstrap(app)


@app.route('/', methods=["GET", "POST"])
def home():
    form = RecipeName()
    if form.validate_on_submit():
        recipe_name = form.recipe_name.data
        return search_results(recipe_name)
    return render_template("index.html", form=form)


@app.route('/results', methods=["GET", "POST"])
def search_results(recipe_name):
    # form = RecipeDetails()
    recipe_search = RecipeSearch()
    recipe_search.search_recipe(recipe_name)
    # if len(query_data["data"]) == 2:
    dish_1 = Dish()
    dish_1.get_details(recipe_search.query_data["data"][0])
    # dish_2 = Dish()
    # dish_2.get_details(recipe_search.query_data["data"][1])
    # print(dish_1.dish_name)
    return render_template("result.html", dish_1=dish_1, recipe_name=recipe_name)


if __name__ == "__main__":
    app.run(debug=True)
