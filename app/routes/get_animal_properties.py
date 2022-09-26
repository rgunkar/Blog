# ISP Broken Code

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#     @abstractmethod
#     def walk(self):
#         pass
#     @abstractmethod
#     def swim(self):
#         pass
#     @abstractmethod
#     def fly(self):
#         pass
#
# class Cat(Animal):
#     def eat(self):
#         return True
#     def walk(self):
#         return True
#     def swim(self):
#         raise NotImplemented
#     def fly(self):
#         raise NotImplemented
#
# class Duck(Animal):
#     def eat(self):
#         return True
#     def walk(self):
#         return True
#     def swim(self):
#         return True
#     def fly(self):
#         raise NotImplemented
#
# class Pigeon(Animal):
#     def eat(self):
#         return True
#     def walk(self):
#         return True
#     def swim(self):
#         raise NotImplemented
#     def fly(self):
#         return True


# ISP Correct Code
from abc import ABC, abstractmethod
from flask import render_template
from app import app


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def walk(self):
        pass


class SwimAbility(ABC):
    @abstractmethod
    def swim(self):
        pass


class FlyAbility(ABC):
    @abstractmethod
    def fly(self):
        pass


class Cat(Animal):
    def eat(self):
        return "eats "

    def walk(self):
        return "walks "

    def __repr__(self):
        return self.eat() + self.walk()

class Duck(Animal, SwimAbility):
    def eat(self):
        return "eats "

    def walk(self):
        return "walks "

    def swim(self):
        return "swims "

    def __repr__(self):
        return self.eat() + self.walk() + self.swim()

class Pigeon(Animal, FlyAbility):
    def eat(self):
        return "eats, "

    def walk(self):
        return "walks, "

    def fly(self):
        return "Fly, "

    def __repr__(self):
        return self.eat() + self.walk() + self.fly()


@app.route('/get_animal_properties/cat')
def get_animal_properties_cat():
    animal_properties = Cat()
    return render_template('animal_properties.html', animal_properties=animal_properties, title='Solid Principle')


@app.route('/get_animal_properties/duck')
def get_animal_properties_duck():
    animal_properties = Duck()
    return render_template('animal_properties.html', animal_properties=animal_properties, title='Solid Principle')


@app.route('/get_animal_properties/pigeon')
def get_animal_properties_pigeon():
    animal_properties = Pigeon()
    return render_template('animal_properties.html', animal_properties=animal_properties, title='Solid Principle')
