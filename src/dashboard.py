import sys

from PyQt6.QtCore import Qt, pyqtSignal, QSize
from PyQt6.QtGui import QCursor, QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QScrollArea, QVBoxLayout, QHBoxLayout
import sqlite3

cur = sqlite3.connect("fitu.db").cursor()

background = '#5A8D6C'
button_color = '#174728'
text_color = '#EEEEE2'
card_color = '#D2DCC4'


# kumpulan font
helloFont = QFont()
helloFont.setFamily('Segoe UI')
helloFont.setPointSize(47)
# helloFont.setBold(True)

quoteFont = QFont()
quoteFont.setFamily('Segoe UI')
quoteFont.setPointSize(25)

buttonFont = QFont()
buttonFont.setFamily('Segoe UI')
buttonFont.setPointSize(18)
buttonFont.setBold(True)

dateFont = QFont()
dateFont.setFamily('Segoe UI')
dateFont.setPointSize(23)
dateFont.setBold(True)

historyFont = QFont()
historyFont.setFamily('Segoe UI')
historyFont.setPointSize(16)

rincianFont = QFont()
rincianFont.setFamily('Segoe UI')
rincianFont.setPointSize(13)

repetisiFont = QFont()
repetisiFont.setFamily('Segoe UI')
repetisiFont.setPointSize(10)

styleSheetCard = (
        "background-color: #5A8D6C;"
        "border-radius: 20px;"
    ) 


