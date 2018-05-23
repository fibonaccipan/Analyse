# -*- coding: utf-8 -*-
"""
this is the main window for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180523
Accomplish : No
Final : No
"""
import sys
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg
import pandas as pd
import edge_test.test as tt

class MainWindow(Qtqw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        exitAct = Qtqw.QAction(Qtqg.QIcon('../img/quit1.png'), '&退出', self)  # 设置退出按钮，属于文件菜单
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(self.app_quit)

        iptDtAct = Qtqw.QAction(Qtqg.QIcon('../img/import.png'), '&导入数据', self)  # 设置导入按钮，属于文件菜单
        iptDtAct.setShortcut('Ctrl+I')
        iptDtAct.setStatusTip('导入比赛数据')
        iptDtAct.triggered.connect(self.import_file)

        delDtAct = Qtqw.QAction(Qtqg.QIcon('../img/import.png'), '&删除场次', self)  # 设置删除按钮，属于文件菜单
        delDtAct.setShortcut('Ctrl+D')
        delDtAct.setStatusTip('删除场次数据')
        delDtAct.triggered.connect(self.delete_round)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(iptDtAct)
        fileMenu = menubar.addMenu('&编辑')
        fileMenu.addAction(delDtAct)

        self.setWindowTitle("狗逼的程序")
        self.setGeometry(300, 300, 600, 300)
        self.setWindowIcon(Qtqg.QIcon('../img/axur17.png'))
        self.show()

    def delete_round(self):
        pass

    def import_file(self):
        pass

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
    tt.test1()
    app = Qtqw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
