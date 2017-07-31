class Strategy:
    '''
    The strategy pattern is a pattern used to select an algorithm for use at runtime, allowing for
    flexibility in the code.

    Classification: Behavioral Pattern
    It takes a family of algorithms, encapsulates each one, and makes them interchangeable.
    Each algorithm usually operates with the same inputs and outputs.
    The algorithms implementations may be very different from each other.
    Long chains of if-else statements may signal a need to use the strategy pattern.
    Also known as the 'Policy Pattern'.
    '''

    def __init__(self, strategy):
        '''
        :param strategy: Object, subclass of AbstractOperation()
        '''
        self.strategy = strategy

    def return_answer(self, value1, value2):
        '''
        :param value1: Integer or Float
        :param value2: Integer or Float
        :return: Calls the calculate() method of the object defined in self.strategy
        '''
        return self.strategy.calculate(value1, value2)

