import pytest
import sys
import os

path = os.getcwd()
sys.path.insert(0,f"{path}/src")

from PyQt6.QtCore import Qt, pyqtSignal, QSize
from PyQt6.QtGui import QCursor, QFont, QPixmap, QMovie, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QScrollArea, QVBoxLayout, QHBoxLayout
import sqlite3
import random

from dashboard import dashboard

cur = sqlite3.connect('fitu.db')
con = cur.cursor()

@pytest.fixture
def app():
    app = dashboard()
    yield app

def test_dashboard(app, qtbot):
    assert app.windowTitle() == 'FitU - Dashboard'
    assert app.height() == 720
    assert app.width() == 1280

def test_element(app, qtbot):
    latihan = cur.execute("""
    SELECT * FROM riwayat_latihan """).fetchall()

    if (len(latihan)<=0):
        assert len(app.findChildren(QPushButton)) == 5
        assert len(app.findChildren(QLabel)) == 8
    else:
        assert len(app.findChildren(QPushButton)) == 7
        assert len(app.findChildren(QLabel)) >= 21
    assert app.findChildren(QPushButton)[0].text() == 'Home'
    assert app.findChildren(QPushButton)[1].text() == 'Customize'
    assert app.findChildren(QPushButton)[2].text() == 'Plan'
    assert app.findChildren(QPushButton)[3].text() == 'List'
    assert app.findChildren(QPushButton)[4].text() == "Let's Start!"
    



