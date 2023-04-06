import sqlite3
import sys
import textwrap
from functools import partial

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QFont, QMovie
from PyQt6.QtWidgets import (QWidget, QApplication, QMainWindow, QWidget, QGridLayout,
                             QGroupBox, QRadioButton, QCheckBox, QMessageBox,
                             QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QDialog)
# from PyQt6 import QtWidgets

background = '#5A8D6C'
button_color = '#174728'
text_color = '#EEEEE2'
card_color = '#D2DCC4'

imgPath = None
descLat = None
titleLat = None

class listLatihan2(QWidget):
    
    
    def __init__(self):
        
        super().__init__()    
        self.con = sqlite3.connect('fitu.db')
        self.listLat = self.fetchListLatihan()  
        self.count = 0 
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
    
    def openDetail(self, count, listLat):
        popup = MyPopup(count, listLat)
        popup.exec()
    
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
            background-color: {background};
            border: none;
            border-radius: 20px;
        }}
        ''') 
        homeButton.setFont(buttonFont)
        homeButton.setFixedSize(96, 42) #pake ini buat kalau dia buletan
        homeButton.move(507, 58)    
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
        listButton.setFixedSize(96, 42)
        listButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            border: none;
            border-radius: 20px;
        }}
        ''')
        listButton.setFont(buttonFont)
        listButton.move(870, 53)
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
        scroll.setGeometry(0, 150, 1265,570) # mengatur posisi dan ukuran QScrollArea
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
                width: 15px;
                margin: 20px 0 20px 0;
            }
            QScrollBar::handle:vertical {
                background-color: #174728;
                border-radius: 6px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 20px;
                background-color: #D2DCC4;
                subcontrol-origin: margin;
                subcontrol-position: top;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
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
        for j in range(5):
            hbox = QHBoxLayout()
            hbox.setContentsMargins(10, 0, 0, 0)
            if(j<4):
                for i in range (4):
                    card = QPushButton(self)
                    card.setFixedSize(266, 266)
                    card.setStyleSheet(styleSheetCard)
                    
                    pathImg = QPixmap(self.listLat[count][6])
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
                    self.count = count
                    hbox.addWidget(card)
                    card.clicked.connect(partial(self.openDetail, self.count, self.listLat))
                    count+=1
            else:
                box = QLabel()
                box.setFixedHeight(12)
                scrollLayout.addWidget(box)
                    
            scrollLayout.addLayout(hbox)
            scrollLayout.setSpacing(50)
            
        
        scroll.setWidget(scrollWidget)
        
class MyPopup(QDialog):
    def __init__(self, count, listLat):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        styleSheet = (
            "background-color: #5A8D6C;"
            "border-radius: 20px;"
        )

        styleSheet2 = (
            "background-color: #D2DCC4;"
            "border-radius: 20px;"
        )

        bg = QLabel(self)
        bg.setFixedSize(942, 464)
        bg.move(198, 164)
        bg.setStyleSheet("background-color: black; border-radius: 20px;")
        
        label = QLabel(bg)
        label.setFixedSize(938,460)
        label.move(2,2)
        label.setStyleSheet(styleSheet2)
        

        okButton = QPushButton(label)
        okButton.setText("OK")
        okButton.setFixedSize(70, 40)
        okButton.move(840, 395)
        okButton.setStyleSheet(styleSheet)
        okButton.clicked.connect(self.close)
        
        
        pathGif = QMovie(listLat[count][6])
        pathGif.setScaledSize(QSize(325,325))
        pathGif.setSpeed(1000)
        gif = QLabel(bg)
        gif.setMovie(pathGif)
        gif.move(20,50)
        pathGif.start()
        
        garis = QLabel(bg)
        garis.setFixedSize(2,440)
        garis.setStyleSheet("background-color: #174728;")
        garis.move(400,10)
        
        title = QLabel(bg)
        title.setText(f'<font style="font-size:28px;font-family="Sogoe UI; ><b>{listLat[count][1]}<b>')
        title.setStyleSheet("color: #174728; background-color: #D2DCC4;")
        title.move(420, 50)
        
        # goal = QLabel(bg)
        # goal.setText(f'<font style="font-size:28px;font-family="Sogoe UI; ><b>{listLat[count][3]}<b>')
        # goal.setStyleSheet("color: #174728; background-color: #D2DCC4;")
        # goal.move(10, 150)
        
        # ex_id = QLabel(bg)
        # ex_id.setText(f'<font style="font-size:28px;font-family="Sogoe UI; ><b>{listLat[count][0]}<b>')
        # ex_id.setStyleSheet("color: #174728; background-color: #D2DCC4;")
        # ex_id.move(10, 200)
        
        # desc = QLabel(bg)
        # desc.setText(f'<font style="font-size:14px;font-family="Sogoe UI; ><b>{listLat[count][2]}<b>')
        # desc.setStyleSheet("color: #174728; background-color: #D2DCC4;")
        # desc.move(10, 250)
        # desc.setWordWrap(True)
        # desc.setFixedWidth(380)
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = listLatihan2()
    ex.show()
    app.exec()