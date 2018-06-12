# -*- coding: utf-8 -*-
"""
this is the examine manage widget ,which is a part of examineManage pop QMainWindow
be used to contain different kind widget and split window layout
for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180606
Accomplish : No
Final : No
"""
import os
import sys
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtCore as Qtqc
import PyQt5.QtGui as Qtqg
# 以下 为自建库
import lib.QTreeWidget as Ovqtree


class EMwidget(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        # 读取rule目录
        self.versionList = os.listdir("../rule")
        self.treeList = []
        for version in self.versionList:  # 循环软件版本级别目录
            examineList = os.listdir("../rule/" + version)  # 得到不同版本软件下的试题规则
            examineList.append(version)  # 在规则列表的头部插入软件版本
            self.treeList.append(examineList)  # 将软件版本和 试题规则的组合列表 并入 treeList，留作后面解析生成树
        self.Qtree = self.initTree()
        self.Qtree.doubleClicked.connect(self.showa)
        self.Qtable = self.initTable()
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 300, 220)
        # self.setWindowTitle('MainWidget')
        Hbox = Qtqw.QHBoxLayout()
        # btn = Qtqw.QPushButton("按钮", self)
        self.setLayout(Hbox)
        # Hbox.addStretch(1)
        Hbox.addWidget(self.Qtree)
        Hbox.addWidget(self.Qtable)
        Hbox.setStretchFactor(self.Qtree, 1)
        Hbox.setStretchFactor(self.Qtable, 4)

    def initTable(self):
        myTable = Qtqw.QTableWidget(5, 3)
        myTable.setEditTriggers(Qtqw.QAbstractItemView.DoubleClicked)
        myTable.verticalHeader().setVisible(False)
        myTable.horizontalHeader().setVisible(False)
        myTable.setSpan(0, 0, 2, 1)
        flag = Qtqc.Qt.ItemFlags(63)
        newItem = Qtqw.QTableWidgetItem("666")
        newItem.setFlags(flag)
        myTable.setItem(0, 0, newItem)
        return myTable

    def initTree(self):
        # Qtree = Qtqw.QTreeWidget()
        Qtree = Ovqtree.QTreeWidget()
        Qtree.setHeaderHidden(True)
        root = Qtqw.QTreeWidgetItem(Qtree)
        # Qtree.contextMenuEvent.connect(self.show)
        root.setText(0, "通用数据分析工具")
        for version in self.treeList:
            lvl1 = Qtqw.QTreeWidgetItem(root)
            lvl1.setText(0, version.pop())
            for examine in version:
                lvl2 = Qtqw.QTreeWidgetItem(lvl1)
                lvl2.setText(0, examine)
        Qtree.expandAll()
        return Qtree

    def showa(self):
        print(self.Qtree.currentItem().text(0))
        if self.Qtree.currentItem().parent().parent():
            if self.Qtree.currentItem().parent().parent().text(0) == "通用数据分析工具":
                self.Qtable.clearContents()
                flag = Qtqc.Qt.ItemFlags(63)
                newItem = Qtqw.QTableWidgetItem("777")
                newItem.setFlags(flag)
                self.Qtable.setItem(1, 1, newItem)
        else:
            print("over")


# if __name__ == '__main__':
#     app = Qtqw.QApplication(sys.argv)
#     mw = EMwidget()
#     sys.exit(app.exec_())
