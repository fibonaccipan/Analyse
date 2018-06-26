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
    def __init__(self, inPath):
        # self.fPath = os.path.abspath('..').replace('\\', '/')
        self.inPath = inPath
        # self.OutPath = outPath
        # self.gameRound = self.importPath[self.importPath.rfind("/")+1:self.importPath.rfind(".")]
        self.tmpPath = "../tmp/"

    def release(self):
        if os.path.exists(self.tmpPath):  # 判断解压目标位置是否存在 存在则删除
            shutil.rmtree(self.tmpPath)
        zpf = zf.ZipFile(self.inPath)  # 解压zip
        zpf.extractall(self.tmpPath)
        # f = open("../rate/step.txt", "w")  # 写入完成率
        # f.write("100")
        # f.close()
        # 返回比赛场次（文件名）
        # return self.gameRound

    def showAll(self):
        print(self.inPath)
        # print(self.fPath)
        print(self.tmpPath)
