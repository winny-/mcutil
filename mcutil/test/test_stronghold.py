from mcutil.common import Point, Vector
from mcutil.stronghold import rotate, guess_locations, locate
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.locate_truths = [
            {
            'input': (
                Vector(498, 363, 72.82),
                Vector(512, 176, 61.81)
                ),
            'output': Point(-293, 608)
            }
        ]

    def test_rotate(self):
        pass

    def test_guess_locations(self):
        pass

    def test_locate(self):
        for truth in self.locate_truths:
            result = locate(*truth['input'])
            self.assertEquals(result, truth['output'])


if __name__ == '__main__':
    unittest.main()
