from ClassIngredient import Ingredient

class Recipe:
    def __init__(self, title):
        self.title=title
        self.ingredients=[]
    def add_ingredient(self, ingredient):
        for item in self.ingredients:
            if item==ingredient:
                item.quantity +=ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        return isinstance(ratio, (int, float)) and ratio > 0
    def scale(self, ratio):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Некорректный коэффициент")

        new_recipe=Recipe(self.title)
        for ingredient in self.ingredients:
            new_ingredient = Ingredient(
                ingredient.name,
                ingredient.quantity*ratio,
                ingredient.unit
            )
            new_recipe.add_ingredient(new_ingredient)
        return new_recipe

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = self.title + "\n"
        for ingredient in self.ingredients:
            result += str(ingredient) + "\n"
        return result