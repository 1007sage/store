import time


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver  # 将driver声明为全局变量

    def register(self, loginname, username, password, confirmPassword, age, sex, classname,
                 email, phoneNumber, address):
        # 点击新同学注册
        self.driver.find_element_by_link_text("新来的童鞋来这里注册一下哦").click()
        # 输入登录名
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(loginname)
        # 输入真实姓名
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys(username)
        # 输入密码
        self.driver.find_element_by_xpath("//*[@id='pwd']").send_keys(password)
        # 确认密码
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys(confirmPassword)
        # 点击下一步
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
        # 输入年龄
        self.driver.find_element_by_xpath("//*[@id='valid_age']").send_keys(age)
        # 输入性别
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys(sex)
        # 选择班级
        self.driver.find_element_by_xpath("//*[@id='classname']").send_keys(classname)
        # 点击下一步
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
        # 输入邮箱
        self.driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys(email)
        # 输入电话号码
        self.driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys(phoneNumber)
        # 输入居住地址
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys(address)
        # 点击注册
        self.driver.find_element_by_xpath("//*[@id='btn_reg']").click()

    def get_success_data(self):
        return self.driver.find_element_by_xpath("//*[@class='panel-title']").text

    def get_fail_data(self):
        return self.driver.find_element_by_class_name("panel-title").text
