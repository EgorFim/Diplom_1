from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE,INGREDIENT_TYPE_FILLING
from data import MOCK_INGREDIENT_1_NAME,MOCK_BUN_NAME,MOCK_BUN_PRICE,MOCK_INGREDIENT_2_NAME,MOCK_INGREDIENT_2_PRICE,MOCK_INGREDIENT_1_PRICE

@pytest.fixture()
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE,'соус',200)

@pytest.fixture()
def bun():
    return Bun('булка',200)

@pytest.fixture()
def mock_ingredient():
    mock = Mock()
    mock.name = MOCK_INGREDIENT_1_NAME
    mock.price = MOCK_INGREDIENT_1_PRICE
    mock.type = INGREDIENT_TYPE_SAUCE
    mock.get_name.return_value = MOCK_INGREDIENT_1_NAME
    mock.get_price.return_value = MOCK_INGREDIENT_1_PRICE
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock

@pytest.fixture()
def mock_ingredient_2():
    mock = Mock()
    mock.name = MOCK_INGREDIENT_2_NAME
    mock.price = MOCK_INGREDIENT_2_PRICE
    mock.type = INGREDIENT_TYPE_FILLING
    mock.get_name.return_value = MOCK_INGREDIENT_2_NAME
    mock.get_price.return_value = MOCK_INGREDIENT_1_NAME
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock

@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.name = MOCK_BUN_NAME
    mock.price = MOCK_BUN_PRICE
    mock.get_name.return_value = MOCK_BUN_NAME
    mock.get_price.return_value = MOCK_BUN_PRICE
    return mock


