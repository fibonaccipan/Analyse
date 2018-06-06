# -*- coding: utf-8 -*-
"""
this is the main window for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180606
Accomplish : No
Final : No
"""
import sys
import datetime
import PyQt5.QtGui as Qtqg
import PyQt5.QtWidgets as Qtqw
# 以下为自建库
import window.examineManage as EM


class MainWindow(Qtqw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.EMwindow = EM.EMwindow()
        self.initUI()

    def initUI(self):
        # 生成菜单栏
        menubar = self.menuBar()

        # 生成 试题管理 按钮
        examineManage = Qtqw.QAction('&试题管理', self)
        examineManage.triggered.connect(self.showEM)
        menubar.addAction(examineManage)

        # 生成 导入数据 按钮
        importData = Qtqw.QAction('&导入数据', self)
        importData.triggered.connect(self.printsss)
        menubar.addAction(importData)

        # 生成 小组数据 按钮
        groupData = Qtqw.QAction('&小组数据', self)
        groupData.triggered.connect(self.printsss)
        menubar.addAction(groupData)

        # 生成 综合数据 按钮
        multipleData = Qtqw.QAction('&综合数据', self)
        multipleData.triggered.connect(self.printsss)
        menubar.addAction(multipleData)

        # 生成 数据分析 按钮
        analyseData = Qtqw.QAction('&数据分析', self)
        analyseData.triggered.connect(self.printsss)
        menubar.addAction(analyseData)

        # 生成 帮助 按钮
        helpMenu = Qtqw.QAction('&帮助', self)
        helpMenu.triggered.connect(self.printsss)
        menubar.addAction(helpMenu)


        self.setWindowTitle("通用数据分析工具")
        self.setGeometry(350, 180, 400, 300)
        self.setWindowIcon(Qtqg.QIcon('../img/ico.png'))
        self.show()

    def closeEvent(self, event: Qtqg.QCloseEvent):
        replay = Qtqw.QMessageBox.question(self, "消息", "确认退出么？",
                                           Qtqw.QMessageBox.Yes | Qtqw.QMessageBox.No, Qtqw.QMessageBox.No)
        if replay == Qtqw.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def showEM(self):
        # print("11111")
        self.EMwindow.show()


    def printsss(self):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    app = Qtqw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())