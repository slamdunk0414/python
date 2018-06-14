create table scores(

id int primary key auto_increment,
stuid int,
subid int,
score decimal(5,2)

foreign key (stuid) references students(id),
foreign key (subid) references subjects(id)

)


'''查询'''
select students.name,subjects.name,scores.score
inner scores
inner join students on scores.stuid = students.id
inner join subjects on scores.subid = students.id