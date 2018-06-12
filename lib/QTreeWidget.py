# -*- coding: utf-8 -*-
"""
override PyQt5.QtWidgets.QTreeWidget Class
defined contextMenuEvent method
https://bbs.csdn.net/topics/380162634
https://www.cnblogs.com/flamebird/archive/2016/12/03/6129919.html
"""
import os
import shutil
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg


class QTreeWidget(Qtqw.QTreeWidget):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event: Qtqg.QContextMenuEvent):
        # print("override success")
        # addVersionAction
        addVersionAction = Qtqw.QAction('&添加', self)
        addVersionAction.triggered.connect(self.addVersionPop)
        # addExamineAction & delVersionAction
        addExamineAction = Qtqw.QAction('&添加', self)
        addExamineAction.triggered.connect(self.addExaminePop)
        delVersionAction = Qtqw.QAction('&删除', self)
        delVersionAction.triggered.connect(self.delVersionFun)
        # delExamineAction
        delExamineAction = Qtqw.QAction('&删除', self)
        delExamineAction.triggered.connect(self.delExamineFun)
        popMenu = Qtqw.QMenu()
        popMenu.clear()
        pointItem = event.pos()  # 右击空白处获取不到位置，会导致 下面的itme 为None, 后面报错退出程序。
        point = Qtqg.QCursor.pos()

        self.item = self.itemAt(pointItem)
        try:
            if self.item.text(0) == "通用数据分析工具":
                popMenu.addAction(addVersionAction)
            elif self.item.parent().text(0) == "通用数据分析工具": # 父节点为root 则为二级节点
                popMenu.addAction(addExamineAction)
                popMenu.addAction(delVersionAction)
            elif self.item.parent().parent().text(0) == "通用数据分析工具": # 父节点的父节点为root 则为三级节点
                popMenu.addAction(delExamineAction)
        except:
            pass
        else:
            popMenu.exec(point)
            event.accept()

    def initPopDialogAddVersion(self):
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

    def initPopDialogAddExamine(self):
        self.addDig = Qtqw.QDialog()
        self.addDig.setGeometry(400, 230, 200, 100)
        self.addDig.setWindowTitle("新建考试")

        self.examineEdit = Qtqw.QLineEdit()
        Hbox = Qtqw.QHBoxLayout()
        Hbox.addWidget(self.examineEdit)

        btn = Qtqw.QPushButton("确定", self)
        btn.clicked.connect(self.saveExamineAddition)
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
        self.initPopDialogAddVersion()
        self.addDig.exec()

    def addExaminePop(self):
        self.initPopDialogAddExamine()
        self.addDig.exec()

    def delVersionFun(self):
        if self.item.parent():
            replay = Qtqw.QMessageBox.question(self, "消息", "该项目所包含内容将全部删除！",
                                               Qtqw.QMessageBox.Yes | Qtqw.QMessageBox.No, Qtqw.QMessageBox.No)
            if replay == Qtqw.QMessageBox.Yes:
                if os.path.exists('../rule/' + self.item.text(0)):
                    shutil.rmtree('../rule/' + self.item.text(0))
                self.item.parent().removeChild(self.item)
            else:
                pass

    def delExamineFun(self):
        # print(self.item.text(0))
        if self.item.parent():
            replay = Qtqw.QMessageBox.question(self, "消息", "确认删除该节点？",
                                               Qtqw.QMessageBox.Yes | Qtqw.QMessageBox.No, Qtqw.QMessageBox.No)
            if replay == Qtqw.QMessageBox.Yes:
                if os.path.exists('../rule/' + self.item.parent().text(0) + '/' + self.item.text(0)):
                    os.remove('../rule/' + self.item.parent().text(0) + '/' + self.item.text(0))
            # print('../rule/' + self.item.parent().text(0) + '/' + self.item.text(0))
                self.item.parent().removeChild(self.item)
            else:
                pass

    def saveVersionAddition(self):
        try:
            os.mkdir('../rule/' + self.versionEdit.text())
            # 给topLevelItem 即 root增加一个child ,setText 为 录入框的文本
            # Qtqw.QTreeWidgetItem(self.topLevelItem(0)).setText(0, self.versionEdit.text())
            Qtqw.QTreeWidgetItem(self.item).setText(0, self.versionEdit.text())
            self.expandAll()
            # print(addItem)
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

    def saveExamineAddition(self):
        try:
            open("../rule/" + self.item.text(0) + "/" + self.examineEdit.text(), "w").write(self.examineEdit.text()) #  .write("None")
            Qtqw.QTreeWidgetItem(self.item).setText(0, self.examineEdit.text())
            self.expandAll()
        except OSError:
            incorrectWarning = Qtqw.QMessageBox()
            incorrectWarning.setText("创建失败！")
            incorrectWarning.setWindowTitle("提示")
            incorrectWarning.setWindowIcon(Qtqg.QIcon('../img/error.png'))
            incorrectWarning.setContentsMargins(10, 10, 25, 10)
            incorrectWarning.exec()
        else:
            self.addDig.close()
