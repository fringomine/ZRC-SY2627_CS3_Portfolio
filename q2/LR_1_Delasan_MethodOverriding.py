class Animal:
    def __init__(self, name, eat, make_sound):
        self.__name = name
        self.__eat = eat
        self.__make_sound = make_sound

    def set_name(self, name):
        self.__name = name

    def set_eat(self, eat):
        self.__eat = eat

    def set_make_sound(self, make_sound):
        self.__make_sound = make_sound

    def get_name(self):
        return self.__name

    def get_eat(self):
        return self.__eat

    def get_make_sound(self):
        return self.__make_sound


class Lion(Animal):
    def __init__(self, name, eat, make_sound):
        super().__init__(name, eat, make_sound)

    def get_name(self):
        return super().get_name()

    def get_eat(self):
        return super().get_eat()

    def get_make_sound(self):
        return super().get_make_sound()


class Elephant(Animal):
    def __init__(self, name, eat, make_sound):
        super().__init__(name, eat, make_sound)

    def get_name(self):
        return super().get_name()

    def get_eat(self):
        return super().get_eat()

    def get_make_sound(self):
        return super().get_make_sound()


class Monkey(Animal):
    def __init__(self, name, eat, make_sound):
        super().__init__(name, eat, make_sound)

    def get_name(self):
        return super().get_name()

    def get_eat(self):
        return super().get_eat()

    def get_make_sound(self):
        return super().get_make_sound()


Lion1 = Lion("Simba", "Fresh Meat", "Roars")
Elephant1 = Elephant("Dumbo", "Grass and fruits", "Trumpets")
Monkey1 = Monkey("George", "Bananas", "Chatters")

print(f"{Lion1.get_name()} {Lion1.get_make_sound()} loudly!")
print(f"{Lion1.get_name()} eats {Lion1.get_eat()}.")
print("-----")
print(f"{Elephant1.get_name()} {Elephant1.get_make_sound()}!")
print(f"{Elephant1.get_name()} eats {Elephant1.get_eat()}.")
print("-----")
print(f"{Monkey1.get_name()} {Monkey1.get_make_sound()}!")
print(f"{Monkey1.get_name()} eats {Monkey1.get_eat()}.")