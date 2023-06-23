import unittest
from main import Car
from main import randomNumber
from main import fakeRandomNumber
from main import Cars
from main import CarData
from main import car_move

class TestCar(unittest.TestCase):
    def setUp(self):
        self.CAR = Car(fakeRandomNumber, "car")
        self.CARS = [Car(fakeRandomNumber, "car"), Car(fakeRandomNumber, "car2")]

    def test(self):
        car = self.CAR
        self.assertEqual(0, car.position)

    def test_move(self):
        self.assertEqual(1, self.CAR.move().position)

    def test_randomNumber(self):
        self.assertTrue(0 <= randomNumber() <= 9)

    def test_cars(self):
        self.assertEqual("car: -\ncar2: -\n", str(Cars(self.CARS).move()))

    def test_winner(self):
        cars = Cars(self.CARS).move()
        winners = list(car for car in cars.winners())
        self.assertEqual("car", winners[0].name)
        self.assertEqual("car2", winners[1].name)

    def test_car_move(self):
        self.assertEqual(1, car_move(CarData("car"), fakeRandomNumber()).position)
