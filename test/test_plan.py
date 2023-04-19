import pytest

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap, QCursor, QFont, QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QScrollArea
import sys
import os

path = os.getcwd()
sys.path.insert(0,f"{path}/src")
from plan import plan

@pytest.fixture
def app():
    app = plan()
    yield app

def test_window(app,qtbot):
    # cek window title
    assert app.windowTitle() == "FitU - Plan"
    assert app.height() == 720
    assert app.width() == 1280
    assert len(app.findChildren(QPushButton)) == 10