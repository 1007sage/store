from collections import Counter
f = open(file="baidu_x_system.log", mode="r+", encoding="utf-8")
# 遍历每行，获取IP
# data = f.readlines()
# list = [i.split(" ")for i in data]
ip = [i[0] for i in [i.split(" ") for i in f.readlines()]]
print(ip)
result = Counter(ip)  # 统计每个ip出现的次数
print(result)