import unittest
from day13.Calc import Calc
class TestCalc(unittest.TestCase):

    def testSubs(self):
        # 1.准备数据
        a = 0
        b = 1
        c = 1
        # 2.调用被测程序
        calc = Calc()
        dif = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, dif)

    def testSubs1(self):
        # 1.准备数据
        a = 1
        b = 0
        c = 1
        # 2.调用被测程序
        calc = Calc()
        dif = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, dif)

    def testSubs2(self):
        # 1.准备数据
        a = -9
        b = -1
        c = -8
        # 2.调用被测程序
        calc = Calc()
        dif = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, dif)

    def testSubs3(self):
        # 1.准备数据
        a = 99
        b = 1
        c = 98
        # 2.调用被测程序
        calc = Calc()
        dif = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, dif)

    def testSubs4(self):
        # 1.准备数据
        a = 1
        b = 99
        c = -98
        # 2.调用被测程序
        calc = Calc()
        dif = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, dif)

    def testSubs5(self):
        # 1.准备数据
        a = -99
        b = 100
        c = -199
        # 2.调用被测程序
        calc = Calc()
        dif = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, dif)

    def testSubs6(self):
        # 1.准备数据
        a = -100
        b = -101
        c = 1
        # 2.调用被测程序
        calc = Calc()
        dif = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, dif)

    def testMulti(self):
        # 1.准备数据
        a = -1
        b = 0
        c = 0
        # 2.调用被测程序
        calc = Calc()
        pro = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, pro)

    def testMulti1(self):
        # 1.准备数据
        a = 0
        b = 1
        c = 1
        # 2.调用被测程序
        calc = Calc()
        pro = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, pro)

    def testMulti2(self):
        # 1.准备数据
        a = -1
        b = -2
        c = 2
        # 2.调用被测程序
        calc = Calc()
        pro = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, pro)

    def testMulti3(self):
        # 1.准备数据
        a = 3
        b = 2
        c = 6
        # 2.调用被测程序
        calc = Calc()
        pro = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, pro)

    def testMulti4(self):
        # 1.准备数据
        a = -1
        b = 5
        c = -5
        # 2.调用被测程序
        calc = Calc()
        pro = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, pro)

    def testMulti5(self):
        # 1.准备数据
        a = 10
        b = -2
        c = -20
        # 2.调用被测程序
        calc = Calc()
        pro = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, pro)

    def testMulti6(self):
        # 1.准备数据
        a = 1
        b = 99
        c = 99
        # 2.调用被测程序
        calc = Calc()
        pro = calc.multi(a, b)

        # 3.断言
        self.assertEqual(c, pro)

    def testDevis(self):
        # 1.准备数据
        a = 0
        b = 1
        c = 0
        # 2.调用被测程序
        calc = Calc()
        quo = calc.devis(a, b)

        # 3.断言
        self.assertEqual(c, quo)

    def testDevis1(self):
        # 1.准备数据
        a = 9
        b = 1
        c = 9
        # 2.调用被测程序
        calc = Calc()
        quo = calc.devis(a, b)

        # 3.断言
        self.assertEqual(c, quo)

    def testDevis2(self):
        # 1.准备数据
        a = -9
        b = 1
        c = -9
        # 2.调用被测程序
        calc = Calc()
        quo = calc.devis(a, b)

        # 3.断言
        self.assertEqual(c, quo)

    def testDevis3(self):
        # 1.准备数据
        a = 9
        b = 3
        c = 3
        # 2.调用被测程序
        calc = Calc()
        quo = calc.devis(a, b)

        # 3.断言
        self.assertEqual(c, quo)

    def testDevis4(self):
        # 1.准备数据
        a = 2
        b = 5
        c = 0.4
        # 2.调用被测程序
        calc = Calc()
        quo = calc.devis(a, b)

        # 3.断言
        self.assertEqual(c, quo)

    def testDevis5(self):
        # 1.准备数据
        a = -2
        b = 5
        c = -0.4
        # 2.调用被测程序
        calc = Calc()
        quo = calc.devis(a, b)

        # 3.断言
        self.assertEqual(c, quo)

    def testDevis6(self):
        # 1.准备数据
        a = -80
        b = -4
        c = 20
        # 2.调用被测程序
        calc = Calc()
        quo = calc.devis(a, b)

        # 3.断言
        self.assertEqual(c, quo)

    def testDevis7(self):
        # 1.准备数据
        a = 80
        b = -4
        c = -20
        # 2.调用被测程序
        calc = Calc()
        quo = calc.devis(a, b)

        # 3.断言
        self.assertEqual(c, quo)