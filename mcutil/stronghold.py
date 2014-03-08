from common import simplify, Point
from math import cos, radians, sin, tan


CLOCKWISE = radians(-120)
COUNTERCLOCKWISE = radians(120)


def rotate(location, direction=CLOCKWISE):
    """
    Find a stronghold 120 degrees clockwise or counter-clockwise from location.
    location is an tuple of x and z. direction can either be CLOCKWISE or
    COUNTERCLOCKWISE.
    """
    location = Point(*location)
    x = simplify(cos(direction) * location.x + -sin(direction) * location.z)
    z = simplify(sin(direction) * location.x + cos(direction) * location.z)
    return Point(x, z)


def guess_locations(location):
    """Convenience function to guess where other Strongholds are located."""
    location = Point(*location)
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
    p1 = Point(*location1['point'])
    p2 = Point(*location2['point'])
    x1, z1 = -p1.x, -p1.z
    f1 = tan(-radians(location1['direction']))
    x2, z2 = -p2.x, -p2.z
    f2 = tan(-radians(location2['direction']))

    z = ((f2 * z2) - (x2 + f1*z1 - x1)) / (f1 - f2)
    x = (f2 * (z + z2)) - x2

    return Point(simplify(x), simplify(z))
