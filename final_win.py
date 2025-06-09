# final_result_window.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from instr import *

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
        else:  # Ages 7-8
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
