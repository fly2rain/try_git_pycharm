import unittest2


def cacl(a, b):
    return a / b


class MyTest(unittest2.TestCase):  # 类名需要以大写字母开头
    def setUp(self):
        print("每个用例执行之前都会执行")

    def tearDown(self):
        print("每个用例执行之后都会执行")

    @classmethod
    def setUpClass(cls):
        print("所有用例执行之前运行")

    @classmethod  # 类方法
    def tearDownClass(cls):
        print("所有用例执行之后运行")

    def test_a(self):
        res = cacl(1, 2)
        self._testMethodDoc = "正案例"  # 用于生成报告时用例描述的显示
        self.assertEqual(0.5, res, 'success')  # 断言

    def test_b(self):
        '''反案例'''  # 用于生成报告是用例描述的第二种显示方式
        res = cacl(1, 2)
        self.assertNotEqual(0.5, res, 'failed')


if __name__ == '__main__':
    unittest2.main()  # 可以运行所有以test开头的用例，用例的执行顺序按照test后面的ascii码值的大小顺序，值小的先执行
