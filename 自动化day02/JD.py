from selenium import webdriver
import time

# 创建一个谷歌驱动
driver = webdriver.Chrome()
# 打开页面
driver.get("https://www.jd.com")
# 窗口最大化
driver.maximize_window()

# 点击你好，请登录
driver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()
# 选择账户登录
driver.find_element_by_link_text("账户登录").click()
# 输入用户名
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("15656133626")
time.sleep(1)
# 输入密码
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("family123")
# 点击登录
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(7)

# 搜索华为Mate40
driver.find_element_by_xpath("//*[@id='key']").send_keys("华为mate40")
time.sleep(1)
driver.find_element_by_class_name("button").click()
time.sleep(3)

# 选择商品
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
time.sleep(3)
# 获取所有窗口的句柄
data = driver.window_handles
# 切换窗口
driver.switch_to.window(data[1])
# 加入购物车
driver.find_element_by_id('InitCartUrl').click()
time.sleep(3)
# 结算
driver.find_element_by_class_name("btn-addtocart").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='cart-body']/div[1]/div[6]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a/b").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='order-submit']/b").click()
time.sleep(3)


# 关闭服务
driver.close()
# 关闭浏览器
driver.quit()
