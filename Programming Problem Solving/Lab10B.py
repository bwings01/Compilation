# create dog class
class Dog:
    # base atrributes
    def __init__(self, age: int, weight: float, name: str, furColor: str, breed: str):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed
    
    # bark method
    def bark(self, barks: str = "Woof! Woof!"):
        return barks

    # rename method
    def rename(self, new_name: str):
        self.name = new_name

    # eat method
    def eat(self, food_amount: float):
        self.weight += food_amount 

print("You are about to create a dog.")
age = int(input("How old is the dog: "))
weight = float(input("How much does the dog weigh: "))
name = input("What is the dog's name: ")
furColor = input("What color is the dog: ")
breed = input("What breed is the dog: ")

# create usrs dog object
dog = Dog(age, weight, name, furColor, breed)
print(f"{dog.name} is a {dog.age} year old {dog.furColor} {dog.breed} that weighs {dog.weight} lbs.")

# have the dog bark to alert usr for food
print(dog.bark())
food_amount = float(input(f"{dog.name} is hungry, how much should he eat: "))
dog.eat(food_amount)

# ask usr to change dog name
new_name = input(f"{dog.name} isn't a very good name. What should they be renamed to: ")
dog.rename(new_name)

# print updated dog info
print(f"{dog.name} is a {dog.age} year old {dog.furColor} {dog.breed} that weighs {dog.weight} lbs.")