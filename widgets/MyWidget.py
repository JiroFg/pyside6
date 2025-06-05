from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_info = QPushButton("Information")
        button_info.clicked.connect(self.button_clicked_info)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_info)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)
    
    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Message title")
        message.setText("Something happend")
        message.setInformativeText("Do you want to do something about it?")
        message.setIcon(QMessageBox.Icon.Critical)
        message.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        message.setDefaultButton(QMessageBox.StandardButton.Ok)
        ret = message.exec()
        if ret == QMessageBox.StandardButton.Ok:
            print("OK")
        else:
            print("Canceling...")

    def button_clicked_critical(self):
        ret = QMessageBox.critical(self, "Message Title", "Critical Message!", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if ret == QMessageBox.StandardButton.Ok:
            print("Okey")
        else:
            print("Not really okey")

    def button_clicked_question(self):
        pass

    def button_clicked_info(self):
        pass

    def button_clicked_warning(self):
        pass

    def button_clicked_about(self):
        pass