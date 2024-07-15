from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QVBoxLayout, QHBoxLayout, QSizePolicy )
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt, QTimer
from time_session_utility import calc_time_spent, time_spent_to_string
from time_history import calc_session_total_time, calc_total_time, get_time_from_sessions_total,calc_last_seven_days_total, calc_last_thirty_days_total
import sys



class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        
        total_spent_time = calc_total_time()

        if not total_spent_time == None:
            total_spent_time: str = f"days:{total_spent_time['days']}, {total_spent_time['hours']}:{total_spent_time['minutes']}:{total_spent_time['seconds']}"
            total_last_update_date = ""
        else:
            total_spent_time_deltatime = "None"
            total_last_update_date = "None"

        layout = QHBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        layout_right = QVBoxLayout()
        
        layout_left = QVBoxLayout()
        #layout_left.setSpacing(10)

        MAIN_FONT_SIZE = 26
        FONT_SIZE = 20
        BG_COLOR = 0X737373
        BLOCKS_COLOR = 0XA6A6A6

        # CURRENT SESSION TIME SPENT LABEL
        self.current_session_time_spent = QLabel("<SPENT_TIME>", self)
        font = self.current_session_time_spent.font()
        font.setPointSize(MAIN_FONT_SIZE)
        self.current_session_time_spent.setFont(font)
        self.current_session_time_spent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.current_session_time_spent.resize(100, 100)

        self.apply_bg_color(self.current_session_time_spent,
                            BLOCKS_COLOR)
        layout_left.addWidget(self.current_session_time_spent)
        
        # TODAY TOTAL  TIME 
        today_total_time = calc_session_total_time(return_as_string=True)
        today_total_time = get_time_from_sessions_total(today_total_time)

        today_total_time = today_total_time
        self.today_total_time = QLabel("<TODAY TIME SPENT>", self)
        font = self.today_total_time.font()
        font.setPointSize(FONT_SIZE)
        self.today_total_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.today_total_time.setText(f"Today's Activity :\n{today_total_time}")
        
        self.apply_bg_color(self.today_total_time, BLOCKS_COLOR)
        layout_right.addWidget(self.today_total_time)
        
        # LAST SEVEN DAYS TOTAL TIME 
        week_total_time = calc_last_seven_days_total(return_as_string=True)
        week_total_time = get_time_from_sessions_total(week_total_time)

        self.last_week_total_time_total_time = QLabel("<LAST SEVEN DAYS TIME SPENT>", self)
        font = self.last_week_total_time_total_time.font()
        font.setPointSize(FONT_SIZE)
        self.last_week_total_time_total_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.last_week_total_time_total_time.setText(f"Week's Activity :\n{week_total_time}")
        self.apply_bg_color(self.last_week_total_time_total_time, BLOCKS_COLOR)
        layout_right.addWidget(self.last_week_total_time_total_time)

        # LAST THIRTY DAYS TOTAL TIME
        month_total_time = calc_last_thirty_days_total(return_as_string=True)
        month_total_time = get_time_from_sessions_total(month_total_time)
        
        self.last_month_total_time = QLabel("<LAST THIRTY DAYS TIME SPENT>", self)
        font = self.last_month_total_time.font()
        font.setPointSize(FONT_SIZE)
        self.last_month_total_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.last_month_total_time.setText(f"Month's Activity :\n{month_total_time}")
        self.apply_bg_color(self.last_month_total_time,
                            BLOCKS_COLOR)
        layout_right.addWidget(self.last_month_total_time)


    
        layout.addLayout(layout_left)
        layout.addLayout(layout_right)
        
        widget = QWidget()
        self.apply_bg_color(widget, BG_COLOR)
        widget.setLayout(layout)
    
        self.setCentralWidget(widget)

        timer = QTimer(self)
        timer.timeout.connect(self.update_labels)
        timer.start(1000)
        
    def apply_bg_color(self, Qobject, choosen_color):
                
            Qobject.setAutoFillBackground(True)
            palette = self.palette()
            palette.setColor(QPalette.ColorRole.Window, QColor(choosen_color))
            Qobject.setPalette(palette)
            

    def update_labels(self):

        # UPDATE CURRENT SESSION TIME
        spent_time = calc_time_spent()
        spent_time = time_spent_to_string(spent_time)
        
        self.current_session_time_spent.setText(f"CURRENT SESSION:\n{spent_time.replace("day", "days")}")

def start():
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()

start()