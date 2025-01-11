import os

from PySide6.QtCore import QSize
from PySide6.QtGui import QCloseEvent, QScreen, QShowEvent
from PySide6.QtWidgets import QApplication, QDialog, QPlainTextEdit


class BaseWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.chbx_wrap = None
        self.txt_input_field = None
        self.data_file_name = None
        self.settings_window = None

    def change_wrap_state(self) -> None:
        if self.chbx_wrap.isChecked():
            self.txt_input_field.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        else:
            self.txt_input_field.setLineWrapMode(QPlainTextEdit.NoWrap)

    def showEvent(self, event: QShowEvent) -> None:
        self.restore_window_state()
        os.makedirs('./files', exist_ok=True)
        if os.path.exists(f'./files/{self.data_file_name}.txt'):
            with open(file=f'./files/{self.data_file_name}.txt', mode='r', encoding='UTF-8') as f:
                self.txt_input_field.setPlainText(f.read())
        else:
            with open(file=f'./files/{self.data_file_name}.txt', mode='a', encoding='UTF-8') as f:
                pass

    def closeEvent(self, event: QCloseEvent) -> None:
        self.settings_window.setValue("size", self.size())
        self.settings_window.setValue("pos", self.pos())
        with open(file=f'./files/{self.data_file_name}.txt', mode='w', encoding='UTF-8') as f:
            f.write(self.txt_input_field.toPlainText())
        event.accept()  # Сообщаем, что ранее выполненный код корректно отработал и можно действительно закрыть окно

    def restore_window_state(self) -> None:
        previous_window_size = self.settings_window.value("size", QSize(600, 300))
        previous_window_coordinates = self.settings_window.value("pos")
        self.resize(previous_window_size)
        if previous_window_coordinates:
            self.move(previous_window_coordinates)
        else:
            self.move_to_center()

    def move_to_center(self) -> None:
        available_screen_size = QScreen.availableGeometry(QApplication.primaryScreen())
        center_available_screen_size = available_screen_size.center()

        app_size = self.frameGeometry()
        app_size.moveCenter(center_available_screen_size)

        self.move(app_size.topLeft())
