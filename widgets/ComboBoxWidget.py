from PySide6.QtWidgets import QWidget, QComboBox, QPushButton, QVBoxLayout


class ComboBoxWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.combo_box = QComboBox()
        self.combo_box.addItems([
            "Earth",
            "Venus",
            "Mars",
            "Pluton",
            "Saturn"
        ])

        current_btn = QPushButton("Current")
        current_btn.clicked.connect(self.current_clicked)
        set_btn = QPushButton("Set")
        set_btn.clicked.connect(self.set_clicked)
        get_btn = QPushButton("Get")
        get_btn.clicked.connect(self.get_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(current_btn)
        layout.addWidget(set_btn)
        layout.addWidget(get_btn)
        self.setLayout(layout)

    def current_clicked(self):
        print("current:", self.combo_box.currentIndex(), self.combo_box.currentText())

    def set_clicked(self):
        self.combo_box.setCurrentIndex(2)

    def get_clicked(self):
        for i in range(self.combo_box.count()):
            print("Index:", i, "element:", self.combo_box.itemText(i))
