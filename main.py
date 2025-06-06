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
from widgets.ButtonWidget import ButtonWidget
from widgets.EditorWidget import EditorWidget
from widgets.ImageLabel import ImageLabel
from widgets.PoliciesWidget import PoliciesWidget
from widgets.GridWidge import GridWidget
from widgets.CheckBoxWidget import CheckBoxWidget
from widgets.CheckExWidget import CheckExWidget
from widgets.RadioWidget import RadioWidget
from config.screen import get_monitor_size
from screeninfo import Monitor
import sys

monitor: Monitor = get_monitor_size()
print(monitor)

app: QApplication = QApplication(sys.argv)
# window = ButtonHolder()
# window = SliderHolder()
# window = RockWidget()
# window = MainWindow(app)
# window = MyWidget()
# window = ButtonWidget()
# window = EditorWidget()
# window = ImageLabel()
# window = PoliciesWidget()
# window = GridWidget()
# window = CheckBoxWidget()
# window = CheckExWidget()
window = RadioWidget()
window.setMinimumSize(1000, 700)

window.show()
app.exec()

