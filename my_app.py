# my_app.py
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *
from second_win import TestWin

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_appearance()
        self.create_widgets()
        self.add_connections()
        self.show()

    def init_appearance(self):
        self.setWindowTitle(txt_title)
        self.setGeometry(win_x, win_y, win_width, win_height)

    def create_widgets(self):
        self.greeting_label = QLabel(txt_hello)
        self.instructions_label = QLabel(txt_instruction)
        self.start_button = QPushButton(txt_next)

        layout = QVBoxLayout()
        layout.addWidget(self.greeting_label)
        layout.addWidget(self.instructions_label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def add_connections(self):
        self.start_button.clicked.connect(self.open_test_window)

    def open_test_window(self):
        self.hide()
        self.test_window = TestWin()

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()
