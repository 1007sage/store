from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="这是HKR的测试报告",
    description="这是一份同学注册的测试报告",
    verbosity=1,
    stream = open(file="同学注册测试报告.html",mode="w+",encoding="utf-8")
)

runner.run(tests)