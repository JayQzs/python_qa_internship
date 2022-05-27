# Write a program that will create a list of people with name, age, height, and weight
# Sort the list of people by age

from faker import Faker

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @staticmethod
    def create_somebody():
        faker = Faker()
        name = faker.name()
        age = faker.random_int(18, 65)
        height = faker.random_int(150, 200)
        weight = faker.random_int(45, 120)
        return Person(name, age, height, weight)

class ListCreator:
    @staticmethod
    def create_list():
        list_people = []
        for i in range(10):
            new_people = Person.create_somebody()
            list_people.append(new_people)
        return list_people


sorted_list = ListCreator.create_list()
sorted_list.sort(key=lambda x: x.age)
for i in sorted_list:
    print(i)
