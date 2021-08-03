from HTMLTestRunner import HTMLTestRunner
import unittest
from mail import send_email
# 加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\pythonworkspace\project\day13", pattern="testCalc.py")

# 使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="计算器减法乘法除法运算的测试报告",
    verbosity=1,
    stream=open("cal.html", mode="w+", encoding="utf-8")
)

# 运行所有用例
runner.run(tests)

# 发送邮件
send_email()