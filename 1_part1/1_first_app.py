from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys

app = QApplication(sys.argv)

window = QDialog()

#window = QWidget()

# window = QMainWindow()
# window.statusBar().showMessage("Status....")
# window.menuBar().addMenu("Options")

window.show()
app.exec()