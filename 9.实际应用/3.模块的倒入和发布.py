
#在包的同级结构下 创建一个setup.py文件

#在文件中

from distutils.core import setup

setup(name='zhp\'sxxx',version='1.0',description='xxx',author='zhp',py_modules=['xx.xx','xx.xx'])

#py_modules用于指定py文件

#制作后 需要执行

#python3 setup.py build

#执行 python3 setup.py sdist 可以打包

#执行 python3 setup.py install 安装