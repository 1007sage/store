from selenium import webdriver
import time

# 创建一个谷歌驱动
driver = webdriver.Chrome()
# 打开页面
driver.get("https://www.suning.com/")
# 窗口最大化
driver.maximize_window()
time.sleep(2)
# 搜索商品
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("华为mate40")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_02:0070094634_12199717163']/i/img").click()
time.sleep(1)
# 获取所有窗口的句柄
data = driver.window_handles
# 切换窗口
driver.switch_to.window(data[1])
# 加入购物车
driver.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()

time.sleep(3)
# 关闭服务
driver.close()
# 关闭浏览器
driver.quit()
