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

    def initTable(self):
        myTable = Qtqw.QTableWidget(47, 13)
        myTable.setEditTriggers(Qtqw.QAbstractItemView.DoubleClicked)
        myTable.verticalHeader().setVisible(False)
        myTable.horizontalHeader().setVisible(False)
        myTable.verticalHeader().setDefaultSectionSize(20)
        myTable.horizontalHeader().setDefaultSectionSize(60)
        # 设置0行高度 显示试题名称
        myTable.setRowHeight(0, 50)
        myTable = self.setTableStruct(myTable)  # 构造表结构，合并单元格
        myTable = self.setTableConstValue2(myTable)  # 固定值填入表格
        return myTable

    def setTableConstValue(self, myTable: Qtqw.QTableWidget):
        # 产品构成及研发
        newItem = Qtqw.QTableWidgetItem("产品构成及研发")
        newItem = self.setItemStyle(newItem)
        myTable.setItem(1, 1, newItem)
        # 产品P 循环
        for i in range(1, 6):
            # 产品P
            newItem = Qtqw.QTableWidgetItem("P" + str(i))
            newItem = self.setItemStyle(newItem)
            myTable.setItem(2 + (i - 1) * 9, 1, newItem)
            # 产品P 表头Title
            newItem = Qtqw.QTableWidgetItem("产品构成")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(3 + (i - 1) * 9, 1, newItem)

            newItem = Qtqw.QTableWidgetItem("数量")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(3 + (i - 1) * 9, 2, newItem)

            newItem = Qtqw.QTableWidgetItem("原料构成")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(3 + (i - 1) * 9, 3, newItem)

            newItem = Qtqw.QTableWidgetItem("数量")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(3 + (i - 1) * 9, 4, newItem)
            # P[R]{1-5} 循环
            for j in range(1, 6):
                # P{1-5}
                newItem = Qtqw.QTableWidgetItem("P" + str(j))
                newItem = self.setItemStyle(newItem)
                myTable.setItem(4 + (j - 1) + (i - 1) * 9, 1, newItem)
                # R{1-5}
                newItem = Qtqw.QTableWidgetItem("R" + str(j))
                newItem = self.setItemStyle(newItem)
                myTable.setItem(4 + (j - 1) + (i - 1) * 9, 3,newItem)
            #  开发费 and 加工费
            newItem = Qtqw.QTableWidgetItem("开发费")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(9 + (i - 1) * 9, 1,newItem)
            newItem = Qtqw.QTableWidgetItem("加工费")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(9 + (i - 1) * 9, 3, newItem)
            #  直接成本 and 开发时间
            newItem = Qtqw.QTableWidgetItem("直接成本")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(10 + (i - 1) * 9, 1, newItem)
            newItem = Qtqw.QTableWidgetItem("开发时间")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(10 + (i - 1) * 9, 3, newItem)

        return myTable

    def setTableConstValue2(self, myTable: Qtqw.QTableWidget):
        contentList = [
            [None],
            [None, "产品构成及研发", None, None, None, None, "生产线"],
            [None, "P1", None, None, None, None, "名称", "超级手工线", "自动线", "柔性线", "自动租赁线", "柔性租赁线"]
        ]
        for lineList in contentList:
            for content in lineList:
                if content:
                    row = contentList.index(lineList)
                    col = lineList.index(content)
                    # print(content + str(row) + str(col))
                    newItem = Qtqw.QTableWidgetItem(content)
                    newItem = self.setItemStyle(newItem)
                    myTable.setItem(row, col, newItem)
        return myTable

    def setTableStruct(self, myTable: Qtqw.QTableWidget):
        # 合并 第 0,5,12 列
        myTable.setSpan(1, 0, 46, 1)
        myTable.setSpan(1, 5, 46, 1)
        myTable.setSpan(1, 12, 46, 1)
        # 合并第0行
        myTable.setSpan(0, 0, 1, 13)
        # 合并 第1 行
        myTable.setSpan(1, 1, 1, 4)
        myTable.setSpan(1, 6, 1, 6)
        # 合并 第2行
        myTable.setSpan(2, 1, 1, 4)
        # 合并 第11 行
        myTable.setSpan(11, 1, 1, 4)
        # 合并 第13 行
        myTable.setSpan(13, 6, 1, 6)
        # 合并 第20 行
        myTable.setSpan(20, 1, 1, 4)
        myTable.setSpan(20, 6, 1, 6)
        # 合并 第29 行
        myTable.setSpan(29, 1, 1, 4)
        # 合并 第30 行
        myTable.setSpan(30, 6, 1, 6)
        # 合并 第36行
        myTable.setSpan(36, 6, 1, 6)
        # 合并 第38 行
        myTable.setSpan(38, 1, 1, 4)
        return myTable

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

    def setItemStyle(self, item: Qtqw.QTableWidgetItem):
        flag = Qtqc.Qt.ItemFlag(32)  # 黑色 不可编辑
        item.setFlags(flag)
        item.setTextAlignment(Qtqc.Qt.AlignCenter)
        return item