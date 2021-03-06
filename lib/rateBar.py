# -*- coding: utf-8 -*-
import threading as td
import lib.stopThread as stptd
import PyQt5.QtCore as Qtqc
import PyQt5.Qt as Qt
import PyQt5.QtWidgets as Qtqw


class QRateBar(Qtqw.QDialog):
    def __init__(self, fwindow: Qtqw.QMainWindow):
        super().__init__()
        self.setWindowModality(Qtqc.Qt.ApplicationModal)
        self.setAttribute(Qtqc.Qt.WA_DeleteOnClose)
        self.fwindow = fwindow
        self.step: int = 0
        self.thd: td.Thread
        # 创建 进度保存文件
        open("../rate/step.txt", "w").write("0")
        self.initUI()

    def initUI(self):
        self.pbar = Qtqw.QProgressBar(self)
        self.pbar.setGeometry(20, 50, 260, 25)
        self.btn = Qtqw.QPushButton('完成', self)
        self.btn.move(170, 125)
        self.btn.clicked.connect(self.Kill)
        self.btn.clicked.connect(self.Qquit)

        self.timer = Qtqc.QBasicTimer()

        self.setGeometry(500, 350, 280, 170)
        self.setWindowFlags(Qt.Qt.WindowTitleHint)  # 使得关闭按钮失效
        self.setWindowTitle('进度')
        # self.show()

    def getstep(self):
        f = open("../rate/step.txt", "r")
        rate = int(f.readline())
        f.close()
        return rate

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('完成')
            return
        # self.step = self.step+1
        self.step = self.getstep()
        self.pbar.setValue(self.step)

    def do(self):
        self.step = 0
        self.btn.setText('取消')
        f = open("../rate/step.txt", "w")
        f.write("0")
        f.close()
        self.timer.start(100, self)

    def Kill(self):
        if self.step >= 100:
            pass
        else:
            # stptd.stop_thread(self.thd)
            pass

    def Qquit(self):
        self.fwindow.close()
        self.timer.stop()
        self.close()
