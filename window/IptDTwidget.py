# -*- coding: utf-8 -*-
"""
this is the import data widget ,which is a part of importData pop QMainWindow
be used to contain different kind widget and split window layout
for  Yanteng's game analysis program,
Author : fibonacci
connect : ericpan1124@yahoo.com
Edit date :20180608
Accomplish : No
Final : No
"""
import sys
import PyQt5.QtWidgets as Qtqw
import PyQt5.QtCore as Qtqc


class IptDTwidget(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print("sassssssssss")