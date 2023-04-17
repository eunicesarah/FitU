import sqlite3
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QMovie, QIcon
from PyQt6.QtCore import Qt, QSize, QUrl, QTimer, QTime
from PyQt6.QtMultimedia import QMediaPlayer
# from PyQt6.QtMultimedia import QSoundEffect
import time
import sys
class plan(QWidget):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.conn = sqlite3.connect("fitu.db")
        self.c = self.conn.cursor()
        self.latihan = self.c.execute("SELECT gif FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = 1").fetchall()
        print(self.latihan)
        # self.remaining_time = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.remaining_time = 0  # initial value in seconds
        self.timer.start(1000)  # set timer to update every second
        self.setUpWindowPlan()
        
        # self.setUpRegisterWindow()
    def setUpWindowPlan(self):
        self.setWindowTitle("FitU - Plan")
        self.setFixedSize(1280, 720)
        # background = QMovie("img/background.gif")
        # background.setScaledSize(QSize(1280, 720))
        # background_label = QLabel(self)
        # background_label.setGeometry(0, 0, 1280, 720)
        # background_label.setMovie(background)
        # background.start()
        
        # set the background style sheet
        # self.setStyleSheet("background-image: url(img/background.gif);")
        
        self.setUpPlan()

    def updateTimer(self):
        # print(type(self.remaining_time))
        if int(self.remaining_time) > 0:
            self.remaining_time = int(self.remaining_time) - 1
            minutes = int(self.remaining_time) // 60
            seconds = int(self.remaining_time) % 60
            self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")
        else:
            self.timer.stop()
            QMessageBox.information(self, "Time's up!", "The countdown timer has ended.")
            # QMessageBox.setStyleSheet(QLabel("color: white"))
    
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

        self.currEx = QLabel(self)
        self.currEx.setFixedSize(360, 335)
        self.currEx.move(460, 105)
        self.currEx.setStyleSheet("background-color: #EEEEE2; border-radius: 25px; border: 2px")
        self.movie = QMovie(self.latihan[0][0])
        self.currEx.setMovie(self.movie)
        self.movie.start()
        # self.movie.setScaledSize(QSize(330, 305))
        self.currEx.setScaledContents(True)
        self.movie.setSpeed(60)

        # nextLabel = QLabel(self)
        # nextLabel.setFixedSize(360, 335)
        # nextLabel.move(460, 105)
        # nextLabel.setStyleSheet("background-color: #5A8D6C; border-radius: 20px;")

        # prevLabel = QLabel(self)
        # prevLabel.setFixedSize(360, 335)
        # prevLabel.move(513, 581)
        # prevLabel.setStyleSheet("background-color: #5A8D6C; border-radius: 20px;")

        nextButton = QPushButton(self)
        nextButton.setGeometry(200, 150, 100, 100)
        nextButton.setIcon(QIcon("img/arrow-right.png"))
        nextButton.setIconSize(QPixmap("img/arrow-right.png").size())
        nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        nextButton.setStyleSheet('''
        QPushButton{
            border: 5px #5A8D6C;
            } 
        QPushButton:hover {
            background-color: #174728;
        }''')
        nextButton.move(700, 581)
        nextButton.clicked.connect(self.nextEx)

        prevButton = QPushButton(self)
        prevButton.setGeometry(200, 150, 100, 100)
        # prevButton.setStyleSheet("background-image: url(img/arrow-left.png)")
        prevButton.setIcon(QIcon("img/arrow-left.png"))
        prevButton.setIconSize(QPixmap("img/arrow-left.png").size())
        # print("size: "+ str(QPixmap("img/arrow-left.png").size()))
        prevButton.setStyleSheet('''
        QPushButton{
            border: 5px #5A8D6C;
            } 
        QPushButton:hover {
            background-color: #174728;
        }''')
        prevButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        prevButton.move(513, 581)
        prevButton.clicked.connect(self.prevEx)

        # filename = "img/BGM NKCTHI.mp3"
        # effect = QSoundEffect(self)
        # effect.setSource(QUrl.fromLocalFile(filename))
        # # possible bug: QSoundEffect::Infinite cannot be used in setLoopCount
        # effect.setLoopCount(-2)
        # effect.play()

        # if self.index == len(self.latihan):
        #     nextButton.setEnabled(False)
        #     titleProgram = c.execute(f"SELECT name FROM program WHERE program_id = {programId}").fetchone()
        #     nameExe = c.execute(f"SELECT name FROM daftar_self.latihan WHERE exercise_id in (SELECT exercise_id FROM self.latihan_program)").fetchall()
        #     date = time.strftime("%Y-%m-%d", time.localtime())
        #     totDuration = c.execute(f"SELECT SUM(duration) FROM daftar_self.latihan WHERE exercise_id in (SELECT exercise_id FROM self.latihan_program)").fetchone()
        #     c.execute("INSERT INTO riwayat_self.latihan program_id, name, title_program, date, tot_duration VALUES ({programId}, {nameExe}, {titleProgram}, {date}, {totDuration})")

        self.name = self.c.execute(f"SELECT title FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = 1").fetchall()
        print(self.name)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText(self.name[self.index][0])
        print(self.name[self.index][0])
        self.nameLabel.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        self.nameLabel.setStyleSheet("color: #EEEEE2")
        self.nameLabel.move(600, 461)
        self.nameLabel.setFixedWidth(200)

        # duration = QLabel(self)
        self.repLabel = QLabel(self)
        self.repLabel.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        self.repLabel.setStyleSheet("color: #EEEEE2")
        self.repLabel.move(547, 510)

        self.timer_label = QLabel(self)
        self.timer_label.setGeometry(0, 0, 200, 50)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.move(547, 510)
        self.timer_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.timer_label.setStyleSheet("background-color: #EEEEE2; border-radius: 10px; border: 2px")
        # durationCount = c.execute(f"SELECT duration FROM daftar_self.latihan WHERE exercise_id in (SELECT exercise_id FROM self.latihan_program WHERE program_id = 1)").fetchall()
        self.repCount = self.c.execute(f"SELECT repetition FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = 1").fetchall()
        self.duration = self.c.execute(f"SELECT duration FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = 1").fetchall()
        print(type(self.duration[self.index+1][0]))
        for i in self.repCount:
            print("rep",i)
        for i in self.duration:
            print("dur",i)

        if self.duration[self.index][0] != None:
            self.remaining_time = self.duration[self.index][0]
            self.resetTimer()
        else:
            self.repetitionLabel()
        print((self.repCount[self.index][0])==None)    

        # player = QMediaPlayer()
        # # playlist = QMediaPlaylist()
        # media = QMediaContent(QUrl.fromLocalFile("BGM ITS OKAY NOT TO BE OKAY.mp3"))  # Add your background music file here
        # player.setMedia(media)
        # player.setPlaybackMode(QMediaPlaylist.Loop)
        # player.setMedia(player)

        # button = QPushButton("Toggle BGM")
        # button.clicked.connect(lambda: player.play() if player.state() == QMediaPlayer.StoppedState else player.stop())
        # player.play()


    def prevEx(self):
        if self.index > 0:
            self.index -= 1
            self.movie = QMovie(self.latihan[self.index][0])
            self.currEx.setMovie(self.movie)
            self.movie.start()
            self.movie.setScaledSize(QSize(330, 305))
            self.movie.setSpeed(60)
            print("kiri:" + str(self.index))
        if self.duration[self.index][0] != None:
            self.remaining_time = self.duration[self.index][0]
            self.resetTimer()
        else:
            self.repetitionLabel()
        self.nameLabel.setText(self.name[self.index][0])
        print(self.index)



    def nextEx(self):
        if self.index < (len(self.latihan)) - 1:
            self.index += 1
            self.movie = QMovie(self.latihan[self.index][0])
            self.currEx.setMovie(self.movie)
            self.movie.start()
            self.movie.setScaledSize(QSize(330, 305))
            self.movie.setSpeed(100)
            print("kanan:" + str(self.index))
        if self.duration[self.index][0] != None:
            self.remaining_time = self.duration[self.index][0]
            self.resetTimer()
        else:
            self.repetitionLabel()
        self.nameLabel.setText(self.name[self.index][0])
        print(self.index)

    
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = plan()
    window.show()
    app.exec()
