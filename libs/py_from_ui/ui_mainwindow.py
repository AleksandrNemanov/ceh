# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 441)
        MainWindow.setMinimumSize(QSize(950, 370))
        MainWindow.setMaximumSize(QSize(950, 900))
        icon = QIcon()
        icon.addFile(u"icons/NoteStack.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"                background-color:#1d1e21; /*1E1E1E*/\n"
"                color: #ffffff;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u043e\u0441\u043a\u0430, \u0433\u0434\u0435 \u043f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0435\u043d\u044b (\u041e\u043f\u0446\u0438\u0438 \u0438 \u0442\u0434)*/\n"
"QMenuBar {\n"
"    background-color: #2b2d30;\n"
"    color: white;                               /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430*/\n"
"    font-family:  DejaVu Sans Mono ;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"/*\u041a\u0430\u043a \u0432\u044b\u0433\u043b\u044f\u0434\u044f\u0442 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0442\u0438\u043f\u0430 \"\u041e\u0446\u043f\u0438\u0438\" \u0438 \u0442\u0434*/\n"
"QMenuBar::item {\n"
"    padding: 5px 10px;                    /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    border: 1px solid transparent;  /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430"
                        "\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    margin: 0;                                    /* \u0412\u043d\u0435\u0448\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"\n"
"/* \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u043a\u0430\u043a \u0431\u0443\u0434\u0443\u0442 \u0432\u044b\u0433\u043b\u044f\u0434\u0435\u0442\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0442\u0438\u043f\u0430 \"\u041e\u0446\u043f\u0438\u0438\" \u0438 \u0442\u0434 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u043a\u0438*/\n"
"QMenuBar::item:selected {\n"
"    background-color: #3f4043;\n"
"    color: white;                               /* \u0427\u0451\u0440\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-family: DejaVu Sans Mono;\n"
"    padding: 5px 5px;                     /* \u041e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u044b\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"}\n"
"\n"
"/* \u0421"
                        "\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0440\u0430\u0441\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e\u0441\u044f QMenu */\n"
"QMenu {\n"
"    background-color: #2E2E2E;    /* \u041e\u043a\u043e\u043d\u0442\u043e\u0432\u043a\u0430 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u043c\u0435\u043d\u044e */\n"
"    color: black;                                /* \u0427\u0451\u0440\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043c\u0435\u043d\u044e */\n"
"    border: 1px solid  #555555;       /* \u0421\u0435\u0440\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 5px;                    /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 5px;                             /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"    font-family:  DejaVu Sans Mon"
                        "o;\n"
"}\n"
"\n"
"/*\u041a\u0430\u043a \u0432\u044b\u0433\u043b\u044f\u0434\u044f\u0442 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u0440\u0430\u0441\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e \u043c\u0435\u043d\u044e*/\n"
"QMenu::item {\n"
"    background-color: #2E2E2E;\n"
"    color: white;                               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    padding: 5px;                             /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f */\n"
"    border: 1px solid transparent;  /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430, \u0447\u0442\u043e\u0431\u044b \u0440\u0430\u0437\u043c\u0435\u0440 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430 \u043d\u0435 \u0438\u0437\u043c\u0435\u043d\u044f\u043b\u0441\u044f */\n"
"    border-radius: 4px;                    /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435"
                        " \u0443\u0433\u043b\u044b */\n"
"}\n"
"\n"
"/*\u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0440\u0430\u0441\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0435\u0433\u043e\u0441\u044f \u043c\u0435\u043d\u044e \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u043a\u0438*/\n"
"QMenu::item:selected {\n"
"    background-color: #2e436e;\n"
"    color: white;                                /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border: 1px;\n"
"    border-radius: 6px;                    /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432, \u0447\u0443\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 \u0447\u0435\u043c \u0432 QMenu, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u0431\u044b\u043b\u043e \u0441\u043a\u0430\u0447\u043a\u043e\u0432 */\n"
"    padding: 6px;                             /* \u0412\u043d\u0443"
                        "\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f, \u0447\u0443\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u0435 \u0447\u0435\u043c \u0432 QMenu, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u0431\u044b\u043b\u043e \u0441\u043a\u0430\u0447\u043a\u043e\u0432 */\n"
