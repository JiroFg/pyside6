from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Main Window")
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        # menus
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit", self.quit_app)
        # edit
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        # toolbar
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("assets/like.svg"), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))

        # status bar
        self.setStatusBar(QStatusBar(self))

        # central widget
        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    def quit_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)
    
    def button1_clicked(self):
        print("Button1 clicked")