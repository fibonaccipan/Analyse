# -*- coding: utf-8 -*-
"""
this is the import data widget ,which is a part of importData pop QMainWindow
be used to contain different kind widget and split window layout
for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180608
Accomplish : No
Final : No
"""
import sys
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtCore as Qtqc


class IptDTwidget(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        Vbox = Qtqw.QVBoxLayout() # 定义纵向布局

        # 定义按钮层的横向布局 及该层控件
        HboxButton = Qtqw.QHBoxLayout()
        btnYes = Qtqw.QPushButton("确定",self)
        btnCancel = Qtqw.QPushButton("取消",self)
        # 设置按钮层左右布局
        HboxButton.addStretch(1)
        HboxButton.addWidget(btnYes)
        HboxButton.addStretch(1)
        HboxButton.addWidget(btnCancel)
        HboxButton.addStretch(1)

        # 定义文件选择层横向布局 及该层控件
        HboxFileChoice = Qtqw.QHBoxLayout()
        LabelFile = Qtqw.QLabel("比赛数据：")
        LabelFile.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        LabelFile.setContentsMargins(0, 0, 0, 3)  # 设置文本的下边距为3个像素
        LineEditFile = Qtqw.QLineEdit()
        LineEditFile.setContentsMargins(0, 0, 0, 0)  # 设置边距为 0个像素
        btnFileChose = Qtqw.QPushButton("选择文件", self)
        # 设置文件选择层左右布局
        # HboxFileChoice.addStretch(1)
        HboxFileChoice.addWidget(LabelFile)
        HboxFileChoice.addWidget(LineEditFile)
        # HboxFileChoice.addStretch(1)
        HboxFileChoice.addWidget(btnFileChose)
        # HboxFileChoice.addStretch(1)
        HboxFileChoice.setStretchFactor(LabelFile, 4)
        HboxFileChoice.setStretchFactor(LineEditFile, 6)
        HboxFileChoice.setStretchFactor(btnFileChose, 3)

        # 定义日期层控件横向布局 及该层控件
        HboxDate = Qtqw.QHBoxLayout()
        LabelDate = Qtqw.QLabel("比赛日期：")
        LabelDate.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        LabelDate.setContentsMargins(0, 0, 0, 0)  # 设置边距为0个像素
        LineEditDate = Qtqw.QDateEdit(Qtqc.QDate.currentDate())
        # https://blog.csdn.net/liang19890820/article/details/52387275 QDateEdit控件的使用说明
        LineEditDate.setDisplayFormat("yyyy-MM-dd")
        LineEditDate.setCalendarPopup(True)  # 调出下拉箭头，单击弹出日期控件
        LabelDateNull = Qtqw.QLabel()
        HboxDate.addWidget(LabelDate)
        HboxDate.addWidget(LineEditDate)
        HboxDate.addWidget(LabelDateNull)
        HboxDate.setStretchFactor(LabelDate, 4)
        HboxDate.setStretchFactor(LineEditDate, 6)
        HboxDate.setStretchFactor(LabelDateNull, 3)

        # 定义比赛名称层级 控件横向布局 及该层控件
        HboxGameName = Qtqw.QHBoxLayout()
        LabelGameName = Qtqw.QLabel("比赛名称：")
        LabelGameName.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        LabelGameName.setContentsMargins(0, 0, 0, 0)  # 设置下边距为0个像素
        LineEditGameName = Qtqw.QLineEdit()
        LabelGameNameNull = Qtqw.QLabel()
        HboxGameName.addWidget(LabelGameName)
        HboxGameName.addWidget(LineEditGameName)
        HboxGameName.addWidget(LabelGameNameNull)
        HboxGameName.setStretchFactor(LabelGameName, 4)
        HboxGameName.setStretchFactor(LineEditGameName, 6)
        HboxGameName.setStretchFactor(LabelGameNameNull, 3)

        # 定义试题层级 控件横向布局 及该层控件
        HboxExamine = Qtqw.QHBoxLayout()
        LabelExamine = Qtqw.QLabel("试题：")
        LabelExamine.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        ComBoxExamine = Qtqw.QComboBox()
        LabelExamineNull = Qtqw.QLabel()
        HboxExamine.addWidget(LabelExamine)
        HboxExamine.addWidget(ComBoxExamine)
        HboxExamine.addWidget(LabelExamineNull)
        HboxExamine.setStretchFactor(LabelExamine, 4)
        HboxExamine.setStretchFactor(ComBoxExamine, 6)
        HboxExamine.setStretchFactor(LabelExamineNull, 3)


        # 设置纵向 各Hbox的布局
        Vbox.addStretch(2)
        Vbox.addLayout(HboxExamine)
        Vbox.addStretch(1)
        Vbox.addLayout(HboxGameName)
        Vbox.addStretch(1)
        Vbox.addLayout(HboxDate)
        Vbox.addStretch(1)
        Vbox.addLayout(HboxFileChoice)
        Vbox.addStretch(1)
        Vbox.addLayout(HboxButton)
        Vbox.addStretch(1)
        self.setLayout(Vbox)
        print("aaaa")
