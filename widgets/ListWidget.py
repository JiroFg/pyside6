from PySide6.QtWidgets import QWidget, QListWidget, QListWidgetItem, QAbstractItemView, QHBoxLayout, QPushButton, QVBoxLayout

class ListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.list_widget.addItems(["Item1", "Item2", "Item3"])
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        button_add = QPushButton("Add")
        button_add.clicked.connect(self.button_add_clicked)

        button_delete = QPushButton("Delete")
        button_delete.clicked.connect(self.button_deleted_clicked)

        button_count = QPushButton("Count")
        button_count.clicked.connect(self.button_count_clicked)

        button_selected = QPushButton("Selected")
        button_selected.clicked.connect(self.button_selected_clicked)

        layout = QHBoxLayout()
        layout.addWidget(button_add)
        layout.addWidget(button_delete)
        layout.addWidget(button_count)
        layout.addWidget(button_selected)

        v_layout = QVBoxLayout()
        v_layout.addLayout(layout)
        v_layout.addWidget(self.list_widget)

        self.setLayout(v_layout)

    def current_item_changed(self, item):
        print("Item changed", item.text())
    
    def current_text_changed(self, text):
        print("Text changed", text)
    
    def button_add_clicked(self):
        self.list_widget.addItem("New item")

    def button_deleted_clicked(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def button_count_clicked(self):
        print("Count", self.list_widget.count())

    def button_selected_clicked(self):
        list = self.list_widget.selectedItems()
        for i in list:
            print(i.text())
