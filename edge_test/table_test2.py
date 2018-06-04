import sys
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtCore as Qtqc
import PyQt5.QtGui as Qtqg

class Window(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        self.MyTable = Qtqw.QTableView()
        self.model = Qtqg.QStandardItemModel()
        self.initUI()

    def initUI(self):
        # self.MyTable.horizontalHeader().setVisible(False)
        # self.MyTable.verticalHeader().setVisible(False)
        self.model.setHorizontalHeaderItem(0, Qtqg.QStandardItem("column1"))

        self.model.setItem(0, 0, Qtqg.QStandardItem("asdf"))

        self.MyTable.setModel(self.model)
        layout = Qtqw.QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)
        self.setGeometry(400, 400, 600, 400)
        self.show()



if __name__ == '__main__':
    app = Qtqw.QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())