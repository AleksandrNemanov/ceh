from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QPlainTextEdit

from libs.window.BaseWindow import BaseWindow
from libs.py_from_ui.ui_branch import Ui_Branch


class BranchWindow(BaseWindow, Ui_Branch):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        # QSettings(organization="MyApp", application="BranchWindow")
        # т.к.QSettings поддерживает только позиционную передачу значений
        self.settings_window = QSettings("MyApp", "BranchWindow")
        self.data_file_name = 'branches'
        self.txt_input_field.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.chbx_wrap.stateChanged.connect(self.change_wrap_state)
