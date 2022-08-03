import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class myWindow(QWidget):

    def __init__(self,file_name):

        super().__init__()
        self.file_name=file_name

        self.setWindowTitle("play")

        # 设置窗口图标
        self.setWindowIcon(QIcon('icons/pic.ico'))

        self.resize(950,580)

        self.mainLayout(self.file_name)


    def mainLayout(self,file_name):

        pyechart_dir = 'pic_html'
        if not os.path.isdir(pyechart_dir):
            os.mkdir(pyechart_dir)
        self.path_dir_pyechart_html = os.getcwd() + os.sep + pyechart_dir

        path_pyechart = self.path_dir_pyechart_html + os.sep +file_name

        self.mainhboxLayout = QHBoxLayout(self)
        self.frame = QFrame(self)
        self.mainhboxLayout.addWidget(self.frame)
        self.hboxLayout = QHBoxLayout(self.frame)

        # 网页嵌入PyQt5
        self.myHtml = QWebEngineView()  ##浏览器引擎控件
        self.myHtml.setGeometry(50,20,1000,600)

        # 打开本地html文件#使用绝对地址定位，在地址前面加上 file:/// ，将地址的 \ 改为/
        self.myHtml.load(QUrl.fromLocalFile("file:/{0}".format(path_pyechart)))

        self.hboxLayout.addWidget(self.myHtml)
        self.setLayout(self.mainhboxLayout)

#测试
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     main = myWindow(file_name)
#
#     main.show()
#     # main.showMaximized()
#     sys.exit(app.exec_())


import os
import tkinter
import tkinter.messagebox

from PIL import Image, ImageTk

# 创建tkinter应用程序窗口
root = tkinter.Tk()
# 设置窗口的大小和位置
root.geometry('430x650+40+30')
# 不允许改变窗口的大小
root.resizable(False, False)
# 设置窗口主题
root.title('PIC-view')
root.iconbitmap(r'C:\Projectfiletest\test\two.ico')
# 获取当前文件夹中所有图片文件列表
suffix = ('.jpg', '.bmp', '.png')
pics = [p for p in os.listdir('C:/Projectfiletest/test') if p.endswith(suffix)]
pics.sort(key=lambda item: int(item[:item.index('.')]))

current = 0

def changePic(flag):
    global current
    new = current + flag

    if new < 0:
        tkinter.messagebox.showerror('', '这已经是第一张图片了')
    elif new >= len(pics):
        tkinter.messagebox.showerror('', '这已经是最后一张图片了')
    else:
        # 获取要切换图片文件名
        pic = pics[new]

        # 创建Image对象并进行缩放
        im = Image.open('./Projectfile/test/{}'.format(pic))
        w, h = im.size

        # 这里假设用来显示图片的Label组件尺寸为 400x600
        if w > 400:
            h = int(h * 400 / w)
            w = 400
        if h > 600:
            w = int(w * 600 / h)
            h = 600

        im = im.resize((w, h))

        # 创建image对象，并设置Label组件图片
        im1 = ImageTk.PhotoImage(im)
        lbPic['image'] = im1
        lbPic.image = im1

        current = new
# 上一张的按钮
def btnPreClick():
    changePic(-1)

# 下一张按钮
def btnNextClick():
    changePic(1)

def get_ico(path):
    ico_img = Image.open(path).resize((32, 32))
    icoBtn = ImageTk.PhotoImage(image=ico_img)
    return icoBtn

pr = get_ico(r'C:\Program Files (x86)\Common Files\LeASOpen\openwithres\start.png')
nt = get_ico(r'C:\Program Files (x86)\Common Files\LeASOpen\openwithres\close.png')

btnPre = tkinter.Button(root, image=pr, command=btnPreClick)
btnPre.place(x=100, y=20, width=80, height=30)

btnNext = tkinter.Button(root, image=nt, command=btnNextClick)
btnNext.place(x=230, y=20, width=80, height=30)

# 用来显示图片的Label组件
lbPic = tkinter.Label(root, text='test', width=400, height=600)
changePic(0)
lbPic.place(x=10, y=50, width=400, height=600)

# 启动
root.mainloop()