# -*- coding: utf-8 -*-
import sys
from pandas import DataFrame
from numpy.random import randn
import numpy as np
import matplotlib.pyplot as plt
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg
class Example(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("狗逼的程序")
        self.setGeometry(300, 300, 600, 300)
        self.setWindowIcon(Qtqg.QIcon('C:/Users/18040267/Downloads/AxureRP_for_chorme_0_6_2/axurerp-128.png'))
        self.show()

    def closeEvent(self, event: Qtqg.QCloseEvent):
        replay = Qtqw.QMessageBox.question(self,"消息","确认退出么？",Qtqw.QMessageBox.Yes|Qtqw.QMessageBox.No,Qtqw.QMessageBox.No)
        if replay == Qtqw.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    df = DataFrame(randn(10, 5), columns=['A', 'B', 'C', 'D', 'E'], index=np.arange(0, 100, 10))
    df.plot()
    plt.show()
    app = Qtqw.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())