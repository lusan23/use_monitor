from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QVBoxLayout,  )
from PyQt6.QtCore import Qt, QTimer
from record_time_script import calc_time_spent, time_spent_to_string, load_total_time
import sys



class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setFixedSize(400, 300)

        total_spent_time = load_total_time()
        if not total_spent_time == None:
            total_spent_time_deltatime = total_spent_time[:14]
            total_last_update_date = total_spent_time[15:]
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
    
        self.total_time_spent.setText(f"TOTAL TIME SPENT: {total_spent_time_deltatime}")
        layout.addWidget(self.total_time_spent)

        # DATE OF THE LAST RECORD
        self.date_last_record = QLabel("<DATE_LAST_RECORD>", self)
        font = self.date_last_record.font()
        font.setPointSize(12)
        self.date_last_record.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.date_last_record.setText(f"LAST RECORD AT:{total_last_update_date}")
        layout.addWidget(self.date_last_record)
        
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