from random import randint
import random
from Math import Math


class Multiplication(Math):

    def __init__(self, result, settings: dict):
        super().__init__(result, settings)
        self.first_number = randint(0, 10)
        self.second_number = random.choice(list(settings['calculations']['multiplication']['allowedDigits']))
        super().setSign('x')
