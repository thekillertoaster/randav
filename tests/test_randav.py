import unittest
import randav as random


class TestRandav(unittest.TestCase):
    def test_randint(self):
        result = random.randint(1, 10)
        self.assertTrue(1 <= result <= 10)

    def test_uniform(self):
        result = random.uniform(0, 1)
        self.assertTrue(0 <= result < 1)

    # Add more test cases here


if __name__ == "__main__":
    unittest.main()
