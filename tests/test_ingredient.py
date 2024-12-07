import pytest

from data import sauce
from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_ingredient_get_price(self,ingredient):
        assert ingredient.get_price() == 200

    def test_ingredient_get_name(self,ingredient):
        assert ingredient.get_name() == 'соус'

    @pytest.mark.parametrize('type,name,price',sauce)
    def test_ingredient_get_type(self,type,name,price):
        ingredient = Ingredient(type,name,price)
        assert ingredient.get_type() == 'SAUCE' or 'FILLING'
