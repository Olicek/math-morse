from random import randint
from Math import Math


class Addition(Math):

    def __init__(self, result, settings: dict):
        super().__init__(result, settings)
        self.first_number = randint(0, result)
        self.second_number = result - self.first_number
        super().setSign('+')
