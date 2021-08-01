# 定义学生类
class Student:
    __username = None
    __age = 0

    # 设置姓名
    def setUsername(self, username):
        self.__username = username

    # 获取姓名
    def getUsername(self):
        return self.__username

    # 设置年龄
    def setAge(self, age):
        if age > 120 or age < 0:
            print("您年龄输入非法！")
        else:
            self.__age = age

    # 获取年龄
    def getAge(self):
        return self.__age

    # 展示
    def showMe(self):
        print("大家好，我叫", self.__username, "，今年", self.__age, "岁了！")

    def compare(self, student):   # self代表我自己    student代表另一个人
        if self.__age > student.getAge():
            print("我比同桌大", (self.__age - student.getAge()), "岁！")
        elif self.__age < student.getAge():
            print("我比同桌小", (student.getAge() - self.__age), "岁！")
        else:
            print("我俩一样大！")

# 具体化学生
s = Student()
s.setUsername("旺财")
s.setAge(55)

s1 = Student()
s1.setUsername("李四")
s1.setAge(56)

s.compare(s1)   # 旺财要和李四比较
s1.compare(s)