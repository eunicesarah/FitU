import sqlite3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QFont
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QGroupBox, QRadioButton, QCheckBox, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QPushButton)

background = '#5A8D6C'
button_color = '#174728'
text_color = '#EEEEE2'
card_color = '#D2DCC4'

class customizeWorkout(QWidget):
    
    
    def __init__(self):
        
        super().__init__()          
        self.setupGUI()
        
    def setupGUI(self):
    
        self.label = QLabel("")
        self.label.setParent(self)
        self.setFixedSize(1280, 720)
        self.setWindowTitle("FIT-U")
        self.setStyleSheet("background-color: #5A8D6C;")
        self.elements()
    
    def elements(self): 
        buttonFont = QFont()
        buttonFont.setFamily('Segoe UI')
        buttonFont.setPointSize(18)  
        
        #STYLESHEET
        styleSheet = (
            "background-color: #D2DCC4;"
            "border-radius: 20px;"
        )
        styleSheet2 = (
            "color: #5A8D6C;"
            "background-color: #D2DCC4;"
            "border-radius: 20px;"
        )
        
        styleSheet3 = (
            "background-color: #5A8D6C;"
            "border-radius: 20px;"
        )
        
        styleSheet4 = (
            "color: #EEEEE2;"
            "background-color: #174728;"
            "border-radius: 20px;"
        )
        
        styleSheet5 = (
            # "color: #D2DCC4;"
            "background-color: #D2DCC4;"
            "border-radius: 20px;"
        )
        
        #NAVBAR
        # masukkan logo
        logo = QLabel(self)
        logo.setPixmap(QPixmap('img/logo-dashboard.png'))
        logo.move(60, 45)

        # tombol home
        homeButton = QPushButton(self)
        homeButton.setText('Home')
        homeButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            border: none;
            border-radius: 20px;
        }}
        ''') 
        homeButton.setFont(buttonFont)
        homeButton.setFixedSize(96, 42) #pake ini buat kalau dia buletan
        homeButton.move(507, 53)    
        homeButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        
        # tombol customize
        customizeButton = QPushButton(self)
        customizeButton.setText('Customize')
        customizeButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {background};
            border: none;
            border-radius: 20px;
        }}
        ''')
        customizeButton.setFont(buttonFont)
        customizeButton.move(649, 58)
        customizeButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        
        # tombol plan
        planButton = QPushButton(self)
        planButton.setText('Plan')
        planButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {background};
            border: none;
            border-radius: 20px;
        }}
        ''')
        planButton.setFont(buttonFont)
        planButton.move(807, 58)
        planButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))

        # tombol list
        listButton = QPushButton(self)
        listButton.setText('List')
        listButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {background};
            border: none;
            border-radius: 20px;
        }}
        ''')
        listButton.setFont(buttonFont)
        listButton.move(898, 58)
        listButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        
        # tombol history
        historyButton = QPushButton(self)
        historyButton.setText('History')
        historyButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {background};
            border: none;
            border-radius: 20px;
        }}
        ''')
        historyButton.setFont(buttonFont)
        historyButton.move(979, 58)
        historyButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        
        # foto profil
        profilePhoto = QLabel(self)
        profilePhoto.setPixmap(QPixmap('img/profile-dashboard.png'))
        profilePhoto.move(1133, 45)
        
        #greenCard2
        greenCard = QLabel(self)
        greenCard.move(116.67, 155.33)
        greenCard.setFixedSize(429.79, 534.56)
        greenCard.setStyleSheet(styleSheet)
        
        #greenCard2
        greenCard2 = QLabel(self)
        greenCard2.move(577.33, 155.33)
        greenCard2.setFixedSize(604.67, 534.67)
        greenCard2.setStyleSheet(styleSheet)
        
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        font.setBold(True)
        
        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(26)
        font1.setWeight(450)
        
        exText = QLabel(self)
        exText.setText("Exercise")
        exText.setFont(font)
        exText.setStyleSheet(styleSheet2)
        exText.setFixedSize(164.72, 35)
        exText.move(145.7,194)
        
        progText = QLabel(self)
        progText.setText("Program Name:")
        progText.setStyleSheet(styleSheet2)
        progText.setFixedSize(361.33, 50)
        progText.setFont(font1)
        progText.move(592, 182.33)
        
        textBox = QLineEdit(self)
        textBox.move(840, 194)
        textBox.setFixedSize(320, 41.33)
        textBox.setStyleSheet(styleSheet3)
        
        vbox = QVBoxLayout()
        vbox.addWidget(textBox)
        
        save = QPushButton(self)
        save.setText("Save")
        save.move(1026.67, 618)
        save.setFixedSize(112, 42)
        save.setStyleSheet(styleSheet4)
        save.setFont(font1)
        
        exLabel = QLabel(self)
        exLabel.move(714.67, 260)
        exLabel.setFixedSize(366.67, 99.33)
        exLabel.setStyleSheet(styleSheet3)
        
        exLabel1 = QLabel(self)
        exLabel1.move(727.59, 270.2)
        exLabel1.setFixedSize(78.89, 78.89)
        exLabel1.setStyleSheet(styleSheet5)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = customizeWorkout()
    ex.show()
    app.exec()