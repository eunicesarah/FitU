import sqlite3
from PyQt6.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt6.QtCore import Qt, QSize
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPixmap, QIcon, QPalette
import sys


class listLatihan(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setBackgroundRole(QPalette.ColorRole.Dark)
        self.resize(1280,720)
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("Fit-U - Daftar Latihan")
        self.setStyleSheet('background-color: #5A8D6C;')
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        stylesheet1 = (
            'background-color: #5A8D6C;'
        )
        stylesheet2 = (
            'background-color: #D2DCC4;'
            'border-radius: 20px;'
        )
        pixmap1 = QPixmap('logo.png')
        card1 = QLabel()
        card1.setFixedSize(266, 266)
        card1.setStyleSheet(stylesheet2)
        card1.setPixmap(pixmap1.scaled(100,100))
        card1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card2 = QLabel()
        card2.setFixedSize(266, 266)
        card2.setStyleSheet(stylesheet2)
        card2.setPixmap(pixmap1.scaled(100,100))
        card2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card3 = QLabel()
        card3.setFixedSize(266, 266)
        card3.setStyleSheet(stylesheet2)
        card3.setPixmap(pixmap1.scaled(100,100))
        card3.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card4 = QLabel()
        card4.setFixedSize(266, 266)
        card4.setStyleSheet(stylesheet2)
        card4.setPixmap(pixmap1.scaled(100,100))
        card4.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card5 = QLabel()
        card5.setFixedSize(266, 266)
        card5.setStyleSheet(stylesheet2)
        card5.setPixmap(pixmap1.scaled(100,100))
        card5.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card6 = QLabel()
        card6.setFixedSize(266, 266)
        card6.setStyleSheet(stylesheet2)
        card6.setPixmap(pixmap1.scaled(100,100))
        card6.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card7 = QLabel()
        card7.setFixedSize(266, 266)
        card7.setStyleSheet(stylesheet2)
        card7.setPixmap(pixmap1.scaled(100,100))
        card7.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card8 = QLabel()
        card8.setFixedSize(266, 266)
        card8.setStyleSheet(stylesheet2)
        card8.setPixmap(pixmap1.scaled(100,100))
        card8.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card9 = QLabel()
        card9.setFixedSize(266, 266)
        card9.setStyleSheet(stylesheet2)
        card9.setPixmap(pixmap1.scaled(100,100))
        card9.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card10 = QLabel()
        card10.setFixedSize(266, 266)
        card10.setStyleSheet(stylesheet2)
        card10.setPixmap(pixmap1.scaled(100,100))
        card10.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card11 = QLabel()
        card11.setFixedSize(266, 266)
        card11.setStyleSheet(stylesheet2)
        card11.setPixmap(pixmap1.scaled(100,100))
        card11.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card12 = QLabel()
        card12.setFixedSize(266, 266)
        card12.setStyleSheet(stylesheet2)
        card12.setPixmap(pixmap1.scaled(100,100))
        card12.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card13 = QLabel()
        card13.setFixedSize(266, 266)
        card13.setStyleSheet(stylesheet2)
        card13.setPixmap(pixmap1.scaled(100,100))
        card13.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card14 = QLabel()
        card14.setFixedSize(266, 266)
        card14.setStyleSheet(stylesheet2)
        card14.setPixmap(pixmap1.scaled(100,100))
        card14.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card15 = QLabel()
        card15.setFixedSize(266, 266)
        card15.setStyleSheet(stylesheet2)
        card15.setPixmap(pixmap1.scaled(100,100))
        card15.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        card16 = QLabel()
        card16.setFixedSize(266, 266)
        card16.setStyleSheet(stylesheet2)
        card16.setPixmap(pixmap1.scaled(100,100))
        card16.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        # padding1 = QLabel()
        # padding1.setFixedSize(100000,10)
        self.vbox.setSpacing(75)
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(card1)
        hbox1.addWidget(card2)
        hbox1.addWidget(card3)
        hbox1.addWidget(card4)
        hbox1.setSpacing(1)
        self.vbox.addLayout(hbox1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(card5)
        hbox2.addWidget(card6)
        hbox2.addWidget(card7)
        hbox2.addWidget(card8)
        hbox2.setSpacing(1)
        self.vbox.addLayout(hbox2)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(card9)
        hbox3.addWidget(card10)
        hbox3.addWidget(card11)
        hbox3.addWidget(card12)
        hbox3.setSpacing(1)
        self.vbox.addLayout(hbox3)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(card13)
        hbox4.addWidget(card14)
        hbox4.addWidget(card15)
        hbox4.addWidget(card16)
        hbox4.setSpacing(1)
        self.vbox.addLayout(hbox4)

        
        
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.show()

        return

        
# con = sqlite3.connect("fitu.db")
# cur = con.cursor()
# daftarLatihan = cur.execute("SELECT * FROM daftar_latihan")

if(__name__ == "__main__"):
    app = QtWidgets.QApplication(sys.argv)
    window = listLatihan()
    sys.exit(app.exec())