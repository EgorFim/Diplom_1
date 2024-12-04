from unittest.mock import patch

from data import RECEIPT
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self,mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    def test_add_ingredient(self,mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]


    def test_get_price(self,mock_ingredient,mock_bun):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        assert burger.get_price() == 600

    def test_remove_ingredient(self,mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self,mock_ingredient,mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0,1)
        assert burger.ingredients == [mock_ingredient_2,mock_ingredient]

    @patch('praktikum.burger.Burger.get_price',return_value = 700)
    def test_get_receipt(self,mock_get_price,mock_bun,mock_ingredient,mock_ingredient_2):
        burger = Burger()
        burger.bun = mock_bun
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_receipt() == RECEIPT


