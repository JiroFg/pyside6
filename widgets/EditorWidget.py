from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

class EditorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor Widget")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.cursorPositionChanged.connect(self.position_changed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.text_holder_label = QLabel("I'm here")
        # 
        label = QLabel("Fullname: ")
        button = QPushButton("Grab Data")
        button.clicked.connect(self.button_clicked)

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)
        self.setLayout(v_layout)

    def button_clicked(self):
        print("Fullname: ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())
    
    def text_changed(self):
        print(self.line_edit.text())
    
    def position_changed(self, old, new):
        print("Old:", old, "New:", new)
    
    def editing_finished(self):
        print("Editing finished...")
    
    def selection_changed(self):
        print("Selection change:", self.line_edit.selectedText())