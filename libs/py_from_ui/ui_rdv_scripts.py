# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_rdv_scripts.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QPlainTextEdit, QSizePolicy, QWidget)

class Ui_RdvScripts(object):
    def setupUi(self, RdvScripts):
        if not RdvScripts.objectName():
            RdvScripts.setObjectName(u"RdvScripts")
        RdvScripts.resize(598, 239)
        icon = QIcon()
        icon.addFile(u"icons/rdv_scripts.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        RdvScripts.setWindowIcon(icon)
        self.gridLayout = QGridLayout(RdvScripts)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chbx_wrap = QCheckBox(RdvScripts)
        self.chbx_wrap.setObjectName(u"chbx_wrap")

        self.gridLayout.addWidget(self.chbx_wrap, 0, 0, 1, 1)

        self.txt_input_field = QPlainTextEdit(RdvScripts)
        self.txt_input_field.setObjectName(u"txt_input_field")
        self.txt_input_field.setStyleSheet(u"QPlainTextEdit {\n"
"    border: none;  /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0440\u0430\u043c\u043a\u0438 */\n"
"    outline: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0441\u0438\u043d\u0438\u0435 \u043b\u0438\u043d\u0438\u0438 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"    background-color: #2E2E2E; /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #C5C5C5; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #2E2E2E;  /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    width: 10px;                /* \u0428\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442"
                        "\u043a\u0438 */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5E5E5E;  /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    min-height: 10px;\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: #4A4A4A;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u0432\u0432\u0435\u0440\u0445 \u0438 \u0432\u043d\u0438\u0437 */\n"
"    height: 15px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;\n"
"    border-radius: 4px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::sub-line:vertic"
                        "al:hover {\n"
"    background-color: #6E6E6E;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
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
"    height: 10px;               /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0433"
                        "\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #5E5E5E;  /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    min-width: 10px;\n"
"    border-radius: 5px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #4A4A4A;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u0432\u043b\u0435\u0432\u043e \u0438 \u0432\u043f\u0440\u0430\u0432\u043e */\n"
"    width: 15px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left;\n"
"    border-radius: 4px;         /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435"
                        "\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043a\u043d\u043e\u043f\u043e\u043a */\n"
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
"}\n"
"")

        self.gridLayout.addWidget(self.txt_input_field, 1, 0, 1, 1)


        self.retranslateUi(RdvScripts)

        QMetaObject.connectSlotsByName(RdvScripts)
    # setupUi

    def retranslateUi(self, RdvScripts):
        RdvScripts.setWindowTitle(QCoreApplication.translate("RdvScripts", u"RDV Scripts", None))
        self.chbx_wrap.setText(QCoreApplication.translate("RdvScripts", u"Wrap", None))
        self.txt_input_field.setPlainText("")
        self.txt_input_field.setPlaceholderText(QCoreApplication.translate("RdvScripts", u"\u041f\u043e\u043b\u0435\u0437\u043d\u044b\u0435 \u0441\u043a\u0440\u0438\u043f\u0442\u044b \u0434\u043b\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f RDV \u043f\u043e\u0442\u043e\u043a\u0430", None))
    # retranslateUi

