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
import threading as thd
import matplotlib
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg
import lib.releaseZip as rls
import lib.processData as pcsd
import lib.rateBar as rtb
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")


class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, Qtqw.QSizePolicy.Expanding, Qtqw.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def initial_figure(self):
        pass


class MyMplCan1(MyMplCanvas):
    def initial_figure(self):
        df = pd.read_excel("E:/Analyse/data/data.xlsx")
        self.axes.plot(df['month'], df['amnt'])


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
        self.release_rate = 0
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()
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
        sptAct.triggered.connect(self.split_file)
        sptAct.triggered.connect(self.pop_widget)

        popAct = Qtqw.QAction(Qtqg.QIcon('../img/process.png'), '&弹窗', self)  # 设置弹窗，属于弹窗菜单
        popAct.setShortcut('Ctrl+P')
        popAct.setStatusTip('弹窗')
        popAct.triggered.connect(self.pop_widget)

        # grid = Qtqw.QGridLayout()
        # btn = Qtqw.QPushButton('Button', self)
        # qwgt1 = Qtqw.QWidget()
        # qwgt1.setLayout(grid)
        # grid.addWidget(btn)
        # qwgt1.setWindowTitle("yes")
        # qwgt1.setGeometry(300, 300, 300, 220)
        #
        # self.centralWidget()
        # self.setCentralWidget(qwgt1)

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

        Qbox = Qtqw.QVBoxLayout(self.main_widget)
        sc = MyMplCan1(self.main_widget, width=5, height=4, dpi=100)
        Qbox.addWidget(sc)

        self.setCentralWidget(self.main_widget)

        # sdockwidget = self.addDockWidget()
        self.setWindowTitle("狗逼的程序")
        self.setGeometry(300, 300, 600, 400)
        self.setWindowIcon(Qtqg.QIcon('../img/ico.png'))
        # print(type(qwgt1))
        self.show()

    def pop_widget(self):
        Qbar = rtb.QRateBar()

        def Qbar_show():
            Qbar.exec()

        t = thd.Thread(target=Qbar_show, name="Qbar_show")
        t.start()
        # Qbar_show()
        Qbar.step = 15
        Qbar.do()
        print(type(Qbar))
        # # def chstp():
        # time.sleep(2)
        # Qbar.step = 5
        # Qbar.do()

    def import_file(self):
        fname = Qtqw.QFileDialog.getOpenFileName()
        self.import_path = fname[0]
        releaser = rls.ReleaseZip(self.import_path)
        self.gameRound, self.release_rate = releaser.release()
        # print(self.release_rate)

    def split_file(self):
        spliter = pcsd.SplitData(self.gameDegree, self.gameRound)
        spliter.splitDate()
        # print(self.gameDegree, self.gameRound)

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
