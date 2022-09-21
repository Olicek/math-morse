from __future__ import annotations

from Math import Math
from addition import Addition
from subtraction import Subtraction


class Print:

    exercises: list[Math]|None

    def __init__(self):
        self.exercises = None
        self.code_digits = None
        self.result = None

    def addResult(self, result: list[str]):
        self.result = result

    def addCodeDigits(self, code_digits: dict):
        self.code_digits = code_digits

    def addExercies(self, exercises: list[Math]):
        self.exercises = exercises

    def print(self):
        if self.code_digits is not None:
            print(self.code_digits)

        if self.exercises is not None:
            for exercise in self.exercises:
                print(str(exercise.first_number) + " " + exercise.sign + " " + str(exercise.second_number))

        if self.result is not None:
            print(self.result)
