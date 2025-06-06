from PySide6.QtWidgets import QWidget, QGroupBox, QCheckBox, QButtonGroup, QVBoxLayout


class CheckExWidget(QWidget):
    def __init__(self):
        super().__init__()
        drinks = QGroupBox('Choose your drink')
        beer = QCheckBox('Beer')
        juice = QCheckBox('Juice')
        coffee = QCheckBox('Coffee')
        beer.setChecked(True)

        btn_group = QButtonGroup(self)
        btn_group.addButton(beer)
        btn_group.addButton(juice)
        btn_group.addButton(coffee)
        btn_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)

        layout = QVBoxLayout()
        layout.addWidget(drinks)
        self.setLayout(layout)