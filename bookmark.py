# Author: sihan
# Date: 2019-12-24

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from utils import *
import cv2

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("bookmark.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ori_img = QPixmap()
        self.btnOpen.clicked.connect(self.open_Image)
        self.btnSave.clicked.connect(self.save_Image)


    def open_Image(self):
        fname = QFileDialog.getOpenFileName(self)
        print(fname)
        self.filePath.setText(fname[0])

        self.ori_img.load(fname[0])
        self.ori_img = self.ori_img.scaledToHeight(200)
        self.lblOri.setPixmap(self.ori_img)

        checked = cv2.imread(fname[0])
        self.img = cut_shuffle_img(checked, 30)
        cv2.imshow('Check Pattern Book Marker', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_Image(self):
        cv2.imwrite('./ch.jpg', self.img)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
