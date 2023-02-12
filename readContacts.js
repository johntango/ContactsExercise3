// generate json with 10 contacts data with fields id, name, email, phone, address, company, jobTitle, notes
// and save it to contacts.json file
var fs = require('fs');
// add faker module to generate fake data
const { faker } = require('@faker-js/faker');


function readContacts() {
    var contacts = [];
    for (var i = 0; i < 3; i++) {
        contacts.push({
            id: i,
            name: faker.name.fullName(),
            email: faker.internet.email(),
            phone: faker.phone.number(),
            address: faker.address.streetAddress(),
            company: faker.company.name(),
            jobTitle: faker.name.jobTitle(),
            notes: faker.lorem.notes()
        });
    }
    return contacts;
}
var contacts = readContacts();
contacts = console.log(JSON.stringify(contacts));
fs.writeFile('contacts.json', JSON.stringify(contacts), function (err) {
    if (err) {
        console.log("Error" + err);
    }
    console.log('contacts.json file generated');
}
);
