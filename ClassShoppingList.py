from ClassIngredient import Ingredient
class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        scaled = recipe.scale(portions)
        for i in scaled.ingredients:
            self._items.append((i, recipe.title))

    def remove_recipe(self, title):
        new_items = []
        for i, rt in self._items:
            if rt != title:
                new_items.append((i, rt))
        self._items = new_items

    def get_list(self):
        totals = {}
        for ing, i in self._items:
            k = (ing.name, ing.unit)
            if k in totals:
                totals[k] += ing.quantity
            else:
                totals[k]=ing.quantity
        result = []
        for item in totals.items():
            k = item[0]
            q = item[1]
            n = k[0]
            u = k[1]
            result.append(Ingredient(n, q, u))
        result.sort(key=lambda x: x.name)
        return result

    def __add__(self, other):
        new_list = ShoppingList()
        new_list._items = self._items.copy() + other._items.copy()
        return new_list