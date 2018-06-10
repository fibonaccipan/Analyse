# -*- coding: utf-8 -*-
"""
override PyQt5.QtWidgets.QTreeWidget Class
defined contextMenuEvent method
https://bbs.csdn.net/topics/380162634
"""
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg


class QTreeWidget(Qtqw.QTreeWidget):

    def contextMenuEvent(self, event: Qtqg.QContextMenuEvent):
        print("override success")
        addRule = Qtqw.QAction('&添加', self)
        addRule.triggered.connect(self.showAdd)
        popMenu = Qtqw.QMenu()
        popMenu.clear()
        pointItem = event.pos()
        point = Qtqg.QCursor.pos()
        item = self.itemAt(pointItem)
        print(item.text(0))
        # if item:
        popMenu.addAction(addRule)
        popMenu.exec(point)
        event.accept()



    def showAdd(self):
        print("add")