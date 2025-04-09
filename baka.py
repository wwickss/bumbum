import random

product = ["bread","cheese","yogurt","banana","watermelon","melon","ice-cream","fanta","fish","cookies"]
nahodna_product = random.choice(product)
print(f"Person 1 chose {nahodna_product}")
nahodna_product = random.choice(product)
print(f"Person 2 chose {nahodna_product}")
print(f"We will buy {nahodna_product}")
print(f"No, let`s buy {nahodna_product}")
if nahodna_product == random.choice(product):
    print("Let`s buy something else")
    