from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QPlainTextEdit

from libs.window.BaseWindow import BaseWindow
from libs.py_from_ui.ui_rdv_requests import Ui_RdvRequests


class RdvRequestsWindow(BaseWindow, Ui_RdvRequests):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        # QSettings(organization="MyApp", application="RdvRequestsWindow")
        # т.к.QSettings поддерживает только позиционную передачу значений
        self.settings_window = QSettings("MyApp", "RdvRequestsWindow")
        self.data_file_name = 'rdv_requests'
        self.txt_input_field.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.chbx_wrap.stateChanged.connect(self.change_wrap_state)
