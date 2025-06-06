from PySide6.QtWidgets import QWidget, QGroupBox, QRadioButton, QVBoxLayout

class RadioWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Widget")
        answers = QGroupBox("Choose Answer")
        answer1 = QRadioButton("A")
        answer2 = QRadioButton("B")
        answer3 = QRadioButton("C")
        answer1.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer1)
        answers_layout.addWidget(answer2)
        answers_layout.addWidget(answer3)
        answers.setLayout(answers_layout)

        layout = QVBoxLayout()
        layout.addWidget(answers)
        self.setLayout(layout)