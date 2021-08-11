from selenium import webdriver  # 浏览器驱动
import time

# 1.创建一个谷歌驱动
driver = webdriver.Chrome()

# 2.打开页面
driver.get(r"D:\汉科软\自动化\day01\练习的html\练习的html\跳转页面\pop.html")

# 3.最大化
driver.maximize_window()

# 4.定义按钮
driver.find_element_by_id("goo").click()

# 5.打开新窗口
data = driver.window_handles
driver.switch_to.window(data[1])

# 6.定位
driver.find_element_by_xpath("//*[@id='kw' and @name='wd']").send_keys("store")
driver.find_element_by_xpath("//*[@id='su']").click()

# 7.停顿3秒钟
time.sleep(3)

# 8.关闭浏览器
driver.quit()