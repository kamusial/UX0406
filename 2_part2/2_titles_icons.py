from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 100, 700, 200)
        self.setWindowIcon(QIcon('../images/java.png'))
        self.setWindowTitle('Moj tytul')
        # self.setFixedWidth(400)
        # self.setFixedHeight(500)
        # self.setStyleSheet('background-color:green')
        # self.setWindowOpacity(0.5)

        # label = QLabel(self)
        # label.setText('tutaj labelka')
        # label.move(100, 100)
        # label.setFont(QFont('Sanserif', 20))
        # self.setStyleSheet('color:red')

        # label = QLabel(self)
        # pixmap = QPixmap('../images/python.png')
        # label.setPixmap(pixmap)

        label = QLabel(self)
        movie = QMovie('../images/sky.gif')
        movie.setSpeed(50)
        label.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())