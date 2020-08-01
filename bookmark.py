# Author: sihan
# Date: 2019-12-24

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
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
        self.level = 0

        self.lvlT.setText(str(self.lvlSlider.value()))

        self.lvlSlider.valueChanged.connect(self.show_slider_lvl)
        self.lvlSlider.valueChanged.connect(self.make_bookmark)

        self.btnOpen.clicked.connect(self.open_image)
        self.btnSave.clicked.connect(self.save_image)
        self.btnShow.clicked.connect(self.show_big)

    def open_image(self):
        self.file_name = QFileDialog.getOpenFileName(self, "Open Image File", ".", "Image files (*.jpg )")
        self.filePath.setText(self.file_name[0])

        self.make_bookmark()

    def save_image(self):
        save_file_Name = QFileDialog.getSaveFileName(self, "Save File", "", "Image files (*.jpg )")
        cv2.imwrite(save_file_Name[0], self.img)

    def make_bookmark(self):
        self.level = self.lvlSlider.value()

        self.ori_img.load(self.file_name[0])
        self.ori_img = self.ori_img.scaledToHeight(200)
        self.lblOri.setPixmap(self.ori_img)

        checked = cv2.imread(self.file_name[0])
        self.img = cut_shuffle_img(checked, self.level)

        height, width, channel = self.img.shape
        bgr_set = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        set_img = QtGui.QImage(bgr_set, width, height, width * channel, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(set_img)
        st = pixmap.scaledToHeight(200)

        self.lblOri2.setPixmap(st)

    def show_slider_lvl(self):
        self.lvlT.setText(str(self.lvlSlider.value()))

    def show_big(self):
        cv2.imshow('Check Pattern Book Marker', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
