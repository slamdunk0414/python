# 1.打印提示

print('*'*50)
print('名片管理系统')
print('1.添加信息')
print('2.删除信息')
print('3.修改信息')
print('4.查询信息')
print('5.退出系统')
print('*'*50)

# 2.接受用户输入

names = []

while True:
    print('')
    flag = int(input('请输入指令'))
    if flag == 1:
        print('输入的是添加信息')

        info = {}
        name = input('请输入一个名字')

        info['name'] = name;

        qq = input('请输入qq号')

        info['qq'] = qq

        names.append(info)

    elif flag == 2:

        name = input('请输入要删除的名字')

        find_flag = False

        for dic in names:
            if dic['name'] == name:
                find_flag = True
                names.remove(dic)
                print('找到了信息 并且已经删除')

        if find_flag != True:
            print('找不到输入的信息')

        print('输入的名字是%s 删除之后列表为%s' % (name, names))

    elif flag == 3:

        name = input('请输入需要修改的名字')

        if name in names:
            index = names.index(name)
            names[index] = 'xxx'
        print(names)

    elif flag == 4:
        name = input('请输入要查询的名字')
        if name in names:
            print('有这个名字')
        else:
            print('没有这个名字')
    elif flag == 5:
        print('输入的是5 退出系统')
        break
    else:
        print('输入有误')
print('退出系统')

