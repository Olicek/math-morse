class Math:
    first_number: int
    second_number: int
    result: int
    settings: dict
    sign: str

    def __init__(self, result: int, settings: dict):
        self.result = result
        self.settings = settings

    def sign(self) -> str:
        return self.sign

    def setSign(self, sign):
        self.sign = sign