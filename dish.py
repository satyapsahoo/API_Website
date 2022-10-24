class Dish:

    def __init__(self):
        self.dish_name = str()
        self.dish_ingredients = str()
        self.dish_instructions = str()
        self.dish_nutrients = str()
        self.dish_servings = str()
        self.dish_image = str()
        self.dish_time = str()

    def get_details(self, data):
        self.dish_name = data["name"]

        ingredients_list = data["ingredients"]
        self.dish_ingredients = str()
        for ing in ingredients_list:
            self.dish_ingredients = self.dish_ingredients + "\n" + ing

        instructions_list = data["instructions"]
        self.dish_instructions = str()
        for ins in instructions_list:
            self.dish_instructions = self.dish_instructions + "\n" + ins

        nutrients_dict = data["nutrients"]
        self.dish_nutrients = str()
        for nutrients in nutrients_dict:
            self.dish_nutrients = self.dish_nutrients + "\n" + nutrients + ":" + nutrients_dict[f"{nutrients}"]

        self.dish_servings = data["servings"]
        self.dish_image = data["image"]
        self.dish_time = "Preparation time:" + data["time"]["prepration_time"] + "\n" + "Cooking time:" + data["time"]["cooking_time"]
