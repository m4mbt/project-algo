# second_win.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from instr import *
from final_win import FinalWin

class ExperimentData:
    def __init__(self, age, first, second, third):
        self.age = int(age)
        self.t1 = int(first)
        self.t2 = int(second)
        self.t3 = int(third)

class TestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.create_widgets()
        self.setup_connections()
        self.show()

    def setup_window(self):
        self.setWindowTitle(txt_title)
        self.setGeometry(win_x, win_y, win_width, win_height)

    def create_widgets(self):
        self.name_label = QLabel('Full name:')
        self.name_input = QLineEdit('Your name here')

        self.age_label = QLabel('Age:')
        self.age_input = QLineEdit('0')

        self.test1_label = QLabel('First test result:')
        self.test1_input = QLineEdit('0')

        self.test2_label = QLabel('Second test result:')
        self.test2_input = QLineEdit('0')

        self.test3_label = QLabel('Third test result:')
        self.test3_input = QLineEdit('0')

        self.timer_display = QLabel('00:00:00')
        self.timer_display.setFont(QFont('Times', 36, QFont.Bold))

        self.start_test1_btn = QPushButton('Begin first test')
        self.start_squats_btn = QPushButton('Begin squats')
        self.start_final_btn = QPushButton('Begin final test')

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.timer_display)
        layout.addWidget(self.test1_label)
        layout.addWidget(self.test1_input)
        layout.addWidget(self.start_test1_btn)
        layout.addWidget(self.start_squats_btn)
        layout.addWidget(self.test2_label)
        layout.addWidget(self.test2_input)
        layout.addWidget(self.start_final_btn)
        layout.addWidget(self.test3_label)
        layout.addWidget(self.test3_input)
        self.setLayout(layout)

    def setup_connections(self):
        self.start_test1_btn.clicked.connect(self.start_first_timer)
        self.start_squats_btn.clicked.connect(self.start_squats_timer)
        self.start_final_btn.clicked.connect(self.start_final_timer)
        self.start_final_btn.clicked.connect(self.show_final_results)

    def start_first_timer(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_first_timer)
        self.timer.start(1000)

    def update_first_timer(self):
        global time
        time = time.addSecs(-1)
        self.timer_display.setText(time.toString('hh:mm:ss'))
        self.timer_display.setStyleSheet('color: rgb(0, 255, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def start_squats_timer(self):
        global time
        time = QTime(0, 0, 45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_squats_timer)
        self.timer.start(1000)

    def update_squats_timer(self):
        global time
        time = time.addSecs(-1)
        self.timer_display.setText(time.toString('hh:mm:ss'))
        self.timer_display.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def start_final_timer(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_final_timer)
        self.timer.start(1000)

    def update_final_timer(self):
        global time
        time = time.addSecs(-1)
        self.timer_display.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') <= '00:00:59' and time.toString('hh:mm:ss') > '00:00:45':
            self.timer_display.setStyleSheet('color: rgb(0, 255, 0)')
        elif time.toString('hh:mm:ss') <= '00:00:45' and time.toString('hh:mm:ss') > '00:00:15':
            self.timer_display.setStyleSheet('color: rgb(0, 0, 0)')
        else:
            self.timer_display.setStyleSheet('color: rgb(0, 255, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def show_final_results(self):
        try:
            self.hide()
            self.experiment = ExperimentData(
                self.age_input.text(),
                self.test1_input.text(),
                self.test2_input.text(),
                self.test3_input.text()
            )
            self.results_window = FinalWin(self.experiment)
        except ValueError:
            self.age_input.setText('0')
            self.test1_input.setText('0')
            self.test2_input.setText('0')
            self.test3_input.setText('0')
