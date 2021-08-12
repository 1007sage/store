class StudentsRegister:

    # 成功注册的数据
    register_success_data = [
        {"loginname":"sage", "username":"wang", "password":"123", "confirmPassword":"123", "age":20, "sex":"女",
         "classname":"Python自动化", "email":"1546129901@qq.com", "phoneNumber":"13685655541", "address":"北京市",
         "expect":"成功"}
    ]

    # 重复使用登录名的数据
    register_fail_data = [
        {"loginname":"admin", "username":"admin", "password":"123", "confirmPassword":"123", "age":30, "sex":"男",
         "classname":"测试开发", "email":"154@qq.com", "phoneNumber":"13685555531", "address":"北京市","expect":"成功"}
    ]
