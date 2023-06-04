from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 100, 700, 200)
        self.setWindowIcon(QIcon('../images/java.png'))
        self.setWindowTitle('Moj tytul')
        # self.setFixedWidth(400)
        # self.setFixedHeight(500)
        self.setStyleSheet('background-color:green')
        self.setWindowOpacity(0.5)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())