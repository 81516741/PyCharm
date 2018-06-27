name = input("请输入名字\n")
print(name)
#if 条件
a = 1
if a < 2:
    print("nimei")
else:
    print("dd")

#关键字
import keyword
print(keyword.kwlist)

#运算
print("#"*100)

#输出
print("%s,%d"%(name,a))

print('<' + name * 5 + '>')

class nimei:
    __nimei3 = 3
    def __init__(self):
        print(self.__nimei3)

    def __del__(self):
        print("我销毁了")


a = nimei()

import glob
print(glob.glob("*.py"))

print(type(a))

student = {"nihao","xiaoming"}
ok = "xiaoming" in student
if ok :
    print("好样的")
else:
    print("不好的")

a1 = set("anidsleof")
a2 = set("ndhefhgrf")
a3 = a1 ^ a2
print(a3)

a4=1
a5 = 2
print(a4 << 2)

for i in reversed(range(1,10,2)) :
    print(i)

import sys

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('/n/nThe PYTHONPATH is', sys.path, '/n')
def he():
    print("hehe")

if __name__ == '__main__':
 print('程序自身在运行')
else:
 print('我来自另一模块')