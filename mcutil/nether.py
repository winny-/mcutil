"""
nether.py -- A Python module for calculating Nether Portal placement
in Minecraft.
"""


from mcutil.common import simplify, Point


def overworld_to_nether(coord):
    """Convert overworld coordinate to nether's corresponding coordinate."""
    x, z = [simplify(n/8.0) for n in coord[:2]]
    return Point(x, z)


def nether_to_overworld(coord):
    """Convert nether coordinate to overworld's corresponding coordinate."""
    x, z = [simplify(n*8.0) for n in coord[:2]]
    return Point(x, z)
