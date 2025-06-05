from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.__button_clicked)
        self.setCentralWidget(button)

    def __button_clicked(self, data):
        print("You clicked the button", data)