from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
)
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont

# Tekst en configuratievariabelen (instr.py)
txt_title = 'Health Check'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Welcome to the Health Check program!'
txt_instruction = (
    "This program helps you use the Rufier test to make a first evaluation of your health.\n"
    "In 45 seconds, do 30 squats and measure your heart rate during the final 15 seconds of the first minute\n"
    "of recovery.\n"
    "Note: If you feel unwell (dizzy or faint), stop immediately."
)

txt_next = 'Start Test'
txt_index = 'Rufier Index: '
txt_workheart = 'Heart Function: '

txt_res1 = 'very low. Please see a doctor as soon as possible!'
txt_res2 = 'fair. We recommend you consult a doctor!'
txt_res3 = 'average. You might want to consider getting checked by a doctor.'
txt_res4 = 'good'
txt_res5 = 'excellent'


# Klasse om de testgegevens op te slaan
class ExperimentData:
    def __init__(self, age, first, second, third):
        self.age = int(age)
        self.t1 = int(first)
        self.t2 = int(second)
        self.t3 = int(third)


# Venster voor het tonen van de eindresultaten
class FinalResultWindow(QWidget):
    def __init__(self, exp_data):
        super().__init__()
        self.exp_data = exp_data
        self.configure_window()
        self.setup_ui()
        self.show()

    def configure_window(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def setup_ui(self):
        self.index_value = self.calculate_index()
        self.index_label = QLabel(txt_index + str(self.index_value))
        self.performance_label = QLabel(txt_workheart + self.evaluate_performance())

        layout = QVBoxLayout()
        layout.addWidget(self.index_label)
        layout.addWidget(self.performance_label)
        self.setLayout(layout)

    def calculate_index(self):
        total_time = self.exp_data.t1 + self.exp_data.t2 + self.exp_data.t3
        index = (4 * total_time - 200) / 10
        return index

    def evaluate_performance(self):
        index = self.index_value
        age = self.exp_data.age

        if age >= 15:
            if index >= 15:
                return txt_res1
            elif 11 <= index < 15:
                return txt_res2
            elif 6 <= index < 11:
                return txt_res3
            elif 0.5 <= index < 6:
                return txt_res4
            else:
                return txt_res5
        elif 13 <= age <= 14:
            if index >= 16.5:
                return txt_res1
            elif 12.5 <= index < 16.5:
                return txt_res2
            elif 7.5 <= index < 12.5:
                return txt_res3
            elif 2 <= index < 7.5:
                return txt_res4
            else:
                return txt_res5
        elif 11 <= age <= 12:
            if index >= 18:
                return txt_res1
            elif 14 <= index < 18:
                return txt_res2
            elif 9 <= index < 14:
                return txt_res3
            elif 3.5 <= index < 9:
                return txt_res4
            else:
                return txt_res5
        elif 9 <= age <= 10:
            if index >= 19.5:
                return txt_res1
            elif 15.5 <= index < 19.5:
                return txt_res2
            elif 10.5 <= index < 15.5:
                return txt_res3
            elif 5 <= index < 10.5:
                return txt_res4
            else:
                return txt_res5
        else:  # Leeftijd 7-8
            if index >= 21:
                return txt_res1
            elif 17 <= index < 21:
                return txt_res2
            elif 12 <= index < 17:
                return txt_res3
            elif 6.5 <= index < 12:
                return txt_res4
            else:
                return txt_res5


# Venster voor de test zelf
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
            self.results_window = FinalResultWindow(self.experiment)
        except ValueError:
            self.age_input.setText('0')
            self.test1_input.setText('0')
            self.test2_input.setText('0')
            self.test3_input.setText('0')


# Hoofdvenster
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
        self.test_window = TestWindow()


# Start de applicatie
if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()