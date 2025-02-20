# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\_EEMS\forms\worksorder_selector.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectWorksorder(object):
    def setupUi(self, SelectWorksorder):
        SelectWorksorder.setObjectName("SelectWorksorder")
        SelectWorksorder.resize(400, 255)
        self.frame = QtWidgets.QFrame(SelectWorksorder)
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
        self.btnCancel = QtWidgets.QPushButton(self.frame)
        self.btnCancel.setGeometry(QtCore.QRect(280, 130, 75, 31))
        self.btnCancel.setStyleSheet("    QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(255, 0, 0));\n"
"    \n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.btnCancel.setObjectName("btnCancel")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.cbWorksorders = QtWidgets.QComboBox(self.frame)
        self.cbWorksorders.setGeometry(QtCore.QRect(10, 60, 351, 31))
        self.cbWorksorders.setStyleSheet("QComboBox{\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"    background: white;\n"
"    border: 1px solid gray;\n"
"    box-shadow: transparent;\n"
"    padding: 1px 18px 1px 3px;\n"
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
        self.cbWorksorders.setObjectName("cbWorksorders")
        self.label_18 = QtWidgets.QLabel(SelectWorksorder)
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

        self.retranslateUi(SelectWorksorder)
        QtCore.QMetaObject.connectSlotsByName(SelectWorksorder)

    def retranslateUi(self, SelectWorksorder):
        _translate = QtCore.QCoreApplication.translate
        SelectWorksorder.setWindowTitle(_translate("SelectWorksorder", "SelectWorksorder"))
        self.btnConfirm.setText(_translate("SelectWorksorder", "Confirm"))
        self.btnCancel.setText(_translate("SelectWorksorder", "Cancel"))
        self.label.setText(_translate("SelectWorksorder", "Select the worksorder package to proceed with:"))
        self.label_18.setText(_translate("SelectWorksorder", "WORKSORDERS"))
