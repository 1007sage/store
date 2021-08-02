from threading import Thread
import time


basket = 0  # 篮子里面包初始为0
class chef(Thread):

    def run(self) -> None:
        global basket
        while True:
            if basket < 600:
                time.sleep(0.5)
                basket += 1
            elif basket == 600:
                time.sleep(0.5)


class customer(Thread):
    money = 3000  # 顾客有3000元
    breadCart = 0  # 买到的面包
    name = ""  # 顾客姓名

    def run(self) -> None:
        while True:
            global basket
            if self.money >= 2:
                if basket > 0:
                    self.breadCart = self.breadCart + 1
                    self.money = self.money - 2
                    print(self.name, "成功抢到1个面包, 已经抢了", self.breadCart, "个面包")
                else:
                    time.sleep(1)
            else:
                print(self.name, "钱已花完，总共抢了", self.breadCart, "个面包")
                break

# 三个厨师
chef1 = chef()
chef2 = chef()
chef3 = chef()

chef1.num = "1"
chef2.num = "2"
chef3.num = "3"

# 六个顾客
c1 = customer()
c2 = customer()
c3 = customer()
c4 = customer()
c5 = customer()
c6 = customer()

c1.name = "李一"
c2.name = "王二"
c3.name = "刘三"
c4.name = "丁四"
c5.name = "陈五"
c6.name = "周六"

chef1.start()
chef2.start()
chef3.start()

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
