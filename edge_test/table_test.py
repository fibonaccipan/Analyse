# -*-  coding:utf-8  -*-
# https://blog.csdn.net/vah101/article/details/6215066 参考方法URL
# https://www.cnblogs.com/findumars/p/5422995.html

import sys
import PyQt5.QtCore as Qtqc
import PyQt5.QtGui as Qtqg
import PyQt5.QtWidgets as Qtqw
import PyQt5.Qt as qt


class Window(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        self.MyTable = Qtqw.QTableWidget(5, 3)
        self.MyTable.setEditTriggers(Qtqw.QAbstractItemView.DoubleClicked)
        self.MyTable.verticalHeader().setVisible(False)
        self.MyTable.horizontalHeader().setVisible(False)
        self.MyTable.setSpan(0, 0, 2, 1)
        self.initUI()

    def initUI(self):
        flag = Qtqc.Qt.ItemFlag(63)
        layout = Qtqw.QHBoxLayout()
        layout.addWidget(self.MyTable)
        newItem = Qtqw.QTableWidgetItem("哈？")
        newItem.setFlags(flag)
        self.MyTable.setItem(1, 1, newItem)
        self.setLayout(layout)
        self.setGeometry(400, 400, 600, 400)
        self.show()



if __name__ == '__main__':
    app = Qtqw.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
