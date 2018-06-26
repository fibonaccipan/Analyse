# -*- coding: utf-8 -*-
"""
override PyQt5.QtWidgets.QTreeWidget Class
defined contextMenuEvent method
https://bbs.csdn.net/topics/380162634
https://www.cnblogs.com/flamebird/archive/2016/12/03/6129919.html
https://www.cnblogs.com/ling123/p/5503465.html
"""
import os
import shutil
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg
# 以下为自建库
import lib.importData as IptDT


class QTreeWidget(Qtqw.QTreeWidget):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event: Qtqg.QContextMenuEvent):
        # print("override success")
        # addVersionAction
        addVersionAction = Qtqw.QAction('&添加', self)
        addVersionAction.triggered.connect(self.addVersionPop)
        # addExamineAction & delVersionAction & renameVersionAction
        addExamineAction = Qtqw.QAction('&添加', self)
        addExamineAction.triggered.connect(self.addExaminePop)
        delVersionAction = Qtqw.QAction('&删除', self)
        delVersionAction.triggered.connect(self.delVersionFun)
        renameVersionAction = Qtqw.QAction('&重命名', self)
        renameVersionAction.triggered.connect(self.renameVersionFun)
        # delExamineAction & renameExamineAction & importDataAction
        delExamineAction = Qtqw.QAction('&删除', self)
        delExamineAction.triggered.connect(self.delExamineFun)
        renameExamineAction = Qtqw.QAction('&重命名', self)
        renameExamineAction.triggered.connect(self.renameExamineFun)
        importDataAction = Qtqw.QAction('&导入数据', self)
        importDataAction.triggered.connect(self.showIptDate)

        popMenu = Qtqw.QMenu()
        popMenu.clear()
        pointItem = event.pos()  # 右击空白处获取不到位置，会导致 下面的itme 为None, 后面报错退出程序。
        point = Qtqg.QCursor.pos()

        self.item = self.itemAt(pointItem)
        try:
            if self.item.text(0) == "新创业者竞赛场次管理":
                popMenu.addAction(addVersionAction)
            elif self.item.parent().text(0) == "新创业者竞赛场次管理":  # 父节点为root 则为二级节点
                popMenu.addAction(addExamineAction)
                popMenu.addAction(delVersionAction)
                popMenu.addAction(renameVersionAction)
            elif self.item.parent().parent().text(0) == "新创业者竞赛场次管理":  # 父节点的父节点为root 则为三级节点
                popMenu.addAction(delExamineAction)
                popMenu.addAction(renameExamineAction)
                popMenu.addAction(importDataAction)
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
                if os.path.exists('../data/' + self.item.text(0)):
                    shutil.rmtree('../data/' + self.item.text(0))
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
                if os.path.exists('../data/' + self.item.parent().text(0) + '/' + self.item.text(0)):
                    os.remove('../data/' + self.item.parent().text(0) + '/' + self.item.text(0))
            # print('../rule/' + self.item.parent().text(0) + '/' + self.item.text(0))
                self.item.parent().removeChild(self.item)
            else:
                pass

    def renameExamineFun(self):
        self.examineItemPreRulePath = "../rule/" + self.currentItem().parent().text(0) + "/"+ self.currentItem().text(0)
        self.examineItemPreDatePath = "../data/" + self.currentItem().parent().text(0) + "/"+ self.currentItem().text(0)
        self.editItem(self.currentItem(), 0)
        self.itemChanged.connect(self.nameExamineChanged)

    def nameExamineChanged(self):
        self.examineItemNewRulePath = "../rule/" + self.currentItem().parent().text(0) + "/"+ self.currentItem().text(0)
        self.examineItemNewDatePath = "../data/" + self.currentItem().parent().text(0) + "/"+ self.currentItem().text(0)
        try:
            os.rename(self.examineItemPreRulePath, self.examineItemNewRulePath)
            if os.path.exists(self.examineItemPreDatePath):
                os.rename(self.examineItemPreDatePath, self.examineItemNewDatePath)
            else:
                os.mkdir(self.examineItemNewDatePath)
        except OSError:
            print(OSError)
            # 提示修改失败
        else:
            print(OSError)
            #提示修改成功

    def renameVersionFun(self):
        self.versionItemPreRulePath = "../rule/" + self.currentItem().text(0)
        self.versionItemPreDatePath = "../data/" + self.currentItem().text(0)
        self.editItem(self.currentItem(), 0)
        self.itemChanged.connect(self.nameVersionChanged)

    def nameVersionChanged(self):
        self.versionItemNewRulePath = "../rule/" + self.currentItem().text(0)
        self.versionItemNewDatePath = "../data/" + self.currentItem().text(0)
        try:
            os.rename(self.versionItemPreRulePath, self.versionItemNewRulePath)
            if os.path.exists(self.versionItemPreDatePath):
                os.rename(self.versionItemPreDatePath, self.versionItemNewDatePath)
            else:
                os.mkdir(self.versionItemNewDatePath)
        except OSError:
            print(OSError)
            # 提示修改失败
        else:
            print(OSError)
            #提示修改成功

    def saveVersionAddition(self):
        try:
            os.mkdir('../rule/' + self.versionEdit.text())
            os.mkdir('../data/' + self.versionEdit.text())
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
            os.mkdir('../data/' + self.item.text(0) + "/" + self.examineEdit.text())
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

    def showIptDate(self):
        # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # print(self.currentItem().text(0))
        # print("llllll")
        self.IptDTwindow = IptDT.IptDTwindow(self.currentItem().parent().text(0) + "/" + self.currentItem().text(0))
        # 传入当前比赛名称
        self.IptDTwindow.show()
