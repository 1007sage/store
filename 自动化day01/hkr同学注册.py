from selenium import webdriver
import time

# 创建谷歌驱动
driver = webdriver.Chrome()
# 网页地址
driver.get('http://localhost:8080/HKR')
# 窗口最大化
driver.maximize_window()

# 新同学注册
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("sage")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("wang")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='pwd']").send_keys("123")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("123")
# 点击下一步
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
time.sleep(2)
# 基本信息
driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("20")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys("女")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='classname']").send_keys("Python自动化")
time.sleep(1)
# 点击下一步
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
time.sleep(2)
# 联系方式
driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys("1546129901@qq.com")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys("13685655541")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("北京市")
time.sleep(3)
# 点击注册
driver.find_element_by_xpath("//*[@id='btn_reg']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[3]/a/span/span").click()

# 关闭浏览器
time.sleep(1)
driver.quit()
