# create sqlite database and customers table in python
import sqlite3
from faker import Faker
faker = Faker()


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':

    create_connection(r"pythonsqlite.db")
    # create customers table with 4 fields

    def checkCustomerTable():
        conn = sqlite3.connect('pythonsqlite.db')
        c = conn.cursor()
        c.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='customers'")
        if c.fetchone() is None:
            createCustomerTable()
        conn.close()

    def createCustomerTable():
        conn = sqlite3.connect('pythonsqlite.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE customers
                     (id integer, name text, email text, orders text)''')
        conn.commit()
        conn.close()

    def addCustomer(id, name, email, orders):
        conn = sqlite3.connect('pythonsqlite.db')
        c = conn.cursor()
        c.execute("INSERT INTO customers VALUES (?,?,?,?)",
                  (id, name, email, orders))
        conn.commit()
        conn.close()

   # add 3 cusomters to the table using faker
    def addCustomers():
        for i in range(3):
            addCustomer(i, faker.name(), faker.email(), faker.date())

    def printCustomerTable():
        conn = sqlite3.connect('pythonsqlite.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM customers'):
            print(row)
        conn.close()

    checkCustomerTable() # check if table exists, if not create it
    addCustomers() # add 3 customers to the table
    printCustomerTable() # print the table
