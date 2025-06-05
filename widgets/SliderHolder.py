from PySide6.QtWidgets import QMainWindow, QSlider
from PySide6.QtCore import Qt

class SliderHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slider Holder App")
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.valueChanged.connect(self.__respond_to_slider)
        self.setCentralWidget(slider)

    def __respond_to_slider(self, data):
        print("Slider moved to:", data)
