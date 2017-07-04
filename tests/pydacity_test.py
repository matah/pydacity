from context import pydacity

import unittest


class PydacityTestSuite(unittest.TestCase):
    """ File stats test cases. """

    def setUp(self):
        self.TEST_FILE = "tests/audio_data/test.wav"

    def test_file_stats(self):
        audioFile = pydacity.AudioFile(self.TEST_FILE)

        self.assertEqual(audioFile.filename, self.TEST_FILE)
        self.assertEqual(audioFile.duration, 6.098866)
        self.assertEqual(audioFile.size, 1076002)
        self.assertEqual(audioFile.codec, 'pcm_s16le')
        self.assertEqual(audioFile.bits_per_sample, 16)
        self.assertEqual(audioFile.bitrate, 1411200)
        self.assertEqual(audioFile.channels, 2)
        self.assertEqual(audioFile.sample_rate, 44100)

if __name__ == '__main__':
    unittest.main()
