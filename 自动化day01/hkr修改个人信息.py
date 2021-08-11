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

# 修改个人信息
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']").click()
time.sleep(1)
# 修改年龄
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").clear()
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys("30")
time.sleep(1)
# 修改性别
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[5]/td[2]/select").send_keys("女")
time.sleep(1)
# 点击修改按钮
driver.find_element_by_xpath("//*[@id='btn_modify']").click()


# 退出登录
driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
time.sleep(2)

# 关闭浏览器
driver.quit()