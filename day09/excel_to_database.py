import xlrd
from DBUtils import insert


# 打开工作簿
wd = xlrd.open_workbook("12月份衣服销售数据.xlsx", encoding_override=True)
# 获取选项卡
st = wd.sheet_by_name("12月份各种服饰销售情况")
# 获取所有行和列
rows = st.nrows
cols = st.ncols

date_index = 0  # 日期列角标
name_index = 1  # 服装名称列角标
price_index = 2  # 价格列角标
count_index = 3  # 库存量列角标
sales_index = 4  # 销售量列角标

for i in range(1, rows):
    date = st.cell_value(i, date_index)  # 获取日期
    name = st.cell_value(i, name_index)  # 获取服装的名称
    price = st.cell_value(i, price_index)  # 获取价格
    count = st.cell_value(i, count_index)  # 获取库存量
    sales = st.cell_value(i, sales_index)  # 获取销售量
    sql = "insert into clothes values(%s,%s,%s,%s,%s)"
    param = [date, name, price, count, sales]

    insert(sql, param)






