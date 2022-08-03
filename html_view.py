from PyQt5.Qt import *

import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class EventFilter(QWidget):
    def __init__(self,parent=None):
        super(EventFilter, self).__init__(parent)

        self.file_name = self.setup_dir_fullname()
        self.index = 0

        self.setWindowTitle("html_view")

        # 设置窗口图标
        self.setWindowIcon(QIcon('icons/two.ico'))

        self.label1 = QLabel("prev")

        self.label2 = QLabel("next")

        self.LabelState=QLabel("测试提示")

        self.image1 = QImage("G:/Projectfile/icons/back.png")

        self.image2 = QImage("G:/Projectfile/icons/next.png")


        self.resize(400, 200)

        # 关键1、对要过滤的控件设置installEventFilter,这些控件的所有事件都会被eventFilter函数接受并处理。
        self.label1.installEventFilter(self)
        self.label2.installEventFilter(self)

        #设置网格布局
        mainLayout=QGridLayout(self)
        mainLayout.addWidget(self.label1,500,0)

        mainLayout.addWidget(self.label2, 500, 2)
        mainLayout.addWidget(self.LabelState, 600, 1)
        self.setLayout(mainLayout)
        print(self.file_name)

    # 关键2、在eventFiltr函数中处理这些控件的事件信息。
    def eventFilter(self, watched,event):

        if watched == self.label1:  #只对label1的点击事件进行过滤，重写行为，其他事件忽略

            #鼠标按下事件（这里仅设置鼠标左键响应）
            if event.type() ==QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.open(self.prev())
                    self.LabelState.setText(self.prev())
                #缩放图片
                transform=QTransform()
                transform.scale(0.5,0.5)
                tmp=self.image1.transformed(transform)
                tmp2 = self.image2.transformed(transform)
                self.label1.setPixmap(QPixmap.fromImage(tmp))
                self.label2.setPixmap(QPixmap.fromImage(tmp2))
            # 鼠标释放事件
            if event.type() == QEvent.MouseButtonRelease:

                self.label1.setPixmap(QPixmap.fromImage(self.image1))

        if watched == self.label2:  # 只对label2的点击事件进行过滤，重写行为，其他事件忽略

            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.open(self.next())
                    self.LabelState.setText(self.next())

                # 转换图片大小
                transform = QTransform()
                transform.scale(0.5, 0.5)
                tmp2 = self.image2.transformed(transform)
                self.label2.setPixmap(QPixmap.fromImage(tmp2))

            # 鼠标释放事件
            if event.type() == QEvent.MouseButtonRelease:

                self.label2.setPixmap(QPixmap.fromImage(self.image2))

        return QWidget.eventFilter(self,watched,event)


    def open(self,file_name1):  # 显示窗体2
        import open_html
        self.second = open_html.myWindow(file_name1)

        self.second.show()

    def setup_dir_fullname(self):
        # 初始化设置存储HTML文件的文件夹名称，默认“pic_html”，这里存放需要预览的html文件。
        pyechart_dir = 'pic_html'
        if not os.path.isdir(pyechart_dir):
            os.mkdir(pyechart_dir)
        self.path_dir_pyechart_html = os.getcwd() + os.sep + pyechart_dir

        self.mylist = os.listdir(self.path_dir_pyechart_html)

        return self.mylist

        ###等效代码###
        # self.mylist = []
        # for dirpath, dirnames, filenames in os.walk(self.path_dir_pyechart_html):
        #     for filepath in filenames:
        #         self.mylist.append(os.path.join(filepath))

    def prev(self):
        return self.show_file(-1)

    def next(self):
        return self.show_file(1)

    def show_file(self, n):
        self.index += n
        if self.index < 0:
            self.index = (len(self.file_name) - 1)
        if self.index > (len(self.file_name) - 1):
            self.index = 0

        self.file_name1 = self.file_name[self.index]
        return self.file_name1


if __name__ == '__main__':
    import sys
    # 1、创建一个应用程序对象
    app = QApplication(sys.argv)

    # 2、控件的操作
    # 创建控件
    window = EventFilter()

    # 展示控件
    window.show()

    # 3、应用程序的执行，进入到消息循环
    sys.exit(app.exec_())