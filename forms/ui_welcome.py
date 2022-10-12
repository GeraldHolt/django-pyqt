# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_WelcomeForm(object):
    def setupUi(self, WelcomeForm):
        if not WelcomeForm.objectName():
            WelcomeForm.setObjectName(u"WelcomeForm")
        WelcomeForm.resize(997, 595)
        icon = QIcon()
        icon.addFile(u"../resources/icons/HCE-C.svg", QSize(), QIcon.Normal, QIcon.Off)
        WelcomeForm.setWindowIcon(icon)
        self.logoFrame = QFrame(WelcomeForm)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setGeometry(QRect(10, 10, 981, 571))
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.logoFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 60, 271, 281))
        self.label.setPixmap(QPixmap(u"../resources/assets/HCE-C.png"))
        self.btnLogin = QPushButton(self.logoFrame)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(230, 440, 521, 31))
        self.btnLogin.setStyleSheet(u"   QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(0, 255, 255) );\n"
"\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1  rgb(0, 255, 255));\n"
"     }")
        self.btnRegister = QPushButton(self.logoFrame)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setGeometry(QRect(230, 520, 521, 31))
        self.btnRegister.setStyleSheet(u"   QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(0, 255, 255) );\n"
"\n"
"     }\n"
"\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 rgb(0, 255, 255));\n"
"     }")

        self.retranslateUi(WelcomeForm)

        QMetaObject.connectSlotsByName(WelcomeForm)
    # setupUi

    def retranslateUi(self, WelcomeForm):
        WelcomeForm.setWindowTitle(QCoreApplication.translate("WelcomeForm", u"Form", None))
        self.label.setText("")
        self.btnLogin.setText(QCoreApplication.translate("WelcomeForm", u"Log in", None))
        self.btnRegister.setText(QCoreApplication.translate("WelcomeForm", u"Create New Account", None))
    # retranslateUi

