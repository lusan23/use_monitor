from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QVBoxLayout,  )
from PyQt6.QtCore import Qt, QTimer
from time_session_utility import calc_time_spent, time_spent_to_string
from time_history import calc_session_total_time, calc_total_time, get_time_from_sessions_total,calc_last_seven_days_total, calc_last_thirty_days_total
import sys



class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setFixedSize(400, 300)
   
        total_spent_time = calc_total_time()
        if not total_spent_time == None:
            total_spent_time: str = f"days:{total_spent_time['days']}, {total_spent_time['hours']}:{total_spent_time['minutes']}:{total_spent_time['seconds']}"
            total_last_update_date = ""
        else:
            total_spent_time_deltatime = "None"
            total_last_update_date = "None"
        layout = QVBoxLayout()

        # TOTAL TIME SPENT LABEL
        self.total_time_spent = QLabel("<TOTAL_TIME_SPENT>", self)
        font = self.total_time_spent.font()
        font.setPointSize(14)
        self.total_time_spent.setFont(font)
        self.total_time_spent.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        self.total_time_spent.setText(f"TOTAL TIME SPENT: {total_spent_time},")
        layout.addWidget(self.total_time_spent)
        
        FONT_SIZE = 14
        # TODAY TOTAL  TIME 
        today_total_time = calc_session_total_time(return_as_string=True)
        today_total_time = get_time_from_sessions_total(today_total_time)

        self.today_total_time = QLabel("<TODAY TIME SPENT>", self)
        font = self.today_total_time.font()
        font.setPointSize(FONT_SIZE)
        self.today_total_time.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.today_total_time.setText(f"Today's Activity :{today_total_time}")
        layout.addWidget(self.today_total_time)
        
        # LAST SEVEN DAYS TOTAL TIME 
        week_total_time = calc_last_seven_days_total(return_as_string=True)
        week_total_time = get_time_from_sessions_total(week_total_time)

        self.last_week_total_time_total_time = QLabel("<LAST SEVEN DAYS TIME SPENT>", self)
        font = self.last_week_total_time_total_time.font()
        font.setPointSize(FONT_SIZE)
        self.last_week_total_time_total_time.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.last_week_total_time_total_time.setText(f"Week's Activity :{week_total_time}")
        layout.addWidget(self.last_week_total_time_total_time)

        # LAST THIRTY DAYS TOTAL TIME
        month_total_time = calc_last_thirty_days_total(return_as_string=True)
        month_total_time = get_time_from_sessions_total(month_total_time)
        
        self.last_month_total_time = QLabel("<LAST THIRTY DAYS TIME SPENT>", self)
        font = self.last_month_total_time.font()
        font.setPointSize(FONT_SIZE)
        self.last_month_total_time.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.last_month_total_time.setText(f"Month's Activity :{month_total_time}")
        layout.addWidget(self.last_month_total_time)

        # CURRENT SESSION TIME SPENT LABEL
        self.current_session_time_spent = QLabel("<SPENT_TIME>", self)
        font = self.current_session_time_spent.font()
        font.setPointSize(14)
        self.current_session_time_spent.setFont(font)
        self.current_session_time_spent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.current_session_time_spent)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        timer = QTimer(self)
        timer.timeout.connect(self.update_labels)
        timer.start(1000)
        

    def update_labels(self):

        # UPDATE CURRENT SESSION TIME
        spent_time = calc_time_spent()
        spent_time = time_spent_to_string(spent_time)
        
        self.current_session_time_spent.setText(f"CURRENT SESSION: {spent_time}")

app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()