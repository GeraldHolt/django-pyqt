# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(420, 595)
        icon = QIcon()
        icon.addFile(u"../resources/icons/HCE-C.svg", QSize(), QIcon.Normal, QIcon.Off)
        LoginForm.setWindowIcon(icon)
        self.logoFrame = QFrame(LoginForm)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setGeometry(QRect(10, 10, 401, 131))
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)
        self.lbLogo = QLabel(self.logoFrame)
        self.lbLogo.setObjectName(u"lbLogo")
        self.lbLogo.setGeometry(QRect(40, 20, 301, 91))
        self.lbLogo.setPixmap(QPixmap(u"../resources/assets/HCE-logo.jpg"))
        self.lbLogo.setScaledContents(True)
        self.loginFrame = QFrame(LoginForm)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setGeometry(QRect(10, 150, 401, 431))
        self.loginFrame.setFrameShape(QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.loginFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(16, 20, 371, 20))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.loginBlock = QFrame(self.loginFrame)
        self.loginBlock.setObjectName(u"loginBlock")
        self.loginBlock.setGeometry(QRect(10, 70, 371, 331))
        self.loginBlock.setStyleSheet(u"QFrame {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.loginBlock.setFrameShape(QFrame.StyledPanel)
        self.loginBlock.setFrameShadow(QFrame.Raised)
        self.leUserName = QLineEdit(self.loginBlock)
        self.leUserName.setObjectName(u"leUserName")
        self.leUserName.setGeometry(QRect(10, 40, 351, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.leUserName.setFont(font1)
        self.leUserName.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lePassword = QLineEdit(self.loginBlock)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setGeometry(QRect(10, 110, 351, 31))
        self.lePassword.setFont(font1)
        self.lePassword.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lePassword.setEchoMode(QLineEdit.Password)
        self.lbUserName = QLabel(self.loginBlock)
        self.lbUserName.setObjectName(u"lbUserName")
        self.lbUserName.setGeometry(QRect(20, 20, 341, 20))
        font2 = QFont()
        font2.setKerning(False)
        self.lbUserName.setFont(font2)
        self.lbUserName.setStyleSheet(u"border: 0px")
        self.lbUserName.setLineWidth(0)
        self.lbPassword = QLabel(self.loginBlock)
        self.lbPassword.setObjectName(u"lbPassword")
        self.lbPassword.setGeometry(QRect(20, 90, 341, 20))
        self.lbPassword.setFont(font2)
        self.lbPassword.setStyleSheet(u"border: 0px")
        self.lbPassword.setLineWidth(0)
        self.btnLogin = QPushButton(self.loginBlock)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(130, 210, 101, 31))
        self.btnLogin.setStyleSheet(u"   QPushButton {\n"
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
        self.lbForgotpass = QLabel(self.loginBlock)
        self.lbForgotpass.setObjectName(u"lbForgotpass")
        self.lbForgotpass.setGeometry(QRect(20, 270, 91, 20))
        self.lbForgotpass.setFont(font2)
        self.lbForgotpass.setStyleSheet(u"border: 0px")
        self.lbForgotpass.setLineWidth(0)
        self.btnForgotpass = QPushButton(self.loginBlock)
        self.btnForgotpass.setObjectName(u"btnForgotpass")
        self.btnForgotpass.setEnabled(True)
        self.btnForgotpass.setGeometry(QRect(20, 290, 31, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnForgotpass.sizePolicy().hasHeightForWidth())
        self.btnForgotpass.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.btnForgotpass.setFont(font3)
        self.btnForgotpass.setToolTipDuration(0)
        self.btnForgotpass.setLayoutDirection(Qt.LeftToRight)
        self.btnForgotpass.setAutoFillBackground(False)
        self.btnForgotpass.setInputMethodHints(Qt.ImhNone)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnForgotpass.setIcon(icon1)
        self.btnForgotpass.setIconSize(QSize(24, 24))
        self.btnForgotpass.setCheckable(False)
        self.btnForgotpass.setFlat(False)
        self.btnRegister = QPushButton(self.loginBlock)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setEnabled(True)
        self.btnRegister.setGeometry(QRect(320, 290, 31, 31))
        sizePolicy.setHeightForWidth(self.btnRegister.sizePolicy().hasHeightForWidth())
        self.btnRegister.setSizePolicy(sizePolicy)
        self.btnRegister.setFont(font3)
        self.btnRegister.setToolTipDuration(0)
        self.btnRegister.setLayoutDirection(Qt.LeftToRight)
        self.btnRegister.setAutoFillBackground(False)
        self.btnRegister.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRegister.setIcon(icon2)
        self.btnRegister.setIconSize(QSize(24, 24))
        self.btnRegister.setCheckable(False)
        self.btnRegister.setFlat(False)
        self.lbRegister = QLabel(self.loginBlock)
        self.lbRegister.setObjectName(u"lbRegister")
        self.lbRegister.setGeometry(QRect(300, 270, 51, 20))
        self.lbRegister.setFont(font2)
        self.lbRegister.setStyleSheet(u"border: 0px")
        self.lbRegister.setLineWidth(0)
        self.lbInvalid = QLabel(self.loginBlock)
        self.lbInvalid.setObjectName(u"lbInvalid")
        self.lbInvalid.setGeometry(QRect(20, 150, 321, 20))
        self.lbInvalid.setFont(font2)
        self.lbInvalid.setStyleSheet(u"border: 0px")
        self.lbInvalid.setLineWidth(0)
        self.lbInvalid.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.loginFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 410, 381, 20))
        font4 = QFont()
        font4.setPointSize(8)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.lbLogo.setText("")
        self.label.setText(QCoreApplication.translate("LoginForm", u"Log in to continue to HCE EEMS System", None))
        self.lbUserName.setText(QCoreApplication.translate("LoginForm", u"Username", None))
        self.lbPassword.setText(QCoreApplication.translate("LoginForm", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginForm", u"Log In", None))
        self.lbForgotpass.setText(QCoreApplication.translate("LoginForm", u"Forgot password?", None))
#if QT_CONFIG(tooltip)
        self.btnForgotpass.setToolTip(QCoreApplication.translate("LoginForm", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnForgotpass.setText("")
#if QT_CONFIG(tooltip)
        self.btnRegister.setToolTip(QCoreApplication.translate("LoginForm", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnRegister.setText("")
        self.lbRegister.setText(QCoreApplication.translate("LoginForm", u"Register", None))
        self.lbInvalid.setText("")
        self.label_2.setText(QCoreApplication.translate("LoginForm", u" 2022 Developed by HCE", None))
    # retranslateUi

