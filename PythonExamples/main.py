
# Create a list of 100 numbers.
numbers = [i for i in range(100)]

def get_even_numbers(numbers):
    #Create a list of even numbers.
    even_numbers = [i for i in numbers if i % 2 ==0]
    return even_numbers

even_numbers =get_even_numbers(numbers)
odd_numbers = [i for i in numbers if i % 2 == 1]

print("Even numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# A list of 10 people.

PEOPLE = [
    Person("Celso", 32),
    Person("Ana", 36),
    Person("Kaka", 3)
]
        