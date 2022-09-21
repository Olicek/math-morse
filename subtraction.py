from random import randint

from Math import Math


class Subtraction(Math):

    number_of_digits = {
        1: 9,
        2: 99,
        3: 999,
        4: 9999,
        5: 99999
    }

    def __init__(self, result, settings: dict):
        super().__init__(result, settings)
        super().setSign('-')

        if settings['calculations']['subtraction']['secondNumberMaxDigits'] is not None:
            second_number_candidate = settings['maxLimit'] - self.result
            if self.number_of_digits[settings['calculations']['subtraction']['secondNumberMaxDigits']] < second_number_candidate:
                second_number_candidate = self.number_of_digits[settings['calculations']['subtraction']['secondNumberMaxDigits']]
        else:
            second_number_candidate = settings['maxLimit'] - self.result

        if second_number_candidate > self.result:
            second_number_candidate = self.result

        self.second_number = randint(0, second_number_candidate)
        self.first_number = self.second_number + self.result

