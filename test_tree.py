import unittest

class TestTree(unittest.TestCase):

    def test_failure(self):
        self.fail("Intentional failure.")


if __name__ == '__main__':
    unittest.main()
