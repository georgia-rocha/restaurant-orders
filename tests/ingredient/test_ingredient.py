from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("tomate")
    ingredient2 = Ingredient("queijo mussarela")

    assert ingredient1.name == "tomate"
    assert ingredient1.restrictions == set()

    assert ingredient2.name == "queijo mussarela"
    assert ingredient2.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient3 = Ingredient("tomate")
    ingredient4 = Ingredient("sal")

    assert ingredient1 == ingredient3
    assert ingredient3 != ingredient4

    assert hash(ingredient1) == hash(ingredient3)
    assert hash(ingredient3) != hash(ingredient4)

    assert repr(ingredient1) == "Ingredient('tomate')"
