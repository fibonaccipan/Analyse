# -*- coding: utf-8 -*-
"""
this is the data process module ,
process excel data from temporary directory  to game directory ,
for  Yanteng's game analysis program.
Author : fibonacci
Connect : ericpan1124@yahoo.com
Edit date :20180524
Accomplish : Yes
Final : No
"""
import os
import shutil
import pandas as pd
import lib.processDataFunc as PDF

class SplitData:
    def __init__(self, gameDegree, gameRound):
        self.fPath = os.path.abspath('..').replace('\\', '/')
        self.fromPath = self.fPath + "/" + "tmp"
        self.gameRound = gameRound
        self.gameDegree = gameDegree
        self.outPath = self.fPath + "/" + self.gameDegree + "/" +self.gameRound

    def splitDate(self):
        if os.path.exists(self.outPath):
            shutil.rmtree(self.outPath)
        filelist = os.listdir(self.fromPath)
        for teamdata in filelist:
            teamoutpath = self.outPath+"/"+teamdata[:teamdata.find(".")]
            teamfrompath = self.fromPath + "/" + teamdata
            os.makedirs(teamoutpath)
            sheetlist = pd.ExcelFile(teamfrompath).sheet_names
            for sheet in sheetlist:
                datatype = teamdata.find("年")
                if datatype > -1:
                    if sheet.rfind("年初广告投放") > -1:
                        PDF.clear_year_ad_data(teamdata, sheet, teamoutpath)
                    if sheet.rfind("综合费用") > -1 or sheet.rfind("利润") > -1 or sheet.rfind("资产负债表") > -1:
                        pass
                else:
                    if sheet.rfind("订单信息") > -1 or sheet.rfind("现金流量表") > -1:
                        pass

    def showAll(self):
        print(self.fPath)
        print(self.fromPath)
        print(self.gameRound)
        print(self.gameDegree)
        print(self.outPath)
