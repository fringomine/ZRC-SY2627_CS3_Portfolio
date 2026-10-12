class Pshs_Galaxy:
    def __init__(self, name):
        self.name = name

class Nationality:
    def __init__(self, country):
        self._name = country
        self._mood = ""
        self.country = country
        self.favfood = ""

    def get_mood(self):
        return self._mood

    def set_mood(self, mood):
        self._mood = mood

class Filpino(Nationality):
    def __init__(self, country):
        super().__init__(country)
        self._mood = "happy"
        self.favfood = "adobo"

class Indonesian(Nationality):
    def __init__(self, country):
        super().__init__(country)
        self._mood = "sad"
        self.favfood = "nasi goreng"

class Spanish(Nationality):
    def __init__(self, country):
        super().__init__(country)
        self._mood = "angry"
        self.favfood = "paella"

class Marvel:
    def __init__(self, hero):
        self.hero = hero

class Avengers(Marvel):
    def __init__(self, hero):
        super().__init__(hero)

class Alien(Pshs_Galaxy):
    def __init__(self, name, planet):
        super().__init__(name)
        self.planet = planet

Maurisity = (Filpino("Philippines"), Indonesian("Indonesia"), Spanish("Spain"), Avengers("Iron Man"), Alien("Xenomorph", "LV-426"))

display = (Maurisity[0].get_mood(), Maurisity[1].get_mood(), Maurisity[2].get_mood())

print(display)
