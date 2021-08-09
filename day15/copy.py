# 使用python复制一张图片到D盘的python文件夹里。
f = open(file="大美女.jpg", mode="rb")
f1 = open(file="D:\汉科软\python\大美女.jpg", mode="wb")
data = f.read()
f1.write(data)

f1.flush()
f1.close()
f.close()

# 编写程序模拟证件上传的功能，让用户输入证件的路径，并拷贝到一个统一的图片路径下。
def copy_file(origin_path, target_path):
    p1 = open(origin_path, mode="rb")
    p2 = open(target_path, mode="wb")
    data = p1.read()
    p2.write(data)
    p2.flush()
    p1.close()
    p2.close()

copy_file(r"D:\pythonworkspace\project\day15\大美女.jpg", r"D:\汉科软\python\大美女.jpg")