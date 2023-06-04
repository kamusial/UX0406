from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys

app = QApplication(sys.argv)
#window = QWidget()
window = QPushButton("Nacisnij")
window.show()
app.exec()