from random import random


class Animal:
    live = True
    sound = None
    _cords = [0, 0, 0]
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if dz in self._cords < 0 :
            print("It's too deep, i can't dive")
        else:
            self._cords.append(self.move)

    def get_cords(self):
        print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')


    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0" )
    def speak(self):
        print( f'{self.sound}')

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        import random
        random_number = random.randint(0, 5)
        print(f"Here are(is) {random_number} eggs for you")
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):

        dz = abs(dz)
        new_z = self._cords[2] - dz * (self.speed / 2)

        self._cords[2] = new_z




class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
class Duckbill (Bird, PoisonousAnimal, AquaticAnimal ):
    sound = "Click-click-click"

db = Duckbill(10)

print(db.live)

print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()

