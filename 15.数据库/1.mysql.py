
进入mysql

mysql -uroot -p



远程连接

mysql -hip地址 -uroot -p


创建数据库
create database 数据库名 charset=utf8;
删除数据库
drop database 数据库名;
切换数据库
use 数据库名;
查看当前选择的数据库
select database();


表操作

查看当前数据库中所有表
show tables;
创建表
auto_increment表示自动增长

create table 表名(列及类型);
如：
create table students(
id int auto_increment primary key,
sname varchar(10) not null
);
修改表

alter table 表名 add|change|drop 列名 类型;
如：
alter table students add birthday datetime;
删除表
drop table 表名;
查看表结构
desc 表名;
更改表名称
rename table 原表名 to 新表名;
查看表的创建语句
show create table '表名';


数据操作

查询
select * from 表名
增加
全列插入：insert into 表名 values(...)
缺省插入：insert into 表名(列1,...) values(值1,...)
同时插入多条数据：insert into 表名 values(...),(...)...;
或insert into 表名(列1,...) values(值1,...),(值1,...)...;
主键列是自动增长，但是在全列插入时需要占位，通常使用0，插入成功后以实际数据为准
修改
update 表名 set 列1=值1,... where 条件
删除
delete from 表名 where 条件
逻辑删除，本质就是修改操作update
alter table students add isdelete bit default 0;
如果需要删除则
update students isdelete=1 where ...;
