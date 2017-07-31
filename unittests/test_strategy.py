import unittest
from strategy.strategy import Strategy
from strategy.operations.add import Add
from strategy.operations.subtract import Subtract
from strategy.operations.multiply import Multiply
from strategy.operations.divide import Divide


class TestStrategy(unittest.TestCase):

    def test_add(self):
        value1, value2 = 3,5
        operation = Add()
        strategy = Strategy(operation)
        self.assertEqual(strategy.return_answer(value1, value2), (value1 + value2))

    def test_subtract(self):
        value1, value2 = 3, 5
        operation = Subtract()
        strategy = Strategy(operation)
        self.assertEqual(strategy.return_answer(value1, value2), (value1 - value2))

    def test_multiply(self):
        value1, value2 = 3, 5
        operation = Multiply()
        strategy = Strategy(operation)
        self.assertEqual(strategy.return_answer(value1, value2), (value1 * value2))

    def test_divide(self):
        value1, value2 = 3, 5
        operation = Divide()
        strategy = Strategy(operation)
        self.assertEqual(strategy.return_answer(value1, value2), (value1 / value2))

    def test_divide_by_zero(self):
        value1, value2 = 3, 0
        operation = Divide()
        strategy = Strategy(operation)
        self.assertEqual(strategy.return_answer(value1, value2), "Can not divide by 0.")


if __name__ == '__main__':
    unittest.main()