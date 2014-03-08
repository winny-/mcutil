from collections import namedtuple


Point = namedtuple('Point', ['x', 'z'])
Point3D = namedtuple('Point3D', ['x', 'z', 'y'])


def Vector(point, direction, simple=None):
    """
    Easy to use Vector type constructor. If three arguments are passed,
    the first two are the x components of the point and the third is
    the direction component of the Vector.
    """
    if simple is not None:
        point = Point(point, direction)
        direction = simple
    return {
        'point': point,
        'direction': direction,
    }


def simplify(n):
    """Remove decimal places."""
    return int(round(n))