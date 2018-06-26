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
import os
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtCore as Qtqc
import PyQt5.QtGui as Qtqg
# 以下为自建库
import lib.releaseZip as rls
import lib.processData as prcd


class IptDTwidget(Qtqw.QWidget):
    def __init__(self, fwindow: Qtqw.QMainWindow):
        super().__init__()
        self.fwindow = fwindow
        # 定义按钮层控件
        self.HboxButton = Qtqw.QHBoxLayout()
        self.btnYes = Qtqw.QPushButton("确定", self)
        self.btnCancel = Qtqw.QPushButton("取消", self)

        # 定义数据文件选择层控件
        self.HboxDataChoice = Qtqw.QHBoxLayout()
        self.LabelData = Qtqw.QLabel("数据文件：")
        self.LineEditData = Qtqw.QLineEdit()
        self.LineEditData.setPlaceholderText("选择数据文件...")
        self.btnDataChose = Qtqw.QPushButton("选择文件", self)

        # 定义订单文件选择层控件
        self.HboxOrderChoice = Qtqw.QHBoxLayout()
        self.LabelOrder = Qtqw.QLabel("订单文件：")
        self.LineEditOrder = Qtqw.QLineEdit()
        self.LineEditOrder.setPlaceholderText("选择订单文件...")
        self.btnOrderChose = Qtqw.QPushButton("选择文件", self)

        # 定义日期层控件
        # self.HboxDate = Qtqw.QHBoxLayout()
        # self.LabelDate = Qtqw.QLabel("比赛日期：")
        # self.LineEditDate = Qtqw.QDateEdit(Qtqc.QDate.currentDate())
        # self.LabelDateNull = Qtqw.QLabel()

        # 定义比赛名称层控件
        # self.HboxGameName = Qtqw.QHBoxLayout()
        # self.LabelGameName = Qtqw.QLabel("比赛名称：")
        # self.LineEditGameName = Qtqw.QLineEdit()
        # self.LineEditGameName.setPlaceholderText("输入比赛名称...")
        # self.LabelGameNameNull = Qtqw.QLabel()

        # 定义试题层控件
        # self.HboxExamine = Qtqw.QHBoxLayout()
        # self.LabelExamine = Qtqw.QLabel("试题：")
        # self.ComBoxExamine = Qtqw.QComboBox()
        # self.LabelExamineNull = Qtqw.QLabel()
        # 定义纵向布局
        self.Vbox = Qtqw.QVBoxLayout()
        # 初始化
        self.initUI()

    def initUI(self):
        self.initBtnLay()
        self.initDataLay()
        self.initOrderLay()
        # self.initDateLay()
        # self.initGameNameLay()
        # self.initExamine()

        # 设置纵向 各Hbox的布局
        self.Vbox.addStretch(2)
        # self.Vbox.addLayout(self.HboxExamine)
        # self.Vbox.addStretch(1)
        # self.Vbox.addLayout(self.HboxGameName)
        # self.Vbox.addStretch(1)
        # self.Vbox.addLayout(self.HboxDate)
        # self.Vbox.addStretch(1)
        self.Vbox.addLayout(self.HboxDataChoice)
        self.Vbox.addStretch(1)
        self.Vbox.addLayout(self.HboxOrderChoice)
        self.Vbox.addStretch(1)
        self.Vbox.addLayout(self.HboxButton)
        self.Vbox.addStretch(2)

        self.setLayout(self.Vbox)

    # def initExamine(self):
    #     # 初始化试题层
    #     self.LabelExamine.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
    #     self.ComBoxExamine.addItem("aaaa")  # 此处去读比赛类型 目录得到循环解析到Item
    #     self.HboxExamine.addWidget(self.LabelExamine)
    #     self.HboxExamine.addWidget(self.ComBoxExamine)
    #     self.HboxExamine.addWidget(self.LabelExamineNull)
    #     self.HboxExamine.setStretchFactor(self.LabelExamine, 4)
    #     self.HboxExamine.setStretchFactor(self.ComBoxExamine, 6)
    #     self.HboxExamine.setStretchFactor(self.LabelExamineNull, 3)

    # def initGameNameLay(self):
    #     # 初始化比赛名称层
    #     self.LabelGameName.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
    #     self.HboxGameName.addWidget(self.LabelGameName)
    #     self.HboxGameName.addWidget(self.LineEditGameName)
    #     self.HboxGameName.addWidget(self.LabelGameNameNull)
    #     self.HboxGameName.setStretchFactor(self.LabelGameName, 4)
    #     self.HboxGameName.setStretchFactor(self.LineEditGameName, 6)
    #     self.HboxGameName.setStretchFactor(self.LabelGameNameNull, 3)

    # def initDateLay(self):
    #     # 初始化日期选择层
    #     # https://blog.csdn.net/liang19890820/article/details/52387275  QDateEdit 控件的使用说明
    #     self.LabelDate.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
    #     self.LineEditDate.setDisplayFormat("yyyy-MM-dd")
    #     self.LineEditDate.setCalendarPopup(True)  # 调出下拉箭头，单击弹出日期控件
    #     self.HboxDate.addWidget(self.LabelDate)
    #     self.HboxDate.addWidget(self.LineEditDate)
    #     self.HboxDate.addWidget(self.LabelDateNull)
    #     self.HboxDate.setStretchFactor(self.LabelDate, 4)
    #     self.HboxDate.setStretchFactor(self.LineEditDate, 6)
    #     self.HboxDate.setStretchFactor(self.LabelDateNull, 3)

    def initDataLay(self):
        # 初始化文件选择层 并设置布局
        self.LabelData.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        self.LabelData.setContentsMargins(0, 0, 0, 3)  # 设置文本的下边距为3个像素
        self.HboxDataChoice.addWidget(self.LabelData)
        self.HboxDataChoice.addWidget(self.LineEditData)
        self.HboxDataChoice.addWidget(self.btnDataChose)
        self.HboxDataChoice.setStretchFactor(self.LabelData, 4)
        self.HboxDataChoice.setStretchFactor(self.LineEditData, 6)
        self.HboxDataChoice.setStretchFactor(self.btnDataChose, 3)
        # 设置选择文件 按钮功能
        self.btnDataChose.clicked.connect(self.choseData)

    def initOrderLay(self):
        # 初始化文件选择层 并设置布局
        self.LabelOrder.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        self.LabelOrder.setContentsMargins(0, 0, 0, 3)  # 设置文本的下边距为3个像素
        self.HboxOrderChoice.addWidget(self.LabelOrder)
        self.HboxOrderChoice.addWidget(self.LineEditOrder)
        self.HboxOrderChoice.addWidget(self.btnOrderChose)
        self.HboxOrderChoice.setStretchFactor(self.LabelOrder, 4)
        self.HboxOrderChoice.setStretchFactor(self.LineEditOrder, 6)
        self.HboxOrderChoice.setStretchFactor(self.btnOrderChose, 3)
        # 设置选择文件 按钮功能
        self.btnOrderChose.clicked.connect(self.choseOrder)

    def initBtnLay(self):
        # 初始化按钮层 并设置布局
        self.HboxButton.addStretch(1)
        self.HboxButton.addWidget(self.btnYes)
        self.HboxButton.addStretch(1)
        self.HboxButton.addWidget(self.btnCancel)
        self.HboxButton.addStretch(1)
        # 设置按钮功能
        self.btnCancel.clicked.connect(self.quit)
        self.btnYes.clicked.connect(self.importAndRelease)

    def quit(self):  # 为取消按钮设计 直接关闭 widget外层的qmainwindow
        self.fwindow.close()
        # print(self.fwindow)
        # pass

    def choseData(self):
        fname = Qtqw.QFileDialog.getOpenFileName()
        # print(fname[0])
        self.LineEditData.setText(fname[0])

    def choseOrder(self):
        fname = Qtqw.QFileDialog.getOpenFileName()
        # print(fname[0])
        self.LineEditOrder.setText(fname[0])

    def importAndRelease(self):
        # print("import function")
        # 判断 内容LineEdit是否为空
        nullWarning = Qtqw.QMessageBox()
        nullWarning.setText("不能提交空！")
        nullWarning.setWindowTitle("提示")
        nullWarning.setWindowIcon(Qtqg.QIcon('../img/error.png'))
        nullWarning.setContentsMargins(10, 10, 25, 10)

        incorrectWarning = Qtqw.QMessageBox()
        incorrectWarning.setText("文件不存在！")
        incorrectWarning.setWindowTitle("提示")
        incorrectWarning.setWindowIcon(Qtqg.QIcon('../img/error.png'))
        incorrectWarning.setContentsMargins(10, 10, 25, 10)
        if self.LineEditData.text() and self.LineEditOrder.text():
            if os.path.exists(self.LineEditData.text()) and os.path.exists(self.LineEditOrder.text()):
                print(self.LineEditData.text())
                releaser = rls.ReleaseZip(self.LineEditData.text())
                releaser.release()
                procDate = prcd.SplitData()
                print(self.LineEditOrder.text())

            else:
                # print("文件目录错误")
                incorrectWarning.exec()
        else:
            nullWarning.exec()
            # print("空文件路径")