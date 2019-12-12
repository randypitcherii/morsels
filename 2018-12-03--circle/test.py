import unittest, math

from solution import Circle

class TestRunner(unittest.TestCase):
    def test_ConstructCircleWithRadius(self):
        c = Circle(1)
        self.assertEqual(1, c.radius)
        self.assertEqual(2, c.diameter)
        self.assertAlmostEqual(math.pi, c.area)

    def test_ConstructCircleWithoutRadius(self):
        c = Circle()
        self.assertEqual(1, c.radius)
        self.assertEqual(2, c.diameter)
        self.assertAlmostEqual(math.pi, c.area)

    def test_RadiusChange(self):
        # create circle and check valid values
        c = Circle()
        self.assertEqual(1, c.radius)
        self.assertEqual(2, c.diameter)
        self.assertAlmostEqual(math.pi, c.area)

        # update radius and check valid values
        c.radius = 3
        self.assertEqual(3, c.radius)
        self.assertEqual(6, c.diameter)
        self.assertAlmostEqual(math.pi * 3**2, c.area)

if __name__ == '__main__':
    unittest.main()
