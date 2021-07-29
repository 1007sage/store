import pymysql

host = "localhost"
user = "root"
password = ""
database = "shopping"

# 增
def insert(sql, param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, param)
    con.commit()
    cur.close()
    con.close()

# 删
def delete(sql, param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, param)
    con.commit()
    cur.close()
    con.close()

# 改
def upparam(sql, param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, param)
    con.commit()
    cur.close()
    con.close()

# 查
def select(sql, param, model, size):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cur = con.cursor()
    cur.execute(sql, param)
    if model == "all":
        return cur.fetchall()
    elif model == "one":
        return cur.fetchone()
    elif model == "many":
        return cur.fetchmany(size)
    con.commit()
    cur.close()
    con.close()