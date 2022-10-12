# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'worksorder_selector.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SelectWorksorder(object):
    def setupUi(self, SelectWorksorder):
        if not SelectWorksorder.objectName():
            SelectWorksorder.setObjectName(u"SelectWorksorder")
        SelectWorksorder.resize(400, 255)
        self.frame = QFrame(SelectWorksorder)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 60, 371, 181))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnConfirm = QPushButton(self.frame)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setGeometry(QRect(20, 130, 75, 31))
        self.btnConfirm.setStyleSheet(u"   QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(43, 200, 7));\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.btnCancel = QPushButton(self.frame)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setGeometry(QRect(280, 130, 75, 31))
        self.btnCancel.setStyleSheet(u"    QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(255, 0, 0));\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 281, 20))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cbWorksorders = QComboBox(self.frame)
        self.cbWorksorders.setObjectName(u"cbWorksorders")
        self.cbWorksorders.setGeometry(QRect(10, 60, 351, 31))
        self.cbWorksorders.setStyleSheet(u"QComboBox{\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    background: white;\n"
"    border: 1px solid gray;\n"
"    box-shadow: transparent;\n"
"	padding: 1px 18px 1px 3px;\n"
"   \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 20px;\n"
"\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 10px;\n"
" }\n"
"\n"
"QComboBox::down-arrow {\n"
"     image:url(:/icons/icons/arrow-down.svg)\n"
" }\n"
"\n"
" QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"     top: 1px;\n"
"     left: 1px;\n"
" }\n"
"\n"
"")
        self.label_18 = QLabel(SelectWorksorder)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(100, 20, 221, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.retranslateUi(SelectWorksorder)

        QMetaObject.connectSlotsByName(SelectWorksorder)
    # setupUi

    def retranslateUi(self, SelectWorksorder):
        SelectWorksorder.setWindowTitle(QCoreApplication.translate("SelectWorksorder", u"SelectWorksorder", None))
        self.btnConfirm.setText(QCoreApplication.translate("SelectWorksorder", u"Confirm", None))
        self.btnCancel.setText(QCoreApplication.translate("SelectWorksorder", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("SelectWorksorder", u"Select the worksorder package to proceed with:", None))
        self.label_18.setText(QCoreApplication.translate("SelectWorksorder", u"WORKSORDERS", None))
    # retranslateUi

