# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'massbalance.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MassBalance(object):
    def setupUi(self, MassBalance):
        if not MassBalance.objectName():
            MassBalance.setObjectName(u"MassBalance")
        MassBalance.resize(1498, 855)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MassBalance.sizePolicy().hasHeightForWidth())
        MassBalance.setSizePolicy(sizePolicy)
        self.label_22 = QLabel(MassBalance)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(450, 10, 571, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.lbProject = QLabel(MassBalance)
        self.lbProject.setObjectName(u"lbProject")
        self.lbProject.setGeometry(QRect(460, 50, 571, 31))
        sizePolicy1.setHeightForWidth(self.lbProject.sizePolicy().hasHeightForWidth())
        self.lbProject.setSizePolicy(sizePolicy1)
        self.lbProject.setFont(font)
        self.lbProject.setAlignment(Qt.AlignCenter)
        self.tableView = QTableView(MassBalance)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 100, 1461, 511))

        self.retranslateUi(MassBalance)

        QMetaObject.connectSlotsByName(MassBalance)
    # setupUi

    def retranslateUi(self, MassBalance):
        MassBalance.setWindowTitle(QCoreApplication.translate("MassBalance", u"Dialog", None))
        self.label_22.setText(QCoreApplication.translate("MassBalance", u"MASS BALANCE", None))
        self.lbProject.setText("")
    # retranslateUi

