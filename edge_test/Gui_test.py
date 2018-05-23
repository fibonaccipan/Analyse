# -*-  coding:utf-8  -*-
import sys
import PyQt5.QtWidgets as Qtqw
from PyQt5.QtGui import QIcon

class Example(Qtqw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('C:/Users/18040267/Downloads/AxureRP_for_chorme_0_6_2/axurerp-128.png'))

        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = Qtqw.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

