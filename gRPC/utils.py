from faker import Faker
import random
from models import db, user

fake = Faker()


def generate_user():
    return fake.first_name(), fake.last_name(), random.randint(0, 100)


def create_users(number: int):
    with open("users.txt", "a+") as file:
        for i in range(number):
            fname, lname, age = generate_user()
            file.write(f"{fname}:{lname}:{age}\n")


def migrate():
    user.User.__table__.create(db.engine)


if __name__ == "__main__":
    # db = next(db.get_session())
    # new_user = user.User(first_name="1", last_name="2", age=1)
    # db.add(new_user)
    # db.commit()
    # migrate()
    # create_users(10000)
    pass
