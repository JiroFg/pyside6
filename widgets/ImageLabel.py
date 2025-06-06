from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap

class ImageLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Label")
        image_label = QLabel()
        image_label.setPixmap(QPixmap("assets/imgs/like.svg"))
        v_layout = QVBoxLayout()
        v_layout.addWidget(image_label)
        self.setLayout(v_layout)