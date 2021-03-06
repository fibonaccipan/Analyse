import sys


from PyQt5.QtWidgets import *


class TreeWidget(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle('TreeWidget')
        # 创建一个Qtree部件
        self.tree = QTreeWidget()
        # 设置部件的列数为2
        # self.tree.setColumnCount(1)
        # 设置头部信息，因为上面设置列数为2，所以要设置两个标识符
        # self.tree.setHeaderLabels(["赛程"])
        # 隐藏头部信息，
        self.tree.setHeaderHidden(False)

        # 设置root为self.tree的子树，所以root就是跟节点
        root = QTreeWidgetItem(self.tree)
        # 设置根节点的名称
        root.setText(0, "root")

        # 为root节点设置子结点
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        # child1.setText(1, 'name1')
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        # child2.setText(1, 'name2')
        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0, 'child4')
        # child4.setText(1, 'name4')

        self.tree.addTopLevelItem(root)
        # 将tree部件设置为该窗口的核心框架
        self.setCentralWidget(self.tree)


app = QApplication(sys.argv)
app.aboutToQuit.connect(app.deleteLater)
tp = TreeWidget()
tp.show()
app.exec_()