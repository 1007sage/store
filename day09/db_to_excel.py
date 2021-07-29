import xlwt
from DBUtils import select

# 创建空白工作薄
wb = xlwt.Workbook()

# 创建选项卡
st = wb.add_sheet("12月服装销售情况", cell_overwrite_ok=True)

# 设计表头
colname = ['日期', '服装名称', '价格/件', '库存数量', '销售量/每日']
for i in range(0, len(colname)):
    st.write(0, i, colname[i])   # 行、列、内容

# 查找全部衣服的sql语句
sql = "SELECT * FROM clothes"
# 调用select方法
sale = select(sql, [], 'all', [])
# 将数据库中获取的数据保存到excel表中
n = 1    # 从第一行开始写入
# for循环将每一行的数据插入到excel表中
for j in sale:
    st.write(n, 0, j[0])
    st.write(n, 1, j[1])
    st.write(n, 2, j[2])
    st.write(n, 3, j[3])
    st.write(n, 4, j[4])
    n += 1

# 保存文件
wb.save("12月sale.xls")

