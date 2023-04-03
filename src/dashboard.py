import sys

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor, QFont, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget


background = '#5A8D6C'
button_color = '#174728'
text_color = '#EEEEE2'
card_color = '#D2DCC4'

class dashboard(QWidget):

    def __init__(self, user=None):
        super().__init__()
        if (user == None):
            self.user = {
                'name': 'krisi',
                'height': 170,
                'weight': 65,
                'gender': 'Perempuan',
                'age': 20,
                'goal': 'I want to have a sixpack stomach'
            }
        else:
            self.user = user
        self.dashboardWindow()
    
    def dashboardWindow(self):
        self.setWindowTitle('Dashboard - FitU')
        self.setFixedSize(1280, 720)
        self.setStyleSheet(f'background-color: {background};')
        self.element()

    def element(self):
        # kumpulan font
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

        # say Hello
        self.hello = QLabel(self)
        self.hello.setText(f"Hello, {self.user['name']}!")
        self.hello.move(101, 236)
        self.hello.setFont(helloFont)
        self.hello.setStyleSheet(f'color: {text_color};')
        self.hello.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # quote
        quote = QLabel(self)
        quote.setText("Saran quote dong maz\nbingung mau naro quote apa nih")
        quote.setStyleSheet(f'color: {text_color};')
        quote.move(101, 320)
        quote.setFont(quoteFont)
        quote.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # tombol start
        start = QPushButton(self)
        start.setText("Let's Start!")
        start.setStyleSheet(f'''
        QPushButton {{
            color: {text_color};
            background-color: {button_color};
            border: none;
            border-radius: 20px;
        }}
        ''') 
        start.setFont(buttonFont)
        start.setFixedSize(233, 47) #pake ini buat kalau dia buletan
        start.move(101, 511)    
        start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # membuat history card
        card = QLabel(self)
        card.setPixmap(QPixmap('img/card-dashboard.png'))
        card.move(633, 172) 

        kiri = QPushButton(self)
        kiri.setText('<')
        kiri.setStyleSheet(f'''
        QPushButton {{
            color: {button_color};
            background-color: {card_color};
            border: none;
            border-radius: 20px;
        }}
        ''')
        kiri.setFont(dateFont)
        kiri.move(727, 195)
        kiri.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        date = QLabel(self)
        date.setText("Date :")
        date.setStyleSheet(f'color: {button_color}; background-color: {card_color};')
        date.move(793, 195)
        date.setFont(dateFont)
        date.setAlignment(Qt.AlignmentFlag.AlignLeft)

        kanan = QPushButton(self)
        kanan.setText('>')
        kanan.setStyleSheet(f'''
        QPushButton {{
            color: {button_color};
            background-color: {card_color};
            border: none;
            border-radius: 20px;
        }}
        ''')
        kanan.setFont(dateFont)
        kanan.move(1047, 195)
        kanan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        duration = QLabel(self)
        duration.setText("Duration :")
        duration.setStyleSheet(f'color: {button_color}; background-color: {card_color};')
        duration.move(667,282)
        duration.setFont(historyFont)
        duration.setAlignment(Qt.AlignmentFlag.AlignLeft)

        prog = QLabel(self)
        prog.setText("Program Name: ")
        prog.setStyleSheet(f'color: {button_color}; background-color: {card_color};')
        prog.move(667, 317)
        prog.setFont(historyFont)
        prog.setAlignment(Qt.AlignmentFlag.AlignLeft)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = dashboard()
    window.show()
    sys.exit(app.exec())
    