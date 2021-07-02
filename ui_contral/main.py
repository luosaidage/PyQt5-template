from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget

from ui.文件校验工具_stackUI import Ui_Form

class Frameless(QWidget,Ui_Form):
    # 无边框窗口和窗口相关设置
    def __init__(self):
        super(Frameless, self).__init__()
        self.setupUi(self)
        # 窗口设置
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框
        self.setMouseTracking(True)  # 设置鼠标跟踪
        self.m_flag = False  # 先设置false
        # 按钮设置
        self.button_close.clicked.connect(self.close)
        self.button_mini.clicked.connect(self.showMinimized)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class CheckTool(Frameless):
    def __init__(self):
        super(CheckTool, self).__init__()
        #先设置4个按钮对应的stackwidget的index
        self.button_file1.page = 1
        self.button_file2.page = 2
        self.button_file3.page = 3
        self.button_file4.page = 4

        self.button_file1.clicked.connect(self.set_page)
        self.button_file2.clicked.connect(self.set_page)
        self.button_file3.clicked.connect(self.set_page)
        self.button_file4.clicked.connect(self.set_page)

        #返回主页
        self.button_back1.clicked.connect(self.back_home)
        self.button_back2.clicked.connect(self.back_home)
        self.button_back3.clicked.connect(self.back_home)
        self.button_back4.clicked.connect(self.back_home)

    def set_page(self):
        print (self.sender().page)
        self.stackedWidget.setCurrentIndex(self.sender().page)

    def back_home(self):
        self.stackedWidget.setCurrentIndex(0)
