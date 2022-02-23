"""Calculate the Foo et al. parameterization for atmospheric sea-spray
physics

Authors
-------
    - Matthew Bourque

Use
---

Dependencies
------------
"""

import argparse
import math


class FooParameterization:
    """The main class for calculating the Foo parameterization"""

    def calculate(self, radius, *args, **kwargs):
        """Calculate the foo parameterization.

        If the calculation is to involve more parameters someday, they
        could be accessed through args and/or kwargs.

        Parameters
        ----------
        radius : float
            The radius of the sphere

        Returns
        -------
        volume : float
            The volume of the sphere
        """

        volume = (4/3) * math.pi * radius**3

        return volume


def parse_args():
    """Parse command line arguments

    Returns
    -------
    args: argparse.Namespace object
        The parsed arguments
    """

    # Help description for arguments
    radius_help = 'The radius [float]'

    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--radius', dest='radius', action='store', type=float, required=True, help=radius_help)
    args = parser.parse_args()

    return args


def test_args(args):
    """Tests the command line arguments to make sure they are valid

    Parameters
    ----------
    args: argparse.Namespace object
        The command line arguments
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
