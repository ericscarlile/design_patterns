import abc


class MyABC(metaclass=abc.ABCMeta):
    """A very basic example of an Abstract Base Class Definition
    Full documentation for Abstract Base Classes (ABC) can be found at https://docs.python.org/3/library/abc.html.
    """

    # This decorator is used to signal that this abstract method must be implemented.
    @abc.abstractmethod
    def do_something(self, value):
        """This method must be implemented"""

    # This decorator is used to signal that this abstract property must be implemented.
    @property
    @abc.abstractmethod
    def some_property(self):
        """This is a setter for a property that must be implemented."""
