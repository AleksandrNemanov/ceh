# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_rdv_adgp.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_RdvADGP(object):
    def setupUi(self, RdvADGP):
        if not RdvADGP.objectName():
            RdvADGP.setObjectName(u"RdvADGP")
        RdvADGP.resize(634, 542)
        RdvADGP.setStyleSheet(u"QWidget {\n"
"    background-color: #1d1e21;\n"
"    color: #D0D0D0;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 10.5pt;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit, QTextEdit {\n"
"    background-color: #292929;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #E0E0E0;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus {\n"
"    border: 1px solid #666666;\n"
"}\n"
"\n"
"\n"
"\n"
"/* \u0413\u0440\u0443\u043f\u043f\u044b */\n"
"QGroupBox {\n"
"    border: 1px solid #444444;\n"
"    border-radius: 4px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 4px;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #A0A0A0;\n"
"}\n"
"\n"
"\n"
"\n"
"/* \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #222222;\n"
"    widt"
                        "h: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #505050;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2E2E2E; /* \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: #D0D0D0;\n"
"    border-radius: 5px; /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 3px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"    text-align: left;\n"
"    padding-left: 5px;\n"
"    border: 1px solid #2c3e35;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #292929; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438"
                        " \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #505050; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 (\u0442\u0435\u043c\u043d\u0435\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e)232323 */\n"
"    padding-left: 4px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043f\u0440\u0430\u0432\u043e \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-top: 8px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043d\u0438\u0437 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"QPlainTextEdit{\n"
"  background-color: #3c3f41;\n"
"  color: #ffffff;\n"
"  border: 1px solid #444444;\n"
"  padding: 2px 1px;\n"
"\n"
"}\n"
"")
        self.pushButton = QPushButton(RdvADGP)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(35, 165, 310, 30))
        self.pushButton_2 = QPushButton(RdvADGP)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(35, 205, 310, 30))
        self.pushButton_3 = QPushButton(RdvADGP)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(35, 245, 310, 30))
        self.pushButton_4 = QPushButton(RdvADGP)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(35, 115, 271, 31))
        self.pushButton_4.setStyleSheet(u"")
        self.pushButton_5 = QPushButton(RdvADGP)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(35, 285, 310, 30))
        self.pushButton_6 = QPushButton(RdvADGP)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(35, 325, 310, 30))
        self.pushButton_7 = QPushButton(RdvADGP)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(35, 365, 310, 30))
        self.pushButton_8 = QPushButton(RdvADGP)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(35, 405, 310, 30))
        self.pushButton_9 = QPushButton(RdvADGP)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(35, 445, 310, 30))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #292929; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    background-image: linear-gradient(to bottom, #444444, #292929); /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0433\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #505050; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    background-image: linear-gradient(to bottom, #2E2E2E, #232323); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 \u0437\u0430\u0442\u0435\u043c\u043d\u0435\u043d\u0438\u044f */\n"
"    box-shadow: inset 0px 3px 5px rgba(0, 0, 0, 0.5); /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u044f\u044f \u0442\u0435\u043d\u044c \u0434"
                        "\u043b\u044f \u044d\u0444\u0444\u0435\u043a\u0442\u0430 \u0432\u0434\u0430\u0432\u043b\u0438\u0432\u0430\u043d\u0438\u044f */\n"
"    padding-left: 4px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043f\u0440\u0430\u0432\u043e \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-top: 4px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043d\u0438\u0437 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        self.pushButton_10 = QPushButton(RdvADGP)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(380, 225, 151, 31))
        self.pushButton_10.setStyleSheet(u"text-align: center;")
        self.label = QLabel(RdvADGP)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 115, 191, 21))
        self.pushButton_11 = QPushButton(RdvADGP)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(550, 225, 61, 31))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    text-align: center;\n"
