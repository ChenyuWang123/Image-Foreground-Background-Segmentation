from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from Final_code import *
import sys

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Segmentation")
        self.setGeometry(100, 100, 500, 550)

        self.inputImagePath = None
        self.imageselected = False
        self.x = 0
        self.y = 0

        self.openButton = QPushButton('Upload Image', self)
        self.openButton.setToolTip('format = jpg/jpeg/png/bmp')
        self.openButton.setStyleSheet("background-color: #8EE5EE;")
        self.openButton.clicked.connect(self.openButtonOnClick)
        self.openButton.setShortcut("Ctrl+O")
		
        self.inputImageView = QLabel("Image Shows Here")
        self.inputImageView.setAlignment(Qt.AlignCenter)
	
        self.startButton = QPushButton('Sever Image', self)
        self.startButton.setStyleSheet("background-color: #8EE5EE;")
        self.startButton.setShortcut("Ctrl+S")
        self.startButton.clicked.connect(self.startButtonOnClick)

        self.coordinatesLabel = QLabel(self)
        self.coordinatesLabel.setAlignment(Qt.AlignCenter)
        self.coordinatesLabel.setText("Location = (" + str(self.x) + " , " + str(self.y) + ")")
        self.coordinatesLabel.setFixedHeight(15)

        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.openButton)
        self.vlayout.addWidget(self.startButton)
        self.vlayout.addWidget(self.inputImageView)
        self.vlayout.addWidget(self.coordinatesLabel)

        self.setLayout(self.vlayout)

        self.show()

    def openFile(self):
        self.inputImagePath, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpeg *.jpg *.bmp)")
        if self.inputImagePath:
            self.InputImage()

    def InputImage(self):
        pixmap = QPixmap(self.inputImagePath).scaled(450, 300)
        self.inputImageView.setPixmap(pixmap)
        self.imageselected = True

    def mousePressEvent(self, QMouseEvent):
        tmpx = QMouseEvent.x() - 26
        tmpy = QMouseEvent.y() - 157
        if tmpx < 450 and tmpx > 0 and tmpx > 0 and tmpy < 350:
            self.x = QMouseEvent.x() - 26
            self.y = QMouseEvent.y() - 157
            self.coordinatesLabel.setText("Location = (" + str(self.x) + " , " + str(self.y) + ")")
        print("coordination X = ", QMouseEvent.x()-26, "coordination Y = ", QMouseEvent.y()-157)
		
    def openButtonOnClick(self):
        self.openFile()

    def startButtonOnClick(self):
        if self.imageselected:
            imagepath = self.inputImagePath
            combo(imagepath, self.x, self.y)
        else:
            msg = QMessageBox.information(self, "Warning", "An input image is needed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    TheUI = UI()
    sys.exit(app.exec_())

