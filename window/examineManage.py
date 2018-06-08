# -*- coding: utf-8 -*-
"""
this is the 试题管理 window for  Yanteng's game analysis program, 模态弹出框
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180606
Accomplish : No
Final : No
"""
import datetime
import PyQt5.QtGui as Qtqg
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtCore as Qtqc
# 以下为自建库
import window.centralWidget as CTwdgt

class EMwindow(Qtqw.QMainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowModality(Qtqc.Qt.ApplicationModal)  # 设置QMainWindow 弹出为模态
        self.setAttribute(Qtqc.Qt.WA_DeleteOnClose)  # 功能待查
        self.initUI()

    def initUI(self):
        self.setWindowTitle("试题管理")
        self.setGeometry(300, 150, 800, 600)
        self.setWindowIcon(Qtqg.QIcon('../img/examine.png'))
        centralWidget = CTwdgt.CentralWidget()
        self.setCentralWidget(centralWidget)
        # self.show()

    def printsss(self):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
