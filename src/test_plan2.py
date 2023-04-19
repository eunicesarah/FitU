import pytest
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt, QTimer, QTime
from plan2 import plan2

@pytest.fixture
def app(qtbot):
    test_plan = plan2(1)
    qtbot.addWidget(test_plan)
    return test_plan

def test_setUpPlan(app, qtbot):
    assert app.nameLabel.text() == 'Push Up'
    assert app.repLabel.text() == ''
    assert app.timer_label.text() == '10 Rep'
    assert app.currEx.movie().fileName() == 'img/exe-pushup.gif'
    assert app.prevButton.isEnabled() == True
    assert app.nextButton.isEnabled() == True

    qtbot.mouseClick(app.nextButton, Qt.MouseButton.LeftButton)
    assert app.nameLabel.text() == 'Bridge'
    assert app.currEx.movie().fileName() == 'img/exe-bridges.gif'
    assert app.prevButton.isEnabled() == True
    assert app.nextButton.isEnabled() == True

    qtbot.mouseClick(app.prevButton, Qt.MouseButton.LeftButton)
    assert app.nameLabel.text() == 'Push Up'
    assert app.currEx.movie().fileName() == 'img/exe-pushup.gif'
    assert app.prevButton.isEnabled() == True
    assert app.nextButton.isEnabled() == True

    qtbot.wait(2000)
    assert app.remaining_time == 30

    qtbot.wait(15000)
    assert app.remaining_time == 30
