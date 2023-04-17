import sqlite3
import sys

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QCursor, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea

BACKGROUNDCOLOR = '#5A8D6C'
BUTTONCOLOR = '#174728'
TEXTCOLOR = '#EEEEE2'
CARDCOLOR = '#D2DCC4'

class plan(QWidget):
    switch = pyqtSignal(str, int, dict )
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('fitu.db')
        self.programExercises = self.fetchProgramExercises()
        self.planWindow()

    def fetchProgramExercises(self):
        c = self.con.cursor()
        c.execute("SELECT * FROM program")
        data = c.fetchall()
        c.close()
        return data

    def planWindow(self):
        self.label = QLabel("")
        self.label.setParent(self)
        self.setWindowTitle('FitU')
        self.setFixedSize(1280, 720)
        self.setStyleSheet(f'background-color: {BACKGROUNDCOLOR};')
        self.elements()

    def elements(self):
        buttonFont = QFont()
        buttonFont.setFamily('Segoe UI')
        buttonFont.setPointSize(18)
        buttonFont.setBold(True)

        # Style sheets
        styleSheetNavbar0 = (f'''
            QPushButton {{
                color: {TEXTCOLOR};
                background-color: {BACKGROUNDCOLOR};
                border: none;
                border-radius: 20px;
            }}
            QPushButton:hover {{
                color: {BUTTONCOLOR};
            }}
        ''')

        styleSheetNavbar1 = (f'''
            QPushButton {{
                color: {TEXTCOLOR};
                background-color: {BUTTONCOLOR};
                border: none;
                border-radius: 20px;
            }}
        ''')

        styleSheetSmallCard = (
            '''
            QPushButton {
                background-color:  #5A8D6C;
                border: 1.2px solid rgba(255, 255, 255, 0.8);
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #174728;
                border: 1.2px solid rgba(255, 255, 255, 0.8);
            }
            '''
        )

        styleSheetBigCard = (
            "background-color: #D2DCC4;"
            "border-radius: 20px;"
        )

        styleSheet = (
            "color: #5A8D6C;"
            "background-color: #D2DCC4;"
            "border-radius: 20px;"
        )
        styleSheetStart = (
        f'''
            QPushButton {{
                color: {TEXTCOLOR};
                background-color: {BACKGROUNDCOLOR};
                border: 1.2px solid rgba(255, 255, 255, 0.8);
                border-radius: 20px;
            }}
            QPushButton:hover {{
                background-color: {BUTTONCOLOR};
            }}
        ''')
        
        styleSheetCutomize = (f'''
            QPushButton {{
            background-color: {CARDCOLOR};
            color: {BUTTONCOLOR};
            border: none;
            border-radius: 20px;
            text-decoration: underline;
            }}
            QPushButton:hover {{
            background-color: {CARDCOLOR};
            color: {BACKGROUNDCOLOR};
            }}
        ''')

        verticallScrollBarStyle = (""" 
            QScrollBar:vertical {
                background-color: white;
                width: 8px;
                margin: 20px 0 20px 0;
            }
            QScrollBar::handle:vertical {
                background-color: #174728;
                border-radius: 3px;
                
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
        """)

        horizontalScrollBarStyle = ("""
            QScrollBar:horizontal {
                background-color: white;
                height: 8px;
                margin: 0 20px 0 20px;
            }
            QScrollBar::handle:horizontal {
                background-color: #174728;
                border-radius: 3px;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 20px;
                background-color: #D2DCC4;
                subcontrol-origin: margin;
                subcontrol-position: left;
            }
            QScrollBar::add-line:horizontal {
                left: 0;
            }
            QScrollBar::sub-line:horizontal {
                right: 0;
            }
        """)

        # Navbar
        # Navbar FitU logo
        logo = QLabel(self)
        logo.setPixmap(QPixmap('img/logo-dashboard.png'))
        logo.move(60, 45)

        # Home Button
        homeButton = QPushButton(self)
        homeButton.setText('Home')
        homeButton.setStyleSheet(styleSheetNavbar0)
        homeButton.setFont(buttonFont)
        homeButton.setFixedSize(96, 42)
        homeButton.move(507, 53)    
        homeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        homeButton.clicked.connect(self.dashboardWindow)

        # Customize Button
        customizeButton = QPushButton(self)
        customizeButton.setText('Customize')
        customizeButton.setStyleSheet(styleSheetNavbar0)
        customizeButton.setFont(buttonFont)
        customizeButton.move(649, 58)
        customizeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        customizeButton.clicked.connect(self.customWindow)
        
        # Plan Button
        planButton = QPushButton(self)
        planButton.setText('Plan')
        planButton.setStyleSheet(styleSheetNavbar1)
        planButton.setFont(buttonFont)
        planButton.setFixedSize(80, 42)
        planButton.move(784, 58)

        # List Button
        listButton = QPushButton(self)
        listButton.setText('List')
        listButton.setStyleSheet(styleSheetNavbar0)
        listButton.setFont(buttonFont)
        listButton.move(898, 58)
        listButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        listButton.clicked.connect(self.listWindow)

        # History Button
        historyButton = QPushButton(self)
        historyButton.setText('History')
        historyButton.setStyleSheet(styleSheetNavbar0)
        historyButton.setFont(buttonFont)
        historyButton.move(979, 58)
        historyButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))   

        # Profile Picture
        profilePicture = QLabel(self)
        profilePicture.setPixmap(QPixmap('img/profile-dashboard.png'))
        profilePicture.move(1133, 45)

        # Create Card
        # Right Side
        rightCard = QLabel(self)
        rightCard.move(116, 155)
        rightCard.setFixedSize(430, 534)
        rightCard.setStyleSheet(styleSheetBigCard)

        # Right Scroll Area (Vertical)
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setGeometry(130, 250, 410, 429) 
        scroll.setStyleSheet("background-color: #D2DCC4;border-radius: none;")
        scrollWidget = QWidget(scroll)
        scrollLayout = QVBoxLayout(scrollWidget)
        scrollWidget.setStyleSheet("background-color: #D2DCC4; border-radius: 20px;")
        scrollWidget.setLayout(scrollLayout)

        scroll.verticalScrollBar().setStyleSheet(verticallScrollBarStyle)

        # Fetch data from database
        data = self.programExercises
        row = len(data)


        for i in range(row):
            exButton = QPushButton(self)
            exButton.setStyleSheet(styleSheetSmallCard)
            exButton.setFixedSize(366, 99)
            exButton.setFont(buttonFont)
            exButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            exButton.clicked.connect(lambda state, index=i: showExercise(index))
            title = QLabel(exButton)
            title.setText(f'<font style="font-size:24px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{data[i][1]}<b>')
            title.move(20, 15)
            title.setStyleSheet("background-color: transparent;")

            con = sqlite3.connect('fitu.db')
            c = con.cursor()
            c.execute("SELECT title FROM latihan_program, daftar_latihan WHERE latihan_program.exercise_id = daftar_latihan.exercise_id AND latihan_program.program_id = ?", (data[i][0],))
            self.data2 = c.fetchall()
            # c.commit()
            c.close()

            predict = len(self.data2)
            dur = QLabel(exButton)
            dur.setText(f'<font style="font-size:18px;" color="#D2DCC4"; font-family="Sogoe UI";>{predict} Minutes')
            dur.move(20, 50)
            dur.setStyleSheet("background-color: transparent;")
            scrollLayout.addWidget(exButton)  
        scroll.setWidget(scrollWidget)
        
        # Left Side
        leftCard = QLabel(self)
        leftCard.move(577, 155)
        leftCard.setFixedSize(604, 534)
        leftCard.setStyleSheet(styleSheetBigCard)

        scroll2 = QScrollArea(self)
        scroll2.setWidgetResizable(True)
        scroll2.setGeometry(610, 230, 545, 350) # mengatur posisi dan ukuran QScrollArea
        scroll2.setStyleSheet("background-color: #D2DCC4;border-radius: none;")
        scrollWidget2 = QWidget(scroll2)
        scrollLayout2 = QHBoxLayout(scrollWidget2)
        scrollWidget2.setStyleSheet("background-color: #D2DCC4; border-radius: 20px;")
        scrollWidget2.setLayout(scrollLayout2)

        scroll2.horizontalScrollBar().setStyleSheet(horizontalScrollBarStyle)
        # create a list to store the exercise data
        exercise_data = []

        # create a function to show exercise data based on index
        def showExercise(index):
            self.clickedRowData = data[index][0]
            con = sqlite3.connect('fitu.db')
            c = con.cursor()
            c.execute("SELECT title, repetition, duration, gif FROM latihan_program, daftar_latihan WHERE latihan_program.exercise_id = daftar_latihan.exercise_id AND latihan_program.program_id = ?", (self.clickedRowData,))
            self.data3 = c.fetchall()
            # print("clicked:" + str(clickedRowData))
            c.close()

            # clear the exercise data list
            exercise_data.clear()

            # append new exercise data to the list
            for i in range(len(self.data3)):
                exercise_data.append(self.data3[i])

            # remove all widgets from scrollLayout2
            for i in reversed(range(scrollLayout2.count())):
                scrollLayout2.itemAt(i).widget().setParent(None)

            # create QLabel widgets for each exercise and add them to scrollLayout2
            for i in range(len(exercise_data)):
                exLabel = QLabel(self)
                exLabel.setFixedSize(202, 270)
                exLabel.setStyleSheet("background-color: #5A8D6C; border-radius: 20px;")
                title = QLabel(exLabel)
                title.setText(f'<font style="font-size:22px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{exercise_data[i][0]}<b>')
                title.move(20, 15)
                repDur = QLabel(exLabel)
                if exercise_data[i][1] == None:
                    repDur.setText(f'<font style="font-size:18px;" color="#D2DCC4"; font-family="Sogoe UI";>{exercise_data[i][2]} Seconds')
                else:
                    repDur.setText(f'<font style="font-size:18px;" color="#D2DCC4"; font-family="Sogoe UI";>{exercise_data[i][1]} Repetitions')
                repDur.move(20, 50)
                exPix = QPixmap(exercise_data[i][3])
                image = QLabel(exLabel)
                image.setPixmap(exPix)
                image.setScaledContents(True)
                image.move(20, 80)
                image.setFixedSize(160, 160)

                scrollLayout2.addWidget(exLabel)
            scroll2.setWidget(scrollWidget2)
            
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        
        #font save
        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(23)
        font1.setBold(True)
        
        exText = QLabel(self)
        exText.setText("Workout Plan")
        exText.setFont(font)
        exText.setStyleSheet(styleSheet)
        exText.setFixedSize(250, 50)
        exText.move(140,185)
        
        progText = QLabel(self)
        progText.setText("Exercise")
        progText.setStyleSheet(styleSheet)
        progText.setFixedSize(165, 50)
        progText.setFont(font)
        progText.move(599, 182)
        
        startButton = QPushButton(self)
        startButton.setFont(font)
        startButton.setText("START >")
        startButton.move(1004, 620)
        startButton.setFixedSize(144, 42)
        startButton.setStyleSheet(styleSheetStart)
        startButton.setFont(font1)
        startButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        startButton.clicked.connect(self.plan2Window)

        custButton = QPushButton(self)
        custButton.setFont(font)
        custButton.setText("Customize")
        custButton.move(825, 620)
        custButton.setStyleSheet(styleSheetCutomize)
        custButton.setFont(font1)
        custButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        custButton.clicked.connect(self.customWindow)
    
    def dashboardWindow(self):
        self.switch.emit("dashboard", {})
    
    def listWindow(self):
        self.switch.emit("listLatihan", {})
    
    def customWindow(self):
        self.switch.emit("customize", self.clickedRowData, {})
    
    def plan2Window(self):
        self.switch.emit("plan2", self.clickedRowData, {})

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = plan()
    ex.show()
    app.exec()
