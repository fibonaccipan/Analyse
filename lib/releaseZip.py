# -*- coding: utf-8 -*-
"""
this is a release zip module , release zip file to temporary directory ,
for  Yanteng's game analysis program,
Author : fibonacci
Connect : ericpan1124@yahoo.com
Edit date :20180524
Accomplish : Yes
Final : No
"""
import zipfile as zf
import os
import shutil


class ReleaseZip:
    def __init__(self, importPath):
        # self.fPath = os.path.abspath('..').replace('\\', '/')
        self.importPath = importPath
        self.gameRound = self.importPath[self.importPath.rfind("/")+1:self.importPath.rfind(".")]
        self.tmpPath = "../tmp/" + self.gameRound

    def release(self):
        if os.path.exists(self.tmpPath):  # 判断解压目标位置是否存在 不存在则创建
            shutil.rmtree(self.tmpPath)
        zpf = zf.ZipFile(self.importPath)  # 解压zip
        zpf.extractall(self.tmpPath)
        f = open("../rate/step.txt", "w")  # 写入完成率
        f.write("100")
        f.close()
        # 返回比赛场次（文件名）
        return self.gameRound

    def showAll(self):
        print(self.importPath)
        # print(self.fPath)
        print(self.tmpPath)