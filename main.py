# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys

# app:QApplication = QApplication(sys.argv)

# window:QMainWindow = QMainWindow()
# window.setWindowTitle("Our first MainWindow App!")

# button: QPushButton = QPushButton()
# button.setText("Press me")

# window.setCentralWidget(button)

# window.show()
# app.exec()

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from widgets.ButtonHolder import ButtonHolder
from widgets.SliderHolder import SliderHolder
from widgets.RockWidget import RockWidget
from layouts.MainWindow import MainWindow
from widgets.MyWidget import MyWidget
import sys

app: QApplication = QApplication(sys.argv)
# window = ButtonHolder()
# window = SliderHolder()
# window = RockWidget()
# window = MainWindow(app)
window = MyWidget()

window.show()
app.exec()

