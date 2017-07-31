import abc

class AbstractOperation(metaclass=abc.ABCMeta):
    """
    In strategy pattern we declare a base object to use that extends ABCMeta from the abc module.
    This is used as a base for all of its children and insists that each child implement certain
    properties or methods.
    """

    @abc.abstractmethod
    def calculate(self, value1, value2):
        """
        This is the method that must be implemented by each child.
        :param value1: Integer or float
        :param value2: Integer or float
        """
