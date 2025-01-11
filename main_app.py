import sys
from typing import Any

from PySide6.QtCore import QSettings, QSize
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit

from libs.sections.format_sql_query import FormatSqlQuery
from libs.sections.format_yaml_json import FormatYamlJsonConverter
from libs.sections.format_yaml_sql import FormatYamlSqlConverter
from libs.static import button_example
from libs.window.BranchWindow import BranchWindow
from libs.window.RdvInstructionWindow import RdvInstructionWindow
from libs.window.RdvPsiWindow import RdvPsiWindow
from libs.window.RdvRequestsWindow import RdvRequestsWindow
from libs.window.RdvScriptsWindow import RdvScriptsWindow
from libs.py_from_ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # QSettings(organization="MyApp", application="MainWindow")
        # т.к.QSettings поддерживает только позиционную передачу значений
        self.settings_main_window = QSettings("MyApp", "MainWindow")
        self.restore_window_state()

        self.ui.txt_main_output_field.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.ui.txt_main_input_field.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.ui.btn_execute_statement.clicked.connect(self.execute_statement)
        self.ui.btn_clear_input_output_fields.clicked.connect(self.clear_input_output_fields)

        self.all_checkboxes = [
            self.ui.chbx_1_format_sql_query,
            self.ui.chbx_2_yaml_sql,
            self.ui.chbx_3_yaml_json
        ]
        for checkbox in self.all_checkboxes:
            # toggled активируется каждый раз, когда меняется состояние чекбокса
            checkbox.toggled.connect(
                self.uncheck_all_checkboxes_except_active)

        self.link_button_example_x_checkbox = {
            self.ui.btn_example_1_format_sql_query: self.ui.chbx_1_format_sql_query,
            self.ui.btn_example_2_yaml_sql: self.ui.chbx_2_yaml_sql,
            self.ui.btn_example_3_yaml_json: self.ui.chbx_3_yaml_json,
        }
        self.link_button_example_x_text_example = {
            self.ui.btn_example_1_format_sql_query: button_example.btn_example_1,
            self.ui.btn_example_2_yaml_sql: button_example.btn_example_2,
            self.ui.btn_example_3_yaml_json: button_example.btn_example_3
        }
        # checked — это параметр, который передает Qt и также он указывает, что сигнал был вызван
        # он нужен для совместимости с системой сигналов и слотов, хотя он не используется в данном случае
        for button, checkbox in self.link_button_example_x_checkbox.items():
            button.clicked.connect(lambda checked, chbox=checkbox, btn=button: self.show_example(chbox, btn))

        self.ui.tab_all_branches.triggered.connect(self.open_window_all_branches)
        self.ui.tab_rdv_scripts.triggered.connect(self.open_window_rdv_scripts)
        self.ui.tab_rdv_info.triggered.connect(self.open_window_rdv_info)
        self.ui.tab_rdv_psi.triggered.connect(self.open_window_rdv_psi)
        self.ui.tab_rdv_instruction.triggered.connect(self.open_window_rdv_instruction)

    def restore_window_state(self) -> None:
        previous_window_size: Any = self.settings_main_window.value("size", QSize(950, 370))
        self.resize(previous_window_size)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.settings_main_window.setValue("size", self.size())

    def open_window_all_branches(self) -> None:
        dialog = BranchWindow(self)
        dialog.exec()

    def open_window_rdv_scripts(self) -> None:
        dialog = RdvScriptsWindow(self)
        dialog.exec()

    def open_window_rdv_info(self) -> None:
        dialog = RdvRequestsWindow(self)
        dialog.exec()

    def open_window_rdv_psi(self) -> None:
        dialog = RdvPsiWindow(self)
        dialog.exec()

    def open_window_rdv_instruction(self) -> None:
        dialog = RdvInstructionWindow(self)
        dialog.exec()

    def show_example(self, checkbox_pushed_button, pushed_button) -> None:
        example = self.link_button_example_x_text_example[pushed_button]
        self.ui.txt_main_input_field.setPlainText(example)
        checkbox_pushed_button.setChecked(True)
        self.execute_statement()

    def uncheck_all_checkboxes_except_active(self) -> None:
        sender = self.sender()
        if sender.isChecked():
            for checkbox in self.all_checkboxes:
                if checkbox != sender:
                    checkbox.setChecked(False)

    def execute_statement(self) -> None:
        if self.ui.chbx_1_format_sql_query.isChecked():
            param1_left_space = self.ui.input_chbx1_param1.toPlainText()
            param2_center_space = self.ui.input_chbx1_param2.toPlainText()
            text_from_input_field = FormatSqlQuery(self.ui.txt_main_input_field.toPlainText())
            self.ui.txt_main_output_field.setPlainText(
                text_from_input_field.to_pretty_sql(left_space=param1_left_space, center_space=param2_center_space))

        elif self.ui.chbx_2_yaml_sql.isChecked():
            self.ui.txt_main_output_field.setPlainText(self.convert_yaml_sql())
        elif self.ui.chbx_3_yaml_json.isChecked():
            self.ui.txt_main_output_field.setPlainText(self.convert_yaml_json())
        else:
            self.ui.txt_main_output_field.setPlainText("")

    def clear_input_output_fields(self) -> None:
        self.ui.txt_main_input_field.setPlainText('')
        self.ui.txt_main_output_field.setPlainText('')

    def convert_yaml_sql(self):
        if self.ui.RadioBtn_chbx2_DAPP.isChecked():
            layer = 'DAPP'
        else:
            self.ui.RadioBtn_chbx2_RDV.setChecked(True)
            layer = 'RDV'

        try:
            yaml_query = FormatYamlSqlConverter(self.ui.txt_main_input_field.toPlainText())
            pretty_sql = yaml_query.to_sql(table_name=self.ui.input_chbx2_param2.toPlainText(), layer=layer)
        except:
            self.push_error_msg()
            pretty_sql = ''

        return pretty_sql

    def convert_yaml_json(self):
        if not self.ui.RadioBtn_chbx3_Nullable_Yes.isChecked() and not self.ui.RadioBtn_chbx3_Nullable_No.isChecked():
            self.ui.RadioBtn_chbx3_Nullable_Yes.setChecked(True)
        if not self.ui.RadioBtn_chbx3_Primary_Yes.isChecked() and not self.ui.RadioBtn_chbx3_Primary_No.isChecked():
            self.ui.RadioBtn_chbx3_Primary_Yes.setChecked(True)

        try:
            yaml_query = FormatYamlJsonConverter(self.ui.txt_main_input_field.toPlainText(),
                                                 is_primary=self.ui.RadioBtn_chbx3_Primary_Yes.isChecked(),
                                                 is_nullable=self.ui.RadioBtn_chbx3_Nullable_Yes.isChecked())
            json_query = yaml_query.to_json(indent=self.ui.input_chbx3_param1.toPlainText())
        except:
            json_query = ''
            self.push_error_msg()

        return json_query

    def push_error_msg(self):
        self.ui.txt_main_input_field.setPlainText(
            'Введен некорректный исходный текст\nнажмите на кнопку "Пример" справа\nнапротив выбранного checkbox')


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
