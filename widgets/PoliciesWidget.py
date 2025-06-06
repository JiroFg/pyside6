from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy, QLineEdit, QPushButton


class PoliciesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Policies")
        label = QLabel("Some text:")
        line_edit = QLineEdit()
        line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        h_layout = QHBoxLayout()
        h_layout.addWidget(label, 2)
        h_layout.addWidget(line_edit, 2)
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(button1, 2)
        h_layout2.addWidget(button2, 1)
        h_layout2.addWidget(button3, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout2)
        self.setLayout(v_layout)