
1.查询

    select * from table
    #结果举例
    mysql> select * from student
        -> ;
    +-----+------+----------------------------+
    | sId | name | birthday                   |
    +-----+------+----------------------------+
    |   1 | zp   | 1990-11-01 00:00:00.000000 |
    |   2 | wy   | 1989-11-06 00:00:00.000000 |
    |   3 | wdy  | NULL                       |
    |   4 | wdy  | NULL                       |
    +-----+------+------------------

    查询去重

    select distinct id from table

    #结果举例
    mysql> select distinct name from student;
    +------+
    | name |
    +------+
    | zp   |
    | wy   |
    | wdy  |
    +------+
    3 rows in set (0.00 sec)


2.where
    select * from table where id > 1;

3.逻辑运算符 and or not

4.like _一个 %多个
    select * from student where name like 'x__'

5.in in(a,b,c) 查询等于a或者b或者c
    select * from student where id in(1,2,3)

6.between 在x与y之间

7.聚合
    count 统计有多少行
    max() 表示求此列最大值
    min() 求最小值
    sum() 求和
    avg() 平均值

8.分组
    group by

    select gender,count(*) from student group by gender;

9.having

    select gender,count(*) from student group by gender having gender = 0;

10.排序

    select * from table

    order by 列1 asc,desc 列2 asc,desc

11.分页
    limit

    select * from table
    limit start,count   从start开始 获取count条数据
