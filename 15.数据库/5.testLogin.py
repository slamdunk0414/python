from MysqlHelper import MysqlHelper

name = input('请输入用户名')
pwd = input('请输入密码')

sql = 'select pwd from users where name = %s'

helper = MysqlHelper('localhost',3306,'python3','root','pengpeng')

result = helper.fetchall(sql,[name])

if len(result) == 0:
    print('用户名错误')
else:
    currentPwd = result[0][0]
    if currentPwd == pwd:
        print('密码正确')
    else:
        print('密码错误')