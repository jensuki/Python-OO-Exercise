"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """
        Initialize a serial # generator starting at 'start'

        Args:
        - self (first parameter)
        - start (int): The starting # for the generator. Default is 100

        """

        self.start = start   # Initialize self.start with the provided start value
        self.current = start # Initialize self.current with the provided start value

    def generate(self):
        """
        Generate the next sequential serial #

        Returns:
        - int: The next sequential serial #

        """

        self.current += 1
        return self.current - 1

    def reset(self):
        """
        Reset the generator to the original start number.

        """
        self.current = self.start

    def __repr__(self):
        """
        Verbal representation of generated serial #

        """
        return f'<SerialGenerator start={self.start} current={self.current}>'

