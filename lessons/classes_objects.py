"""Example of a class and object instantiation."""

class Pizza: 
    """Models the idea of a pizza."""

    # Attribute Definitions 
    size: str 
    toppings: int 
    extra_cheese: bool = False


def __init__(self, size: str, toppings: int):
    self.size = size
    self.toppings = toppings
    




def price(self) -> float:
    """Calculate the price of a pizza."""
    total: float = 0.0
    if self.size == "large":
        total += 10.0
    else:
        total += 8.0

    total += self.toppings * 0.75

    if self.extra_cheese:
        total += 1.0
        
    return total

a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${price(a_pizza)}")