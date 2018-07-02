# -*- coding: utf-8 -*-
import os

class SaveRule:
    def __init__(self, path):
        # 设置文件指指针
        self.fp = None
        if os.path.exists(path):
            self.fp = open(path, 'w')

    def saveDict(self, dictVar: dict):
        # 存入 文件
        self.fp.write(str(dictVar))
        self.fp.close()


class ReadRule:
    def __init__(self, path):
        # 打开 path目录的文件 得到文件指针
        self.fp = None
        self.dict = {}
        if os.path.exists(path):
            self.fp = open(path, 'r')

    def __del__(self):  # 析构函数 关闭文件指针
        try:
            self.fp.close()
        except:
            pass

    def getDict(self):
        try:
            self.dict = eval(self.fp.read())
        except:
            print("analyze rule error")
        return self.dict


