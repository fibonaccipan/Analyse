# -*- coding: utf-8 -*-
import lib.rateBar as rtb
import threading as thd


class PopWidget:

    def __init__(self):
        self.Qbar = rtb.QRateBar()

    def Qbar_show(self):
        self.Qbar.exec()

    def Qbar_do(self):
        self.Qbar.do()

    def pop(self):
        tshow = thd.Thread(target=self.Qbar_show, name="Qbar_show")
        tshow.start()
        tbarrun = thd.Thread(target=self.Qbar_do(), name="Qbar_do")
        tbarrun.start()
