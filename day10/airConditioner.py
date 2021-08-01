# 定义空调类
class airConditioner:
    __brand = ""
    __price = 0

    # 设置品牌
    def setbrand(self, brand):
        self.__brand = brand

    # 获取品牌
    def getbrand(self):
        return self.__brand

    # 设置价格
    def setprice(self, price):
        if price < 0:
            print("对不起，输入非法！")
        else:
            self.__price = price

    # 获取价格
    def getprice(self):
        return self.__price

    # 开机
    def startingUp(self):
        print("空调开机了...")

    # 关机
    def shutDown(self, minutes):
        print(self.__brand, "空调将在", minutes, "分钟后自动关闭...")

# 创建空调对象
a = airConditioner()
a.setbrand("Green")
a.setprice(8999)
print("这台空调的品牌为:", a.getbrand(), "价格为:", a.getprice(), "元")
a.startingUp()
a.shutDown(5)
