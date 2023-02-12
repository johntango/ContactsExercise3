# generate product table with 3 entries and fields: product_id, product_name, product_price, product_description
# generate a table of customers and their orders
# and save it to customers.json file
# fields: id name, email, orders (id, date, total, status, items (id, name, price, quantity, total))
from faker import Faker
import random
import json

faker = Faker()


def getCustomers():
    customers = []
    for i in range(3):
        customers.append({
            "id": i,
            "name": faker.name(),
            "email": faker.email(),
            "orders": getOrders()
        })
    return customers


def getOrders():
    orders = []
    for i in range(3):
        orders.append({
            "id": i,
            "date": faker.date(),
            # set price as number between 1 and 100


            # "status": random.choice(['pending', 'delivered', 'cancelled']),
            "items": getItems()
        })
    return orders


def getItems():
    items = []
    for i in range(3):
        items.append({
            "id": i,
            "name": faker.name(),
            "price": faker.random_int(min=1, max=10, step=1),
            "quantity": 10,
            "total": faker.random_int(min=1, max=100, step=1),
        })
    return items


customers = getCustomers()


def write_json(data, filename='customers2.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


write_json(customers)
