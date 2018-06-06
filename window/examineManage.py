# -*- coding: utf-8 -*-
"""
this is the 试题管理 window for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180606
Accomplish : No
Final : No
"""
import datetime
import PyQt5.QtGui as Qtqg
import PyQt5.QtWidgets as Qtqw


class EMwindow(Qtqw.QMainWindow):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
        # 生成 菜单栏
        menubar = self.menuBar()

        # 生成 小组数据 按钮
        groupData = Qtqw.QAction('&小组数据', self)
        groupData.triggered.connect(self.printsss)
        menubar.addAction(groupData)

        # 生成 综合数据 按钮
        multipleData = Qtqw.QAction('&综合数据', self)
        multipleData.triggered.connect(self.printsss)
        menubar.addAction(multipleData)

        # 生成 数据分析 按钮
        analyseData = Qtqw.QAction('&数据分析', self)
        analyseData.triggered.connect(self.printsss)
        menubar.addAction(analyseData)

        self.setWindowTitle("试题管理")
        self.setGeometry(250, 125, 1000, 800)
        self.setWindowIcon(Qtqg.QIcon('../img/ico.png'))
        # self.show()

    def printsss(self):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))