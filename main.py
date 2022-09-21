import json
from random import randint
import random

from Print import Print
from addition import Addition
from codeDict import CodeDict
from multiplication import Multiplication
from subtraction import Subtraction


def introduction():
    print('')


def calculate(letters, code_dict, setting) -> list:
    exercises = []
    for letter in letters:
        operation = random.choice(list(setting['calculations'].keys()))

        if operation == 'addition':
            exercise = Addition(code_dict[letter], setting)
        elif operation == 'subtraction':
            exercise = Subtraction(code_dict[letter], setting)
        elif operation == 'multiplication':
            exercise = Multiplication(code_dict[letter], setting)
        else:
            raise ValueError("Operace muze byt pouze + nebo -")

        exercises.append(exercise)

    return exercises


def settings():
    # Opening JSON file
    f = open('settings.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    setting = data['settings']

    keysToDelete = []
    for k, v in setting['calculations'].items():
        if v is None:
            keysToDelete.append(k)

    for k in keysToDelete:
        del setting['calculations'][k]

    # Closing file
    f.close()

    return setting


def generate():
    introduction()
    setting = settings()
    text = input('Insert word or sentence which you want convert to morse code (use ony alphabet signs): ')
    letters = [x for x in text.upper()]

    max_number = setting['maxLimit']
    allowed_chars = [x for x in setting['allowedChars'].upper()]


    if len(allowed_chars) > max_number:
        print(f"Prilis mnoho povolenych znaku. Pocet povolenych znaku je {len(allowed_chars)} a limit maximalniho cisla je {max_number}")

    code_dict = CodeDict(max_number)
    for char in allowed_chars:
        code_dict.add_letter(char)

    exercises = calculate(letters, code_dict.code_digit, setting)

    my_print = Print()
    Print.addResult(my_print, letters)
    Print.addCodeDigits(my_print, code_dict.code_digit)
    Print.addExercies(my_print, exercises)

    Print.print(my_print)


# run the script
if __name__ == "__main__":
    generate()
