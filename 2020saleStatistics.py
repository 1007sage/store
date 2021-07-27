import xlrd

# 1.打开工作簿
wd = xlrd.open_workbook("data.xlsx", encoding_override=True)
# 2.打开要操作的选项卡
# 整体存储数据库
store = {}
'''
   存储结构：
        风衣:{
            "sum_money":xxx,  # 总销售额
            "sum_count":xxx,   # 总销售量
        },
        "羽绒服":{
            "sum_money":xxx,
            "sum_count":xxx    
        }
'''
# 获取所有工作簿选项卡个数
nsheet = wd.nsheets

# 现在要获取所有工作簿的表格数据
for i in range(nsheet):  # 遍历每个选项卡
    # 获取第n个选项卡
    st = wd.sheet_by_index(i)
    # 获取有多少行
    nrow = st.nrows
    for j in range(1, nrow):  # 遍历选项卡每一行
        cell = st.row_values(j)  # 获取第j行数据
        if cell[1] in store:  # 判断在存储库是否存在
            store[cell[1]] = {  # 若存在，则累加数据
                "sum_money": round(store[cell[1]]["sum_money"] + cell[2] * cell[4], 2),
                "sum_count": int(store[cell[1]]["sum_count"] + cell[4])
            }
        else:  # 若不存在，这是以第一次统计数据
            store[cell[1]] = {
                "sum_money": round(cell[2] * cell[4], 2),
                "sum_count": int(cell[4])
            }
# 全年统计总和
all_sum = sum(store[item]["sum_money"] for item in store)  # 全部总销售额
all_count = sum(store[item]["sum_count"] for item in store)  # 全部总销售量
print("------------------------------------------")
print("全年的统计总销售额：￥", round(all_sum, 2))
print("全年的统计总销售量：", round(all_count, 2), "件！")
for name in store:
    print(name, "的销售额占比为：", round(store[name]["sum_money"] / all_sum * 100, 2), "%")
    print(name, "的销售量占比为：", round(store[name]["sum_count"] / all_count * 100, 2), "%")


print("--------------每个月的销售总金额--------------")
totalsale = 0  # 初始化销售额
for m in range(12):
    month = str(m + 1) + '月'
    st = wd.sheet_by_name(month)
    rows = st.nrows  # 获取行数
    cols = st.ncols  # 获取列数

    sum = 0   # 初始化金额
    moneylist = []  # 钱的集合
    numlist = []  # 销售量的集合

    for i in range(cols):
        if i == 2:
            moneylist = st.col_values(i)[1:]    # 列出除表头的单价的集合
        elif i == 4:
            numlist = st.col_values(i)[1:]    # 列出除表头的数量的集合

    for j in range(len(moneylist)):
            sum = sum + moneylist[j] * numlist[j]
    print(m + 1, "月的销售总金额为：", round(sum, 1))
    totalsale += sum
print("全年的销售额为：￥",round(totalsale, 1))
print("--------------------------------------------")

print("-------------每个季度的销售额占比-------------")
totalsale1 = 0
for mm in range(0,3):
    month = str(mm+1) + '月'
    st = wd.sheet_by_name(month)
    rows = st.nrows  # 获取行数
    cols = st.ncols  # 获取列数

    sum = 0  # 初始化金额
    moneylist1 = []  # 钱的集合
    numlist1 = []  # 销售量的集合

    for i in range(cols):
        if i == 2:
            moneylist1 = st.col_values(i)[1:]  # 列出除表头的单价的集合
        elif i == 4:
            numlist1 = st.col_values(i)[1:]  # 列出除表头的数量的集合
    for j in range(len(moneylist1)):
            sum = sum + moneylist1[j] * numlist1[j]
    print(mm + 1, "月的销售总金额为：", round(sum, 1))
    totalsale1 += sum
print("第一季度销售总额为：",round(totalsale1,1))
print("第一季度的销售额占比为：",round(totalsale1/totalsale,3)*100,"%")

totalsale2 = 0
for mm in range(3,6):
    month = str(mm+1) + '月'
    st = wd.sheet_by_name(month)
    rows = st.nrows  # 获取行数
    cols = st.ncols  # 获取列数

    sum = 0  # 初始化金额
    moneylist1 = []  # 钱的集合
    numlist1 = []  # 销售量的集合

    for i in range(cols):
        if i == 2:
            moneylist1 = st.col_values(i)[1:]  # 列出除表头的单价的集合
        elif i == 4:
            numlist1 = st.col_values(i)[1:]  # 列出除表头的数量的集合
    for j in range(len(moneylist1)):
            sum = sum + moneylist1[j] * numlist1[j]
    print(mm + 1, "月的销售总金额为：", round(sum, 1))
    totalsale2 += sum
print("第二季度销售总额为：",round(totalsale2,1))
print("第二季度的销售额占比为：",round(totalsale2/totalsale,3)*100,"%")

totalsale3 = 0
for mm in range(6,9):
    month = str(mm+1) + '月'
    st = wd.sheet_by_name(month)
    rows = st.nrows  # 获取行数
    cols = st.ncols  # 获取列数

    sum = 0  # 初始化金额
    moneylist1 = []  # 钱的集合
    numlist1 = []  # 销售量的集合

    for i in range(cols):
        if i == 2:
            moneylist1 = st.col_values(i)[1:]  # 列出除表头的单价的集合
        elif i == 4:
            numlist1 = st.col_values(i)[1:]  # 列出除表头的数量的集合
    for j in range(len(moneylist1)):
            sum = sum + moneylist1[j] * numlist1[j]
    print(mm + 1, "月的销售总金额为：", round(sum, 1))
    totalsale3 += sum
print("第三季度销售总额为：",round(totalsale3,1))
print("第三季度的销售额占比为：",round(totalsale3/totalsale,3)*100,"%")

totalsale4 = 0
for mm in range(9,12):
    month = str(mm+1) + '月'
    st = wd.sheet_by_name(month)
    rows = st.nrows  # 获取行数
    cols = st.ncols  # 获取列数

    sum = 0  # 初始化金额
    moneylist1 = []  # 钱的集合
    numlist1 = []  # 销售量的集合

    for i in range(cols):
        if i == 2:
            moneylist1 = st.col_values(i)[1:]  # 列出除表头的单价的集合
        elif i == 4:
            numlist1 = st.col_values(i)[1:]  # 列出除表头的数量的集合
    for j in range(len(moneylist1)):
            sum = sum + moneylist1[j] * numlist1[j]
    print(mm + 1, "月的销售总金额为：", round(sum, 1))
    totalsale4 += sum
print("第四季度销售总额为：",round(totalsale4,1))
print("第四季度的销售额占比为：",round(totalsale4/totalsale,3)*100,"%")
print("-------------------------------------------")






