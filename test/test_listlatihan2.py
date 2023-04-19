from PyQt6.QtWidgets import QApplication
import sys
import os

path = os.getcwd()
sys.path.insert(0,f"{path}/src")
from listlatihan2 import listLatihan2
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QCursor, QFont, QMovie
from PyQt6.QtWidgets import (QWidget, QApplication, QWidget,
                             QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QDialog)
import pytest

@pytest.fixture
def app():
    app = listLatihan2()
    yield app

def test_window(app,qtbot):
    # cek window title
    assert app.windowTitle() == "FitU - Daftar Latihan"
    assert app.height() == 720
    assert app.width() == 1280
    assert len(app.findChildren(QPushButton)) == 20

def test_listLat(app,qtbot):
    # cek jumlah latihan yang ditampilkan apakah berisi 16 latihan
    assert len(app.listLat) == 16
    assert isinstance(app.findChild(QScrollArea), QScrollArea)
    assert len(app.findChild(QScrollArea).findChildren(QPushButton)) == len(app.listLat)
