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
# https://www.cnblogs.com/ling123/p/5503465.html
# https://blog.csdn.net/zhulove86/article/details/52530214
"""
import os
import pandas as pd
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtCore as Qtqc
import PyQt5.QtGui as Qtqg
# 以下 为自建库
import lib.QTreeWidget as Ovqtree
import lib.ruleOperate as RuOpt


class EMwidget(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        # 定义 修改标识
        self.changeFlag = 0
        # 定义 记录表格位置的 tuple
        self.varPosTuple = (  # 填入可编辑空格的位置
            (3, 7), (3, 8), (3, 9), (3, 10), (3, 11),
            (4, 2), (4, 4), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11),
            (5, 2), (5, 4), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11),
            (6, 2), (6, 4), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11),
            (7, 2), (7, 4), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11),
            (8, 2), (8, 4), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11),
            (9, 2), (9, 4), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11),
            (10, 2), (10, 4), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11),
            (11, 7), (11, 8), (11, 9), (11, 10), (11, 11),
            (12, 7), (12, 8), (12, 9), (12, 10), (12, 11),
            (13, 2), (13, 4),
            (14, 2), (14, 4),
            (15, 2), (15, 4), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11),
            (16, 2), (16, 4), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11),
            (17, 2), (17, 4), (17, 7), (17, 8), (17, 9), (17, 10), (17, 11),
            (18, 2), (18, 4), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11),
            (19, 2), (19, 4), (19, 7), (19, 8), (19, 9), (19, 10), (19, 11),
            (22, 2), (22, 4), (22, 7), (22, 9), (22, 11),
            (23, 2), (23, 4), (23, 7), (23, 9), (23, 11),
            (24, 2), (24, 4), (24, 9), (24, 11),
            (25, 2), (25, 4), (25, 7), (25, 9), (25, 11),
            (26, 2), (26, 4), (26, 7), (26, 9), (26, 11),
            (27, 2), (27, 4), (27, 9), (27, 11),
            (28, 2), (28, 4), (28, 7), (28, 9), (28, 11),
            (29, 7), (29, 9),
            (31, 2), (31, 4),
            (32, 2), (32, 4), (32, 7), (32, 8), (32, 9), (32, 10), (32, 11),
            (33, 2), (33, 4), (33, 7), (33, 8), (33, 9), (33, 10), (33, 11),
            (34, 2), (34, 4), (34, 7), (34, 8), (34, 9), (34, 10), (34, 11),
            (35, 2), (35, 4), (35, 7), (35, 8), (35, 9), (35, 10), (35, 11),
            (36, 2), (36, 4),
            (37, 2), (37, 4),
            (38, 7), (38, 8), (38, 10), (38, 11),
            (40, 2), (40, 4),
            (41, 2), (41, 4),
            (42, 2), (42, 4),
            (43, 2), (43, 4),
            (44, 2), (44, 4),
            (45, 2), (45, 4),
            (46, 2), (46, 4),
        )
        # 读取rule目录
        self.versionList = os.listdir("../rule")
        self.treeList = []
        for version in self.versionList:  # 循环软件版本级别目录
            if os.path.isfile("../rule/" + version):
                os.remove("../rule/" + version)
                continue
            examineList = os.listdir("../rule/" + version)  # 得到不同版本软件下的试题规则
            examineList.append(version)  # 在规则列表的头部插入软件版本
            self.treeList.append(examineList)  # 将软件版本和 试题规则的组合列表 并入 treeList，留作后面解析生成树
        self.currentItem: Qtqw.QTableWidgetItem = None  # 表格展示内容的当前 试题 在树上的item
        self.Qtree = self.initTree()
        # self.Qtree.doubleClicked.connect(self.setTableVariable)
        self.Qtree.clicked.connect(self.setTableVariable)
        self.Qtree.clicked.connect(self.updateOrderTable)

        self.treeSearchText = Qtqw.QLineEdit()  # 结构树 的搜索框
        self.treeSearchText.setPlaceholderText("输入搜索内容...")
        self.treeSearchText.textChanged.connect(self.searchOnTree)

        self.QRuleTable = self.initRuleTable()
        self.QRuleTable.cellClicked.connect(self.checkCurrentQtreeItem)
        # 初始化 按钮控件和插入表格的widget
        self.QbtnWdgt = Qtqw.QWidget()
        self.btnSave = Qtqw.QPushButton("保存")
        self.btnSave.clicked.connect(self.saveTableVariable)
        self.btnReLoad = Qtqw.QPushButton("重载")
        self.btnReLoad.clicked.connect(self.reLoadTable)
        self.initBtnWdgt()
        self.QRuleTable.setCellWidget(39, 6, self.QbtnWdgt)
        # 初始化 选项卡
        self.QOrderTable = self.initOrderTable()
        self.Qtable_2 = self.initRuleTable()
        self.QTab = Qtqw.QTabWidget()
        self.QTab.addTab(self.QRuleTable, "规则")
        self.QTab.addTab(self.Qtable_2, "预测")
        self.QTab.addTab(self.QOrderTable, "详单")
        # 定义 QOrderTable 表头的 下拉选择框
        self.QComboBoxYear = Qtqw.QComboBox()
        # self.QComboBoxYear.additem("aaa")
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 300, 220)
        # self.setWindowTitle('MainWidget')
        Hbox = Qtqw.QHBoxLayout()
        Vbox = Qtqw.QVBoxLayout()
        # btn = Qtqw.QPushButton("按钮", self)
        # self.treeSearchText.setContentsMargins(0, 0, 0, 0)
        # self.Qtree.setContentsMargins(0, 0, 0, 0)
        Vbox.addWidget(self.treeSearchText)
        Vbox.addWidget(self.Qtree)
        self.setLayout(Hbox)
        # Hbox.addStretch(1)
        Hbox.addLayout(Vbox)
        Hbox.addWidget(self.QTab)
        Hbox.setStretchFactor(Vbox, 1)
        Hbox.setStretchFactor(self.QTab, 4)

        # self.Qtable.setCellWidget(39, 6, self.QbtnWdgt)

    def initTree(self):
        # Qtree = Qtqw.QTreeWidget()
        Qtree = Ovqtree.QTreeWidget()
        Qtree.setHeaderHidden(True)
        root = Qtqw.QTreeWidgetItem(Qtree)
        root.setFont(0, Qtqg.QFont("Times", 10, Qtqg.QFont.Bold))
        # Qtree.contextMenuEvent.connect(self.show)
        root.setText(0, "新创业者竞赛场次管理")
        for version in self.treeList:
            lvl1 = Qtqw.QTreeWidgetItem(root)
            lvl1.setFlags(Qtqc.Qt.ItemFlag(2) | Qtqc.Qt.ItemFlag(32))
            lvl1.setFont(0, Qtqg.QFont("Times", 9, Qtqg.QFont.Bold))
            lvl1.setText(0, version.pop())
            for examine in version:
                lvl2 = Qtqw.QTreeWidgetItem(lvl1)
                lvl2.setFlags(Qtqc.Qt.ItemFlag(2) | Qtqc.Qt.ItemFlag(32))
                lvl2.setText(0, examine)
        Qtree.expandAll()
        return Qtree

    def initOrderTable(self):
        # 为选中树节点， return 一个表头
        myTable = Qtqw.QTableWidget(1, 11)
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
        return myTable

    def updateOrderTable(self):
        try:
            if self.Qtree.currentItem().parent().parent():
                secondPath = self.Qtree.currentItem().parent().text(0) + "/"
                thridPath = self.Qtree.currentItem().text(0) + "/"
                df = pd.read_excel("../data/" + secondPath + thridPath + "order.xlsx")
                columns = [x.strip() for x in df.columns]
                df.columns = columns
                # 定义表格框架
                myTable = Qtqw.QTableWidget(len(df)+1, df.columns.size)
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
                myTable.setCellWidget(0, 1, self.QComboBoxYear)
                self.QComboBoxYear.clear()
                self.QComboBoxYear.addItems(["aaaaa","bbbb"])

                # pandas query https://www.cnblogs.com/en-heng/p/5630849.html
                df = df[(df['年份'] == '')]
                #  构造函数内新建 下拉按钮，并设置 选中事件。 这里 为按钮增加内容
                #
                # 完成新表构建，删除旧Tab并插入新表
                self.QTab.removeTab(2)
                self.QTab.insertTab(2, myTable, "详单")
                print(df)
        except:
            print("order file doesn't exists")

    def initRuleTable(self):
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
        newItem = Qtqw.QTableWidgetItem("试题")
        newItem = self.setItemStyle(newItem)
        newItem.setFont(Qtqg.QFont("Times", 20, Qtqg.QFont.Bold))
        myTable.setItem(0, 0, newItem)
        return myTable

    def initBtnWdgt(self):
        Hbox = Qtqw.QHBoxLayout()
        Hbox.addStretch(1)
        Hbox.addWidget(self.btnSave)
        Hbox.addStretch(1)
        Hbox.addWidget(self.btnReLoad)
        Hbox.addStretch(1)
        self.QbtnWdgt.setLayout(Hbox)

    def setTableVariable(self):
        try:
            if self.Qtree.currentItem().parent().parent():
                print(self.Qtree.currentItem().text(0))
                self.currentItem = self.Qtree.currentItem()
                filePath = "../rule/" + self.Qtree.currentItem().parent().text(0) + "/" + self.Qtree.currentItem().text(0)
                Operater = RuOpt.ReadRule(filePath)
                dict = {}
                dict = Operater.getDict()
                newItem = Qtqw.QTableWidgetItem(self.Qtree.currentItem().text(0))
                newItem = self.setEditItemStyle(newItem)
                newItem.setFont(Qtqg.QFont("Times", 20, Qtqg.QFont.Bold))
                self.QRuleTable.setItem(0, 0, newItem)
                # 载入 读文件得到 dictionary  填入表格
                for varPos in self.varPosTuple:
                    key = "Item_" + str(varPos[0]) + "_" + str(varPos[1])
                    try:
                        newItem = Qtqw.QTableWidgetItem(dict[key])
                    except :
                        newItem = Qtqw.QTableWidgetItem()
                    newItem = self.setEditItemStyle(newItem)
                    self.QRuleTable.setItem(varPos[0], varPos[1], newItem)
                self.changeFlag = 0  # 设置修改标志为 未修改
        except:
            print("ROOT Double clicked")

    def reLoadTable(self):
        dict = {}
        if self.currentItem:
            filePath = "../rule/" + self.Qtree.currentItem().parent().text(0) + "/" + self.Qtree.currentItem().text(0)
            Operater = RuOpt.ReadRule(filePath)
            dict = Operater.getDict()
            for varPos in self.varPosTuple:
                key = "Item_" + str(varPos[0]) + "_" + str(varPos[1])
                newItem = Qtqw.QTableWidgetItem(dict[key])
                newItem = self.setEditItemStyle(newItem)
                self.QRuleTable.setItem(varPos[0], varPos[1], newItem)
            self.changeFlag = 0  # 设置标志位 未修改

    def checkCurrentQtreeItem(self):
        if self.currentItem:
            self.changeFlag = 1  # 有选中的 树节点，并且点击了报表  视为 对表格修改过
        else:
            nullCurrentWarning = Qtqw.QMessageBox()
            nullCurrentWarning.setText("请选择试题！")
            nullCurrentWarning.setWindowTitle("提示")
            nullCurrentWarning.setWindowIcon(Qtqg.QIcon('../img/error.png'))
            nullCurrentWarning.setContentsMargins(10, 10, 25, 10)
            nullCurrentWarning.exec()

    def saveTableVariable(self):
        dict = {}
        for varPos in self.varPosTuple:
            key = "Item_" + str(varPos[0]) + "_" + str(varPos[1])
            try:
                variable = self.QRuleTable.item(varPos[0], varPos[1]).text()
            except:
                variable = ""
            dict[key] = variable
        if self.currentItem:
            filePath = "../rule/" + self.currentItem.parent().text(0) + "/" + self.currentItem.text(0)
            Operater = RuOpt.SaveRule(filePath)
            Operater.saveDict(dict)
        self.changeFlag = 0  # 保存成功 视为表格未修改过

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
                myTable.setItem(4 + (j - 1) + (i - 1) * 9, 3, newItem)
            #  开发费 and 加工费
            newItem = Qtqw.QTableWidgetItem("开发费")
            newItem = self.setItemStyle(newItem)
            myTable.setItem(9 + (i - 1) * 9, 1, newItem)
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
            [None, "直接成本", None, "开发时间", None, None, "名称", "开发费", "开发时间 ", " 名称 ", " 开发费 ", " 开发时间"],
            [None, "P5", None, None, None, None, "ISO9000", None, None, "ISO14000"],
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
        # 合并 第 0,5,12 列  设置不可编辑
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
        for i in (0, 5, 12):
            newItem = Qtqw.QTableWidgetItem()
            newItem = self.setItemStyle(newItem)
            myTable.setItem(1, i, newItem)
        newItem = Qtqw.QTableWidgetItem()
        newItem = self.setItemStyle(newItem)
        myTable.setItem(39, 6, newItem)
        return myTable

    def showa(self):
        if self.Qtree.currentItem().parent().parent():
            filepath = "../rule/" + self.Qtree.currentItem().text(0) + "/" + self.Qtree.currentItem().parent().text(0)
            # if self.Qtree.currentItem().parent().parent().text(0) == "新创业者竞赛场次管理":
            #     self.Qtable.clearContents()
            #     flag = Qtqc.Qt.ItemFlags(63)
            #     newItem = Qtqw.QTableWidgetItem("777")
            #     newItem.setFlags(flag)
            #     self.Qtable.setItem(1, 1, newItem)
            Operater = RuOpt.ReadRule(filepath)
            print(str(Operater.getDict()))
            # Operater.getDict()
        else:
            print("else")

    def searchOnTree(self):
        # print("search on tree!")
        searchWord = self.treeSearchText.text()
        for i in range(self.Qtree.topLevelItem(0).childCount()):
            # print(i)
            versionHidden = True
            version =self.Qtree.topLevelItem(0).child(i)
            # print(version.text(0))
            for j in range(version.childCount()):
                # print(i, j, self.Qtree.topLevelItem(0).child(i).child(j).text(0))
                examineHidden = True
                examine = version.child(j)
                # print(examine.text(0))
                if searchWord in examine.text(0):
                    examineHidden = False
                    versionHidden = False
                examine.setHidden(examineHidden)
                # print(examineHidden)
            version.setHidden(versionHidden)

    def setItemStyle(self, item: Qtqw.QTableWidgetItem):
        # 32 黑色不可编辑
        # 60 黑色不可编辑不可选中 高亮
        flag = Qtqc.Qt.ItemFlag(60)
        item.setFlags(flag)
        item.setTextAlignment(Qtqc.Qt.AlignCenter)
        return item

    def setEditItemStyle(self, item: Qtqw.QTableWidgetItem):
        flag = Qtqc.Qt.ItemFlag(63)  # 黑色 可编辑
        item.setFlags(flag)
        item.setTextAlignment(Qtqc.Qt.AlignCenter)
        return item