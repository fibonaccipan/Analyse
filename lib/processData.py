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
import time
import shutil
import pandas as pd
import multiprocessing as mtprc
import threading as td
import lib.rateBar as rtb
import lib.processDataFunc as PDF


class SplitData:
    def __init__(self,  gameRound, orderInPath):
        # self.fPath = os.path.abspath('..').replace('\\', '/')
        self.fromPath = "../tmp/"
        self.gameRound = gameRound
        self.outPath = "../data/" + self.gameRound
        self.orderInPath = orderInPath
        self.orderOutPath = "../data/" + self.gameRound + "/order.xlsx"

    def splitDate(self):
        if os.path.exists(self.outPath):
            shutil.rmtree(self.outPath)
        filelist = os.listdir(self.fromPath)
        # time.sleep(10)
        for teamdata in filelist:
            teamoutpath = self.outPath+"/"+teamdata[:teamdata.find(".")]
            teamfrompath = self.fromPath + "/" + teamdata
            os.makedirs(teamoutpath)
            sheetlist = pd.ExcelFile(teamfrompath).sheet_names  # 需要抛异常
            for sheet in sheetlist:
                datatype = teamdata.find("年")
                if datatype > -1:
                    if sheet.rfind("年初广告投放") > -1:
                        cleanr = PDF.clear_data(teamfrompath, sheet, teamoutpath)
                        cleanr.clear_year_ad_data()
                    if sheet.rfind("综合费用") > -1 or sheet.rfind("利润") > -1 or sheet.rfind("资产负债表") > -1:
                        cleanr = PDF.clear_data(teamfrompath, sheet, teamoutpath)
                        cleanr.clear_year_normal_data()
                else:
                    if sheet.rfind("订单信息") > -1 or sheet.rfind("现金流量表") > -1:
                        cleanr = PDF.clear_data(teamfrompath, sheet, teamoutpath)
                        cleanr.clear_team_normal()
            f = open("../rate/step.txt", "w")
            f.write(str(int((filelist.index(teamdata)+1)*100/len(filelist))))
            f.close()
            time.sleep(0.2)

    def processOrder(self):
        # print(self.orderOutPath)
        cleanr = PDF.clear_data(self.orderInPath, "Sheet1", self.orderOutPath)
        cleanr.clear_order()


    def showAll(self):
        # print(self.fPath)
        print(self.fromPath)
        print(self.gameRound)
        print(self.outPath)
