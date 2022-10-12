# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_SignupForm(object):
    def setupUi(self, SignupForm):
        if not SignupForm.objectName():
            SignupForm.setObjectName(u"SignupForm")
        SignupForm.resize(420, 595)
        icon = QIcon()
        icon.addFile(u"../resources/icons/HCE-C.svg", QSize(), QIcon.Normal, QIcon.Off)
        SignupForm.setWindowIcon(icon)
        self.logoFrame = QFrame(SignupForm)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setGeometry(QRect(10, 10, 401, 131))
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)
        self.lbLogo = QLabel(self.logoFrame)
        self.lbLogo.setObjectName(u"lbLogo")
        self.lbLogo.setGeometry(QRect(110, 0, 181, 121))
        self.lbLogo.setPixmap(QPixmap(u"Z:/__CUSTOMER LOGOS/HCE.png"))
        self.lbLogo_2 = QLabel(self.logoFrame)
        self.lbLogo_2.setObjectName(u"lbLogo_2")
        self.lbLogo_2.setGeometry(QRect(50, 20, 301, 91))
        self.lbLogo_2.setPixmap(QPixmap(u"../resources/assets/HCE-logo.jpg"))
        self.lbLogo_2.setScaledContents(True)
        self.registerFrame = QFrame(SignupForm)
        self.registerFrame.setObjectName(u"registerFrame")
        self.registerFrame.setGeometry(QRect(10, 150, 401, 431))
        self.registerFrame.setFrameShape(QFrame.StyledPanel)
        self.registerFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.registerFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(16, 20, 371, 20))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.registerBlock = QFrame(self.registerFrame)
        self.registerBlock.setObjectName(u"registerBlock")
        self.registerBlock.setGeometry(QRect(10, 70, 371, 331))
        self.registerBlock.setStyleSheet(u"QFrame {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.registerBlock.setFrameShape(QFrame.StyledPanel)
        self.registerBlock.setFrameShadow(QFrame.Raised)
        self.leEmail = QLineEdit(self.registerBlock)
        self.leEmail.setObjectName(u"leEmail")
        self.leEmail.setGeometry(QRect(10, 90, 351, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.leEmail.setFont(font1)
        self.leEmail.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lePassword = QLineEdit(self.registerBlock)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setGeometry(QRect(10, 150, 351, 31))
        self.lePassword.setFont(font1)
        self.lePassword.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lePassword.setEchoMode(QLineEdit.Password)
        self.lbEmail = QLabel(self.registerBlock)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setGeometry(QRect(20, 70, 341, 20))
        font2 = QFont()
        font2.setKerning(False)
        self.lbEmail.setFont(font2)
        self.lbEmail.setStyleSheet(u"border: 0px")
        self.lbEmail.setLineWidth(0)
        self.lbPassword = QLabel(self.registerBlock)
        self.lbPassword.setObjectName(u"lbPassword")
        self.lbPassword.setGeometry(QRect(20, 130, 341, 20))
        self.lbPassword.setFont(font2)
        self.lbPassword.setStyleSheet(u"border: 0px")
        self.lbPassword.setLineWidth(0)
        self.btnRegister = QPushButton(self.registerBlock)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setGeometry(QRect(130, 290, 101, 31))
        self.btnRegister.setStyleSheet(u"   QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(0, 0, 223) );\n"
"\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.lbConfirmpass = QLabel(self.registerBlock)
        self.lbConfirmpass.setObjectName(u"lbConfirmpass")
        self.lbConfirmpass.setGeometry(QRect(20, 190, 341, 20))
        self.lbConfirmpass.setFont(font2)
        self.lbConfirmpass.setStyleSheet(u"border: 0px")
        self.lbConfirmpass.setLineWidth(0)
        self.leConfirmpass = QLineEdit(self.registerBlock)
        self.leConfirmpass.setObjectName(u"leConfirmpass")
        self.leConfirmpass.setGeometry(QRect(10, 210, 351, 31))
        self.leConfirmpass.setFont(font1)
        self.leConfirmpass.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leConfirmpass.setEchoMode(QLineEdit.Password)
        self.lbInvalid = QLabel(self.registerBlock)
        self.lbInvalid.setObjectName(u"lbInvalid")
        self.lbInvalid.setGeometry(QRect(20, 260, 321, 20))
        self.lbInvalid.setFont(font2)
        self.lbInvalid.setStyleSheet(u"border: 0px")
        self.lbInvalid.setLineWidth(0)
        self.lbInvalid.setAlignment(Qt.AlignCenter)
        self.leUserName = QLineEdit(self.registerBlock)
        self.leUserName.setObjectName(u"leUserName")
        self.leUserName.setGeometry(QRect(10, 30, 351, 31))
        self.leUserName.setFont(font1)
        self.leUserName.setMouseTracking(True)
        self.leUserName.setFocusPolicy(Qt.ClickFocus)
        self.leUserName.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbLastName = QLabel(self.registerBlock)
        self.lbLastName.setObjectName(u"lbLastName")
        self.lbLastName.setGeometry(QRect(20, 10, 341, 20))
        self.lbLastName.setFont(font2)
        self.lbLastName.setStyleSheet(u"border: 0px")
        self.lbLastName.setLineWidth(0)
        self.label_2 = QLabel(self.registerFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 410, 381, 20))
        font3 = QFont()
        font3.setPointSize(8)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(SignupForm)

        QMetaObject.connectSlotsByName(SignupForm)
    # setupUi

    def retranslateUi(self, SignupForm):
        SignupForm.setWindowTitle(QCoreApplication.translate("SignupForm", u"Form", None))
        self.lbLogo.setText("")
        self.lbLogo_2.setText("")
        self.label.setText(QCoreApplication.translate("SignupForm", u"Register to continue to HCE EEMS System", None))
        self.lbEmail.setText(QCoreApplication.translate("SignupForm", u"Email Address", None))
        self.lbPassword.setText(QCoreApplication.translate("SignupForm", u"Password", None))
        self.btnRegister.setText(QCoreApplication.translate("SignupForm", u"Register", None))
        self.lbConfirmpass.setText(QCoreApplication.translate("SignupForm", u"Confirm Password", None))
        self.lbInvalid.setText(QCoreApplication.translate("SignupForm", u"Invalid Email or Password", None))
        self.lbLastName.setText(QCoreApplication.translate("SignupForm", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("SignupForm", u" 2022 Developed by HCE", None))
    # retranslateUi