"}")
        self.checkBox_3 = QCheckBox(RdvADGP)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 170, 21, 22))
        self.checkBox_4 = QCheckBox(RdvADGP)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(10, 210, 21, 22))
        self.checkBox_5 = QCheckBox(RdvADGP)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(10, 250, 21, 22))
        self.checkBox_6 = QCheckBox(RdvADGP)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(10, 290, 21, 22))
        self.checkBox_7 = QCheckBox(RdvADGP)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(10, 330, 21, 22))
        self.checkBox_8 = QCheckBox(RdvADGP)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(10, 370, 21, 22))
        self.checkBox_9 = QCheckBox(RdvADGP)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(10, 410, 21, 22))
        self.checkBox_10 = QCheckBox(RdvADGP)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(10, 450, 21, 22))
        self.checkBox = QCheckBox(RdvADGP)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(353, 20, 21, 22))
        self.plainTextEdit = QPlainTextEdit(RdvADGP)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(380, 145, 151, 31))
        self.plainTextEdit_2 = QPlainTextEdit(RdvADGP)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(380, 185, 151, 31))
        self.plainTextEdit_3 = QPlainTextEdit(RdvADGP)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(180, 55, 361, 31))
        self.plainTextEdit_3.setStyleSheet(u"")
        self.plainTextEdit_4 = QPlainTextEdit(RdvADGP)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(380, 15, 241, 31))
        self.plainTextEdit_5 = QPlainTextEdit(RdvADGP)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(180, 15, 171, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_5.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_5.setSizePolicy(sizePolicy)
        self.plainTextEdit_6 = QPlainTextEdit(RdvADGP)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(10, 15, 161, 31))
        sizePolicy.setHeightForWidth(self.plainTextEdit_6.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_6.setSizePolicy(sizePolicy)
        self.plainTextEdit_7 = QPlainTextEdit(RdvADGP)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setGeometry(QRect(10, 55, 111, 31))
        sizePolicy.setHeightForWidth(self.plainTextEdit_7.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_7.setSizePolicy(sizePolicy)
        self.checkBox_11 = QCheckBox(RdvADGP)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setGeometry(QRect(10, 120, 21, 22))
        self.plainTextEdit_8 = QPlainTextEdit(RdvADGP)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setGeometry(QRect(380, 265, 231, 210))
        self.plainTextEdit_8.setStyleSheet(u"QPlainTextEdit{\n"
"    background-color: #3c3f41;\n"
"    color: #ffffff;\n"
"    border: 1px solid #555555;\n"
"    padding: 5px;\n"
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
"    border-radius: 0px;          /* \u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0440"
                        "\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
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
"    background-color: #6E6E6E;  /* \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438"
                        " */\n"
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
"    height: 10px;                /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    ma"
                        "rgin: 0px 0px 0px 0px;\n"
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
"    border-radius: 0px;          /* \u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438"
                        "\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
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
        self.pushButton_12 = QPushButton(RdvADGP)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(550, 55, 71, 31))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    text-align: center;\n"
"}")
        self.pushButton_13 = QPushButton(RdvADGP)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(130, 55, 41, 31))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"    text-align: center;\n"
"}")
        self.pushButton_14 = QPushButton(RdvADGP)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(35, 495, 310, 30))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"    font-family: Arial, sans-serif; /* \u0428\u0440\u0438\u0444\u0442 */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #292929; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    background-image: linear-gradient(to bottom, #444444, #292929); /* \u0411\u043e\u043b\u0435\u0435 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0433\u0440\u0430\u0434\u0438\u0435\u043d\u0442 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #505050; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    background-image: linear-gradient(to bottom, #2E2E2E, #232323); /* \u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442 \u0437\u0430\u0442\u0435\u043c\u043d\u0435\u043d\u0438\u044f */\n"
"    box-shadow: inset 0px 3px 5px rgba(0, 0, 0, 0.5); /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u044f\u044f \u0442\u0435\u043d\u044c \u0434"
                        "\u043b\u044f \u044d\u0444\u0444\u0435\u043a\u0442\u0430 \u0432\u0434\u0430\u0432\u043b\u0438\u0432\u0430\u043d\u0438\u044f */\n"
