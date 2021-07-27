
import pymysql
import random
import time
# 连接数据库
con = pymysql.connect(host="localhost", user="root", password="", database="bank")

# 创建控制台
cursor = con.cursor()

bank_name = "中国工商银行昌平回龙观支行"  # 银行名称
registerDate = time.strftime("%d/%m/%Y %H:%M:%S")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    sql = "select account from person"
    cursor.execute(sql)
    data = cursor.fetchall()
    length = len(data)
    # 1.判断数据库是否已满
    if length >= 100:
        return 3
    # # 2.判断用户是否存在
    if data is not None:
        return 2
    else:
    # # 3.正常开户
        sql = "insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param = [account,username,password,country,province,street,gate,money,registerDate,bank_name]
        cursor.execute(sql, param)
        con.commit()
        return 1

# 开户
def addUser():
    username = input("请输入您的用户名：")
    while True:
        password = input("请输入您的开户密码：")
        if len(password) != 6:
            print('密码必须设置为6位！')
        else:
            if password.isdigit():
                password = int(password)
                break
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = input("请输入您的开户初始余额：")
    if money.isdigit():
        money = int(money)
    else:
        print('初始金额请输入数字！')
    account = random.randint(10000000, 99999999)  # 随机产生8位数字
    status = bank_addUser(account, username, password, country, province, street, gate, money)
    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在。")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息----------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            -----------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))

# 银行的存钱逻辑
def bank_saveMoney(account, saveMon):
    sql = "select * from person where account = %s"
    a = [account]
    cursor.execute(sql, a)
    data = cursor.fetchall()
    if data is None:
        return False
    else:
        sql = "update person set money = money + %s WHERE account = %s"
        param = [saveMon, account]
        cursor.execute(sql, param)
        con.commit()

# 存钱
def saveMoney():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        saveMon = input('请输入您要存入的金额：￥')
        if saveMon.isdigit():
            saveMon = int(saveMon)
            status = bank_saveMoney(account, saveMon)
            if status is False:
                print('账号不存在！')
                saveMoney()
            else:
                cursor.execute("SELECT * FROM `person` where account = %s " % account)
                record = cursor.fetchone()
                li = []
                li.append(record)
                print('存钱成功，您当前余额为', li[0][7], '元！')
        else:
            print('金额输入错误，请重新输入！')
    else:
        print('账号格式输入错误，请重新输入！')
        saveMoney()

# 银行的取钱逻辑
def bank_getMoney(account, pwd, getMon):
    cursor.execute("SELECT * FROM `person` where account = %s" % account)
    record = cursor.fetchone()
    li = []
    li.append(record)
    if record is None:
        return 1
    if li[0][2] != pwd:
        return 2
    if getMon > li[0][7]:
        return 3


# 取钱
def getMoney():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        pwd = input('请输入您的密码：\n')
        if pwd.isdigit():
            pwd = int(pwd)
            getMon = input('请输入您要提取的金额：￥')
            if getMon.isdigit():
                getMon = int(getMon)
                status = bank_getMoney(account, pwd, getMon)
                if status == 1:
                    print('您输入的账号不存在！')
                    getMoney()
                else:
                    if status == 2:
                        print('您输入的密码错误！')
                        getMoney()
                    else:
                        if status == 3:
                            print('您的账号余额不足！')
                            getMoney()
                        else:
                            sql = "update person set money = money - %s WHERE account = %s"
                            param = [getMon, account]
                            cursor.execute(sql, param)
                            con.commit()
                            cursor.execute("SELECT * FROM `person` where account = %s " % account)
                            record = cursor.fetchone()
                            li = []
                            li.append(record)
                            print('取钱成功，您的当前余额为', li[0][7], '元！')
            else:
                print('金额输入错误，请重新输入！')
                getMoney()
        else:
            print('密码必须为数字！')
            getMoney()
    else:
        print('账号输入错误，请重新输入！')
        getMoney()

