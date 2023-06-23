import unittest
from main import Car
from main import random_number
from main import fake_random_number
from main import Cars
from main import CarData
from main import car_move
from main import cars_move
from main import winners

class TestCar(unittest.TestCase):
    def setUp(self):
        self.CAR = Car(fake_random_number, "car")
        self.CARS = [Car(fake_random_number, "car"), Car(fake_random_number, "car2")]
        self.CARDATAS = [CarData("car"), CarData("car2")]

    def test_new_car(self):
        car = self.CAR
        self.assertEqual(0, car.position)

    def test_move_car(self):
        self.assertEqual(1, self.CAR.move().position)

    def test_randomNumber(self):
        self.assertTrue(0 <= random_number() <= 9)

    def test_move_cars(self):
        self.assertEqual("car: -\ncar2: -\n", str(Cars(self.CARS).move()))

    def test_winner(self):
        cars = Cars(self.CARS).move()
        winners = list(car for car in cars.winners())
        self.assertEqual("car", winners[0].name)
        self.assertEqual("car2", winners[1].name)



    def test_cardata_move(self):
        self.assertEqual(1, car_move(CarData("car"), fake_random_number).position)

    def test_cardata_winner(self):
        result = winners(cars_move(self.CARS, fake_random_number))
        self.assertEqual("car", result[0].name)
        self.assertEqual("car2", result[1].name)
