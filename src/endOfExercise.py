import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QRadioButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QIcon
from PyQt6.QtCore import Qt, pyqtSignal

class endOfExe(QWidget):
    switch = pyqtSignal(str, dict)
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('fitu.db')
        self.setUpWindow()
    
    def setUpWindow(self):
        self.setWindowTitle("FitU - End Of Exercise")
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setUpEndOfExe()
    
    def setUpEndOfExe(self):
        self.setStyleSheet('background-color: #5A8D6C')

        self.congratsSize = QFont()
        self.congratsSize.setPointSize(40)
        self.congratsSize.setFamily("Segoe UI")
        self.congratsSize.setBold(True)

        self.stayHealSize = QFont()
        self.stayHealSize.setPointSize(20)
        self.stayHealSize.setFamily("Segoe UI")
        self.stayHealSize.setBold(True)

        self.backSize = QFont()
        self.backSize.setPointSize(15)
        self.backSize.setFamily("Segoe UI")
        # backSize.setBold(True)

        self.congrats = QLabel(self)
        self.congrats.setText("Congratulations")
        self.congrats.setFont(self.congratsSize)
        self.congrats.setStyleSheet("color: #EEEEE2")
        self.congrats.move(450, 170)

        self.done = QLabel(self)
        self.done.setText("you've done the exercise!")
        self.done.setFont(self.congratsSize)
        self.done.setStyleSheet("color: #EEEEE2")
        self.done.move(325, 250)

        self.stayHealthy = QLabel(self)
        self.stayHealthy.setText("STAY HEALTHY AND POWERFUL!")
        self.stayHealthy.setFont(self.stayHealSize)
        self.stayHealthy.setStyleSheet("color: #EEEEE2")
        self.stayHealthy.move(435, 375)

        self.backButtonon = QPushButton(self)
        self.backButtonon.setText("Back To Dashboard")
        self.backButtonon.setStyleSheet('''
        QPushButton {
            color: rgba(255, 255, 255, 1);
            background-color:  #174728;
            border-radius: 20;
        }
        QPushButton:hover {
            background-color: #EEEEE2;
            color: #174728;
        }
        ''')
        self.backButtonon.resize(200, 50)
        self.backButtonon.setFont(self.backSize)
        self.backButtonon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButtonon.move(560, 450)
        self.backButtonon.clicked.connect(self.backToDash)

    

    def backToDash(self):
        self.switch.emit("dashboard", {})
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = endOfExe()
    window.show()
    app.exec()