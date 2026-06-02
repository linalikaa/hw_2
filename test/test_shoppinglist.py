import pytest
from ClassIngredient import Ingredient
from ClassRecipe import Recipe
from ClassShoppingList import ShoppingList

def make_bowl():
    r = Recipe("Боул")
    r.add_ingredient(Ingredient("Гребешки", 200, "г"))
    r.add_ingredient(Ingredient("Креветки", 150, "г"))
    r.add_ingredient(Ingredient("Авокадо", 1, "шт"))
    r.add_ingredient(Ingredient("Киноа", 50, "г"))
    return r

def make_cheesecake():
    r = Recipe("Чизкейк")
    r.add_ingredient(Ingredient("Творожный сыр", 200, "г"))
    r.add_ingredient(Ingredient("Ваниль", 50, "г"))
    r.add_ingredient(Ingredient("Шоколад", 100, "г"))
    return r

def test_add_items():
    sl=ShoppingList()
    sl.add_recipe(make_bowl(), 1)
    assert len(sl._items) == 4

def test_scale():
    sl = ShoppingList()
    sl.add_recipe(make_bowl(), 2)
    assert sl._items[1][0].quantity==300.0

def test_zero_portions():
    sl= ShoppingList()
    with pytest.raises(ValueError):
        sl.add_recipe(make_bowl(), 0)

def test_negative_portions():
    sl = ShoppingList()
    with pytest.raises(ValueError):
        sl.add_recipe(make_bowl(), -1)

def test_remove():
    sl=ShoppingList()
    sl.add_recipe(make_bowl(), 1)
    sl.remove_recipe("Боул")
    assert sl._items == []

def test_remove_unknown():
    sl=ShoppingList()
    sl.add_recipe(make_bowl(), 1)
    sl.remove_recipe("Рандом")
    assert len(sl._items) == 4

def test_remove_only_one():
    sl = ShoppingList()
    sl.add_recipe(make_bowl(), 1)
    sl.add_recipe(make_cheesecake(), 1)
    sl.remove_recipe("Боул")
    for item in sl._items:
        assert item[1]=="Чизкейк"

def test_sum():
    sl = ShoppingList()
    sl.add_recipe(make_bowl(), 1)
    sl.add_recipe(make_cheesecake(), 1)
    result=sl.get_list()
    found = False
    for ing in result:
        if ing.name=="Шоколад":
            assert ing.quantity == 100.0
            found = True
    assert found

def test_sorted():
    sl = ShoppingList()
    sl.add_recipe(make_bowl(), 1)
    result=sl.get_list()
    names = []
    for ing in result:
        names.append(ing.name)
    assert names==sorted(names)

def test_combine():
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    sl1.add_recipe(make_bowl(), 1)
    sl2.add_recipe(make_cheesecake(), 1)
    combined = sl1+sl2
    assert len(combined.get_list())==len(sl1.get_list()) + len(sl2.get_list())

def test_not_change():
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    sl1.add_recipe(make_bowl(), 1)
    sl2.add_recipe(make_cheesecake(), 1)
    i = sl1 + sl2
    assert len(sl1._items)==4
    assert len(sl2._items) == 3