from selenium import webdriver
import time

# 创建一个谷歌驱动
driver = webdriver.Chrome()

# 打开页面
driver.get(r"http://localhost:8080/HKR")

# 最大化
driver.maximize_window()

# 输入登录名
driver.find_element_by_xpath("//*[@id='loginname' and @name='loginname']").send_keys("root")
time.sleep(1)

# 输入密码
driver.find_element_by_xpath("//*[@id='password' and @name='password']").send_keys("root")
time.sleep(1)

# 登录
driver.find_element_by_id("submit").click()
time.sleep(1)

# 下拉培训时间
driver.find_element_by_xpath("//*[@name='time' and @class='show_tea']").send_keys("9（上晚自习）")
time.sleep(1)

# 下拉授课讲师
driver.find_element_by_xpath("//*[@name='teaName' and @class='show_tea']").send_keys("贾生")
time.sleep(2)

# 评价内容
# driver.find_element_by_css_selector('div.label_box label:nth-child(2)>div').click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[2]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[2]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[2]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[2]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[3]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[3]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[3]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[1]/div").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='textarea']").send_keys("无")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='subtn']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a/span/span").click()

# 退出登录
driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
time.sleep(3)

# 关闭浏览器
time.sleep(2)
driver.quit()