from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QPushButton, QTabWidget, QVBoxLayout


class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        tab_widget = QTabWidget(self)

        widget_form = QWidget()
        label_fullname = QLabel("Fullname:")
        line_edit_fullname = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_fullname)
        form_layout.addWidget(line_edit_fullname)
        widget_form.setLayout(form_layout)

        widget_buttons = QWidget()
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(button1)
        buttons_layout.addWidget(button2)
        buttons_layout.addWidget(button3)
        widget_buttons.setLayout(buttons_layout)

        tab_widget.addTab(widget_form, "Form")
        tab_widget.addTab(widget_buttons, "Buttons")

        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)
