#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product


# Useful to use with random's `sample` method to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    for i in range(num_products):
        adj = sample(ADJECTIVES, 1)
        noun = sample(NOUNS,1)
        item = adj[0] + ' ' + noun[0]
        price = randint(5, 101)
        weight = randint(5, 101)
        flammability = uniform(0.0, 2.5)
        print(f'1 - {item} costing ${price}')
        products.append(Product(item, price, weight, flammability))
    return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.

if __name__ == '__main__':
    print("Name equals Main!!")
    generate_products()

if __name__ == '__main__':
    inventory_report(generate_products())