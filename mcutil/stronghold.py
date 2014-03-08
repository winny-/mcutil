# stronghold.py
#
# This file is in the public domain.

from collections import namedtuple
from math import cos, radians, sin, tan


CLOCKWISE = radians(-120)
COUNTERCLOCKWISE = radians(120)

Location = namedtuple('Location', ['x', 'z'])
Vector = namedtuple('Vector', ['x', 'z', 'f'])


def simplify(n):
    """Remove decimal places."""
    return int(round(n))


def rotate(location, direction=CLOCKWISE):
    """
    Find a stronghold 120 degrees clockwise or counter-clockwise from location.
    location is an tuple of x and z. direction can either be CLOCKWISE or
    COUNTERCLOCKWISE.
    """
    location = Location(*location)
    x = simplify(cos(direction) * location.x + -sin(direction) * location.z)
    z = simplify(sin(direction) * location.x + cos(direction) * location.z)
    return Location(x, z)


def guess_locations(location):
    """Convenience function to guess where other Strongholds are located."""
    location = Location(*location)
    return (location,
            rotate(location, CLOCKWISE),
            rotate(location, COUNTERCLOCKWISE))


def locate(location1, location2):
    """
    Locate a stronghold based on two tuples of data: location1 and location2.
    Each contains a x coordinate, a z coordinate, and the value of the
    Minecraft "facing" debug value (f). For best results, x and z should be
    integral while f should have two decimal places.
    """
    location1 = Vector(*location1)
    location2 = Vector(*location2)

    x1 = -location1.x
    z1 = -location1.z
    f1 = tan(-radians(location1.f))
    x2 = -location2.x
    z2 = -location2.z
    f2 = tan(-radians(location2.f))

    z = ((f2 * z2) - (x2 + f1*z1 - x1)) / (f1 - f2)
    x = (f2 * (z + z2)) - x2

    return Location(simplify(x), simplify(z))
