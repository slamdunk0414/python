from multiprocessing import Pool,Manager
import os
import time

def copyToFile(name,old_file,new_file,queue):

    fr = open(old_file + "/" + name)
    fw = open(new_file + "/" + name, 'w')

    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    queue.put(name)

def main():

    oldName = input('请输入要拷贝的文件夹')

    newName = oldName + '-copy'

    os.mkdir(newName)

    fileNames = os.listdir(oldName)

    queue = Manager().Queue()

    p = Pool(5)
    for name in fileNames:
        p.apply_async(copyToFile, args = (name, oldName, newName,queue))

    num = 0
    allnum = len(fileNames)

    while True:
        queue.get()
        num += 1
        ratate = num / allnum
        print('\r ratete is %f %%' % (ratate * 100), end='')
        print('\r num is %d total is %d'%(num,allnum))
        if num == allnum:
            break

    print('copy finish')


if __name__ == '__main__':
    main()


