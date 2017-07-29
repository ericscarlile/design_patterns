from abstract_base_class.my_abc import MyABC


class MyClass(MyABC):
    """Implementation of MyABC"""

    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of the abstract method required by MyABC class"""
        self._myprop *= 2 + value

    @property
    def some_property(self):
        """Setting the abstract property required by the MyABC class"""
        return self._myprop
