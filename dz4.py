import random

class RandomMathematicOperation:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
        self.result = self._perform_random_mathematic_operation()

    def _perform_random_mathematic_operation(self):
        operations = [
            self._add,
            self._subtract,
            self._multiply,
            self._divide
        ]
        operation = random.choice(operations)
        return operation()

    def _add(self):
        return self._num1 + self._num2

    def _subtract(self):
        return self._num1 - self._num2

    def _multiply(self):
        return self._num1 * self._num2

    def _divide(self):
        if self._num2 != 0:
            return self._num1 / self._num2


    def __str__(self):
        return str(self.result)

number1 = 25
number2 = 10
mathematicoperation = RandomMathematicOperation(number1, number2)
print(mathematicoperation)
