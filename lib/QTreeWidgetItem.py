# -*- coding: utf-8 -*-
"""
override PyQt5.QtWidgets.QTreeWidgetItem Class
defined contextMenuItemEvent method
https://bbs.csdn.net/topics/380162634
"""
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtGui as Qtqg


class QTreeWidgetItem(Qtqw.QTreeWidgetItem):

    def contextMenuEvent(self, event: Qtqg.QContextMenuEvent):
        print("override success")

    def showAdd(self):
        print("add")