# pip install pyqt6

import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle("Заголовок окна")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        label_text = QLabel("Напиши свой текст:", self)
        label_text.move(100, 100)

        self.label_image = QLabel(self)
        self.label_image.move(400, 100)
        image_source = "pngwing.com.png"
        image_pixmap = QPixmap(image_source)
        image_pixmap = image_pixmap.scaled(
            300,
            300,
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )

        self.label_image.setPixmap(image_pixmap)

        self.label_input = QLineEdit(self)
        self.label_input.move(100, 160)
        self.mem_text = QLabel(self)
        self.mem_text.setFixedWidth(300)
        self.mem_text.setStyleSheet("color: white; font-size: 24px; padding-left: 20px;")
        self.mem_text.move(400, 100)

        button = QPushButton("Написать", self)
        button.move(100, 200)

        button.clicked.connect(self.addText)

    def addText(self):
        text = self.label_input.text()
        self.mem_text.setText(text)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())