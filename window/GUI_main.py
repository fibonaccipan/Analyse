# -*- coding: utf-8 -*-
"""
this is the main window for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180523
Accomplish : No
Final : No
"""
import os
import sys
import time
import matplotlib
import threading as td
import lib.rateBar as rtb

import lib.releaseZip as rls
import lib.processData as pcsd
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg

matplotlib.use("Qt5Agg")





class MainWindow(Qtqw.QMainWindow):
    def __init__(self):
        self.fPath = os.path.abspath('..').replace('\\', '/')
        self.import_path: str = ""
        self.gameDegree: str = "easy"
        self.main_widget = Qtqw.QWidget()
        filelist = os.listdir(self.fPath + "/tmp")

        if filelist:
            self.gameRound = filelist.pop()
        else:
            self.gameRound = "noNameGame"

        self.Qbar = rtb.QRateBar()
        self.Qbar.show()
        self.Qbar.hide()
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()
        # 定义菜单栏按钮
        exitAct = Qtqw.QAction(Qtqg.QIcon('../img/quit.png'), '&退出', self)  # 设置退出按钮，属于文件菜单
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(self.app_quit)

        iptDtAct = Qtqw.QAction(Qtqg.QIcon('../img/import.png'), '&导入数据', self)  # 设置导入按钮，属于文件菜单
        iptDtAct.setShortcut('Ctrl+I')
        iptDtAct.setStatusTip('导入比赛数据')
        iptDtAct.triggered.connect(self.import_file)

        sptAct = Qtqw.QAction(Qtqg.QIcon('../img/process.png'), '&处理数据', self)  # 设置处理按钮，属于编辑菜单
        sptAct.setShortcut('Ctrl+X')
        sptAct.setStatusTip('处理场次数据')
        # sptAct.triggered.connect(self.pop_widget)
        sptAct.triggered.connect(self.split_file)

        popAct = Qtqw.QAction(Qtqg.QIcon('../img/process.png'), '&弹窗', self)  # 设置弹窗，属于弹窗菜单  测试用
        popAct.setShortcut('Ctrl+P')
        popAct.setStatusTip('弹窗')
        popAct.triggered.connect(self.pop_widget)

        # grid = Qtqw.QGridLayout() # 测试QgridLayout的框架插入图像。
        # btn = Qtqw.QPushButton('Button', self)
        # qwgt1 = Qtqw.QWidget()
        # qwgt1.setLayout(grid)
        # grid.addWidget(btn)
        # qwgt1.setWindowTitle("yes")
        # qwgt1.setGeometry(300, 300, 300, 220)
        #
        # self.centralWidget()
        # self.setCentralWidget(qwgt1)
        # 菜单栏按钮 位置初始化
        menubar = self.menuBar()
        # 文件菜单
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(iptDtAct)
        # 编辑菜单
        editMenu = menubar.addMenu('&编辑')
        editMenu.addAction(sptAct)
        # 其他菜单
        otherMenu = menubar.addMenu('&弹窗')
        otherMenu.addAction(popAct)

        # 主窗体的 框架，放入画布
        Qbox = Qtqw.QVBoxLayout(self.main_widget)
        # sc = MyMplCan1(self.main_widget, width=5, height=4, dpi=100)
        # Qbox.addWidget(sc)

        self.setCentralWidget(self.main_widget)

        self.setWindowTitle("狗逼的程序")
        self.setGeometry(300, 150, 800, 600)
        self.setWindowIcon(Qtqg.QIcon('../img/ico.png'))
        self.show()

    def pop_widget(self):   # 测试弹窗用，已废弃
        self.Qbar.show()
        self.Qbar.do()
        def Qbar_show():
            print("def content")
        t = td.Thread(target=Qbar_show, name="Qbar_show")
        t.start()
        print("end")

    def import_file(self):
        fname = Qtqw.QFileDialog.getOpenFileName()
        self.import_path = fname[0]
        self.Qbar.show()
        self.Qbar.do()

        def back_job():
            releaser = rls.ReleaseZip(self.import_path)
            self.gameRound = releaser.release()
        t = td.Thread(target=back_job, name="back_import_job")
        t.start()
        self.Qbar.thd = t

    def split_file(self):
        self.Qbar.show()
        self.Qbar.do()

        def back_job():
            spliter = pcsd.SplitData(self.gameDegree,)
            spliter.splitDate()
        t = td.Thread(target=back_job, name="back_split_job")
        t.start()
        self.Qbar.thd = t
        # time.sleep(5)
        # stptd.stop_thread(t)

    def app_quit(self):
        replay = Qtqw.QMessageBox.question(self, "消息", "确认退出么？",
                                           Qtqw.QMessageBox.Yes | Qtqw.QMessageBox.No, Qtqw.QMessageBox.No)
        if replay == Qtqw.QMessageBox.Yes:
            Qtqw.qApp.quit()
        else:
            pass

    def closeEvent(self, event: Qtqg.QCloseEvent):
        replay = Qtqw.QMessageBox.question(self, "消息", "确认退出么？",
                                           Qtqw.QMessageBox.Yes | Qtqw.QMessageBox.No, Qtqw.QMessageBox.No)
        if replay == Qtqw.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = Qtqw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
