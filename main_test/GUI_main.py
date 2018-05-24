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
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg
import lib.releaseZip as rls
import lib.processData as pcsd


class MainWindow(Qtqw.QMainWindow):
    def __init__(self):
        self.fPath = os.path.abspath('..').replace('\\', '/')
        self.import_path: str = ""
        self.gameDegree: str = "easy"
        filelist = os.listdir(self.fPath + "/tmp")
        self.gameRound = filelist.pop()
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()
        exitAct = Qtqw.QAction(Qtqg.QIcon('../img/quit1.png'), '&退出', self)  # 设置退出按钮，属于文件菜单
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(self.app_quit)

        iptDtAct = Qtqw.QAction(Qtqg.QIcon('../img/import.png'), '&导入数据', self)  # 设置导入按钮，属于文件菜单
        iptDtAct.setShortcut('Ctrl+I')
        iptDtAct.setStatusTip('导入比赛数据')
        iptDtAct.triggered.connect(self.import_file)

        sptAct = Qtqw.QAction(Qtqg.QIcon('../img/import.png'), '&处理数据', self)  # 设置处理按钮，属于文件菜单
        sptAct.setShortcut('Ctrl+X')
        sptAct.setStatusTip('处理场次数据')
        sptAct.triggered.connect(self.split_file)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(iptDtAct)
        # 分割处理数据
        fileMenu = menubar.addMenu('&编辑')
        fileMenu.addAction(sptAct)

        self.setWindowTitle("狗逼的程序")
        self.setGeometry(300, 300, 600, 600)
        self.setWindowIcon(Qtqg.QIcon('../img/axur17.png'))
        self.show()

    def delete_round(self):
        pass

    def import_file(self):
        fname = Qtqw.QFileDialog.getOpenFileName()
        self.import_path = fname[0]
        releaser = rls.ReleaseZip(self.import_path)
        self.gameRound = releaser.release()

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
            print(self.import_path)


if __name__ == '__main__':
    app = Qtqw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
