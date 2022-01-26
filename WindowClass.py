from queue import Queue
from re import S
from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
import PyQt6.QtCore
import sys
import main

class WindowClass(QWidget):
    def __init__(self):
        super().__init__()
        self.yesPixmap = QPixmap('imgForYesBtn.png')
        self.noPixmap = QPixmap('imgForNoBtn.png')
        self.text = "I am in your home\nDo you consent?"
        self.noText = "No was never an option..."
        self.yesText = "Good...\nI am coming after you now..."

        self.initUI()
        self.alignEverything()
        self.layouts()

    def initUI(self):
        self.setWindowTitle("mario.exe")
        self.resize(300,300)

        self.yesButton = QPushButton(self)
        self.noButton = QPushButton(self)
        self.noButton.setToolTip('I wouldnt do that if I were you...')
        self.yesButton.setText("Yes")
        self.noButton.setText("No")

        self.txtLabel = QLabel(self.text)
        self.txtLabel.setHidden(False)

        self.label = QLabel()
        self.label.setPixmap(QPixmap('startingImg.png'))

        self.noButton.clicked.connect(self.noBtnFunction)
        self.yesButton.clicked.connect(self.yesBtnFunction)

    def yesBtnFunction(self):
        self.txtLabel.setText(self.yesText)   
        self.label.setPixmap(self.yesPixmap)
        self.hideButtons()

    def noBtnFunction(self):
        self.txtLabel.setText(self.noText)
        self.label.setPixmap(self.noPixmap)
        self.hideButtons()

    def alignEverything(self):
        self.txtLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def layouts(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.txtLabel)
        layout.addWidget(self.yesButton)
        layout.addWidget(self.noButton)

    def hideButtons(self):
        self.yesButton.setHidden(True)
        self.noButton.setHidden(True)