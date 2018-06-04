
class Test:
    def __init__(self):
        self.dict1 = {"aaa": "111", "bbb": "222", "ccc": "333", "ddd": "444"}
        self.dict2: dict

    def fun(self):
        print(self.dict1)
        print(self.dict1["aaa"])
        f = open('./temp.txt','w')
        f.write(str(self.dict1))
        f.close()

    def rd(self):
        f = open('./temp.txt', 'r')
        a = f.read()
        self.dict2 = eval(a)
        f.close()


if __name__ == '__main__':
    t1 = Test()
    t1.fun()
    t1.rd()
    print(t1.dict2)
    print(t1.dict2["bbb"])
