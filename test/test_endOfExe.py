import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QRadioButton, QCheckBox, QMessageBox
from PyQt6.QtGui import QFont, QPixmap, QCursor
from PyQt6.QtCore import Qt, pyqtSignal
import sys
import os
import pytest

path = os.getcwd()
sys.path.insert(0,f"{path}/src")
from endOfExercise import endOfExe

def test_endOfExe(qtbot):
    window = endOfExe()
    qtbot.addWidget(window)


    # Check window title and size
    assert window.windowTitle() == "FitU - End Of Exercise"
    assert window.size() == window.minimumSize()

    # Check presence and properties of all widgets
    assert isinstance(window.findChildren(QLabel)[0], QLabel)
    assert window.findChildren(QLabel)[0].text() == "Congratulations"
    assert isinstance(window.findChildren(QLabel)[1], QLabel)
    assert window.findChildren(QLabel)[1].text() == "you've done the exercise!"
    assert isinstance(window.findChildren(QLabel)[2], QLabel)
    assert window.findChildren(QLabel)[2].text() == "STAY HEALTHY AND POWERFUL!"
    assert isinstance(window.findChildren(QPushButton)[0], QPushButton)
    assert window.findChildren(QPushButton)[0].text() == "Back To Dashboard"

    # Assume we have a parent widget called 'parentWidget'
# and we want to find a child QLabel with object name 'myLabel'



    # Test clicking on the back button emits the signal
    # with qtbot.waitSignal(window.switch, raising=True) as blocker:
    #     qtbot.mouseClick(window.findChild(QPushButton, "backButton"), Qt.MouseButton.LeftButton)
    # assert blocker.args == ("dashboard", {})
