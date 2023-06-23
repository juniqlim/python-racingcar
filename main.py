import random
from dataclasses import dataclass


class Car:
    def __init__(self, func, name, position=0):
        self.__name = name
        self.__position = position
        self.randomNumber = func

    @property
    def name(self):
        return self.__name
    @property
    def position(self):
        return self.__position

    def move(self):
        if self.randomNumber() > 5:
            return Car(self.randomNumber, self.name, self.position + 1)
        return self


class Cars:
    def __init__(self, cars):
        self.cars = cars

    def move(self):
        return Cars(list(car.move() for car in self.cars))

    def __str__(self):
        result = ""
        for car in self.cars:
            result += car.name + ": " + ("-" * car.position) + "\n"
        return result

    def winners(self):
        winners = []
        result = ""
        maxPosition = 0
        for car in self.cars:
            if car.position > maxPosition:
                maxPosition = car.position
        for car in self.cars:
            if car.position == maxPosition:
                result += car.name + ", "
                winners.append(car)
        return winners


def randomNumber():
    return int(random.random() * 10)


def fakeRandomNumber():
    return 6


def car_move(car, randomNumber):
    if randomNumber > 5:
        return CarData(car.name, car.position + 1)
    return car


@dataclass(frozen=True)
class CarData:
    name: str
    position: int = 0
