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
        card1 = QLabel()
        card1.setFixedSize(266, 266)
        card1.setStyleSheet(stylesheet2)
        card2 = QLabel()
        card2.setFixedSize(266, 266)
        card2.setStyleSheet(stylesheet2)
        card3 = QLabel()
        card3.setFixedSize(266, 266)
        card3.setStyleSheet(stylesheet2)
        card4 = QLabel()
        card4.setFixedSize(266, 266)
        card4.setStyleSheet(stylesheet2)
        card5 = QLabel()
        card5.setFixedSize(266, 266)
        card5.setStyleSheet(stylesheet2)
        card6 = QLabel()
        card6.setFixedSize(266, 266)
        card6.setStyleSheet(stylesheet2)
        card7 = QLabel()
        card7.setFixedSize(266, 266)
        card7.setStyleSheet(stylesheet2)
        card8 = QLabel()
        card8.setFixedSize(266, 266)
        card8.setStyleSheet(stylesheet2)
        card9 = QLabel()
        card9.setFixedSize(266, 266)
        card9.setStyleSheet(stylesheet2)
        card10 = QLabel()
        card10.setFixedSize(266, 266)
        card10.setStyleSheet(stylesheet2)
        card11 = QLabel()
        card11.setFixedSize(266, 266)
        card11.setStyleSheet(stylesheet2)
        card12 = QLabel()
        card12.setFixedSize(266, 266)
        card12.setStyleSheet(stylesheet2)
        card13 = QLabel()
        card13.setFixedSize(266, 266)
        card13.setStyleSheet(stylesheet2)
        card14 = QLabel()
        card14.setFixedSize(266, 266)
        card14.setStyleSheet(stylesheet2)
        card15 = QLabel()
        card15.setFixedSize(266, 266)
        card15.setStyleSheet(stylesheet2)
        card16 = QLabel()
        card16.setFixedSize(266, 266)
        card16.setStyleSheet(stylesheet2)
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(card1)
        hbox1.addWidget(card2)
        hbox1.addWidget(card3)
        self.vbox.addLayout(hbox1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(card4)
        hbox2.addWidget(card5)
        hbox2.addWidget(card6)
        self.vbox.addLayout(hbox2)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(card7)
        hbox3.addWidget(card8)
        hbox3.addWidget(card9)
        self.vbox.addLayout(hbox3)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(card10)
        hbox4.addWidget(card11)
        hbox4.addWidget(card12)
        self.vbox.addLayout(hbox4)
        hbox5 = QHBoxLayout()
        hbox5.addWidget(card13)
        hbox5.addWidget(card14)
        hbox5.addWidget(card15)
                

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.show()

        return

        
# con = sqlite3.connect("fitu.db")
# cur = con.cursor()
# daftarLatihan = cur.execute("SELECT * FROM daftar_latihan")

if(__name__ == "__main__"):
    app = QtWidgets.QApplication(sys.argv)
    window = listLatihan()
    sys.exit(app.exec())