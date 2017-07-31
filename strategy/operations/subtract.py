from strategy.operations.operation import AbstractOperation


class Subtract(AbstractOperation):
    """
        Object uses AbstractOperation as a parent and implements the required methods or properties.
        This is one of the four strategies that can be used for our pattern.
        """

    def calculate(self, value1, value2):
        return value1 - value2
