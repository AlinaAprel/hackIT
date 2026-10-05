# pip install pyqt6

import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
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
        label = QLabel("Рисунок", self)
        label.move(100, 100)
        
        image_label = QLabel(self)
        image_label.move(150, 150)
        
        image_source = "pngwing.com.png"
        image_pixmap = QPixmap(image_source)
        
        image_pixmap = image_pixmap.scaled(
            300, 300, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        
        image_label.setPixmap(image_pixmap)

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())