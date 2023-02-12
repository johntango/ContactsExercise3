# generate json with 10 contacts data with fields id, name, email, phone, address, company, jobTitle, notes
# and save it to contacts.json file
import json
from faker import Faker
faker = Faker()

def read_contacts():
    contacts = []
    for i in range(10):
        contacts.append({
            "id": i,

            "name": faker.name(),
            "email": faker.email(),
            "phone": faker.phone_number(),
            "address": faker.address(),
            "company": faker.company(),
            "jobTitle": faker.job(),
            "notes": faker.text()
        })
    return contacts


contacts = read_contacts()
with open('contactsPy.json', 'w') as outfile:
    json.dump(contacts, outfile)
print('contactsPy.json file generated')