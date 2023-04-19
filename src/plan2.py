import sqlite3
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QMovie, QIcon
from PyQt6.QtCore import Qt, QSize, QUrl, QTimer, pyqtSignal
from PyQt6.QtMultimedia import QMediaPlayer
from plan import plan
import time
# from PyQt6.QtMultimedia import QSoundEffect
import time
import sys
class plan2(QWidget):
    switch = pyqtSignal(str, int, dict)
    def __init__(self, program_id):
        super().__init__()
        self.index = 0
        self.conn = sqlite3.connect("fitu.db")
        self.c = self.conn.cursor()
        self.program_id = program_id
        self.latihan = self.c.execute(f"SELECT gif FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = {self.program_id}").fetchall()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.remaining_time = 0  # initial value in seconds
        self.timer.start(1000)  # set timer to update every second
        self.setUpWindowPlan()
        
        # self.setUpRegisterWindow()
    def setUpWindowPlan(self):
        self.setWindowTitle("FitU - Exercise")
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setUpPlan()

    def updateTimer(self):
        if int(self.remaining_time) > 0:
            self.remaining_time = int(self.remaining_time) - 1
            minutes = int(self.remaining_time) // 60
            seconds = int(self.remaining_time) % 60
            self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")
        else:
            self.timer.stop()
            QMessageBox.information(self, "Time's up!", "Let's go to next exercise!")
    
    def resetTimer(self):
        self.remaining_time = self.duration[self.index][0]
        self.timer.start(1000)
        if(int(self.duration[self.index][0])<59):
            self.timer_label.setText("00:"+str(self.remaining_time))
        else:
            self.timer_label.setText("00:"+str(self.remaining_time))
    def repetitionLabel(self):
        self.timer.stop()
        self.timer_label.setText(str(self.repCount[self.index][0])+ " Rep")

    def setUpPlan(self):
        self.setStyleSheet('background-color: #5A8D6C')
       
        backButton = QPushButton(self)
        backButton.setGeometry(200, 150, 100, 100)
        backButton.resize(60, 60)
        backButton.setIcon(QIcon("img/arrow-left.png"))
        backButton.setIconSize(QPixmap("img/arrow-left.png").size())
        backButton.setStyleSheet("background-color: #174728; color: #EEEEE2; border-radius: 30px; border: 2px;")
        backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        backButton.move(50, 64)
        backButton.clicked.connect(lambda: self.switch.emit("plan", 0, {}))

        self.currEx = QLabel(self)
        self.currEx.setFixedSize(360, 335)
        self.currEx.move(460, 105)
        self.currEx.setStyleSheet("background-color: #EEEEE2; border-radius: 25px; border: 2px")
        self.movie = QMovie(self.latihan[0][0])
        self.currEx.setMovie(self.movie)
        self.movie.start()
        self.currEx.setScaledContents(True)
        self.movie.setSpeed(60)

        self.nextButton = QPushButton(self)
        self.nextButton.setGeometry(200, 150, 100, 100)
        self.nextButton.setIcon(QIcon("img/arrow-right.png"))
        self.nextButton.setIconSize(QPixmap("img/arrow-right.png").size())
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.setStyleSheet('''
        QPushButton{
            border: 5px #5A8D6C;
            } 
        QPushButton:hover {
            background-color: #174728;
        }''')
        self.nextButton.move(700, 581)
        self.nextButton.clicked.connect(self.nextEx)

        self.prevButton = QPushButton(self)
        self.prevButton.setGeometry(200, 150, 100, 100)
        self.prevButton.setIcon(QIcon("img/arrow-left.png"))
        self.prevButton.setIconSize(QPixmap("img/arrow-left.png").size())
        self.prevButton.setStyleSheet('''
        QPushButton{
            border: 5px #5A8D6C;
            } 
        QPushButton:hover {
            background-color: #174728;
        }''')
        self.prevButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.prevButton.move(513, 581)
        self.prevButton.clicked.connect(self.prevEx)


        self.name = self.c.execute(f"SELECT title FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = {self.program_id}").fetchall()
        self.nameLabel = QLabel(self)
        self.nameLabel.setText(self.name[self.index][0])
        self.nameLabel.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        self.nameLabel.setWordWrap(True)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nameLabel.setStyleSheet("color: #EEEEE2")
        self.nameLabel.move(0, 461)
        self.nameLabel.setFixedWidth(1280)

        # duration = QLabel(self)
        self.repLabel = QLabel(self)
        self.repLabel.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        self.repLabel.setStyleSheet("color: #EEEEE2")
        self.repLabel.move(547, 510)

        self.timer_label = QLabel(self)
        self.timer_label.setGeometry(0, 0, 200, 50)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.move(547, 510)
        self.timer_label.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        self.timer_label.setStyleSheet("background-color: #EEEEE2; border-radius: 10px; border: 2px")
        self.start = time.time()
        # durationCount = c.execute(f"SELECT duration FROM daftar_self.latihan WHERE exercise_id in (SELECT exercise_id FROM self.latihan_program WHERE program_id = 1)").fetchall()
        self.repCount = self.c.execute(f"SELECT repetition FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = {self.program_id}").fetchall()
        self.duration = self.c.execute(f"SELECT duration FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = {self.program_id}").fetchall()

        if self.duration[self.index][0] != None:
            self.remaining_time = self.duration[self.index][0]
            self.resetTimer()
        else:
            self.repetitionLabel() 

        self.historyButton = QPushButton(self)
        self.historyButton.setFixedSize(80, 80)
        self.historyButton.setEnabled(False)
        self.historyButton.setText("end")
        self.historyButton.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold, ))

        self.historyButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.historyButton.setStyleSheet('''
        QPushButton{
            border: 5px #5A8D6C;
             color: #EEEEE2;
             border-radius: 30px;
            }
        QPushButton:hover {
            background-color: #174728;
        }''')
        self.historyButton.move(615, 585)
        self.historyButton.clicked.connect(self.addHistory)

    def prevEx(self):
        if self.index > 0:
            self.index -= 1
            self.movie = QMovie(self.latihan[self.index][0])
            self.currEx.setMovie(self.movie)
            self.movie.start()
            self.movie.setScaledSize(QSize(330, 305))
            self.movie.setSpeed(60)

        if self.duration[self.index][0] != None:
            self.remaining_time = self.duration[self.index][0]
            self.resetTimer()
        else:
            self.repetitionLabel()
        self.nameLabel.setText(self.name[self.index][0])




    def nextEx(self):
        if self.index < (len(self.latihan)) - 1:
            self.index += 1
            self.movie = QMovie(self.latihan[self.index][0])
            self.currEx.setMovie(self.movie)
            self.movie.start()
            self.movie.setScaledSize(QSize(330, 305))
            self.movie.setSpeed(100)

        if self.duration[self.index][0] != None:
            self.remaining_time = self.duration[self.index][0]
            self.resetTimer()
        else:
            self.repetitionLabel()
        self.nameLabel.setText(self.name[self.index][0])
        if self.index == (len(self.latihan)) - 1:
            self.historyButton.setEnabled(True)
            

    def addHistory(self):
        # if self.index +1 >= len(self.latihan):
            self.timer.stop()
            self.nextButton.setEnabled(False)
            titleProgram = self.c.execute(f"SELECT title_program FROM program WHERE program_id = {self.program_id}").fetchone()
            nameExe = self.c.execute(f"SELECT title FROM daftar_latihan WHERE exercise_id in (SELECT exercise_id FROM latihan_program WHERE program_id = {self.program_id})").fetchall()
            date = time.strftime("%Y-%m-%d", time.localtime())
            histId = self.c.execute("SELECT DISTINCT history_id FROM riwayat_latihan").fetchall()
            totDuration = (time.time() - self.start) // 60
            for i in range (len(self.latihan)):
                self.c.execute(f"""INSERT INTO riwayat_latihan (history_id, program_id, name, title_program, date, calories, tot_duration) 
                VALUES 
                ({len(histId)+401}, {self.program_id}, '{nameExe[i][0]}', '{(titleProgram[0])}', '{date}', NULL, {int(totDuration)})""")
                self.conn.commit()
            self.switch.emit("endOfExe",0,  {})
            
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = plan2()
    window.show()
    app.exec()
