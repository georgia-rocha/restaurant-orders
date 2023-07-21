import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.items = self.r_file(source_path)
        self.dishes = self.generate_menu()

    def r_file(self, path):
        with open(path, "r") as file:
            menu = csv.DictReader(file)
            return list(menu)

    def generate_menu(self):
        menu = {}
        for item in self.items:
            recipe_name = item["dish"]
            recipe_price = float(item["price"])
            ingredient_name = item["ingredient"]
            recipe_amount = int(item["recipe_amount"])

            recipe = menu.get(recipe_name, Dish(recipe_name, recipe_price))
            recipe.add_ingredient_dependency(
                Ingredient(ingredient_name), recipe_amount)
            menu[recipe_name] = recipe

        return list(menu.values())
