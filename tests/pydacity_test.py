from context import pydacity

import unittest


class PydacityTestSuite(unittest.TestCase):
    """ File stats test cases. """

    def setUp(self):
        self.TEST_FILE = "test.wav"

    def test_file_stats(self):
        stats = pydacity.file_stats(self.TEST_FILE)
        self.assertEqual(stats["filename"], self.TEST_FILE)
        self.assertEqual(stats["duration"], 12.3)

if __name__ == '__main__':
    unittest.main()
