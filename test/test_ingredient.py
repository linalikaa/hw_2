
import pytest
from ClassIngredient import Ingredient

def test_init_sets_name():
    ing = Ingredient("Лосось", 300, "г")
    assert ing.name == "Лосось"

def test_init_sets_unit():
    ing = Ingredient("Маракуя", 150, "г")
    assert ing.unit == "г"

def test_init_quantity_is_float():
    ing = Ingredient("Бельгийский шоколад", 200, "г")
    assert isinstance(ing.quantity, float)

def test_init_quantity_value():
    ing = Ingredient("Мука", 100, "г")
    assert ing.quantity == 100.0

def test_quantity_negative_raises():
    with pytest.raises(ValueError):
        Ingredient("Творожный сыр", -1, "г")

def test_quantity_zero_raises():
    with pytest.raises(ValueError):
        Ingredient("Фисташка", 0, "г")

def test_str():
    ing = Ingredient("Авокадо", 500, "г")
    assert str(ing) == "Авокадо: 500.0 г"

def test_eq_same_name_and_unit():
    assert Ingredient("Сахар", 500, "г") == Ingredient("Сахар", 200, "г")

def test_eq_different_quan_still_equal():
    assert Ingredient("Креветки", 300, "г") == Ingredient("Креветки", 500, "г")

def test_eq_dif_name():
    assert Ingredient("Гребешки", 200, "г") != Ingredient("Паста", 200, "г")

def test_eq_dif_unit():
    assert Ingredient("Соус песто", 50, "мл") != Ingredient("Соус песто", 50, "г")