from selenium import webdriver
import time

# 创建一个谷歌驱动
driver = webdriver.Chrome()
# 打开页面
driver.get("https://www.taobao.com/")
# 窗口最大化
driver.maximize_window()

# 点击亲，请登录
driver.find_element_by_link_text("亲，请登录").click()
# 输入手机号
driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("17769246499")
# 输入密码
driver.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("111")
driver.find_element_by_xpath("//*[@id='login-form']/div[4]/button").click()
time.sleep(10)

# 关闭服务
driver.close()
# 关闭浏览器
driver.quit()
