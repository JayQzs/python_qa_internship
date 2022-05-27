# Write a program that will create a list of people with name, age, height, and weight
# Sort the list of people by age

from faker import Faker

def fake_data():
    faker = Faker()
    name = faker.name()
    age = faker.random_int(18, 65)
    height = faker.random_int(150, 200)
    weight = faker.random_int(45, 120)
    return name, age, height, weight

def create_list():
    for i in range(10):
        print(fake_data())

print(create_list())