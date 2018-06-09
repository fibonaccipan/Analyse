import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg
# 右键菜单https://bbs.csdn.net/topics/380162634


class OverQtreeWidget(Qtqw.QTreeWidget):

    def contextMenuEvent(self, e: Qtqg.QContextMenuEvent):

        print("override success")
