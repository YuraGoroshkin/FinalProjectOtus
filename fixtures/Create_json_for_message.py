import pytest
from faker import Faker

fake = Faker()


# @pytest.fixture
def json_message():
    data = {
        "messageid": fake.random_number(digits=3),
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "subject": fake.sentence(),
        "description": fake.text()
    }

    return data