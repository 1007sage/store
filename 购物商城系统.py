# 导入模板
import random
# 1.准备商品
shop = [
    ["老干妈",10],
    ["lenovo PC",6000],
    ["薯片",7.5],
    ["CASIO Watch",1490],
    ["汉堡",20],
    ["泡芙",15],
    ["Dior999",250],
    ["辣条",3]
]
# 2.初始化金额
money = input("请输入您的余额：￥")
if money.isdigit():
    money = int(money)
else:
    print("请输入您的余额！")
    money = input("请输入您的余额：￥")
    money = int(money)


# 3.空的购物车
mycart = []

# 4.提示是否抽一张优惠券
a = int(input("是否抽取优惠券？ 1.是  2.否\n"))
if a == 2:
    print("土豪！开始买东西吧！")
elif a == 1:
    print("开始抽取优惠券！")
    num= int(random.randint(1,30))
    if 1 <= num <= 10:
        print("恭喜您获得老干妈七折活动优惠券！")
    else:
        print("恭喜您获得联想电脑一折活动优惠券！")
else:
    print("请按照要求输入是否抽取优惠券")

# 5.买东西
while money >= 3:
    # 5.1 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    # 5.2 请输入您想要的商品
    chose = input("请输入您想要的商品编号：")
    # 5.3 先判断输入的是不是数字
    if chose.isdigit():
        chose = int(chose)
        # 5.4 再判断是否存在该商品
        if chose > 7:
            print("您输入的商品不存在！")
        else:
            # 5.5 判断您的余额是否足够
            if money < shop[chose][1]:
                print("对不起，您的钱不够！")
            else:
                # 5.6 将商品添加到购物车 ，余额减去对应的钱
                if chose == 0 and 1 <= num <=10:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]*0.7
                    print("恭喜，成功添加购物车！,已使用老干妈七折活动优惠券，您的余额还剩￥：",money)
                elif chose == 1 and 10 < num <= 30:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1] * 0.1
                    print("恭喜，成功添加购物车！,已使用联想电脑一折活动优惠券，您的余额还剩￥：", money)
                else:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    print("恭喜，成功添加购物车！您的余额还剩￥：", money)
    elif chose == "q" or chose == "Q":
        print("再见！欢迎下次光临！")
        break
    else:
        print("对不起，您输入有误，请重新输入！")
else:
    print("余额不足！再见！")

# 打印购物小票
print("------------------------")
print("以下是您的购物小票，请拿好：")
for key, value in enumerate(mycart):
    print(key,value)
print("本次余额还剩：￥",money)
print("------------------------")

