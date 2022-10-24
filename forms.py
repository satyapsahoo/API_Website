from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# WTForm
class RecipeName(FlaskForm):
    recipe_name = StringField("Recipe Name", validators=[DataRequired()])
    submit = SubmitField("Search Recipe")


# class RecipeDetails(FlaskForm):
#     recipe_name = StringField("Recipe Name", validators=[DataRequired()])
#     dish_name = StringField("Dish Name")
#     dish_ingredients = StringField("Ingredients")
#     dish_instructions = StringField("Instructions")
#     dish_nutrients = StringField("Nutrients")
#     dish_servings = StringField("Servings")
#     dish_image = StringField("Image")
#     dish_time = StringField("Preparation Time")



