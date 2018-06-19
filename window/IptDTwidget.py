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


class IptDTwidget(Qtqw.QWidget):
    def __init__(self, fwindow: Qtqw.QMainWindow):
        super().__init__()
        self.fwindow = fwindow
        # 定义按钮层控件
        self.HboxButton = Qtqw.QHBoxLayout()
        self.btnYes = Qtqw.QPushButton("确定", self)
        self.btnCancel = Qtqw.QPushButton("取消", self)
        # 定义文件选择层控件
        self.HboxFileChoice = Qtqw.QHBoxLayout()
        self.LabelFile = Qtqw.QLabel("比赛数据：")
        self.LineEditFile = Qtqw.QLineEdit()
        self.LineEditFile.setPlaceholderText("选择比赛文件...")
        self.btnFileChose = Qtqw.QPushButton("选择文件", self)
        # 定义日期层控件
        self.HboxDate = Qtqw.QHBoxLayout()
        self.LabelDate = Qtqw.QLabel("比赛日期：")
        self.LineEditDate = Qtqw.QDateEdit(Qtqc.QDate.currentDate())
        self.LabelDateNull = Qtqw.QLabel()
        # 定义比赛名称层控件
        self.HboxGameName = Qtqw.QHBoxLayout()
        self.LabelGameName = Qtqw.QLabel("比赛名称：")
        self.LineEditGameName = Qtqw.QLineEdit()
        self.LineEditGameName.setPlaceholderText("输入比赛名称...")
        self.LabelGameNameNull = Qtqw.QLabel()
        # 定义试题层控件
        self.HboxExamine = Qtqw.QHBoxLayout()
        self.LabelExamine = Qtqw.QLabel("试题：")
        self.ComBoxExamine = Qtqw.QComboBox()
        self.LabelExamineNull = Qtqw.QLabel()
        # 定义纵向布局
        self.Vbox = Qtqw.QVBoxLayout()
        # 初始化
        self.initUI()

    def initUI(self):
        self.initBtnLay()
        self.initFileLay()
        self.initDateLay()
        self.initGameNameLay()
        self.initExamine()

        # 设置纵向 各Hbox的布局
        self.Vbox.addStretch(2)
        self.Vbox.addLayout(self.HboxExamine)
        self.Vbox.addStretch(1)
        self.Vbox.addLayout(self.HboxGameName)
        self.Vbox.addStretch(1)
        self.Vbox.addLayout(self.HboxDate)
        self.Vbox.addStretch(1)
        self.Vbox.addLayout(self.HboxFileChoice)
        self.Vbox.addStretch(1)
        self.Vbox.addLayout(self.HboxButton)
        self.Vbox.addStretch(2)

        self.setLayout(self.Vbox)

    def initExamine(self):
        # 初始化试题层
        self.LabelExamine.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        self.ComBoxExamine.addItem("aaaa")  # 此处去读比赛类型 目录得到循环解析到Item
        self.HboxExamine.addWidget(self.LabelExamine)
        self.HboxExamine.addWidget(self.ComBoxExamine)
        self.HboxExamine.addWidget(self.LabelExamineNull)
        self.HboxExamine.setStretchFactor(self.LabelExamine, 4)
        self.HboxExamine.setStretchFactor(self.ComBoxExamine, 6)
        self.HboxExamine.setStretchFactor(self.LabelExamineNull, 3)

    def initGameNameLay(self):
        # 初始化比赛名称层
        self.LabelGameName.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        self.HboxGameName.addWidget(self.LabelGameName)
        self.HboxGameName.addWidget(self.LineEditGameName)
        self.HboxGameName.addWidget(self.LabelGameNameNull)
        self.HboxGameName.setStretchFactor(self.LabelGameName, 4)
        self.HboxGameName.setStretchFactor(self.LineEditGameName, 6)
        self.HboxGameName.setStretchFactor(self.LabelGameNameNull, 3)

    def initDateLay(self):
        # 初始化日期选择层
        # https://blog.csdn.net/liang19890820/article/details/52387275  QDateEdit 控件的使用说明
        self.LabelDate.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        self.LineEditDate.setDisplayFormat("yyyy-MM-dd")
        self.LineEditDate.setCalendarPopup(True)  # 调出下拉箭头，单击弹出日期控件
        self.HboxDate.addWidget(self.LabelDate)
        self.HboxDate.addWidget(self.LineEditDate)
        self.HboxDate.addWidget(self.LabelDateNull)
        self.HboxDate.setStretchFactor(self.LabelDate, 4)
        self.HboxDate.setStretchFactor(self.LineEditDate, 6)
        self.HboxDate.setStretchFactor(self.LabelDateNull, 3)

    def initFileLay(self):
        # 初始化文件选择层 并设置布局
        self.LabelFile.setAlignment(Qtqc.Qt.AlignRight | Qtqc.Qt.AlignVCenter)  # 设置文本右对齐，纵向居中
        self.LabelFile.setContentsMargins(0, 0, 0, 3)  # 设置文本的下边距为3个像素
        self.HboxFileChoice.addWidget(self.LabelFile)
        self.HboxFileChoice.addWidget(self.LineEditFile)
        self.HboxFileChoice.addWidget(self.btnFileChose)
        self.HboxFileChoice.setStretchFactor(self.LabelFile, 4)
        self.HboxFileChoice.setStretchFactor(self.LineEditFile, 6)
        self.HboxFileChoice.setStretchFactor(self.btnFileChose, 3)
        # 设置选择文件 按钮功能
        self.btnFileChose.clicked.connect(self.choseFile)

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

    def quit(self):
        self.fwindow.close()

    def choseFile(self):
        fname = Qtqw.QFileDialog.getOpenFileName()
        # print(fname[0])
        self.LineEditFile.setText(fname[0])

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
        if self.LineEditFile.text() and self.LineEditGameName.text():
            if os.path.exists(self.LineEditFile.text()):
                print(self.LineEditFile.text())
            else:
                # print("文件目录错误")
                incorrectWarning.exec()
        else:
            nullWarning.exec()
            # print("空文件路径")