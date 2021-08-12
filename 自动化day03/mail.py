import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr

# def send_email():
sender = '1546129901@qq.com'  # 发件人邮箱账号
my_pass = 'qianpoheeyxwfech'  # 发件人邮箱授权码
user = '2956761599@qq.com'  # 收件人邮箱账号

msg = MIMEMultipart()  # 创建一个邮件
msg['From'] = formataddr(["王明慧", sender])  # 括号里对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["", user])  # 括号里对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "HKR同学注册测试用例执行结果"  # 邮件的主题，也可以说是标题

server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，SMTP端口是25
server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

# 发送附件
att = MIMEText(open('同学注册测试报告.html', 'rb').read(), 'base64', 'utf-8')  # 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment; filename=file.html"  # filename为文件名字
msg.attach(att)

# 以附件形式发送图片
Image = MIMEImage(open('失败.jpg', 'rb').read())  # 图片的路径
Image.add_header('Content-ID', '失败.jpg')  # 定义图片 ID，在 HTML 文本中引用
msg.attach(Image)

try:
    server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败")