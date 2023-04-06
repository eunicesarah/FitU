import sqlite3
import sys
import textwrap

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QFont
from PyQt6.QtWidgets import (QWidget, QApplication, QMainWindow, QWidget, QGridLayout,
                             QGroupBox, QRadioButton, QCheckBox, QMessageBox,
                             QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea)
# from PyQt6 import QtWidgets

background = '#5A8D6C'
button_color = '#174728'
text_color = '#EEEEE2'
card_color = '#D2DCC4'

class listLatihan2(QWidget):
    
    
    def __init__(self):
        
        super().__init__()    
        self.con = sqlite3.connect('fitu.db')
        self.listLat = self.fetchListLatihan()   
        self.setUpListLatihanWindow()   
        self.setupGUI()
        
    def fetchListLatihan(self):
        cur = self.con.cursor()
        rows = cur.execute("SELECT * FROM daftar_latihan")
        rows = cur.fetchall()
        cur.close()
        return rows
    
    def setUpListLatihanWindow(self):
        self.setFixedSize(1280,720)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setWindowTitle("Fit-U - Daftar Latihan")
        self.setStyleSheet('background-color: #5A8D6C;')
        
    def setupGUI(self):   
    
        buttonFont = QFont()
        buttonFont.setFamily('Segoe UI')
        buttonFont.setPointSize(18)  
        
        #STYLESHEET
        styleSheetCard = (
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
        #Membuat scroll area
        
       
        # scroll.setWidget(greenCard)
        scroll = QScrollArea(self)
        scroll.setGeometry(0, 150, 1280,570) # mengatur posisi dan ukuran QScrollArea
        scroll.setStyleSheet("background-color: #5A8D6C;border-radius: none;")
        scrollWidget = QWidget(scroll)
        scrollLayout = QVBoxLayout(scrollWidget)
        scrollWidget.setStyleSheet("background-color: #5A8D6C; border-radius: 20px;")
        scrollWidget.setLayout(scrollLayout)
        vertical_scrollbar = scroll.verticalScrollBar()
        # Mengatur bentuk scroll bar
        scroll_bar_style = """
            QScrollBar:vertical {
                background-color: #D2DCC4;
                width: 20px;
                margin: 20px 0 20px 0;
            }
            QScrollBar::handle:vertical {
                background-color: #174728;
                border-radius: 10px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 20px;
                background-color: #D2DCC4;
                subcontrol-origin: margin;
                subcontrol-position: top;
            }
            QScrollBar::add-line:vertical {
                top: 0;
            }
            QScrollBar::sub-line:vertical {
                bottom: 0;
            }
        """
        scroll.verticalScrollBar().setStyleSheet(scroll_bar_style)
        count = 0
        for j in range(4):
            hbox = QHBoxLayout()
            hbox.setContentsMargins(10, 0, 0, 0)
            for i in range (4):
                card = QLabel(self)
                card.setFixedSize(266, 266)
                card.setStyleSheet(styleSheetCard)
                pathImg = QPixmap('img/logo.png')
                image = QLabel(card)
                image.setPixmap(pathImg.scaled(100,100))
                image.move(83, 10)
                title = QLabel(card)
                title.setText(f'<font style="font-size:24px;font-family="Sogoe UI;" ><b>{self.listLat[count][1]}<b>')
                title.move(10, 120)
                repDur = QLabel(card)
                if(count<8):
                    repDur.setText(f'<font style="font-size:14px;font-family="Sogoe UI;"><b>{self.listLat[count][4]} Detik<b>')
                    repDur.move(203, 130)
                else:
                    repDur.setText(f'<font style="font-size:14px;font-family="Sogoe UI;"><b>{self.listLat[count][5]} Repetisi<b>')
                    repDur.move(187,130)
                desc = QLabel(card)
                t = f'<font style="font-size:12px;font-family="Sogoe UI;">{self.listLat[count][2]}'
                desc.setText(t)
                desc.move(10, 170)
                desc.setWordWrap(True)
                desc.setFixedWidth(245)
                hbox.addWidget(card)
                count+=1
            scrollLayout.addLayout(hbox)
            scrollLayout.setSpacing(50)
            
        
        scroll.setWidget(scrollWidget)
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = listLatihan2()
    ex.show()
    app.exec()