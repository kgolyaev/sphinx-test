class MyAddClass():
    """
    MyAddClass
    ===============
    A class developed to test sphinx documentation builder. It stores two 
    numbers and has a method to return their sum.

    :param x: 
        First input parameter, created to simulate how well documentation 
        parser handles new lines.
    :param y: 
        Another parameter, this time without new lines.

    :result: An object of class MyAddClass.
    
    :example:
    >>> x_input, y_input = 1, 2
    >>> test_class = MyTestClass(x=x_input, 
    ...                          y=y_input)
    >>> test_class
    <test_class.MyAddClass at 0x24c6027ff98>
    """

    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def add(self):
        """
        Class method
        ===============
        Adds ``self.x`` and ``self.y`` and returns their sum. Also checks for 
        them being numeric and throws ``TypeError`` when inputs are messed up.

        :result: 
            An number that is ``self.x + self.y``.

        :raises: 
            ``TypeError`` if ``self.x`` or ``self.y`` is not numeric. Should 
            really be implemented through ``@properties``.

        :example:
        >>> instance = MyTestClass(x=1, y=2)
        >>> instance
        3
        """
        
        try:
            _x = self.x + 1
        except TypeError:
            print("self.x is not numeric!")
        try:
            _y = self.y + 1
        except TypeError:
            print("self.y is not numeric!")
        return self.x + self.y







