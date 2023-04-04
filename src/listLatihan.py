import sqlite3
from PyQt6.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt6.QtCore import Qt, QSize
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPixmap, QIcon, QPalette, QFont, QCursor
import sys

background = '#5A8D6C'
button_color = '#174728'
text_color = '#EEEEE2'
card_color = '#D2DCC4'

class listLatihan(QMainWindow):

    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('fitu.db')
        self.listLat = self.fetchListLatihan()
        self.setUpListLatihanWindow()
        self.initUI()
        
    def fetchListLatihan(self):
        cur = self.con.cursor()
        rows = cur.execute("SELECT * FROM daftar_latihan")
        rows = cur.fetchall()
        cur.close()
        
        return rows

    def setUpListLatihanWindow(self):
        self.resize(1280,720)
        self.setWindowIcon(QIcon("../img/logo.png"))
        self.setWindowTitle("Fit-U - Daftar Latihan")
        self.setStyleSheet('background-color: #5A8D6C;')
        
    def initUI(self):
        
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        stylesheet1 = (
            'background-color: #5A8D6C;'
        )
        stylesheet2 = (
            'background-color: #D2DCC4;'
            'border-top-left-radius: 20px;'
            'border-top-right-radius: 20px;'
        )
        stylesheet3 = (
            'background-color: #D2DCC4;'
            'border-bottom-left-radius: 20px;'
            'border-bottom-right-radius: 20px;'
            'padding-left: 10px;'
            'padding-right: 10px;'
            'padding-top: 5px;'
        )
        header = QLabel()
        header.setFixedSize(10,5)
        header.setStyleSheet(stylesheet1)
        self.vbox.addWidget(header)      

        logo = QLabel(self)
        logo.setPixmap(QPixmap('../img/logo-dashboard.png'))
        logo.move(60, 45)
        
        helloFont = QFont()
        helloFont.setFamily('Segoe UI')
        helloFont.setPointSize(47)

        quoteFont = QFont()
        quoteFont.setFamily('Segoe UI')
        quoteFont.setPointSize(25)

        buttonFont = QFont()
        buttonFont.setFamily('Segoe UI')
        buttonFont.setPointSize(18)

        dateFont = QFont()
        dateFont.setFamily('Segoe UI')
        dateFont.setPointSize(23)

        historyFont = QFont()
        historyFont.setFamily('Segoe UI')
        historyFont.setPointSize(16)
        
        # tombol home
        homeButton = QPushButton()
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
        homeButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        
        # tombol customize
        customizeButton = QPushButton()
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
        customizeButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        
        # tombol plan
        planButton = QPushButton()
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
        planButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))

        # tombol list
        listButton = QPushButton()
        listButton.setText('List')
        listButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            border: none;
            border-radius: 20px;
        }}
        ''')
        listButton.setFont(buttonFont)
        listButton.setFixedSize(96, 42)
        listButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        
        # tombol history
        historyButton = QPushButton()
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
        historyButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        
        # foto profil
        profilePhoto = QLabel()
        profilePhoto.setPixmap(QPixmap('../img/profile-dashboard.png'))

        
        kotakKecil = QLabel()
        kotakKecil.setFixedSize(5,5)
        kotakKecil2 = QLabel()
        kotakKecil2.setFixedSize(10,10)
        kotakKecil3 = QLabel()
        kotakKecil3.setFixedSize(30,30)
        kotakKecil4 = QLabel()
        kotakKecil4.setFixedSize(50,50)
        kotakKecil5 = QLabel()
        kotakKecil5.setFixedSize(3,3)
        
        # self.vbox.addWidget(kotakKecil)
        # self.vbox.addWidget(kotakKecil)
        # self.vbox.addWidget(kotakKecil)
        # self.vbox.addWidget(kotakKecil)
        # self.vbox.addWidget(kotakKecil)
        # self.vbox.addWidget(kotakKecil5)
        
        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setContentsMargins(0,50,63,0)
        hbox.addWidget(logo)
        hbox.addWidget(kotakKecil4)
        hbox.addWidget(kotakKecil4)
        hbox.addWidget(kotakKecil4)
        hbox.addWidget(kotakKecil4)
        hbox.addWidget(kotakKecil4)
        hbox.addWidget(kotakKecil4)
        hbox.addWidget(kotakKecil2)
        hbox.addWidget(kotakKecil5)
        hbox.addWidget(homeButton)
        hbox.addWidget(kotakKecil)
        hbox.addWidget(kotakKecil4)
        hbox.addWidget(customizeButton)
        hbox.addWidget(kotakKecil3)
        hbox.addWidget(kotakKecil2)
        hbox.addWidget(kotakKecil)
        hbox.addWidget(planButton)
        hbox.addWidget(kotakKecil)
        hbox.addWidget(listButton)
        hbox.addWidget(kotakKecil2)
        hbox.addWidget(kotakKecil5)
        hbox.addWidget(historyButton)
        hbox.addWidget(kotakKecil4)
        hbox.addWidget(kotakKecil2)
        hbox.addWidget(kotakKecil2)
        hbox.addWidget(kotakKecil5)
        hbox.addWidget(kotakKecil)
        hbox.addWidget(profilePhoto)
        # hbox.addWidget(kotakKecil4)
        # hbox.addWidget(kotakKecil2)
        # hbox.addWidget(kotakKecil5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        
        self.vbox.addLayout(hbox)
        self.vbox.addWidget(kotakKecil)
        self.vbox.addWidget(kotakKecil)
        self.vbox.addWidget(kotakKecil)
        self.vbox.addWidget(kotakKecil)
        self.vbox.addWidget(kotakKecil)
        
        kotakKecil.setFixedSize(10,10)
        
        

        pixmap1 = QPixmap("../img/push-up.gif")
        card1 = QLabel()
        card1.setFixedSize(266, 100)
        card1.setStyleSheet(stylesheet2)
        card1.setPixmap(pixmap1.scaled(100,100))
        card1.setWordWrap(True)
        card1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[0][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[0][4]} Repetisi</font></p><b> <b><p><font color="aqua">{self.listLat[0][2]}</font></p></b>'
        card101 = QLabel()
        card101.setFixedSize(266, 168)
        card101.setStyleSheet(stylesheet3)
        card101.setText(text)
        card101.setWordWrap(True)
        card101.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[1][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[1][4]} Repetisi</font></p><b> <b><p><font color="aqua">{self.listLat[1][2]}</font></p></b>'
        card2 = QLabel()
        card2.setFixedSize(266, 100)
        card2.setStyleSheet(stylesheet2)
        card2.setPixmap(pixmap1.scaled(100,100))
        card2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card102 = QLabel()
        card102.setFixedSize(266, 168)
        card102.setStyleSheet(stylesheet3)
        card102.setText(text)
        card102.setWordWrap(True)
        card102.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[2][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[2][4]} Repetisi</font></p><b> <b><p><font color="aqua">{self.listLat[2][2]}</font></p></b>'
        card3 = QLabel()
        card3.setFixedSize(266, 100)
        card3.setStyleSheet(stylesheet2)
        card3.setPixmap(pixmap1.scaled(100,100))
        card3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card103 = QLabel()
        card103.setFixedSize(266, 168)
        card103.setStyleSheet(stylesheet3)
        card103.setText(text)  
        card103.setWordWrap(True)  
        card103.setAlignment(Qt.AlignmentFlag.AlignJustify)    
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[3][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[3][4]} Repetisi</font></p><b> <b><p><font color="aqua">{self.listLat[3][2]}</font></p></b>'
        card4 = QLabel()
        card4.setFixedSize(266, 100)
        card4.setStyleSheet(stylesheet2)
        card4.setPixmap(pixmap1.scaled(100,100))
        card4.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card104 = QLabel()
        card104.setFixedSize(266, 168)
        card104.setStyleSheet(stylesheet3)
        card104.setText(text)
        card104.setWordWrap(True)   
        card104.setAlignment(Qt.AlignmentFlag.AlignJustify)   

        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[4][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[4][4]} Repetisi</font></p><b> <b><p><font color="aqua">{self.listLat[4][2]}</font></p></b>'
        card5 = QLabel()
        card5.setFixedSize(266, 100)
        card5.setStyleSheet(stylesheet2)
        card5.setPixmap(pixmap1.scaled(100,100))
        card5.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card105 = QLabel()
        card105.setFixedSize(266, 168)
        card105.setStyleSheet(stylesheet3)
        card105.setText(text)
        card105.setWordWrap(True)
        card105.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[5][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[5][4]} Repetisi</font></p><b> <b><p><font color="aqua">{self.listLat[5][2]}</font></p></b>'
        card6 = QLabel()
        card6.setFixedSize(266, 100)
        card6.setStyleSheet(stylesheet2)
        card6.setPixmap(pixmap1.scaled(100,100))
        card6.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card106 = QLabel()
        card106.setFixedSize(266, 168)
        card106.setStyleSheet(stylesheet3)
        card106.setText(text)
        card106.setWordWrap(True)
        card106.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[6][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[6][4]} Repetisi</font></p><b> <b><p><font color="aqua">{self.listLat[6][2]}</font></p></b>'
        card7 = QLabel()
        card7.setFixedSize(266, 100)
        card7.setStyleSheet(stylesheet2)
        card7.setPixmap(pixmap1.scaled(100,100))
        card7.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card107 = QLabel()
        card107.setFixedSize(266, 168)
        card107.setStyleSheet(stylesheet3)
        card107.setText(text)
        card107.setWordWrap(True)
        card107.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[7][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[7][4]} Repetisi</font></p><b> <b><p><font color="aqua">{self.listLat[7][2]}</font></p></b>'
        card8 = QLabel()
        card8.setFixedSize(266, 100)
        card8.setStyleSheet(stylesheet2)
        card8.setPixmap(pixmap1.scaled(100,100))
        card8.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card108 = QLabel()
        card108.setFixedSize(266, 168)
        card108.setStyleSheet(stylesheet3)
        card108.setText(text)
        card108.setWordWrap(True)
        card108.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[8][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[8][5]} Detik</font></p><b> <b><p><font color="aqua">{self.listLat[8][2]}</font></p></b>'
        card9 = QLabel()
        card9.setFixedSize(266, 100)
        card9.setStyleSheet(stylesheet2)
        card9.setPixmap(pixmap1.scaled(100,100))
        card9.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card109 = QLabel()
        card109.setFixedSize(266, 168)
        card109.setStyleSheet(stylesheet3)
        card109.setText(text)
        card109.setWordWrap(True)
        card109.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[9][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[9][5]} Detik</font></p><b> <b><p><font color="aqua">{self.listLat[9][2]}</font></p></b>'
        card10 = QLabel()
        card10.setFixedSize(266, 100)
        card10.setStyleSheet(stylesheet2)
        card10.setPixmap(pixmap1.scaled(100,100))
        card10.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card110 = QLabel()
        card110.setFixedSize(266, 168)
        card110.setStyleSheet(stylesheet3)
        card110.setText(text)
        card110.setWordWrap(True)
        card110.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[10][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[10][5]} Detik</font></p><b> <b><p><font color="aqua">{self.listLat[10][2]}</font></p></b>'
        card11 = QLabel()
        card11.setFixedSize(266, 100)
        card11.setStyleSheet(stylesheet2)
        card11.setPixmap(pixmap1.scaled(100,100))
        card11.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card111 = QLabel()
        card111.setFixedSize(266, 168)
        card111.setStyleSheet(stylesheet3)
        card111.setText(text)
        card111.setWordWrap(True)
        card111.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[11][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[11][5]} Detik</font></p><b> <b><p><font color="aqua">{self.listLat[11][2]}</font></p></b>'
        card12 = QLabel()
        card12.setFixedSize(266, 100)
        card12.setStyleSheet(stylesheet2)
        card12.setPixmap(pixmap1.scaled(100,100))
        card12.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card112 = QLabel()
        card112.setFixedSize(266, 168)
        card112.setStyleSheet(stylesheet3)
        card112.setText(text)
        card112.setWordWrap(True)
        card112.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[12][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[12][5]} Detik</font></p><b> <b><p><font color="aqua">{self.listLat[12][2]}</font></p></b>'
        card13 = QLabel()
        card13.setFixedSize(266, 100)
        card13.setStyleSheet(stylesheet2)
        card13.setPixmap(pixmap1.scaled(100,100))
        card13.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card113 = QLabel()
        card113.setFixedSize(266, 168)
        card113.setStyleSheet(stylesheet3)
        card113.setText(text)
        card113.setWordWrap(True)
        card113.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[13][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[13][5]} Detik</font></p><b> <b><p><font color="aqua">{self.listLat[13][2]}</font></p></b>'
        card14 = QLabel()
        card14.setFixedSize(266, 100)
        card14.setStyleSheet(stylesheet2)
        card14.setPixmap(pixmap1.scaled(100,100))
        card14.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card114 = QLabel()
        card114.setFixedSize(266, 168)
        card114.setStyleSheet(stylesheet3)
        card114.setText(text)
        card114.setWordWrap(True)
        card114.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[14][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[14][5]} Detik</font></p><b> <b><p><font color="aqua">{self.listLat[14][2]}</font></p></b>'
        card15 = QLabel()
        card15.setFixedSize(266, 100)
        card15.setStyleSheet(stylesheet2)
        card15.setPixmap(pixmap1.scaled(100,100))
        card15.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card115 = QLabel()
        card115.setFixedSize(266, 168)
        card115.setStyleSheet(stylesheet3)
        card115.setText(text)
        card115.setWordWrap(True)
        card115.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        text = f'<b><p><font style="font-size:24px;" color="purple">{self.listLat[15][1]}</font><tab></p></b> <b><p><font color="red" style="font-size:14px;">{self.listLat[15][5]} Detik</font></p><b> <b><p><font color="aqua">{self.listLat[15][2]}</font></p></b>'
        card16 = QLabel()
        card16.setFixedSize(266, 100)
        card16.setStyleSheet(stylesheet2)
        card16.setPixmap(pixmap1.scaled(100,100))
        card16.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card116 = QLabel()
        card116.setFixedSize(266, 168)
        card116.setStyleSheet(stylesheet3)
        card116.setText(text)
        card116.setWordWrap(True)
        card116.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        
        self.vbox.setSpacing(0)
        self.vbox.setContentsMargins(0, 0,0,0)
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(card1)
        hbox1.addWidget(card2)
        hbox1.addWidget(card3)
        hbox1.addWidget(card4)
        hbox1.setSpacing(1)
        self.vbox.addLayout(hbox1)
        hbox11 = QHBoxLayout()
        hbox11.addWidget(card101)
        hbox11.addWidget(card102)
        hbox11.addWidget(card103)
        hbox11.addWidget(card104)
        hbox11.setSpacing(1)
        self.vbox.addLayout(hbox11)
        self.vbox.addWidget(kotakKecil)
        self.vbox.addWidget(kotakKecil)
        
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(card5)
        hbox2.addWidget(card6)
        hbox2.addWidget(card7)
        hbox2.addWidget(card8)
        hbox2.setSpacing(1)
        self.vbox.addLayout(hbox2)
        hbox12 = QHBoxLayout()
        hbox12.addWidget(card105)
        hbox12.addWidget(card106)
        hbox12.addWidget(card107)
        hbox12.addWidget(card108)
        hbox12.setSpacing(1)
        self.vbox.addLayout(hbox12)
        self.vbox.addWidget(kotakKecil)
        self.vbox.addWidget(kotakKecil)
        
        
        hbox3 = QHBoxLayout()
        hbox3.addWidget(card9)
        hbox3.addWidget(card10)
        hbox3.addWidget(card11)
        hbox3.addWidget(card12)
        hbox3.setSpacing(1)
        self.vbox.addLayout(hbox3)
        hbox13 = QHBoxLayout()
        hbox13.addWidget(card109)
        hbox13.addWidget(card110)
        hbox13.addWidget(card111)
        hbox13.addWidget(card112)
        hbox13.setSpacing(1)
        self.vbox.addLayout(hbox13)
        self.vbox.addWidget(kotakKecil)
        self.vbox.addWidget(kotakKecil)
        
        
        hbox4 = QHBoxLayout()
        hbox4.addWidget(card13)
        hbox4.addWidget(card14)
        hbox4.addWidget(card15)
        hbox4.addWidget(card16)
        hbox4.setSpacing(1)
        self.vbox.addLayout(hbox4)
        hbox14 = QHBoxLayout()
        hbox14.addWidget(card113)
        hbox14.addWidget(card114)
        hbox14.addWidget(card115)
        hbox14.addWidget(card116)
        hbox14.setSpacing(1)
        self.vbox.addLayout(hbox14)
        self.vbox.addWidget(kotakKecil)
        self.vbox.addWidget(kotakKecil)

        
        
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.show()

        return


if(__name__ == "__main__"):
    app = QtWidgets.QApplication(sys.argv)
    window = listLatihan()
    sys.exit(app.exec())