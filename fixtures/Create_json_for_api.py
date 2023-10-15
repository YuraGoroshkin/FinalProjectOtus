from faker import Faker
from random import randint

fake = Faker()


class CreateJson:
    def json_message(self):
        data_message = {
            "messageid": fake.random_number(digits=3),
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "subject": fake.sentence(),
            "description": fake.text()
        }
        print(data_message)
        return data_message

    def json_room(self):
        data_room = {
            "roomid": fake.unique.random_number(digits=3),
            "roomName": fake.name(),
            "type": fake.random_element(elements=('Single', 'Double', 'Suite')),
            "accessible": fake.random_element(elements=(True, False)),
            "image": fake.image_url(),
            "description": fake.text(),
            "features": [
                fake.random_element(elements=('Radio', 'TV', 'Views', 'Safe', 'WiFi', 'Refreshments'))
            ],
            "roomPrice": randint(100, 999)
        }
        print(data_room)
        return data_room
