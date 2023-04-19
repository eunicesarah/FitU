import pytest
from PyQt6.QtWidgets import QApplication, QLineEdit, QRadioButton, QCheckBox, QPushButton
from PyQt6.QtCore import Qt

from register import register

@pytest.fixture
def app(qtbot):
    test_register = register()
    qtbot.addWidget(test_register)
    return test_register

def test_name_input(app, qtbot):
    name_input = app.nameInput
    qtbot.keyClicks(name_input, "Test Name")
    assert name_input.text() == "Test Name"

def test_age_input(app, qtbot):
    age_input = app.age
    qtbot.keyClicks(age_input, "25")
    assert age_input.text() == "25"

def test_height_input(app, qtbot):
    height_input = app.height
    qtbot.keyClicks(height_input, "180")
    assert height_input.text() == "180"

def test_weight_input(app, qtbot):
    weight_input = app.weight
    qtbot.keyClicks(weight_input, "75")
    assert weight_input.text() == "75"

def test_gender_selection(app, qtbot):
    male_button = app.male
    female_button = app.female

    qtbot.mouseClick(male_button, Qt.MouseButton.LeftButton)
    assert male_button.isChecked()

    qtbot.mouseClick(female_button, Qt.MouseButton.LeftButton)
    assert female_button.isChecked()

def test_body_type_selection(app, qtbot):
    fit_checkbox = app.fit
    thin_checkbox = app.thin

    qtbot.mouseClick(fit_checkbox, Qt.MouseButton.LeftButton)
    assert fit_checkbox.isChecked()

    qtbot.mouseClick(thin_checkbox, Qt.MouseButton.LeftButton)
    assert thin_checkbox.isChecked()

def test_register_button(app, qtbot):
    register_button = app.registerButton
    name_input = app.nameInput
    age_input = app.age
    height_input = app.height
    weight_input = app.weight
    male_button = app.male
    female_button = app.female
    fit_checkbox = app.fit
    thin_checkbox = app.thin

    # Input test data
    qtbot.keyClicks(name_input, "Test Name")
    qtbot.keyClicks(age_input, "25")
    qtbot.keyClicks(height_input, "180")
    qtbot.keyClicks(weight_input, "75")
    qtbot.mouseClick(male_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(fit_checkbox, Qt.MouseButton.LeftButton)

    # Check if switch signal is emitted
    # with qtbot.waitSignal(app.switch):
    #     qtbot.mouseClick(register_button, Qt.MouseButton.LeftButton)
