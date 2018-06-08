# -*- coding: utf-8 -*-
"""
this is the 导入数据 window for  Yanteng's game analysis program, 模态弹出框
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180608
Accomplish : No
Final : No
"""
import datetime
import PyQt5.QtGui as Qtqg
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtCore as Qtqc
# 以下为自建库
import window.IptDTwidget as IptDTwdgt


class IptDTwindow(Qtqw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qtqc.Qt.ApplicationModal)  # 设置QMainWindow 弹出为模态
        self.setAttribute(Qtqc.Qt.WA_DeleteOnClose)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("导入数据")
        self.setGeometry(400, 230, 400, 300)
        self.setWindowIcon(Qtqg.QIcon('../img/import.png'))
        centralWidget = IptDTwdgt.IptDTwidget(self)
        # 将本QMainWindow 作为参数传入自己包含的widget，为widget内按钮关闭外QMainWindow 提供操作对象
        self.setCentralWidget(centralWidget)
