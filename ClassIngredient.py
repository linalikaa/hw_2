class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.unit = unit
        self.quantity=quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return self.name + ": " + str(self.quantity) + " " + self.unit
    def __repr__(self):
        return "Ingredient('" + self.name + "', " + str(self.quantity) + ", '" + self.unit + "')"
    def __eq__(self, other):
        return isinstance(other, Ingredient) and self.name == other.name and self.unit == other.unit