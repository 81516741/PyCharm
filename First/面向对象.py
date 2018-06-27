class People:
    def __init__(self,name):
        self.name = name

    def overMethod(self):
        print("我是父类方法{}".format(self.name))

class Student(People):
    item = {}
    def overMethod(self):
        super(Student,self).overMethod()
        print("我是子类方法{}".format(self.name))

    def __setitem__(self, key, value):
        self.item[key] = value
        print("call setitem")

    def __getitem__(self, key):
        print("call getitem")
        return self.item.get(key)

s = Student("小明")
s.overMethod()
s[0] = 3
print(s[0])

def testfun():
    print("nimed")
