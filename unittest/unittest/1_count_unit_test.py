# cf. https://www.jianshu.com/p/a73a9b68abbf

class Count:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 加法
    def div(self):
        return self.a / self.b


#### Unit Test Cases ----------------------------------
import unittest2 as unittest
# import unittest

class TestCount(unittest.TestCase):
    # 测试的初始化
    def setUp(self):
        print("test start")

    # 测试用例add的编写
    def test_add(self):
        self.Count = Count(2, 3)
        self.assertEqual(self.Count.add(), 5)

    # 测试用例sub的编写
    def test_sub(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.sub(), 3)

    # 测试用例mul的编写
    def test_mul(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.mul(), 18)

    # 测试用例div的编写
    def test_div(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.div(), 2)

    # 测试的回收-测试的环境还原
    def tearDown(self):
        print("test end")


if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_sub"))
    suite.addTest(TestCount("test_mul"))
    suite.addTest(TestCount("test_div"))

    # 测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
