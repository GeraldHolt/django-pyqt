# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\_EEMS\forms\pop_up_message.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopUpMessage(object):
    def setupUi(self, PopUpMessage):
        PopUpMessage.setObjectName("PopUpMessage")
        PopUpMessage.resize(400, 255)
        self.frame = QtWidgets.QFrame(PopUpMessage)
        self.frame.setGeometry(QtCore.QRect(20, 60, 371, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnConfirm = QtWidgets.QPushButton(self.frame)
        self.btnConfirm.setGeometry(QtCore.QRect(20, 130, 75, 31))
        self.btnConfirm.setStyleSheet("   QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(43, 200, 7));\n"
"    \n"
"    \n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.btnConfirm.setObjectName("btnConfirm")
        self.lbPopUpMessage = QtWidgets.QLabel(self.frame)
        self.lbPopUpMessage.setGeometry(QtCore.QRect(20, 39, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbPopUpMessage.setFont(font)
        self.lbPopUpMessage.setText("")
        self.lbPopUpMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPopUpMessage.setObjectName("lbPopUpMessage")
        self.label_18 = QtWidgets.QLabel(PopUpMessage)
        self.label_18.setGeometry(QtCore.QRect(100, 20, 221, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")

        self.retranslateUi(PopUpMessage)
        QtCore.QMetaObject.connectSlotsByName(PopUpMessage)

    def retranslateUi(self, PopUpMessage):
        _translate = QtCore.QCoreApplication.translate
        PopUpMessage.setWindowTitle(_translate("PopUpMessage", "Message"))
        self.btnConfirm.setText(_translate("PopUpMessage", "Confirm"))
        self.label_18.setText(_translate("PopUpMessage", "MESSAGE"))
