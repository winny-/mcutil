from collections import namedtuple


Point = namedtuple('Point', ['x', 'z'])
Point3D = namedtuple('Point3D', ['x', 'z', 'y'])
Vector = lambda p, d: {'point': p, 'direction': d}
