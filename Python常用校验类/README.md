
# Python常用校验类

### 简介
在项目开发中，常常需要校验客户端提交参数和入参参数的合法性,PyVaildTool是一个Python工具类，它帮助我们简化每一行代码，减少每一个方法。

### 1、校验手机号

```
# 校验手机号
    @staticmethod
    def vaildPhoneNum(phoneNum):
        phone_pattern = re.compile(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
        if phone_pattern.match(phoneNum):
            return True
        else:
            return False
```
### 2、校验邮箱
```
# 校验邮箱有效性
    @staticmethod
    def vaildEmail(email):
        email_pattern = re.compile(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$')
        if email_pattern.match(email):
            return True
        else:
            return False
```

### 3、 校验身份证号：
```
# 校验身份证
    @staticmethod
    def vaildIDCard(idCard):
        idCard_pattern = re.compile(r'^\d{15}|\d{18}$')
        if idCard_pattern.match(idCard):
            return True
        else:
            return False
```

### 4、校验密码 6-16位字母、数字）
```
# 校验密码 6-16位字母、数字）
    @staticmethod
    def vaildPwd(password):
        pwd_pattern = re.compile(r'^[0-9A-Za-z]{6,16}$')
        if pwd_pattern.match(password):
            return True
        else:
            return False
```
