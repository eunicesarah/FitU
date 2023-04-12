import sqlite3
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QRadioButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QMovie, QIcon
from PyQt6.QtCore import Qt, QSize
import sys
conn = sqlite3.connect("fitu.db")
c = conn.cursor()
latihan = c.execute("SELECT gif FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = 1").fetchall()
print(latihan)
class plan(QWidget):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.setUpWindowPlan()
        
        # self.setUpRegisterWindow()
    def setUpWindowPlan(self):
        self.setWindowTitle("FitU - Plan")
        self.setFixedSize(1280, 720)
        self.setUpPlan()

    def setUpPlan(self):
        

        self.setStyleSheet('background-color: #5A8D6C')

        backButton = QPushButton("<", self)
        backButton.setGeometry(200, 150, 100, 100)
        backButton.resize(50, 50)
        backButton.setStyleSheet("background-color: #174728; color: #EEEEE2; border-radius: 25px; border: 2px; font-size: 23px; font-weight: bold")
        backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        backButton.move(50, 64)

        self.currEx = QLabel(self)
        self.currEx.setFixedSize(360, 335)
        self.currEx.move(460, 105)
        self.currEx.setStyleSheet("background-color: #EEEEE2; border-radius: 25px; border: 2px")
        self.movie = QMovie(latihan[0][0])
        self.currEx.setMovie(self.movie)
        self.movie.start()
        # self.movie.setScaledSize(QSize(330, 305))
        self.currEx.setScaledContents(True)
        self.movie.setSpeed(60)

        nextButton = QPushButton(self)
        nextButton.setGeometry(200, 150, 100, 100)
        nextButton.setIcon(QIcon("img/arrow-right.png"))
        nextButton.setIconSize(QPixmap("img/arrow-right.png").size())
        nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        nextButton.move(700, 581)
        nextButton.clicked.connect(self.nextEx)

        prevButton = QPushButton(self)
        prevButton.setGeometry(200, 150, 100, 100)
        prevButton.setIcon(QIcon("img/arrow-left.png"))
        prevButton.setIconSize(QPixmap("img/arrow-left.png").size())
        prevButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        prevButton.move(513, 581)
        prevButton.clicked.connect(self.prevEx)



    def prevEx(self):
        if self.index > 0:
            self.index -= 1
            self.movie = QMovie(latihan[self.index][0])
            self.currEx.setMovie(self.movie)
            self.movie.start()
            self.movie.setScaledSize(QSize(330, 305))
            self.movie.setSpeed(60)
            print("kiri:" + str(self.index))


    def nextEx(self):
        if self.index < (len(latihan)/2) - 1:
            self.index += 1
            self.movie = QMovie(latihan[self.index][0])
            self.currEx.setMovie(self.movie)
            self.movie.start()
            self.movie.setScaledSize(QSize(330, 305))
            self.movie.setSpeed(100)
            print("kanan:" + str(self.index))
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = plan()
    window.show()
    app.exec()
