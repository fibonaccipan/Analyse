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
    def __init__(self,importPath,gameDegree):
        # self.init_ui()
        self.importPath = importPath
        self.fPath = os.path.abspath('..').replace('\\','/')
        self.tmpPath = self.fPath + "/" + "tmp"
        self.gameDegree = self.fPath + "/" + gameDegree

    def showAll(self):
        print(self.importPath)
        print(self.fPath)
        print(self.tmpPath)
        print(self.gameDegree)

    def release(self):
        if os.path.exists(self.tmpPath):
            shutil.rmtree(self.tmpPath)
        zpf = zf.ZipFile(self.importPath)
        zpf.extractall(self.tmpPath)
        return self.importPath[self.importPath.rfind("/"):self.importPath.rfind(".")]  # 返回比赛场次（文件名）
