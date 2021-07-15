#导入模板
import random
#使用random模块
num=int(random.randint(0,200))
count = 0
gold = 2000
while True:
    if gold == 0:
        print("金币不足，退出游戏")
        break
    else:
        guess = int(input("请输入您要猜的数字："))
        count = count + 1
        gold = gold - 200
        if num > guess:
            print("小了！")
        elif num < guess:
            print("大了！")
        else:
            print("恭喜你，猜中了！本次幸运数字为：",num,",本次猜了",count,"次！")
            gold = gold + 5000
            print("剩余金币：",gold)

            a =int(input("是否继续游戏？1.继续2.退出\n"))
            if a == 2:
                print("Bye!欢迎下次来玩！")
                break
            else:
                print("新的一轮开始啦！")

num = int(random.randint(0, 200))#重新获取随机数
count = 0






