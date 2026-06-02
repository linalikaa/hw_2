import pytest
from ClassIngredient import Ingredient
from ClassRecipe import Recipe

def test_init_title():
    r = Recipe("Чизкейк")
    assert r.title == "Чизкейк"

def test_init_ing_empty_by_default():
    r = Recipe("Чизкейк")
    assert r.ingredients == []

def test_add_ing_new():
    r = Recipe("Фондан")
    r.add_ingredient(Ingredient("Шоколад", 200, "г"))
    assert len(r) == 1

def test_add_ing_duble_sums_quantity():
    r = Recipe("Тартар")
    r.add_ingredient(Ingredient("Тунец", 300, "г"))
    r.add_ingredient(Ingredient("Тунец", 200, "г"))
    assert len(r) == 1
    assert r.ingredients[0].quantity == 500.0

def test_add_ing_different_unit_not_merged():
    r = Recipe("Ризотто")
    r.add_ingredient(Ingredient("Рис", 200, "гр"))
    r.add_ingredient(Ingredient("Рис", 1, "кг"))
    assert len(r) == 2

def test_sc_returns_new_object():
    r = Recipe("Тирамису")
    r.add_ingredient(Ingredient("Маскарпоне", 250, "г"))
    assert r.scale(2) is not r

def test_sс_multiplies_quantity():
    r = Recipe("Паэлья")
    r.add_ingredient(Ingredient("Рис", 400, "г"))
    scaled = r.scale(2)
    assert scaled.ingredients[0].quantity == 800.0

def test_sc_does_n_change_origin():
    r = Recipe("Болоньезе")
    r.add_ingredient(Ingredient("Паста", 200, "г"))
    r.scale(3)
    assert r.ingredients[0].quantity == 200.0

def test_sc_invalid_ratio_raises():
    r = Recipe("Павлова")
    r.add_ingredient(Ingredient("Белки", 300, "г"))
    with pytest.raises(ValueError):
        r.scale(-1)

def test_sc_zero_raises():
    r = Recipe("Гаспачо")
    r.add_ingredient(Ingredient("Томаты", 500, "г"))
    with pytest.raises(ValueError):
        r.scale(0)

def test_len():
    r = Recipe("Цезарь")
    r.add_ingredient(Ingredient("Айсберг", 200, "г"))
    r.add_ingredient(Ingredient("Курица", 100, "г"))
    assert len(r) == 2