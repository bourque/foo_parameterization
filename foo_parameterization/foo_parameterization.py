import math


class FooParameterization:
    """
    """

    def calculate(self, radius, *args, **kwargs):
        """
        """

        volume = (4/3) * math.pi * radius**3

        # if calculation is to involve more parameters, it could reference args
        # and/or kwargs

        return volume


if __name__ == '__main__':

    # Perform calcuation
    foo = FooParameterization()
    result = foo.calculate(1)

    # Print the results
    print(f'Result: {result}')
