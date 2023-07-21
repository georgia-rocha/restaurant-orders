from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():

    with pytest.raises(TypeError):
        Dish("Lasanha", "84.99")

    with pytest.raises(ValueError):
        Dish("Lasanha", -84.99)

    recipe1 = Dish("Lasanha", 84.99)
    recipe2 = Dish("Passaporte", 19.99)
    recipe3 = Dish("Lasanha", 84.99)

    assert recipe1.name == "Lasanha"
    assert recipe1.price == 84.99
    assert recipe1 != recipe2
    assert recipe1 == recipe3

    assert hash(recipe1) == hash(recipe1)
    assert hash(recipe1) != hash(recipe2)

    ingredient1 = Ingredient("Queijo")
    ingredient2 = Ingredient("Tomate")

    recipe2.add_ingredient_dependency(ingredient1, 2)
    recipe2.add_ingredient_dependency(ingredient2, 2)

    assert ingredient1 in recipe2.recipe
    assert recipe2.recipe[ingredient1] == 2
    assert ingredient2 in recipe2.recipe
    assert recipe2.recipe[ingredient2] == 2

    ingredient1.restrictions = {"LACTOSE"}
    restrictions = recipe2.get_restrictions()
    assert "LACTOSE" in restrictions

    ingredients = recipe2.get_ingredients()
    assert ingredient1 in ingredients
    assert ingredient2 in ingredients

    recipe_with_special_characters = Dish("manteiga@", 3.99)
    assert repr(recipe_with_special_characters) == "Dish('manteiga@', R$3.99)"