"    padding-left: 4px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043f\u0440\u0430\u0432\u043e \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    padding-top: 4px; /* \u0421\u0434\u0432\u0438\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u043d\u0438\u0437 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        self.plainTextEdit_9 = QPlainTextEdit(RdvADGP)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setGeometry(QRect(380, 495, 231, 31))
        self.checkBox_13 = QCheckBox(RdvADGP)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setGeometry(QRect(10, 500, 21, 22))
        self.frame = QFrame(RdvADGP)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(370, 105, 251, 375))
        self.frame.setStyleSheet(u" border: 1px solid #444444;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(RdvADGP)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(2, 105, 351, 375))
        self.frame_2.setStyleSheet(u" border: 1px solid #444444;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 351, 51))
        self.frame_4.setStyleSheet(u" border: 1px solid #444444;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(RdvADGP)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(2, 489, 621, 42))
        self.frame_3.setStyleSheet(u" border: 1px solid #444444;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.plainTextEdit_5.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.label.raise_()
        self.pushButton_11.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.checkBox_7.raise_()
        self.checkBox_8.raise_()
        self.checkBox_9.raise_()
        self.checkBox_10.raise_()
        self.checkBox.raise_()
        self.plainTextEdit.raise_()
        self.plainTextEdit_2.raise_()
        self.plainTextEdit_3.raise_()
        self.plainTextEdit_4.raise_()
        self.plainTextEdit_6.raise_()
        self.plainTextEdit_7.raise_()
        self.checkBox_11.raise_()
        self.plainTextEdit_8.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.plainTextEdit_9.raise_()
        self.checkBox_13.raise_()

        self.retranslateUi(RdvADGP)

        QMetaObject.connectSlotsByName(RdvADGP)
    # setupUi

    def retranslateUi(self, RdvADGP):
        RdvADGP.setWindowTitle(QCoreApplication.translate("RdvADGP", u"RDV ADGP", None))
        self.pushButton.setText(QCoreApplication.translate("RdvADGP", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0439 \u0441\u0431\u043e\u0440\u043a\u0438 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.pushButton_2.setText(QCoreApplication.translate("RdvADGP", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u043d\u043e\u0432\u043e\u0439 \u0441\u0431\u043e\u0440\u043a\u0438 \u0444\u0430\u0439\u043b\u043e\u0432", None))
        self.pushButton_3.setText(QCoreApplication.translate("RdvADGP", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u044e\u044e \u0441\u0431\u043e\u0440\u043a\u0443", None))
        self.pushButton_4.setText(QCoreApplication.translate("RdvADGP", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0432\u0441\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043d\u0438\u0436\u0435", None))
        self.pushButton_5.setText(QCoreApplication.translate("RdvADGP", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c rollback \u0438\u0437 \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f", None))
        self.pushButton_6.setText(QCoreApplication.translate("RdvADGP", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c logicalFilePath", None))
        self.pushButton_7.setText(QCoreApplication.translate("RdvADGP", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c ids", None))
        self.pushButton_8.setText(QCoreApplication.translate("RdvADGP", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c author", None))
        self.pushButton_9.setText(QCoreApplication.translate("RdvADGP", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b \u0441\u0431\u043e\u0440\u043a\u0438 \u0432 changelogs/current", None))
        self.pushButton_10.setText(QCoreApplication.translate("RdvADGP", u"\u0417\u0430\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("RdvADGP", u"\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438 \u0437\u0430\u043c\u0435\u043d\u0443 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.pushButton_11.setText(QCoreApplication.translate("RdvADGP", u"clear", None))
        self.checkBox_3.setText("")
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.checkBox_6.setText("")
        self.checkBox_7.setText("")
        self.checkBox_8.setText("")
        self.checkBox_9.setText("")
        self.checkBox_10.setText("")
        self.checkBox.setText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"\u041d\u043e\u0432\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"\u0421\u0442\u0430\u0440\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0440\u0442\u0430", None))
        self.plainTextEdit_4.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"\u041c\u0435\u0441\u0442\u043e\u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0440\u0435\u043f\u043e\u0437\u0438\u0442\u043e\u0440\u0438\u044f", None))
        self.plainTextEdit_5.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"Password \u0412\u0420\u041c", None))
        self.plainTextEdit_6.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"User \u0412\u0420\u041c", None))
        self.plainTextEdit_7.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"\u2116 Story", None))
        self.checkBox_11.setText("")
        self.plainTextEdit_8.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"\u0412\u044b\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.pushButton_12.setText(QCoreApplication.translate("RdvADGP", u"clear", None))
        self.pushButton_13.setText(QCoreApplication.translate("RdvADGP", u"clear", None))
        self.pushButton_14.setText(QCoreApplication.translate("RdvADGP", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0430\u043a\u043a\u0441\u0435\u0441\u0441\u043e\u0440\u044b \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.plainTextEdit_9.setPlaceholderText(QCoreApplication.translate("RdvADGP", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
        self.checkBox_13.setText("")
    # retranslateUi

