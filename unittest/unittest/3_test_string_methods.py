# cd. https://docs.python.org/2/library/unittest.html

import unittest2 as unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print("Start test")

    def tearDown(self):
        print("  - Tear Down")

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        rst = ["hello", "world"]
        self.assertEqual(s.split(), rst)
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
    # x = round(1e-9 - 1e-10, 7)
    # print(x)