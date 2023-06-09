import sqlite3
import sys

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QFont
from PyQt6.QtWidgets import (QApplication, QWidget, QMessageBox, QLabel, QLineEdit, QVBoxLayout, QPushButton, QScrollArea)

background = '#5A8D6C'
button_color = '#174728'
text_color = '#EEEEE2'
cardColor = '#D2DCC4'

class customizeWorkout(QWidget):
    switch = pyqtSignal(str, int, dict)

    def __init__(self, program_id):
        
        super().__init__()
        self.con = sqlite3.connect('fitu.db')
        self.listEx = self.fetchListEx()    
        self.program_id = program_id  
        self.setupGUI()
        
    def fetchListEx(self):
        cur = self.con.cursor()
        rows = cur.execute("SELECT * FROM daftar_latihan")
        rows = cur.fetchall()
        cur.close()   
        
        return rows
        
    def setupGUI(self):
    
        self.label = QLabel("")
        self.label.setParent(self)
        self.setFixedSize(1280, 720)
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setWindowTitle("FitU - Customize Workout")
        self.setStyleSheet("background-color: #5A8D6C;")
        self.elements()
    
    def exLabel(self):
        exLabel = QLabel()
           
        exLabel.setFixedSize(367, 99)
        exLabel.setStyleSheet("background-color: #5A8D6C; border-radius: 20px;")
        exLabel1 = QLabel(exLabel)
        exLabel1.move(10, 10)
        exLabel1.setFixedSize(79, 79)
        exLabel1.setStyleSheet(f'''
            border: none;
            "background-color: #D2DCC4;"
            "border-radius: 20px;"
        
        ''') 
    
    def elements(self): 
        buttonFont = QFont()
        buttonFont.setFamily('Segoe UI')
        buttonFont.setPointSize(18)
        buttonFont.setBold(True)
        
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
            f'''
        QPushButton {{
            color: {text_color};
            background-color: {background};
            border: none;
            border-radius: 20px;
        }}
        '''
        )
        
        styleSheet5 = (
            # "color: #D2DCC4;"
            "background-color: #D2DCC4;"
            "border-radius: 20px;"
        )
                # Mengatur bentuk scroll bar
        scroll_bar_style = """
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
        """
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
        QPushButton:hover {{
            color: {button_color};
        }}

        ''')
        homeButton.setFont(buttonFont)
        # homeButton.setFixedSize(96, 42) #pake ini buat kalau dia buletan
        homeButton.move(670, 58)    
        homeButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        homeButton.clicked.connect(self.dashboardWindow)
        
        # tombol customize
        customizeButton = QPushButton(self)
        customizeButton.setText('Customize')
        customizeButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            border: none;
            border-radius: 20px;
        }}
        ''')
        customizeButton.setFont(buttonFont)
        customizeButton.setFixedSize(140, 42)
        customizeButton.move(787, 53)   
        customizeButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        # customizeButton.clicked.connect(self.customizeWindow)
        
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
        QPushButton:hover {{
            color: {button_color};
        }}

        ''')
        planButton.setFont(buttonFont)
        planButton.move(956, 58)
        planButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        planButton.clicked.connect(self.planWindow)

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
        QPushButton:hover {{
            color: {button_color};
        }}

        ''')
        listButton.setFont(buttonFont)
        listButton.move(1047, 58)
        listButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        listButton.clicked.connect(self.listWindow)
        
        # foto profil
        profilePhoto = QLabel(self)
        profilePhoto.setPixmap(QPixmap('img/profile-dashboard.png'))
        profilePhoto.move(1133, 45)
         
        #greenCard
        greenCard = QLabel(self)
        greenCard.move(116, 155)
        greenCard.setFixedSize(430, 534)
        greenCard.setStyleSheet(styleSheet)
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setGeometry(130, 250, 410, 429) 
        scroll.setStyleSheet("background-color: #D2DCC4;border-radius: none;")
        scrollWidget = QWidget(scroll)
        scrollLayout = QVBoxLayout(scrollWidget)
        scrollWidget.setStyleSheet("background-color: #D2DCC4; border-radius: 20px;")
        scrollWidget.setLayout(scrollLayout)
        scroll.verticalScrollBar().setStyleSheet(scroll_bar_style)
        
        addButtonList = []
        count = 0
        for i in range(16):
            exLabel = QLabel(self)  
            exLabel.setFixedSize(367, 99)
            exLabel.setStyleSheet("background-color: #5A8D6C; border-radius: 20px;")
            exLabel1 = QLabel(exLabel)
            exLabel1.move(10, 10)
            exLabel1.setFixedSize(79, 79)
            exLabel1.setStyleSheet(styleSheet5)
            pic = QLabel(exLabel)
            pic.setPixmap(QPixmap(self.listEx[i][6]).scaled(79, 79))
            pic.move(10, 10)
            pic.setFixedSize(79, 79)
            pic.setStyleSheet(styleSheet5)
            addButton = QPushButton(exLabel)
            addButton.setIcon(QIcon('img/add button.png'))
            addButton.setIconSize(QPixmap('img/add button.png').size())
            addButton.setGeometry(320, 55, 36, 36)
            addButton.move(320, 55)
            addButton.setCursor(
                QCursor(Qt.CursorShape.PointingHandCursor))
            addButtonList.append(addButton)
            addButton.clicked.connect(lambda checked, index=i: handleButtonClicked(index, addButtonList))
            title = QLabel(exLabel)
            title.setText(f'<font style="font-size:24px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{self.listEx[count][1]}<b>')
            title.move(100, 15)
            repDur = QLabel(exLabel)
            if(count<8):
                repDur.setText(f'<font style="font-size:14px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{self.listEx[count][4]} Seconds<b>')
                repDur.move(100, 60)
            else:
                repDur.setText(f'<font style="font-size:14px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{self.listEx[count][5]} Repetition<b>')
                repDur.move(100,60)
            scrollLayout.addWidget(exLabel)

            addButton.setCursor(
                QCursor(Qt.CursorShape.PointingHandCursor))
            count+=1
        scroll.setWidget(scrollWidget)
        greenCard2 = QLabel(self)
        greenCard2.move(577, 155)
        greenCard2.setFixedSize(604, 534)
        greenCard2.setStyleSheet(styleSheet)
        scroll2 = QScrollArea(self)
        scroll2.setWidgetResizable(True)
        scroll2.setGeometry(620, 250, 410, 429)
        scroll2.setStyleSheet("background-color: #D2DCC4;border-radius: none;")
        scrollWidget2 = QWidget(scroll2)
        scrollLayout2 = QVBoxLayout(scrollWidget2)
        scrollWidget2.setStyleSheet("background-color: #D2DCC4; border-radius: 20px;")
        scrollWidget2.setLayout(scrollLayout2)
        scroll2.verticalScrollBar().setStyleSheet(scroll_bar_style)
        scroll2.setWidget(scrollWidget2)
        
        area2 = []
        if self.program_id != 0:
            cur = self.con.cursor()
            self.latihan = cur.execute(f"SELECT exercise_id FROM daftar_latihan NATURAL JOIN latihan_program WHERE program_id = {self.program_id}").fetchall()
            show = []
            for i in range(len(self.latihan)):
                temp = cur.execute(f"SELECT title, duration, repetition, gif FROM daftar_latihan WHERE exercise_id = {self.latihan[i][0]}").fetchall()
                show.append(temp[0])
            for i in range(len(self.latihan)):
                area2.append(self.latihan[i][0])
                exLabell = QLabel(self)
                exLabell.setFixedSize(367, 99)
                exLabell.setStyleSheet("background-color: #5A8D6C; border-radius: 20px;")
                exLabel1 = QLabel(exLabell)
                exLabel1.move(10, 10)
                exLabel1.setFixedSize(79, 79)
                exLabel1.setStyleSheet(styleSheet5)
                temp = self.latihan[i][0] - 200
                if temp>0:
                    temp+=7
                else:
                    temp+=99
                button = addButtonList[temp]
                button.setEnabled(False)
                button.setIcon(QIcon('img/check button.png'))    
                pic = QLabel(exLabell)
                pic.setPixmap(QPixmap(show[i][3]).scaled(79, 79))
                pic.move(10, 10)
                pic.setFixedSize(79, 79)
                pic.setStyleSheet(styleSheet5)
                
                title = QLabel(exLabell)
                title.setText(f'<font style="font-size:24px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{show[i][0]}<b>')
                title.move(100, 15)
                repDur = QLabel(exLabell)
                if(show[i][1] != None):
                        repDur.setText(f'<font style="font-size:14px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{show[i][1]} Seconds<b>')
                        repDur.move(100, 60)
                else:
                    repDur.setText(f'<font style="font-size:14px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{show[i][2]} Repetition<b>')
                    repDur.move(100,60)
                # deleteButtonn = QPushButton(exLabell)
                # deleteButtonn.setIcon(QIcon('img/delete button.png'))
                # deleteButtonn.setIconSize(QPixmap('img/delete button.png').size())
                # deleteButtonn.setGeometry(320, 55, 36, 36)
                # deleteButtonn.move(320, 55)
                # deleteButtonn.setCursor(
                #     QCursor(Qt.CursorShape.PointingHandCursor))
                # deleteButtonn.clicked.connect(lambda checked, index=i: handleDeleteButtonClickedd(index, exLabell, scrollLayout2))
                scrollLayout2.addWidget(exLabell)
                
        def handleButtonClicked(i, buttonList):
            area2.append(self.listEx[i][0])
            button = buttonList[i]
            button.setEnabled(False)
            button.setIcon(QIcon('img/check button.png'))
            button.setIconSize(QPixmap('img/check button.png').size())
            exLabel = QLabel(self)
            exLabel.setFixedSize(367, 99)
            exLabel.setStyleSheet("background-color: #5A8D6C; border-radius: 20px;")
            exLabel1 = QLabel(exLabel)
            exLabel1.move(10, 10)
            exLabel1.setFixedSize(79, 79)
            exLabel1.setStyleSheet(styleSheet5)
            pic = QLabel(exLabel)
            pic.setPixmap(QPixmap(self.listEx[i][6]).scaled(79, 79))
            pic.move(10, 10)
            pic.setFixedSize(79, 79)
            pic.setStyleSheet(styleSheet5)
            title = QLabel(exLabel)
            title.setText(f'<font style="font-size:24px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{self.listEx[i][1]}<b>')
            title.move(100, 15)
            repDur = QLabel(exLabel)
            if(i<8):
                    repDur.setText(f'<font style="font-size:14px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{self.listEx[i][4]} Seconds<b>')
                    repDur.move(100, 60)
            else:
                repDur.setText(f'<font style="font-size:14px;" color="#D2DCC4"; font-family="Sogoe UI";><b>{self.listEx[i][5]} Repetition<b>')
                repDur.move(100,60)
            deleteButton = QPushButton(exLabel)
            deleteButton.setIcon(QIcon('img/delete button.png'))
            deleteButton.setIconSize(QPixmap('img/delete button.png').size())
            deleteButton.setGeometry(320, 55, 36, 36)
            deleteButton.move(320, 55)
            deleteButton.setCursor(
                QCursor(Qt.CursorShape.PointingHandCursor))
            deleteButton.clicked.connect(lambda checked, index=i: handleDeleteButtonClicked(index, exLabel, scrollLayout2))
            scrollLayout2.addWidget(exLabel)
        
        # def handleDeleteButtonClickedd(index):
        #     # area2.remove(self.latihan[index][0])
        #     print(index)
        #     # exLabel = scrollLayout2.itemAt(index).widget()
        #     exLabel.setParent(None)
        #     scrollLayout2.removeWidget(exLabel)
        #     if exLabel is not None:
        #         exLabel.setParent(None)
            
            
        #     scrollLayout2.removeWidget(exLabel)
        #     # exLabel.deleteLater()

                             
        def handleDeleteButtonClicked(index, exLabel, layout):  
            area2.remove(self.listEx[index][0])
            exLabel.setParent(None)
            layout.removeWidget(exLabel)
            # exLabel.deleteLater()
            for i, button in enumerate(addButtonList):
                        if i == index:
                            button.setEnabled(True)
                            button.setIcon(QIcon('img/add button.png'))
                            button.setIconSize(QPixmap('img/add button.png').size())
                            
        def saveButtonClicked():
            if not progNameInput.text().strip():
                QMessageBox.about(self, "Error", "Please input program name")
            else:
                if(area2 == []):
                    QMessageBox.about(self, "Error", "Please add exercise")
                else:
                    QMessageBox.about(self, "Success", "Program saved")
                    cur = self.con.cursor()
                    data = cur.execute("SELECT program_id FROM program")
                    lenProg = len(data.fetchall())
                    cur.execute(
                        f"INSERT INTO program (program_id, title_program) VALUES ({lenProg+1} ,'{progNameInput.text()}')"
                        )
                    for i in area2:
                        cur.execute(
                            f"INSERT INTO latihan_program (program_id, exercise_id) VALUES ({lenProg+1} ,{i})"
                            )
                    self.con.commit()

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
        exText.setText("Exercise")
        exText.setFont(font)
        exText.setStyleSheet(styleSheet2)
        exText.setFixedSize(165, 35)
        exText.move(140,185)
        
        progText = QLabel(self)
        progText.setText("Program Name:")
        progText.setStyleSheet(styleSheet2)
        progText.setFixedSize(361, 50)
        progText.setFont(font1)
        progText.move(599, 182)
        
        progNameInput = QLineEdit(self)
        progNameInput.move(840, 184)
        progNameInput.setFixedSize(320, 50)
        progNameInput.setFont(QFont("Segoe UI", 14))
        progNameInput.setStyleSheet('''
            padding: 11px 30px 11px 30px;
            border: 1px solid rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            color: #D2DCC4;
            background-color: {background};
        ''')
  
        saveButton = QPushButton(self)
        saveButton.setText('Save')
        saveButton.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            border: none;
            border-radius: 20px;
        }}
        ''')
        saveButton.setFont(buttonFont)
        saveButton.setFixedSize(95, 42)
        saveButton.move(1065, 635)     
        saveButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))       
        saveButton.clicked.connect(saveButtonClicked)

    def planWindow(self):
        self.switch.emit("plan", 0, {})
    
    def listWindow(self):
        self.switch.emit("listLatihan", 0, {})
    
    def dashboardWindow(self):
        self.switch.emit("dashboard", 0, {})
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = customizeWorkout()
    ex.show()
    app.exec()