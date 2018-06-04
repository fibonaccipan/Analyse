# -*-  coding:utf-8  -*-
# https://blog.csdn.net/vah101/article/details/6215066 参考方法URL
# http://www.jyguagua.com/?p=2835
import sys
import PyQt5.QtCore as Qtqc
import PyQt5.QtGui as Qtqg
import PyQt5.QtWidgets as Qtqw


class Window(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        self.MyTable = Qtqw.QTableWidget(5, 3)
        self.MyTable.setEditTriggers(Qtqw.QAbstractItemView.DoubleClicked)
        self.MyTable.verticalHeader().setVisible(False)
        self.MyTable.horizontalHeader().setVisible(False)
        self.initUI()

    def initUI(self):
        layout = Qtqw.QHBoxLayout()
        layout.addWidget(self.MyTable)
        newItem = Qtqw.QTableWidgetItem("哈？")
        self.MyTable.setItem(1, 1, newItem)
        self.setLayout(layout)
        self.setGeometry(400, 400, 600, 400)
        self.show()



if __name__ == '__main__':
    app = Qtqw.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
