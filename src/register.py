import sqlite3
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QRadioButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor, QIcon
from PyQt6.QtCore import Qt, pyqtSignal
import sys
class register(QWidget):
    switch = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('fitu.db')
        self.setUpWindow()

    def setUpWindow(self):
        self.setWindowTitle("FitU - Register")
        self.setWindowIcon(QIcon("img/logo.png"))
        self.setFixedSize(1280, 720)
        self.setUp()

    def setUp(self):
        #Background
        background = QLabel(self)
        bacgroundImage = QPixmap("img/register-page.png")
        background.setPixmap(bacgroundImage)
        background.move(0, 0)

        inputSize = QFont()
        inputSize.setFamily("Segoe UI")
        inputSize.setPointSize(10)

        genderSize = QFont()
        genderSize.setFamily("Segoe UI")
        genderSize.setPointSize(14)

        registerText = QFont()
        registerText.setFamily("Segoe UI")
        registerText.setPointSize(16)

        self.nameInput = QLineEdit(self)
        self.nameInput.setPlaceholderText("Input Your Name")
        self.nameInput.setFixedSize(379, 44)
        self.nameInput.setFont(inputSize)
        self.nameInput.setStyleSheet('''
        padding: 11px 30px 11px 30px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        color: rgba(23, 71, 40, 1);
        background-color: #D2DCC4
        ''')
        self.nameInput.move(773, 196)

        self.age = QLineEdit(self)
        self.age.setPlaceholderText("Input Your Age")
        self.age.setFixedSize(172, 44)
        self.age.setFont(inputSize)
        self.age.setStyleSheet('''
        padding: 11px 30px 11px 30px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        color: rgba(23, 71, 40, 1);
        background-color: #D2DCC4
        ''')
        self.age.move(976, 285)

        self.height = QLineEdit(self)
        self.height.setPlaceholderText("Input Your Height")
        self.height.setFixedSize(172, 44)
        self.height.setFont(inputSize)
        self.height.setStyleSheet('''
        padding: 11px 30px 11px 30px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        color: rgba(23, 71, 40, 1);
        background-color: #D2DCC4
        ''')
        self.height.move(769, 392)

        self.weight = QLineEdit(self)  
        self.weight.setPlaceholderText("Input Your Weight")
        self.weight.setFixedSize(172, 44)
        self.weight.setFont(inputSize)
        self.weight.setStyleSheet('''
        padding: 11px 30px 11px 30px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        color: rgba(23, 71, 40, 1);
        background-color: #D2DCC4
        ''')
        self.weight.move(976, 392)

        self.male = QRadioButton(self)
        self.male.move(780, 285)
        self.male.setStyleSheet(f'background-color: #174728 ; color: #D2DCC4 ')
        self.male.setText("Male")
        self.male.setFont(genderSize)
        self.male.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.female = QRadioButton(self)
        self.female.move(780, 315)
        self.female.setStyleSheet('background-color: #174728 ; color: #D2DCC4 ')
        self.female.setText("Female")
        self.female.setFont(genderSize)
        self.female.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.registerButton = QPushButton(self)
        self.registerButton.setText("Register")
        self.registerButton.setFixedSize(172, 44)
        self.registerButton.setStyleSheet('''
        QPushButton {
            color: rgba(23, 71, 40, 1);
            background-color:  #D2DCC4;
            border: 1px solid rgba(255, 255, 255, 0.8);
            border-radius: 20px;
        }
        QPushButton:hover {
            background-color: #5A8D6C;
            color: #D2DCC4;
        }
        ''')
        self.registerButton.move(873, 545)
        self.registerButton.setFont(registerText)
        self.registerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.registerButton.clicked.connect(self.register)


        self.fit = QCheckBox(self)
        self.fit.move(781, 486)
        self.fit.setText("Fit our body")
        self.fit.setFont(genderSize)
        self.fit.setStyleSheet('background-color: #174728 ; color: #D2DCC4 ')
        self.fit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.thin = QCheckBox(self)
        self.thin.move(781, 516)
        self.thin.setText("Thin")
        self.thin.setFont(genderSize)
        self.thin.setStyleSheet('background-color: #174728 ; color: #D2DCC4 ')
        self.thin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def register(self):
        if (self.nameInput.text() == '' or self.age.text() == '' or self.height.text() == '' or self.weight.text() == '' 
        or (not self.male.isChecked() and not self.female.isChecked()) 
        or (not self.fit.isChecked() and not self.thin.isChecked())):
            msgBox = QMessageBox()
            msgBox.setText("<p>Please fill out the form properly!</p>")
            msgBox.setWindowTitle("Registration Failed")
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setStyleSheet("background-color: white")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return
        # elif (not self.nameInput.text().isalpha() and self.nameInput.text().isspace()):
        #     msgBox = QMessageBox()
        #     msgBox.setText("<p>Name must be in alphabet</p>")
        #     msgBox.setWindowTitle("Registration Failed")
        #     msgBox.setIcon(QMessageBox.Icon.Warning)
        #     msgBox.setStyleSheet("background-color: white")
        #     msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        #     msgBox.exec()
        #     return
        
        elif not self.age.text().isdigit() or not self.height.text().isdigit() or not self.weight.text().isdigit():
            msgBox = QMessageBox()
            msgBox.setText("<p>Age, Height, and Weight must be in number</p>")
            msgBox.setWindowTitle("Registration Failed")
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setStyleSheet("background-color: white")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
            msgBox.exec()

        else:
            c = self.conn.cursor()
            if (self.female.isChecked()):
                if (self.fit.isChecked() == self.thin.isChecked()):
                    c.execute(
                        f"INSERT INTO user (name, height, weight, goal, gender, age) VALUES ('{self.nameInput.text()}', '{self.height.text()}', '{self.weight.text()}', 'fit, thin', 'female', '{self.age.text()}')"
                    )
                    self.conn.commit()
                elif (self.thin.isChecked()):
                    c.execute(
                        f"INSERT INTO user (name, height, weight, goal, gender, age) VALUES ('{self.nameInput.text()}', '{self.height.text()}', '{self.weight.text()}', 'thin', 'female', '{self.age.text()}')"
                    )
                    self.conn.commit()
                elif (self.fit.isChecked()):
                    c.execute(
                        f"INSERT INTO user (name, height, weight, goal, gender, age) VALUES ('{self.nameInput.text()}', '{self.height.text()}', '{self.weight.text()}', 'fit', 'female', '{self.age.text()}')"
                    )
                    self.conn.commit()
                # if (self.fit and self.thin):
                


            elif(self.male.isChecked()):
                if(self.fit.isChecked() and self.thin.isChecked()):
                    c.execute(
                        f"INSERT INTO user (name, height, weight, goal, gender, age) VALUES ('{self.nameInput.text()}', '{self.height.text()}', '{self.weight.text()}', 'fit, thin', 'male', '{self.age.text()}')"
                    )
                    self.conn.commit()
                elif (self.thin.isChecked()):
                    c.execute(
                        f"INSERT INTO user (name, height, weight, goal, gender, age) VALUES ('{self.nameInput.text()}', '{self.height.text()}', '{self.weight.text()}', 'thin', 'male', '{self.age.text()}')"
                    )
                    self.conn.commit()

                elif (self.fit.isChecked()):
                    c.execute(
                        f"INSERT INTO user (name, height, weight, goal, gender, age) VALUES ('{self.nameInput.text()}', '{self.height.text()}', '{self.weight.text()}', 'fit', 'male', '{self.age.text()}')"
                    )
                    self.conn.commit()
                # if (self.fit and self.thin):

                
            self.nameInput.clear()
            self.age.clear()
            self.height.clear()
            self.weight.clear()
            self.switch.emit()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = register()
    window.show()
    app.exec()