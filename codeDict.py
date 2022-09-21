from random import randint


class CodeDict:

    code_digit: dict
    max_number: int

    def __init__(self, max_number: int):
        self.max_number = max_number
        self.code_digit = {}

    def add_letter(self, letter: str):
        number = randint(1, int(self.max_number))

        if letter in self.code_digit:
            return

        if number in self.code_digit.values():
            self.add_letter(letter)

        self.code_digit[letter] = randint(1, int(self.max_number))
