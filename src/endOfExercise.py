import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QRadioButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor
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
        self.setUpEndOfExe()
    
    def setUpEndOfExe(self):
        self.setStyleSheet('background-color: #5A8D6C')

        congratsSize = QFont()
        congratsSize.setPointSize(40)
        congratsSize.setFamily("Segoe UI")
        congratsSize.setBold(True)

        stayHealSize = QFont()
        stayHealSize.setPointSize(20)
        stayHealSize.setFamily("Segoe UI")
        stayHealSize.setBold(True)

        backSize = QFont()
        backSize.setPointSize(15)
        backSize.setFamily("Segoe UI")
        # backSize.setBold(True)

        congrats = QLabel(self)
        congrats.setText("Congratulations")
        congrats.setFont(congratsSize)
        congrats.setStyleSheet("color: #EEEEE2")
        congrats.move(450, 170)

        done = QLabel(self)
        done.setText("you've done the exercise!")
        done.setFont(congratsSize)
        done.setStyleSheet("color: #EEEEE2")
        done.move(325, 250)

        stayHealthy = QLabel(self)
        stayHealthy.setText("STAY HEALTHY AND POWERFUL!")
        stayHealthy.setFont(stayHealSize)
        stayHealthy.setStyleSheet("color: #EEEEE2")
        stayHealthy.move(435, 375)

        backButton = QPushButton(self)
        backButton.setText("Back To Dashboard")
        backButton.setStyleSheet('''
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
        backButton.resize(200, 50)
        backButton.setFont(backSize)
        backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        backButton.move(560, 450)
        backButton.clicked.connect(self.backToDash)
    
    def backToDash(self):
        self.switch.emit("dashboard", {})
    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = endOfExe()
    window.show()
    app.exec()