
import pymysql

try:

    name = input('请输入一个用户名：')

    conn = pymysql.connect(host='localhost',port = 3306,user = 'root',passwd='pengpeng',db='python3',charset='utf8')

    cursor1 = conn.cursor()

    # sql = 'insert into students(name) values("zdp") ;'

    sql1 = 'insert into students(name) values(%s)'

    # cursor1.execute(sql)

    cursor1.execute(sql1,[name])
    conn.commit()

    cursor1.close()
    conn.close()

except Exception as e:
    print(e)