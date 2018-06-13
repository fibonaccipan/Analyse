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
        # 设置行高为20
        myTable.verticalHeader().setDefaultSectionSize(20)
        # 设置列宽为80
        # myTable.horizontalHeader().setDefaultSectionSize(80)
        # 设置行高列宽为自适应
        # myTable.verticalHeader().setSectionResizeMode(Qtqw.QHeaderView.Stretch)
        myTable.horizontalHeader().setSectionResizeMode(Qtqw.QHeaderView.Stretch)
        # 设置0行高度 显示试题名称
        myTable.setRowHeight(0, 50)
        myTable = self.setTableStruct(myTable)  # 构造表结构，合并单元格
        myTable = self.setTableConstValue2(myTable)  # 固定值填入表格
        # 设置第0,5,12列宽 为20
        # myTable.setColumnWidth(0, 20)
        # myTable.setColumnWidth(5, 20)
        # myTable.setColumnWidth(12, 20)
        # 设置表名
        newItem = Qtqw.QTableWidgetItem("第xx试题")
        newItem = self.setItemStyle(newItem)
        # titleFont = Qtqg.QFont("song", pointSize=20, Qtqg.QFont.Bold)
        newItem.setFont(Qtqg.QFont("Times", 20, Qtqg.QFont.Bold))
        myTable.setItem(0, 0, newItem)
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
            [None, "P1", None, None, None, None, "名称", "超级手工线", "自动线", "柔性线", "自动租赁线", "柔性租赁线"],
            [None, "产品构成", "数量", "原料构成", " 数量 ", None, "投资总额"],
            [None, "P1", None, "R1", None, None, "每季投资额"],
            [None, "P2", None, "R2", None, None, "安装周期"],
            [None, "P3", None, "R3", None, None, "生产周期"],
            [None, "P4", None, "R4", None, None, "总转产费用"],
            [None, "P5", None, "R5", None, None, "转产周期"],
            [None, "开发费", None, "加工费", None, None, "维修费"],
            [None, "直接成本", None, "开发时间", None, None, "残值"],
            [None, "P2", None, None, None, None, "折旧费"],
            [None, "产品构成", "数量", "原料构成", " 数量 ", None, "折旧时间"],
            [None, "P1", None, "R1", None, None, "市场开拓及原料设置"],
            [None, "P2", None, "R2", None, None, "名称", "开发费", "开发时间", " 名称 ", "购买单价", "提前期"],
            [None, "P3", None, "R3", None, None, "本地"],
            [None, "P4", None, "R4", None, None, "区域"],
            [None, "P5", None, "R5", None, None, "国内"],
            [None, "开发费", None, "加工费", None, None, "亚洲"],
            [None, "直接成本", None, "开发时间", None, None, "国际"],
            [None, "P3", None, None, None, None, "重要参数"],
            [None, "产品构成", "数量", "原料构成", " 数量 ", None, "贴现账期", "贴现率", "违约金比例", None, "贷款额倍数"],
            [None, "P1", None, "R1", None, None, "1季 2季", None, "初始现金", None, "管理费"],
            [None, "P2", None, "R2", None, None, "3季 4季", None, "信息费", None, "所得税率"],
            [None, "P3", None, "R3", None, None, "库存拍卖", "折价率", "长贷年限", None, "最小得单额"],
            [None, "P4", None, "R4", None, None, "产品", None, "原料紧采倍", None, "产品紧采倍"],
            [None, "P5", None, "R5", None, None, "原料", None, "选单时间", None, "首单补时"],
            [None, "开发费", None, "加工费", None, None, "贷款类型", "年息", "市场同开数", None, "市场老大"],
            [None, "直接成本", None, "开发时间", None, None, "长期贷款", None, "竞单时间", None, "竞单同竞数"],
            [None, "P4", None, None, None, None, "短期贷款", None, "最大厂房数"],
            [None, "产品构成", "数量", "原料构成", " 数量 ", None, "厂房"],
            [None, "P1", None, "R1", None, None, "名称", "购买价格", "租金", "出售价格", "容量", "购买上限"],
            [None, "P2", None, "R2", None, None, "大厂房"],
            [None, "P3", None, "R3", None, None, "中厂房"],
            [None, "P4", None, "R4", None, None, "小厂房"],
            [None, "P5", None, "R5", None, None, "迷你厂房"],
            [None, "开发费", None, "加工费", None, None, "IOS资格认证", "年息", "市场同开数", None, "市场老大"],
            [None, "直接成本", None, "开发时间", None, None, "名称", "开发费", "开发时间", " 名称 ", " 开发费 ", "开发时间"],
            [None, "P5"],
            [None, "产品构成", "数量", "原料构成", " 数量 "],
            [None, "P1", None, "R1"],
            [None, "P2", None, "R2"],
            [None, "P3", None, "R3"],
            [None, "P4", None, "R4"],
            [None, "P5", None, "R5"],
            [None, "开发费", None, "加工费"],
            [None, "直接成本", None, "开发时间"]
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
        # 合并 第39行第6列往后所有
        myTable.setSpan(39, 6, 8, 6)
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