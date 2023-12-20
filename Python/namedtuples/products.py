"""named tuples are great when working with csv data"""
import csv
from collections import namedtuple

with open("products.csv", "r") as f:
    reader = csv.reader(f)
    fields = next(reader)
    Product = namedtuple("Product", fields)
    all_products = [Product(*row) for row in reader]

for product in all_products:
    print(f"{product.Name}: ${product.SalePrice}")
