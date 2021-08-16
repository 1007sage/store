from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'  # Appium Server, 端口默认为4723

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.1.2',
    'deviceName': '127.0.0.1:62001',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',
    'noReset': "true"
}

driver = webdriver.Remote(server, desired_caps)  # 连接手机和APP

while True:
    try:
        time.sleep(7)
        start_x = 500
        start_y = 1300
        distance = 1000
        driver.swipe(start_x, start_y, start_x, start_y - distance)
    except:
        print('没有更多视频了')
        driver.close()
        driver.quit()
        break