"}")
        MainWindow.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        self.action123_2 = QAction(MainWindow)
        self.action123_2.setObjectName(u"action123_2")
        self.other_button = QAction(MainWindow)
        self.other_button.setObjectName(u"other_button")
        self.tab_all_branches = QAction(MainWindow)
        self.tab_all_branches.setObjectName(u"tab_all_branches")
        self.tab_all_branches.setCheckable(False)
        self.tab_all_branches.setChecked(False)
        self.tab_all_branches.setEnabled(True)
        self.tab_rdv_scripts = QAction(MainWindow)
        self.tab_rdv_scripts.setObjectName(u"tab_rdv_scripts")
        self.tab_rdv_info = QAction(MainWindow)
        self.tab_rdv_info.setObjectName(u"tab_rdv_info")
        self.tab_rdv_psi = QAction(MainWindow)
        self.tab_rdv_psi.setObjectName(u"tab_rdv_psi")
        self.tab_rdv_instruction = QAction(MainWindow)
        self.tab_rdv_instruction.setObjectName(u"tab_rdv_instruction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.btn_execute_statement = QPushButton(self.centralwidget)
        self.btn_execute_statement.setObjectName(u"btn_execute_statement")
        self.btn_execute_statement.setGeometry(QRect(9, 157, 931, 31))
        self.btn_execute_statement.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50; /* \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 10px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 12px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388E3C; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438"
                        " \u043d\u0430\u0436\u0430\u0442\u0438\u0438 (\u0442\u0435\u043c\u043d\u0435\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e) */\n"
"    padding-left: 12px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043f\u0440\u0430\u0432\u043e \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-top: 12px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043d\u0438\u0437 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        self.txt_main_output_field = QPlainTextEdit(self.centralwidget)
        self.txt_main_output_field.setObjectName(u"txt_main_output_field")
        self.txt_main_output_field.setGeometry(QRect(634, 203, 306, 191))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(False)
        self.txt_main_output_field.setFont(font)
        self.txt_main_output_field.setStyleSheet(u"QPlainTextEdit{\n"
"    background-color: #3c3f41;\n"
"    color: #ffffff;\n"
"    border: 1px solid #555555;\n"
"    padding: 5px;\n"
"    font-family: Consolas, Courier, monospace;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #2E2E2E;  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    width: 10px;                 /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5E5E5E;  /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    min-height: 10px;\n"
"    border-radius: 0px;          /* \u041e\u0442"
                        "\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: #4A4A4A;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u0432\u0432\u0435\u0440\u0445 \u0438 \u0432\u043d\u0438\u0437 */\n"
"    height: 10px;               /* \u0420\u0430\u0437\u043c\u0435\u0440 \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;\n"
"    border-radius: 0px;          /* \u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: #6E6E6E;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a"
                        " \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: #2E2E2E;  /* \u0424\u043e\u043d \u043f\u0440\u0438 \u043f\u0443\u0441\u0442\u043e\u043c \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0435 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: #2E2E2E;  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    height: 10px;                /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b"
                        " \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #5E5E5E;  /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    min-width: 10px;\n"
"    border-radius: 0px;          /* \u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #4A4A4A;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u0432\u043b\u0435\u0432\u043e \u0438 \u0432\u043f\u0440\u0430\u0432\u043e */\n"
"    width: 10px;                /* \u0420\u0430\u0437\u043c\u0435\u0440 \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left;\n"
"    border-radius: 0px;          /* \u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438"
                        "\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color: #6E6E6E;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background-color: #2E2E2E;  /* \u0424\u043e\u043d \u043f\u0440\u0438 \u043f\u0443\u0441\u0442\u043e\u043c \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0435 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"}")
        self.txt_main_input_field = QPlainTextEdit(self.centralwidget)
        self.txt_main_input_field.setObjectName(u"txt_main_input_field")
        self.txt_main_input_field.setGeometry(QRect(322, 203, 306, 191))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        self.txt_main_input_field.setFont(font1)
        self.txt_main_input_field.setStyleSheet(u"QPlainTextEdit{\n"
"    background-color: #3c3f41;\n"
"    color: #ffffff;\n"
"    border: 1px solid #555555;\n"
"    padding: 5px;\n"
"    font-family: Consolas, Courier, monospace;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #2E2E2E;  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    width: 10px;                 /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5E5E5E;  /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    min-height: 10px;\n"
"    border-radius: 0px;          /* \u041e\u0442"
                        "\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: #4A4A4A;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u0432\u0432\u0435\u0440\u0445 \u0438 \u0432\u043d\u0438\u0437 */\n"
"    height: 10px;               /* \u0420\u0430\u0437\u043c\u0435\u0440 \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;\n"
"    border-radius: 0px;          /* \u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: #6E6E6E;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a"
                        " \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: #2E2E2E;  /* \u0424\u043e\u043d \u043f\u0440\u0438 \u043f\u0443\u0441\u0442\u043e\u043c \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0435 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: #2E2E2E;  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    height: 10px;                /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b"
                        " \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #5E5E5E;  /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    min-width: 10px;\n"
"    border-radius: 0px;          /* \u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #4A4A4A;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u0432\u043b\u0435\u0432\u043e \u0438 \u0432\u043f\u0440\u0430\u0432\u043e */\n"
"    width: 10px;                /* \u0420\u0430\u0437\u043c\u0435\u0440 \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left;\n"
"    border-radius: 0px;          /* \u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438"
                        "\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color: #6E6E6E;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background-color: #2E2E2E;  /* \u0424\u043e\u043d \u043f\u0440\u0438 \u043f\u0443\u0441\u0442\u043e\u043c \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0435 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"}")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(70, 238, 181, 131))
        self.plainTextEdit.setStyleSheet(u"            QPlainTextEdit{\n"
"                background-color: #3c3f41;\n"
"                color: #ffffff;\n"
"                border: 1px solid #555555;\n"
"                padding: 5px;\n"
"                font-family: Consolas, Courier, monospace;\n"
"                font-size: 12px;\n"
"            }")
        self.btn_clear_input_output_fields = QPushButton(self.centralwidget)
        self.btn_clear_input_output_fields.setObjectName(u"btn_clear_input_output_fields")
        self.btn_clear_input_output_fields.setGeometry(QRect(269, 203, 41, 21))
        self.btn_clear_input_output_fields.setStyleSheet(u"QPushButton {\n"
"    background-color: #3c3f41; /* \u0421\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438 3c3f41 */\n"
"    color: white; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 3px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 12px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0443\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #616161; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446"
                        "\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #424242; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 (\u0442\u0435\u043c\u043d\u0435\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e) */\n"
"    padding-left: 5px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043f\u0440\u0430\u0432\u043e \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-top: 5px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043d\u0438\u0437 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        self.input_chbx1_param1 = QPlainTextEdit(self.centralwidget)
        self.input_chbx1_param1.setObjectName(u"input_chbx1_param1")
        self.input_chbx1_param1.setGeometry(QRect(247, 120, 256, 29))
        self.input_chbx1_param1.setStyleSheet(u"            QPlainTextEdit{\n"
"                background-color: #3c3f41;\n"
"                color: #ffffff;\n"
"                border: 1px solid #555555;\n"
"            }")
        self.input_chbx1_param2 = QPlainTextEdit(self.centralwidget)
        self.input_chbx1_param2.setObjectName(u"input_chbx1_param2")
        self.input_chbx1_param2.setGeometry(QRect(509, 120, 256, 29))
        font2 = QFont()
        font2.setKerning(True)
        self.input_chbx1_param2.setFont(font2)
        self.input_chbx1_param2.setMouseTracking(False)
        self.input_chbx1_param2.setStyleSheet(u"            QPlainTextEdit{\n"
"                background-color: #3c3f41;\n"
"                color: #ffffff;\n"
"                border: 1px solid #555555;\n"
"            }")
        self.chbx_1_format_sql_query = QCheckBox(self.centralwidget)
        self.chbx_1_format_sql_query.setObjectName(u"chbx_1_format_sql_query")
        self.chbx_1_format_sql_query.setGeometry(QRect(14, 120, 227, 29))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(29, 30, 33, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.chbx_1_format_sql_query.setPalette(palette)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.chbx_1_format_sql_query.setFont(font3)
        self.chbx_1_format_sql_query.setTabletTracking(False)
        self.chbx_1_format_sql_query.setAcceptDrops(False)
        self.chbx_1_format_sql_query.setAutoFillBackground(False)
        self.chbx_1_format_sql_query.setStyleSheet(u"")
        self.chbx_1_format_sql_query.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.chbx_1_format_sql_query.setCheckable(True)
        self.chbx_1_format_sql_query.setChecked(False)
        self.chbx_1_format_sql_query.setAutoRepeat(False)
        self.chbx_1_format_sql_query.setAutoExclusive(False)
        self.chbx_1_format_sql_query.setTristate(False)
        self.btn_example_1_format_sql_query = QPushButton(self.centralwidget)
        self.btn_example_1_format_sql_query.setObjectName(u"btn_example_1_format_sql_query")
        self.btn_example_1_format_sql_query.setGeometry(QRect(771, 125, 46, 19))
        self.btn_example_1_format_sql_query.setStyleSheet(u"QPushButton {\n"
"    background-color: #4A4A4A; /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0444\u043e\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    color: #D3D3D3; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 3px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 10px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 1px solid #383838; /* \u0422\u043e\u043d\u043a\u0430\u044f \u0442\u0435\u043c\u043d\u0430\u044f \u0433\u0440\u0430\u043d"
                        "\u0438\u0446\u0430 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5C5C5C; /* \u0427\u0443\u0442\u044c \u0441\u0432\u0435\u0442\u043b\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3A3A3A; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-left: 5px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043f\u0440\u0430\u0432\u043e \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-top: 5px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043d\u0438\u0437 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 1px solid #2C2C2C; /* \u0411\u043e\u043b\u0435\u0435 \u0442\u0435\u043c\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442"
                        "\u0438\u0438 */\n"
"}\n"
"")
        self.btn_example_2_yaml_sql = QPushButton(self.centralwidget)
        self.btn_example_2_yaml_sql.setObjectName(u"btn_example_2_yaml_sql")
        self.btn_example_2_yaml_sql.setGeometry(QRect(771, 85, 46, 19))
        self.btn_example_2_yaml_sql.setStyleSheet(u"QPushButton {\n"
"    background-color: #4A4A4A; /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0444\u043e\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    color: #D3D3D3; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 3px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 10px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 1px solid #383838; /* \u0422\u043e\u043d\u043a\u0430\u044f \u0442\u0435\u043c\u043d\u0430\u044f \u0433\u0440\u0430\u043d"
                        "\u0438\u0446\u0430 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5C5C5C; /* \u0427\u0443\u0442\u044c \u0441\u0432\u0435\u0442\u043b\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3A3A3A; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-left: 5px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043f\u0440\u0430\u0432\u043e \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-top: 5px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043d\u0438\u0437 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 1px solid #2C2C2C; /* \u0411\u043e\u043b\u0435\u0435 \u0442\u0435\u043c\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442"
                        "\u0438\u0438 */\n"
"}\n"
"")
        self.chbx_2_yaml_sql = QCheckBox(self.centralwidget)
        self.chbx_2_yaml_sql.setObjectName(u"chbx_2_yaml_sql")
        self.chbx_2_yaml_sql.setGeometry(QRect(14, 86, 227, 16))
        palette1 = QPalette()
        brush3 = QBrush(QColor(224, 224, 224, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush4 = QBrush(QColor(224, 224, 224, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.chbx_2_yaml_sql.setPalette(palette1)
        self.chbx_2_yaml_sql.setStyleSheet(u"QCheckBox {\n"
"    color: #E0E0E0; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    spacing: 5px; /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u0444\u043b\u0430\u0436\u043a\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */\n"
"}\n"
"")
        self.input_chbx2_param2 = QPlainTextEdit(self.centralwidget)
        self.input_chbx2_param2.setObjectName(u"input_chbx2_param2")
        self.input_chbx2_param2.setGeometry(QRect(374, 80, 391, 29))
        self.input_chbx2_param2.setStyleSheet(u"            QPlainTextEdit{\n"
"                background-color: #3c3f41;\n"
"                color: #ffffff;\n"
"                border: 1px solid #555555;\n"
"            }")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(247, 80, 110, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.RadioBtn_chbx2_DAPP = QRadioButton(self.layoutWidget)
        self.RadioBtn_chbx2_DAPP.setObjectName(u"RadioBtn_chbx2_DAPP")

        self.horizontalLayout.addWidget(self.RadioBtn_chbx2_DAPP)

        self.RadioBtn_chbx2_RDV = QRadioButton(self.layoutWidget)
        self.RadioBtn_chbx2_RDV.setObjectName(u"RadioBtn_chbx2_RDV")

        self.horizontalLayout.addWidget(self.RadioBtn_chbx2_RDV)

        self.input_chbx3_param1 = QPlainTextEdit(self.centralwidget)
        self.input_chbx3_param1.setObjectName(u"input_chbx3_param1")
        self.input_chbx3_param1.setGeometry(QRect(534, 35, 231, 31))
        self.input_chbx3_param1.setMouseTracking(True)
        self.input_chbx3_param1.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.input_chbx3_param1.setStyleSheet(u"            QPlainTextEdit{\n"
"                background-color: #3c3f41;\n"
"                color: #ffffff;\n"
"                border: 1px solid #555555;\n"
"            }")
        self.input_chbx3_param1.setInputMethodHints(Qt.InputMethodHint.ImhMultiLine)
        self.input_chbx3_param1.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.btn_example_3_yaml_json = QPushButton(self.centralwidget)
        self.btn_example_3_yaml_json.setObjectName(u"btn_example_3_yaml_json")
        self.btn_example_3_yaml_json.setGeometry(QRect(771, 39, 46, 19))
        self.btn_example_3_yaml_json.setStyleSheet(u"QPushButton {\n"
"    background-color: #4A4A4A; /* \u041f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u043d\u044b\u0439 \u0441\u0435\u0440\u043e-\u0441\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u0444\u043e\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    color: #D3D3D3; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 3px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    font-size: 10px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border: 1px solid #383838; /* \u0422\u043e\u043d\u043a\u0430\u044f \u0442\u0435\u043c\u043d\u0430\u044f \u0433\u0440\u0430\u043d"
                        "\u0438\u0446\u0430 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5C5C5C; /* \u0427\u0443\u0442\u044c \u0441\u0432\u0435\u0442\u043b\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3A3A3A; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-left: 5px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043f\u0440\u0430\u0432\u043e \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-top: 5px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043d\u0438\u0437 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 1px solid #2C2C2C; /* \u0411\u043e\u043b\u0435\u0435 \u0442\u0435\u043c\u043d\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442"
                        "\u0438\u0438 */\n"
"}\n"
"")
        self.chbx_3_yaml_json = QCheckBox(self.centralwidget)
        self.chbx_3_yaml_json.setObjectName(u"chbx_3_yaml_json")
        self.chbx_3_yaml_json.setGeometry(QRect(14, 32, 113, 22))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.chbx_3_yaml_json.setPalette(palette2)
        self.chbx_3_yaml_json.setFont(font3)
        self.chbx_3_yaml_json.setTabletTracking(False)
        self.chbx_3_yaml_json.setAcceptDrops(False)
        self.chbx_3_yaml_json.setAutoFillBackground(False)
        self.chbx_3_yaml_json.setStyleSheet(u"")
        self.chbx_3_yaml_json.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.chbx_3_yaml_json.setCheckable(True)
        self.chbx_3_yaml_json.setChecked(False)
        self.chbx_3_yaml_json.setAutoRepeat(False)
        self.chbx_3_yaml_json.setAutoExclusive(False)
        self.chbx_3_yaml_json.setTristate(False)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(248, 18, 134, 54))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.RadioBtn_chbx3_Primary_Yes = QRadioButton(self.layoutWidget1)
        self.RadioBtn_chbx3_Primary_Yes.setObjectName(u"RadioBtn_chbx3_Primary_Yes")

        self.verticalLayout.addWidget(self.RadioBtn_chbx3_Primary_Yes)

        self.RadioBtn_chbx3_Primary_No = QRadioButton(self.layoutWidget1)
        self.RadioBtn_chbx3_Primary_No.setObjectName(u"RadioBtn_chbx3_Primary_No")

        self.verticalLayout.addWidget(self.RadioBtn_chbx3_Primary_No)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(485, 19, 47, 52))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RadioBtn_chbx3_Nullable_Yes = QRadioButton(self.layoutWidget2)
        self.RadioBtn_chbx3_Nullable_Yes.setObjectName(u"RadioBtn_chbx3_Nullable_Yes")

        self.verticalLayout_2.addWidget(self.RadioBtn_chbx3_Nullable_Yes)

        self.RadioBtn_chbx3_Nullable_No = QRadioButton(self.layoutWidget2)
        self.RadioBtn_chbx3_Nullable_No.setObjectName(u"RadioBtn_chbx3_Nullable_No")

        self.verticalLayout_2.addWidget(self.RadioBtn_chbx3_Nullable_No)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(397, 31, 81, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 36))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.rdv = QMenu(self.menu)
        self.rdv.setObjectName(u"rdv")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.tab_all_branches)
        self.menu.addSeparator()
        self.menu.addAction(self.rdv.menuAction())
        self.rdv.addAction(self.tab_rdv_scripts)
        self.rdv.addAction(self.tab_rdv_info)
        self.rdv.addAction(self.tab_rdv_instruction)
        self.rdv.addAction(self.tab_rdv_psi)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CEH", None))
        self.action123_2.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.other_button.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0449\u0435", None))
        self.tab_all_branches.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043c\u043e\u0438 \u0432\u0435\u0442\u043a\u0438", None))
        self.tab_rdv_scripts.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0441\u043a\u0440\u0438\u043f\u0442\u044b", None))
        self.tab_rdv_info.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u044b\u0435 \u0437\u0430\u044f\u0432\u043a\u0438", None))
        self.tab_rdv_psi.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0421\u0418 \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.tab_rdv_instruction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438 \u0438 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.btn_execute_statement.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.txt_main_output_field.setPlainText("")
        self.btn_clear_input_output_fields.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.input_chbx1_param1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430", None))
        self.input_chbx1_param2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u043e \u0446\u0435\u043d\u0442\u0440\u0443 (default = 4)", None))
        self.chbx_1_format_sql_query.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 SQL \u0437\u0430\u043f\u0440\u043e\u0441\u0430", None))
        self.btn_example_1_format_sql_query.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.btn_example_2_yaml_sql.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.chbx_2_yaml_sql.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437 YAML \u0432 SQL                                             ", None))
        self.input_chbx2_param2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0432\u0438\u0442\u0440\u0438\u043d\u044b (default = \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435\u0422\u0430\u0431\u043b\u0438\u0446\u044b)", None))
        self.RadioBtn_chbx2_DAPP.setText(QCoreApplication.translate("MainWindow", u"DAPP", None))
        self.RadioBtn_chbx2_RDV.setText(QCoreApplication.translate("MainWindow", u"RDV", None))
        self.input_chbx3_param1.setPlainText("")
        self.input_chbx3_param1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430 (default=8) \u0414\u043b\u044f \u0440\u0435\u0441\u0443\u0440c\u0430 Ok", None))
        self.btn_example_3_yaml_json.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u0440", None))
        self.chbx_3_yaml_json.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437 YAML \u0432 JSON", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c\n"
"\"primary_key\"?", None))
        self.RadioBtn_chbx3_Primary_Yes.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.RadioBtn_chbx3_Primary_No.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.RadioBtn_chbx3_Nullable_Yes.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.RadioBtn_chbx3_Nullable_No.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0435\u0441\u043b\u0438\n"
"\u043d\u0435\u0442 \"nullable\"?", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0446\u0438\u0438", None))
        self.rdv.setTitle(QCoreApplication.translate("MainWindow", u"RDV", None))
    # retranslateUi

