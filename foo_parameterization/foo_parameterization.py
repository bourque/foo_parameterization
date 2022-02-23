import argparse
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


def parse_args():
    """
    """

    # Help description for arguments
    radius_help = 'The radius [float]'

    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-r --radius', dest='radius', action='store', type=float, required=True, help=radius_help)
    args = parser.parse_args()

    return args

def test_args(args):
    """
    """

    # Ensure that the radius is not a negative number
    assert args.radius >= 0, f'The given radius ({args.radius}) is a negative number'


if __name__ == '__main__':

    # Parse the arguments and make sure they are valid
    args = parse_args()
    test_args(args)

    # Perform calcuation
    foo = FooParameterization()
    result = foo.calculate(args.radius)

    # Print the results
    print(f'Result: {result}')
