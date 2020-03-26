#!/usr/bin/python3
# -*- coding:utf-8 -*-

# QSplitter


import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splittle1 = QSplitter(Qt.Horizontal)
        splittle1.addWidget(topleft)
        splittle1.addWidget(topright)

        splittle2 = QSplitter(Qt.Vertical)
        splittle2.addWidget(splittle1)
        splittle2.addWidget((bottom))

        hbox.addWidget(splittle2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