# 银行的转账逻辑
def bank_transferMoney(account, account1, pwd, transferMon):
    cursor.execute("SELECT * FROM `person` where account = %s" % account)
    record = cursor.fetchone()
    li = [record]
    if record is None:
        return 1
    cursor.execute("SELECT * FROM `person` where account = %s" % account1)
    record = cursor.fetchone()
    if record is None:
        return 1
    if pwd != li[0][2]:
        return 2
    if transferMon > li[0][7]:
        return 3

# 转账
def transferMoney():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        account1 = input('请输入您要转入的账号：\n')
        if account1.isdigit():
            account1 = int(account1)
            if account == account1:
                print('不能自己给自己转账！')
                transferMoney()
            else:
                pwd = input('请输入您的密码：\n')
                if pwd.isdigit():
                    pwd = int(pwd)
                    transferMon = input('请输入您要转的金额：\n')
                    if transferMon.isdigit():
                        transferMon = int(transferMon)
                        status = bank_transferMoney(account, account1, pwd, transferMon)
                        if status == 1:
                            print('您输入的账号不存在！')
                            transferMoney()
                        else:
                            if status == 1:
                                print('您要转入的账号不存在！')
                                transferMoney()
                            else:
                                if status == 2:
                                    print('您输入的密码不正确！')
                                    transferMoney()
                                else:
                                    if status == 3:
                                        print('您的账号余额不足！')
                                        transferMoney()
                                    else:
                                        cursor.execute("update person set money = money - %s WHERE account = %s" % (transferMon,account) )
                                        cursor.execute("update person set money = money + %s WHERE account = %s" % (transferMon,account1))
                                        con.commit()
                                        cursor.execute("select * from person WHERE account = %s" % account)
                                        record = cursor.fetchone()
                                        li = [record]
                                        print('转账成功，您向账号', account1, '转账', transferMon,
                                              '元，您的账号当前余额为：', li[0][7], '元！')
                    else:
                        print('金额请输入数字！')
                else:
                    print('密码必须为数字！')
                    transferMoney()
        else:
            print('您输入的要转入的账号格式错误！')
            transferMoney()
    else:
        print('您输入的账号格式错误！')
        transferMoney()

# 银行的查询逻辑
def bank_query(account, pwd):
    cursor.execute("select * from person WHERE account = %s" % account)
    record = cursor.fetchone()
    li = [record]
    if record is None:
        print('您输入的账号不存在！')
        query()
    else:
        if pwd != li[0][2]:
            print('您输入的密码不正确！')
            query()
        else:
            print('查询成功，您的个人信息如下:')
            info = '''
                        ----------个人信息----------
                        用户名：%s
                        密码：%s
                        账号：%s
                        地址信息
                            国家：%s
                            省份：%s
                            街道：%s
                            门牌号: %s
                        余额：%s
                        开户行地址：%s
                        ------------------------------
                    '''
            print(info % (li[0][1], li[0][2], li[0][0], li[0][3],li[0][4],li[0][5],
                          li[0][6],li[0][7],li[0][8]))


# 查询
def query():
    account = input('请输入您的账号：\n')
    if account.isdigit():
        account = int(account)
        pwd = input('请输入您的密码：\n')
        pwd = int(pwd)
        bank_query(account, pwd)
    else:
        print('账号格式输入错误！')
        query()

# 退出
def exit():
    print('Bye!')


# 菜单界面
def welcome():
    print('*'.center(40, '*'))
    print('*         中国工商银行-账户管理系统         *')
    print('*'.center(40, '*'))
    print('*                1.开户                 *')
    print('*                2.存钱                 *')
    print('*                3.取钱                 *')
    print('*                4.转账                 *')
    print('*                5.查询                 *')
    print('*                6.Bye!                *')
    print('*'.center(40, '*'))

while True:
    welcome()
    num = input('请输入您要进行的业务:\n')
    if num.isdigit():
        num = int(num)
        if num == 1:
            addUser()  # 开户
        elif num == 2:
            saveMoney()  # 存钱
        elif num == 3:
            getMoney()  # 取钱
        elif num == 4:
            transferMoney()  # 转账
        elif num == 5:
            query()  # 查询
        elif num == 6:
            exit()  # 退出
            break
        else:
            print('您选择的业务不存在，请重新输入！')
    else:
        print('请输入数字！')
# 关闭资源
cursor.close()
con.close()