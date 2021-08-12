from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from init import StudentsRegister
from RegisterPage import RegisterPage
import time


@ddt
class TestRegister(TestCase):
    # 在每个操作前先做预备工作
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/HKR")
        time.sleep(2)

    # 在每个用例执行后，将浏览器关闭
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    # 注册成功用例
    @data(*StudentsRegister.register_success_data)
    def testRegistersuccess(self, testdata):
        # 提取登录名、真实姓名、密码、确认密码、年龄、性别、班级、邮箱、电话号码、居住地址、期望结果
        loginname = testdata["loginname"]
        username = testdata["username"]
        password = testdata["password"]
        confirmPassword = testdata["confirmPassword"]
        age = testdata["age"]
        sex = testdata["sex"]
        classname = testdata["classname"]
        email = testdata["email"]
        phoneNumber = testdata["phoneNumber"]
        address = testdata["address"]
        expect = testdata["expect"]

        register = RegisterPage(self.driver)
        register.register(loginname, username, password, confirmPassword, age, sex, classname,
                          email, phoneNumber, address)

        # 获取实际结果
        result = register.get_success_data()
        # 断言
        self.assertEqual(expect, result)


    # 重复使用登录名的数据
    @data(*StudentsRegister.register_fail_data)
    def testRegisterfail(self, testdata):
        # 提取登录名、真实姓名、密码、确认密码、年龄、性别、班级、邮箱、电话号码、居住地址、期望结果
        loginname = testdata["loginname"]
        username = testdata["username"]
        password = testdata["password"]
        confirmPassword = testdata["confirmPassword"]
        age = testdata["age"]
        sex = testdata["sex"]
        classname = testdata["classname"]
        email = testdata["email"]
        phoneNumber = testdata["phoneNumber"]
        address = testdata["address"]
        expect = testdata["expect"]

        register = RegisterPage(self.driver)
        register.register(loginname, username, password, confirmPassword, age, sex, classname,
                          email, phoneNumber, address)

        # 获取实际结果
        result = register.get_fail_data()
        # 截图
        self.driver.save_screenshot("失败.jpg")
        # 断言
        self.assertEqual(expect, result)