class dashboard(QWidget):
    switch = pyqtSignal(str, dict)
    def __init__(self, user=None):
        super().__init__()
        self.biodata = cur.execute("SELECT * FROM user").fetchall()
        print(self.biodata)
        # if (self.biodata == None):
        #     self.switch.emit('register', {})
        #     self.user = {
        #         'name': f'{self.biodata[0][0]}',
        #         'height': self.biodata[0][1],
        #         'weight': self.biodata[0][2],
        #         'goal': f'{self.biodata[0][3]}',
        #         'gender': f'{self.biodata[0][4]}',
        #         'age': self.biodata[0][5]
        #     }
        # else:
        #     self.user = user
        self.con = sqlite3.connect("fitu.db")
        self.index_history = int(-1)
        self.banyaknyaKartu = int(-1)
        self.dashboardWindow()
    
    def dashboardWindow(self):
        self.setWindowTitle('Dashboard - FitU')
        self.setFixedSize(1280, 720)
        self.setStyleSheet(f'background-color: {background};')
        self.label = QLabel("")
        self.label.setParent(self)
        self.element()

    def historyElement(self, historyIdx, idx):
        self.cur = self.con.cursor()
        self.index_history = idx
        tanggal = cur.execute(f"""
            SELECT strftime(date) FROM riwayat_latihan WHERE history_id = '{historyIdx[self.index_history][0]}'
        """).fetchone()[0]
        
        # menyiapkan history card
        self.card = QLabel(self)
        self.card.setPixmap(QPixmap('img/card-dashboard.png'))
        self.card.move(633, 172)

        daftar_latihan = cur.execute(f"""
            SELECT name FROM riwayat_latihan WHERE date = '{tanggal}'
        """).fetchall()

        jumlahCard = len(daftar_latihan)

        self.banyaknyaKartu = jumlahCard
        print(self.banyaknyaKartu)

        self.date = QLabel(self)
        self.date.setText(f"{tanggal}")
        self.date.setStyleSheet(f'color: {button_color}; background-color: {card_color};')
        self.date.move(820, 195)
        self.date.setFont(dateFont)
        self.date.setAlignment(Qt.AlignmentFlag.AlignLeft)

        keterangan = cur.execute(f"""
                SELECT tot_duration, title_program FROM riwayat_latihan WHERE date = '{tanggal}'
        """).fetchone()
        self.duration = QLabel(self)
        self.duration.setText("Duration : " + str(keterangan[0]) + " minutes")
        self.duration.setStyleSheet(f'color: {button_color}; background-color: {card_color};')
        self.duration.move(667,282)
        self.duration.setFixedWidth(300)
        self.duration.setFont(historyFont)
        self.duration.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.prog = QLabel(self)
        self.prog.setText("Program Name: " + keterangan[1])
        self.prog.setStyleSheet(f'color: {button_color}; background-color: {card_color};')
        self.prog.move(667, 317)
        self.prog.setFixedWidth(300)
        self.prog.setFont(historyFont)
        self.prog.setAlignment(Qt.AlignmentFlag.AlignLeft)

        
        self.scroll = QScrollArea(self)
        self.scroll.setGeometry(654, 369, 486, 204) # mengatur posisi dan ukuran QScrollArea
        self.scroll.setStyleSheet(f"background-color: {card_color}; border-radius: 0px;")
        self.scrollWidget = QWidget(self.scroll)
        self.scrollLayout = QHBoxLayout(self.scrollWidget)
        self.scrollWidget.setStyleSheet(f"background-color: {card_color}; border-radius: 0px;")
        self.scrollWidget.setLayout(self.scrollLayout)
        horizontal_scrollbar = self.scroll.horizontalScrollBar()
        # Mengatur bentuk scroll bar
        scroll_bar_style = """
            QScrollBar:horizontal {
                border : 0px;
                background-color: #5A8D6C;
                height: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background-color: #174728;
                border-radius: 50px;
                border: 0px;
            }
        """
        self.scroll.horizontalScrollBar().setStyleSheet(scroll_bar_style)
        self.hbox = QHBoxLayout()
        for j in range(self.banyaknyaKartu):
            self.label = QLabel()
            self.label.setFixedSize(150, 175)
            self.label.setStyleSheet(styleSheetCard)
            self.hbox.addWidget(self.label)
            nama_latihan = daftar_latihan[j][0]
            repetisi_latihan = cur.execute(f"""
                SELECT repetition FROM daftar_latihan WHERE title = '{nama_latihan}'
            """).fetchone()
            durasi_latihan = cur.execute(f"""
                SELECT duration FROM daftar_latihan WHERE title = '{nama_latihan}'
            """).fetchone()
            gambar_latihan = cur.execute(f"""
                SELECT gif FROM daftar_latihan WHERE title = '{nama_latihan}'
            """).fetchone()
            self.con.commit()
            self.show_nama_latihan = QLabel(self.label)
            self.show_nama_latihan.setText(nama_latihan)
            self.show_nama_latihan.setStyleSheet(f'color: {card_color};')
            self.show_nama_latihan.move(10, 120)
            self.show_nama_latihan.setFont(rincianFont)
            self.show_nama_latihan.setAlignment(Qt.AlignmentFlag.AlignLeft)

            self.show_repetisi_latihan = QLabel(self.label)
            if (repetisi_latihan[0] == None):
                self.show_repetisi_latihan.setText("Duration: " + str(durasi_latihan[0]) + " seconds")
            else:
                self.show_repetisi_latihan.setText("Repetition: " + str(repetisi_latihan[0]))
            self.show_repetisi_latihan.setStyleSheet(f'color: {card_color};')
            self.show_repetisi_latihan.move(10, 145)
            self.show_repetisi_latihan.setFont(repetisiFont)
            self.show_repetisi_latihan.setAlignment(Qt.AlignmentFlag.AlignLeft)

            self.gif = cur.execute(f"""
                SELECT gif FROM daftar_latihan WHERE title = '{nama_latihan}'
                """).fetchone()[0]
            self.gif2 = QMovie(self.gif)
            self.gif2.setScaledSize(QSize(90, 90))
            self.gif2.start()
            self.show_gambar_latihan = QLabel(self.label)
            self.show_gambar_latihan.setMovie(self.gif2)
            self.show_gambar_latihan.move(25, 20)
        self.scrollLayout.addLayout(self.hbox)
        self.scroll.setWidget(self.scrollWidget)
        
        self.kiri = QPushButton(self)
        self.kiri.setText('<')
        self.kiri.setStyleSheet(f'''
        QPushButton {{
            color: {button_color};
            background-color: {card_color};
            border: none;
            border-radius: 20px;
        }}
        ''')
        self.kiri.setFont(dateFont)
        self.kiri.move(727, 195)
        self.kiri.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kiri.clicked.connect(lambda:self.prev(historyIdx))

        
        self.kanan = QPushButton(self)
        self.kanan.setText('>')
        self.kanan.setStyleSheet(f'''
        QPushButton {{
            color: {button_color};
            background-color: {card_color};
            border: none;
            border-radius: 20px;
        }}
        ''')
        self.kanan.setFont(dateFont)
        self.kanan.move(1047, 195)
        self.kanan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kanan.clicked.connect(lambda:self.next(historyIdx))

        if(self.index_history == len(historyIdx)-1):
            self.kanan.hide()
            self.kiri.show()
        elif (self.index_history == 0):
            self.kiri.hide()
            self.kanan.show()
        else:
            self.kiri.show()
            self.kanan.show()

    def historyKosong(self):
        # menyiapkan history card
        self.card = QLabel(self)
        self.card.setPixmap(QPixmap('img/card-dashboard.png'))
        self.card.move(633, 172)

        self.text1 = QLabel(self)
        self.text1.setText("You Haven't Completed\nAny Training yet!")
        self.text1.setStyleSheet(f'color: {button_color}; background-color: {card_color};')
        self.text1.move(743, 286)
        dateFont.setBold(False)
        self.text1.setFont(dateFont)
        self.text1.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.text2 = QLabel(self)
        self.text2.setText("Let's start training now!")
        self.text2.setStyleSheet(f'color: {button_color}; background-color: {card_color};')
        self.text2.move(780, 448)
        dateFont.setPointSize(18)
        self.text2.setFont(dateFont)
        dateFont.setBold(True)
        dateFont.setPointSize(23)
        self.text2.setAlignment(Qt.AlignmentFlag.AlignLeft)

   
    def element(self):
        self.cur = self.con.cursor()
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
        homeButton.move(660, 53)    
        # homeButton.setCursor(
        #     QCursor(Qt.CursorShape.PointingHandCursor))
        
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
        QPushButton:hover {{
            color: {button_color};
        }}
        ''')
        customizeButton.setFont(buttonFont)
        customizeButton.move(798, 58)
        customizeButton.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        customizeButton.clicked.connect(self.customWindow)
        
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
        
        
        # # tombol history
        # historyButton = QPushButton(self)
        # historyButton.setText('History')
        # historyButton.setStyleSheet(f'''
        # QPushButton {{
        #     color: {text_color};
        #     background-color: {background};
        #     border: none;
        #     border-radius: 20px;
        # }}
        # ''')
        # historyButton.setFont(buttonFont)
        # historyButton.move(979, 58)
        # historyButton.setCursor(
        #     QCursor(Qt.CursorShape.PointingHandCursor))
        
        # foto profil
        profilePhoto = QLabel(self)
        profilePhoto.setPixmap(QPixmap('img/profile-dashboard.png'))
        profilePhoto.move(1133, 45)

        # say Hello
        self.hello = QLabel(self)
        # self.hello.setText(f"Hello, krisi!")
        self.hello.move(101, 236)
        self.hello.setFont(helloFont)
        if(self.biodata == []):
            self.hello.setText(f"Hello, dummy!")
        else:
            self.hello.setText(f"Hello, {self.biodata[0][0]}!")
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
         QPushButton:hover {{
            color: #5A8D6C;
            background-color: #D2DCC4;
        }}
        ''') 
        start.setFont(buttonFont)
        start.setFixedSize(233, 47) #pake ini buat kalau dia buletan
        start.move(101, 511)    
        start.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # membuat history card
        historyIdx = cur.execute("""
                                SELECT DISTINCT history_id FROM riwayat_latihan
                                """).fetchall()
        
        # menyiapkan history card

        if (len(historyIdx) <= 0):
            self.historyKosong()
        else:
            tanggal  = historyIdx[0][0]
            idx = (len(historyIdx)-1)
            self.historyElement(historyIdx, idx)

    def prev(self, historyIdx):
            self.cur = self.con.cursor()
            self.index_history -= 1
            if(self.index_history == len(historyIdx)-1):
                self.kanan.hide()
                self.kiri.show()
            elif (self.index_history == 0):
                self.kiri.hide()
                self.kanan.show()
            else:
                self.kiri.show()
                self.kanan.show()
            self.scroll.setParent(None)
            tanggal = cur.execute(f"""
            SELECT strftime(date) FROM riwayat_latihan WHERE history_id = '{historyIdx[self.index_history][0]}'
        """).fetchone()[0]
            self.date.setText(f"{tanggal}")
            daftar_latihan = cur.execute(f"""
                SELECT name FROM riwayat_latihan WHERE date = '{tanggal}'
                """).fetchall()
            jumlahCard = len(daftar_latihan)
            keterangan = cur.execute(f"""
                SELECT tot_duration, title_program FROM riwayat_latihan WHERE date = '{tanggal}'
                """).fetchone()
            
            self.duration.setText("Duration : " + str(keterangan[0]) + " minutes")
            self.prog.setText("Program Name: " + keterangan[1])
            for i in reversed(range(self.banyaknyaKartu)):
                self.hbox.itemAt(i).widget().setParent(None)

            self.scroll = QScrollArea(self)
            self.scroll.setGeometry(654, 369, 486, 204) # mengatur posisi dan ukuran QScrollArea
            self.scroll.setStyleSheet(f"background-color: {card_color}; border-radius: 0px;")
            self.scrollWidget = QWidget(self.scroll)
            self.scrollLayout = QVBoxLayout(self.scrollWidget)
            self.scrollWidget.setStyleSheet(f"background-color: {card_color}; border-radius: 0px;")
            self.scrollWidget.setLayout(self.scrollLayout)
            horizontal_scrollbar = self.scroll.horizontalScrollBar()
            # Mengatur bentuk scroll bar
            scroll_bar_style = """
                QScrollBar:horizontal {
                    border : 0px;
                    background-color: #5A8D6C;
                    height: 10px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:horizontal {
                    background-color: #174728;
                    border-radius: 50px;
                    border: 0px;
                }
            """
            self.scroll.horizontalScrollBar().setStyleSheet(scroll_bar_style)
            self.hbox = QHBoxLayout()
            

            self.banyaknyaKartu = jumlahCard
            for j in range(self.banyaknyaKartu):
                self.label = QLabel()
                self.label.setFixedSize(150, 175)
                self.label.setStyleSheet(styleSheetCard)
                self.hbox.addWidget(self.label)
                nama_latihan = daftar_latihan[j][0]
                repetisi_latihan = cur.execute(f"""
                    SELECT repetition FROM daftar_latihan WHERE title = '{nama_latihan}'
                """).fetchone()
                durasi_latihan = cur.execute(f"""
                    SELECT duration FROM daftar_latihan WHERE title = '{nama_latihan}'
                """).fetchone()
                gambar_latihan = cur.execute(f"""
                    SELECT gif FROM daftar_latihan WHERE title = '{nama_latihan}'
                """).fetchone()
                self.con.commit()
                self.show_nama_latihan = QLabel(self.label)
                self.show_nama_latihan.setText(nama_latihan)
                self.show_nama_latihan.setStyleSheet(f'color: {card_color};')
                self.show_nama_latihan.move(10, 120)
                self.show_nama_latihan.setFont(rincianFont)
                self.show_nama_latihan.setAlignment(Qt.AlignmentFlag.AlignLeft)

                self.show_repetisi_latihan = QLabel(self.label)
                if (repetisi_latihan[0] == None):
                    self.show_repetisi_latihan.setText("Duration: " + str(durasi_latihan[0]) + " seconds")
                else:
                    self.show_repetisi_latihan.setText("Repetition: " + str(repetisi_latihan[0]))
                self.show_repetisi_latihan.setStyleSheet(f'color: {card_color};')
                self.show_repetisi_latihan.move(10, 145)
                self.show_repetisi_latihan.setFont(repetisiFont)
                self.show_repetisi_latihan.setAlignment(Qt.AlignmentFlag.AlignLeft)

                self.gif = cur.execute(f"""
                    SELECT gif FROM daftar_latihan WHERE title = '{nama_latihan}'
                    """).fetchone()[0]
                self.gif2 = QMovie(self.gif)
                self.gif2.setScaledSize(QSize(90, 90))
                self.gif2.start()
                self.show_gambar_latihan = QLabel(self.label)
                self.show_gambar_latihan.setMovie(self.gif2)
                self.show_gambar_latihan.move(25, 20)
            self.scrollLayout.addLayout(self.hbox)
            self.scroll.setWidget(self.scrollWidget)
            self.scroll.show()


    
    def next(self, historyIdx):
            self.cur = self.con.cursor()
            self.index_history += 1
            if(self.index_history == len(historyIdx)-1):
                self.kanan.hide()
                self.kiri.show()
            elif (self.index_history == 0):
                self.kiri.hide()
                self.kanan.show()
            else:
                self.kiri.show()
                self.kanan.show()
            self.scroll.setParent(None)
            tanggal = cur.execute(f"""
            SELECT strftime(date) FROM riwayat_latihan WHERE history_id = '{historyIdx[self.index_history][0]}'
        """).fetchone()[0]
            self.date.setText(f"{tanggal}")
            daftar_latihan = cur.execute(f"""
                SELECT name FROM riwayat_latihan WHERE date = '{tanggal}'
                """).fetchall()
            jumlahCard = len(daftar_latihan)
            keterangan = cur.execute(f"""
                SELECT tot_duration, title_program FROM riwayat_latihan WHERE date = '{tanggal}'
                """).fetchone()
            
            self.duration.setText("Duration : " + str(keterangan[0]) + " minutes")
            self.prog.setText("Program Name: " + keterangan[1])

            for i in reversed(range(self.banyaknyaKartu)):
                self.hbox.itemAt(i).widget().setParent(None)

            self.scroll = QScrollArea(self)
            self.scroll.setGeometry(654, 369, 486, 204) # mengatur posisi dan ukuran QScrollArea
            self.scroll.setStyleSheet(f"background-color: {card_color}; border-radius: 0px;")
            self.scrollWidget = QWidget(self.scroll)
            self.scrollLayout = QVBoxLayout(self.scrollWidget)
            self.scrollWidget.setStyleSheet(f"background-color: {card_color}; border-radius: 0px;")
            self.scrollWidget.setLayout(self.scrollLayout)
            horizontal_scrollbar = self.scroll.horizontalScrollBar()
            # Mengatur bentuk scroll bar
            scroll_bar_style = """
                QScrollBar:horizontal {
                    border : 0px;
                    background-color: #5A8D6C;
                    height: 10px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:horizontal {
                    background-color: #174728;
                    border-radius: 50px;
                    border: 0px;
                }
            """
            self.scroll.horizontalScrollBar().setStyleSheet(scroll_bar_style)
            self.hbox = QHBoxLayout()

            self.banyaknyaKartu = jumlahCard
            for j in range(self.banyaknyaKartu):
                self.label = QLabel()
                self.label.setFixedSize(150, 175)
                self.label.setStyleSheet(styleSheetCard)
                self.hbox.addWidget(self.label)
                nama_latihan = daftar_latihan[j][0]
                repetisi_latihan = cur.execute(f"""
                    SELECT repetition FROM daftar_latihan WHERE title = '{nama_latihan}'
                """).fetchone()
                durasi_latihan = cur.execute(f"""
                    SELECT duration FROM daftar_latihan WHERE title = '{nama_latihan}'
                """).fetchone()
                gambar_latihan = cur.execute(f"""
                    SELECT gif FROM daftar_latihan WHERE title = '{nama_latihan}'
                """).fetchone()
                self.con.commit()
                self.show_nama_latihan = QLabel(self.label)
                self.show_nama_latihan.setText(nama_latihan)
                self.show_nama_latihan.setStyleSheet(f'color: {card_color};')
                self.show_nama_latihan.move(10, 120)
                self.show_nama_latihan.setFont(rincianFont)
                self.show_nama_latihan.setAlignment(Qt.AlignmentFlag.AlignLeft)

                self.show_repetisi_latihan = QLabel(self.label)
                if (repetisi_latihan[0] == None):
                    self.show_repetisi_latihan.setText("Duration: " + str(durasi_latihan[0]) + " seconds")
                else:
                    self.show_repetisi_latihan.setText("Repetition: " + str(repetisi_latihan[0]))
                self.show_repetisi_latihan.setStyleSheet(f'color: {card_color};')
                self.show_repetisi_latihan.move(10, 145)
                self.show_repetisi_latihan.setFont(repetisiFont)
                self.show_repetisi_latihan.setAlignment(Qt.AlignmentFlag.AlignLeft)

                self.gif = cur.execute(f"""
                    SELECT gif FROM daftar_latihan WHERE title = '{nama_latihan}'
                    """).fetchone()[0]
                self.gif2 = QMovie(self.gif)
                self.gif2.setScaledSize(QSize(90, 90))
                self.gif2.start()
                self.show_gambar_latihan = QLabel(self.label)
                self.show_gambar_latihan.setMovie(self.gif2)
                self.show_gambar_latihan.move(25, 20)
            self.scrollLayout.addLayout(self.hbox)
            self.scroll.setWidget(self.scrollWidget)
            self.scroll.show()
    
    def planWindow(self):
        self.switch.emit("plan", {})
    
    def listWindow(self):
        self.switch.emit("listLatihan", {})
    
    def customWindow(self):
        self.switch.emit("customize", {})
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = dashboard()
    window.show()
    sys.exit(app.exec())