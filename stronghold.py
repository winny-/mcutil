# stronghold.py
#
# This file is in the public domain.

import math


CLOCKWISE = 'clockwise'
COUNTERCLOCKWISE = 'counter-clockwise'


def rotate(point, direction=CLOCKWISE):
    """
    Find a stronghold 120 degrees clockwise or counter-clockwise from point.
    point is an tuple of x and z. direction can either by CLOCKWISE or COUNTERCLOCKWISE
    """

    if direction == CLOCKWISE:
        radians = math.radians(-120)
    elif direction == COUNTERCLOCKWISE:
        radians = math.radians(120)
    else:
        raise RuntimeError('direction "{}" is unknown.'.format(direction))

    # {{cos(t), -sin(t)},{sin(t), cos(t)}} {{x},{z}}
    return (math.cos(radians) * point[0] + -math.sin(radians) * point[1],
            math.sin(radians) * point[0] + math.cos(radians) * point[1])


def guess_locations(location):
    return (location, rotate(location, CLOCKWISE), rotate(location, COUNTERCLOCKWISE))


def locate(location1, location2):
    """
    Locate a stronghold based on two tuples of data: location1 and location2.
    Each contains a x coordinate, a z coordinate, and the value of the Minecraft "facing" debug value.
    """

    # y-X1=tan(-F1deg)(x-Z1) ; y-X2=tan(-F2deg)(x-Z2)

    # y+x1=f1(x+z1) ; y+x2=f2(x+z2)
    x1 = -location1[0]
    z1 = -location1[1]
    f1 = math.tan(-math.radians(location1[2]))
    x2 = -location2[0]
    z2 = -location2[1]
    f2 = math.tan(-math.radians(location2[2]))

    # y+x1=f1*x+tmp_z1 ; y+x2=f2*x+tmp_z2
    tmp_z1 = f1 * z1
    tmp_z2 = f2 * z2

    # y=f1*x+tmp_z1
    tmp_z1 = tmp_z1 - x1

    # f1*x+tmp_z1=f2*x+tmp_z2

    # f1*x=f2*x+tmp_z2
    tmp_z1 = x2 + tmp_z1
    tmp_z1 = tmp_z2 - tmp_z1

    # tmp_f1*x=tmp_z2
    tmp_f1 = f1 - f2

    x = tmp_z1/tmp_f1

    # y+x2=tmp
    tmp = f2*(x+z2)

    # y=tmp-x2
    y = tmp - x2

    # yeah... x is really z and y is really x. Deal with it.
    return (y, x)
