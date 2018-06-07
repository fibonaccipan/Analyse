# -*- coding: utf-8 -*-
"""
this is the central widget to every pop QMainWindow
for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180606
Accomplish : No
Final : No
"""
import sys
import PyQt5.QtWidgets as Qtqw


class CentralWidget(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('MainWidget')

        Hbox = Qtqw.QHBoxLayout()
        # btn = Qtqw.QPushButton("按钮", self)
        Qtree = Qtqw.QTreeView(parent=None)
        self.setLayout(Hbox)
        # Hbox.addStretch(2)
        Hbox.addWidget(Qtree)
        # Hbox.addStretch(1)


if __name__ == '__main__':
    app = Qtqw.QApplication(sys.argv)
    mw = CentralWidget()
    sys.exit(app.exec_())