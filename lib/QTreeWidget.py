# -*- coding: utf-8 -*-
"""
override PyQt5.QtWidgets.QTreeWidget Class
defined contextMenuEvent method
https://bbs.csdn.net/topics/380162634
"""
import os
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg


class QTreeWidget(Qtqw.QTreeWidget):
    def __init__(self):
        super().__init__()



    def contextMenuEvent(self, event: Qtqg.QContextMenuEvent):
        print("override success")
        addVersionAction = Qtqw.QAction('&添加', self)
        addVersionAction.triggered.connect(self.addVersionPop)
        # addExamineAction
        popMenu = Qtqw.QMenu()
        popMenu.clear()
        pointItem = event.pos()  # 右击空白处获取不到位置，会导致 下面的itme 为None, 后面报错退出程序。
        point = Qtqg.QCursor.pos()

        item = self.itemAt(pointItem)
        try:
            if item.text(0) == "通用数据分析工具":
                popMenu.addAction(addVersionAction)
            else:
                print(item.text(0))
        except:
            pass
        else:
            popMenu.exec(point)
            event.accept()

    def initPopDialog(self):
        # print("1111")
        self.addDig = Qtqw.QDialog()
        self.addDig.setGeometry(400, 230, 200, 100)
        self.addDig.setWindowTitle("新建版本")

        self.versionEdit = Qtqw.QLineEdit()
        Hbox = Qtqw.QHBoxLayout()
        Hbox.addWidget(self.versionEdit)

        btn = Qtqw.QPushButton("确定", self)
        btn.clicked.connect(self.saveVersionAddition)
        Hboxbtn = Qtqw.QHBoxLayout()
        Hboxbtn.addStretch(1)
        Hboxbtn.addWidget(btn)
        Hboxbtn.addStretch(1)

        Vbox = Qtqw.QVBoxLayout()
        Vbox.addStretch(1)
        Vbox.addLayout(Hbox)
        Vbox.addStretch(1)
        Vbox.addLayout(Hboxbtn)
        Vbox.addStretch(1)
        self.addDig.setLayout(Vbox)


    def addVersionPop(self):
        self.initPopDialog()
        self.addDig.exec()

    def saveVersionAddition(self):
        try:
            os.mkdir('../rule/' + self.versionEdit.text())
        except OSError:
            # print("创建失败！")
            incorrectWarning = Qtqw.QMessageBox()
            incorrectWarning.setText("创建失败！")
            incorrectWarning.setWindowTitle("提示")
            incorrectWarning.setWindowIcon(Qtqg.QIcon('../img/error.png'))
            incorrectWarning.setContentsMargins(10, 10, 25, 10)
            incorrectWarning.exec()
        else:
            self.addDig.close()
