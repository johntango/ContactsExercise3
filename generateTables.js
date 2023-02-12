// generate a table of customers and their orders 
// and save it to customers.json file 
// fields: id name, email, orders (id, date, total, status, items (id, name, price, quantity, total))
const { faker } = require('@faker-js/faker');
var fs = require('fs');

function getCustomers() {
    var customers = [];
    for (var i = 0; i < 3; i++) {
        customers.push({
            id: i,
            name: faker.name.fullName(),
            email: faker.internet.email(),
            orders: getOrders()
        });
    }
    return customers;
}
function getOrders() {
    var orders = [];
    for (var i = 0; i < 3; i++) {
        orders.push({
            id: i,
            date: faker.date.past(),
            total: faker.commerce.price(),
            //status: faker.random.arrayElement(['pending', 'delivered', 'cancelled']),
            items: getItems()
        });
    }
    return orders;
}
function getItems() {
    var items = [];
    for (var i = 0; i < 3; i++) {
        items.push({
            id: i,
            name: faker.commerce.productName(),
            price: faker.commerce.price(),
            // get a random number between 1 and 10
            quantity: 10,
            total: faker.commerce.price()
        });
    }
    return items;
}
var customers = getCustomers();
var object = { "customers": customers };

// write a json file give a json object customers



fs.writeFile('customers.json', JSON.stringify(object), function (err) {
    if (err) {
        console.log("Error" + err);
    }
    console.log('contacts.json file generated');
}
);

