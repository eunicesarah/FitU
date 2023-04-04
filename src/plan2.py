import sqlite3
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QRadioButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QMovie
from PyQt6.QtCore import Qt, QSize
import sys
class plan(QWidget):

    def __init__(self):
        super().__init__()
        self.setUpWindowPlan()
        

        # self.setUpRegisterWindow()
        # self.conn = sqlite3.connect("fitu.db")
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
        self.movie = QMovie("img/exercise-unscreen.gif")
        self.currEx.setMovie(self.movie)
        self.movie.start()
        self.movie.setScaledSize(QSize(330, 305))
        self.movie.setSpeed(60)

        nextButton = QPushButton(">", self)
        nextButton.setGeometry(200, 150, 100, 100)
        nextButton.resize(93, 89)
        nextButton.setStyleSheet("background-color: #5A8D6C; color: #EEEEE2; border-radius: 25px; border: 2px; font-size: 50px; font-weight: bold")
        nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        nextButton.move(700, 581)

        prevButton = QPushButton("<", self)
        prevButton.setGeometry(200, 150, 100, 100)
        prevButton.resize(93, 89)
        prevButton.setStyleSheet("background-color: #5A8D6C; color: #EEEEE2; border-radius: 25px; border: 2px; font-size: 50px; font-weight: bold")
        prevButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        prevButton.move(513, 581)

        # self.label = QLabel()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = plan()
    window.show()
    app.exec()