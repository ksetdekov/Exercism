import unittest


def int32_to_ip(int32):
    bin_value = bin(int32)[2:].zfill(32)
    parts = [bin_value[i:i + 8] for i in range(0, len(bin_value), 8)]
    parts = [str(int(k, 2)) for k in parts]

    return '.'.join(parts)


class TestingFunction(unittest.TestCase):
    def testCases(self):  # test method names begin with 'test'
        self.assertEqual(int32_to_ip(2154959208), "128.114.17.104")

    def testZero(self):  # test method names begin with 'test'
        self.assertEqual(int32_to_ip(0), "0.0.0.0")

    def testBig(self):  # test method names begin with 'test'
        self.assertEqual(int32_to_ip(2149583361), "128.32.10.1")


if __name__ == '__main__':
    unittest.main()
