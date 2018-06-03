
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import lib.splitDimToCol as split


class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, Qtqw.QSizePolicy.Expanding, Qtqw.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def initial_figure(self):
        pass


class MyMplCan1(MyMplCanvas):
    def initial_figure(self):
        df = pd.read_excel("E:/Analyse/data/data.xlsx")
        spliter = split.SplitDimToCol(df, 0, 1)
        df = spliter.split()
        self.axes.plot(df)
        # self.axes.plot(df['month'], df['amnt'])