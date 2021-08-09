import pymysql
host = "localhost"
user = "root"
password = ""
database = "用户数据"

con = pymysql.connect(host=host, user=user, password=password, database=database)
cur = con.cursor()

f = open(file="userData.txt", mode="r+", encoding="utf-8")  # 获取文件句柄
lines = f.readlines()  # 获取每一行数据放在一个列表
rows = len(open(file="userData.txt", mode="r+", encoding="utf-8").readlines())  # 获取行数
sum = 0
# 遍历每行
for i in range(rows):
    a = lines[i].split(',', 2)  # 按，分割次数
    sql = "insert into user values(%s,%s,%s)"
    param = [a[0], a[1], a[2]]
    cur.execute(sql, param)
    con.commit()
    mon = int(a[2])
    sum += mon
print("录入成功！")
print("所有人资产总和为:", sum, "元")
cur.close()
con.close()
f.close() # 关闭资源

