# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_ControlPanel(object):
    def setupUi(self, ControlPanel):
        if not ControlPanel.objectName():
            ControlPanel.setObjectName(u"ControlPanel")
        ControlPanel.resize(1541, 851)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ControlPanel.sizePolicy().hasHeightForWidth())
        ControlPanel.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../resources/icons/HCE-C.svg", QSize(), QIcon.Normal, QIcon.Off)
        ControlPanel.setWindowIcon(icon)
        self.centralwidget = QWidget(ControlPanel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setGeometry(QRect(10, 10, 251, 831))
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 90, 215, 201))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lbDashborad = QLabel(self.frame_2)
        self.lbDashborad.setObjectName(u"lbDashborad")
        self.lbDashborad.setGeometry(QRect(70, 11, 121, 20))
        font = QFont()
        font.setPointSize(9)
        self.lbDashborad.setFont(font)
        self.lbCustomer = QLabel(self.frame_2)
        self.lbCustomer.setObjectName(u"lbCustomer")
        self.lbCustomer.setGeometry(QRect(70, 61, 121, 20))
        self.lbCustomer.setFont(font)
        self.lbQuotation = QLabel(self.frame_2)
        self.lbQuotation.setObjectName(u"lbQuotation")
        self.lbQuotation.setGeometry(QRect(70, 160, 121, 20))
        self.lbQuotation.setFont(font)
        self.lbContacts = QLabel(self.frame_2)
        self.lbContacts.setObjectName(u"lbContacts")
        self.lbContacts.setGeometry(QRect(70, 111, 121, 20))
        self.lbContacts.setFont(font)
        self.btnContacts = QPushButton(self.frame_2)
        self.btnContacts.setObjectName(u"btnContacts")
        self.btnContacts.setGeometry(QRect(10, 100, 51, 41))
        self.btnContacts.setToolTipDuration(0)
        icon1 = QIcon()
        icon1.addFile(u"../resources/assets/smile.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnContacts.setIcon(icon1)
        self.btnContacts.setIconSize(QSize(24, 24))
        self.btnDashboard = QPushButton(self.frame_2)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setEnabled(True)
        self.btnDashboard.setGeometry(QRect(10, 0, 48, 41))
        sizePolicy.setHeightForWidth(self.btnDashboard.sizePolicy().hasHeightForWidth())
        self.btnDashboard.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setKerning(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.btnDashboard.setFont(font1)
        self.btnDashboard.setToolTipDuration(0)
        self.btnDashboard.setLayoutDirection(Qt.LeftToRight)
        self.btnDashboard.setAutoFillBackground(False)
        self.btnDashboard.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u"../resources/assets/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDashboard.setIcon(icon2)
        self.btnDashboard.setIconSize(QSize(24, 24))
        self.btnDashboard.setCheckable(False)
        self.btnDashboard.setFlat(False)
        self.btnCustomer = QPushButton(self.frame_2)
        self.btnCustomer.setObjectName(u"btnCustomer")
        self.btnCustomer.setGeometry(QRect(10, 50, 51, 41))
        self.btnCustomer.setToolTipDuration(0)
        icon3 = QIcon()
        icon3.addFile(u"../resources/assets/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCustomer.setIcon(icon3)
        self.btnCustomer.setIconSize(QSize(24, 24))
        self.btnQuotation = QPushButton(self.frame_2)
        self.btnQuotation.setObjectName(u"btnQuotation")
        self.btnQuotation.setGeometry(QRect(10, 150, 51, 41))
        self.btnQuotation.setToolTipDuration(0)
        icon4 = QIcon()
        icon4.addFile(u"../resources/assets/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnQuotation.setIcon(icon4)
        self.btnQuotation.setIconSize(QSize(24, 24))
        self.frame_4 = QFrame(self.leftMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 700, 215, 111))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.lbGeneralInfo = QLabel(self.frame_4)
        self.lbGeneralInfo.setObjectName(u"lbGeneralInfo")
        self.lbGeneralInfo.setGeometry(QRect(70, 20, 141, 20))
        self.lbGeneralInfo.setFont(font)
        self.lbCalculations = QLabel(self.frame_4)
        self.lbCalculations.setObjectName(u"lbCalculations")
        self.lbCalculations.setGeometry(QRect(70, 70, 141, 20))
        self.lbCalculations.setFont(font)
        self.btnGeneralInfo = QPushButton(self.frame_4)
        self.btnGeneralInfo.setObjectName(u"btnGeneralInfo")
        self.btnGeneralInfo.setGeometry(QRect(10, 11, 51, 41))
        self.btnGeneralInfo.setToolTipDuration(0)
        icon5 = QIcon()
        icon5.addFile(u"../resources/assets/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGeneralInfo.setIcon(icon5)
        self.btnGeneralInfo.setIconSize(QSize(24, 24))
        self.btnCalculation = QPushButton(self.frame_4)
        self.btnCalculation.setObjectName(u"btnCalculation")
        self.btnCalculation.setGeometry(QRect(11, 60, 51, 41))
        self.btnCalculation.setToolTipDuration(0)
        icon6 = QIcon()
        icon6.addFile(u"../resources/assets/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCalculation.setIcon(icon6)
        self.btnCalculation.setIconSize(QSize(24, 24))
        self.frame_6 = QFrame(self.leftMenuSubContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 590, 215, 101))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.lbProcurement = QLabel(self.frame_6)
        self.lbProcurement.setObjectName(u"lbProcurement")
        self.lbProcurement.setGeometry(QRect(70, 20, 131, 20))
        self.lbProcurement.setFont(font)
        self.lbAnalysis = QLabel(self.frame_6)
        self.lbAnalysis.setObjectName(u"lbAnalysis")
        self.lbAnalysis.setGeometry(QRect(70, 70, 131, 20))
        self.lbAnalysis.setFont(font)
        self.btnProcurement = QPushButton(self.frame_6)
        self.btnProcurement.setObjectName(u"btnProcurement")
        self.btnProcurement.setGeometry(QRect(10, 11, 51, 41))
        self.btnProcurement.setToolTipDuration(0)
        icon7 = QIcon()
        icon7.addFile(u"../resources/assets/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnProcurement.setIcon(icon7)
        self.btnProcurement.setIconSize(QSize(24, 24))
        self.btnAnalysis = QPushButton(self.frame_6)
        self.btnAnalysis.setObjectName(u"btnAnalysis")
        self.btnAnalysis.setGeometry(QRect(10, 60, 51, 41))
        self.btnAnalysis.setToolTipDuration(0)
        icon8 = QIcon()
        icon8.addFile(u"../resources/assets/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAnalysis.setIcon(icon8)
        self.btnAnalysis.setIconSize(QSize(24, 24))
        self.frame_7 = QFrame(self.leftMenuSubContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 520, 215, 61))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.lbDocControl = QLabel(self.frame_7)
        self.lbDocControl.setObjectName(u"lbDocControl")
        self.lbDocControl.setGeometry(QRect(70, 20, 131, 20))
        self.lbDocControl.setFont(font)
        self.btnDocControl = QPushButton(self.frame_7)
        self.btnDocControl.setObjectName(u"btnDocControl")
        self.btnDocControl.setGeometry(QRect(10, 9, 51, 41))
        self.btnDocControl.setToolTipDuration(0)
        icon9 = QIcon()
        icon9.addFile(u"../resources/assets/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDocControl.setIcon(icon9)
        self.btnDocControl.setIconSize(QSize(24, 24))
        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 300, 215, 211))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lbWorksorder = QLabel(self.frame_3)
        self.lbWorksorder.setObjectName(u"lbWorksorder")
        self.lbWorksorder.setGeometry(QRect(70, 20, 121, 20))
        self.lbWorksorder.setFont(font)
        self.lbResources = QLabel(self.frame_3)
        self.lbResources.setObjectName(u"lbResources")
        self.lbResources.setGeometry(QRect(70, 70, 121, 20))
        self.lbResources.setFont(font)
        self.lbTimesheets = QLabel(self.frame_3)
        self.lbTimesheets.setObjectName(u"lbTimesheets")
        self.lbTimesheets.setGeometry(QRect(70, 120, 121, 20))
        self.lbTimesheets.setFont(font)
        self.lnInvoices = QLabel(self.frame_3)
        self.lnInvoices.setObjectName(u"lnInvoices")
        self.lnInvoices.setGeometry(QRect(70, 170, 131, 20))
        self.lnInvoices.setFont(font)
        self.btnInvoices = QPushButton(self.frame_3)
        self.btnInvoices.setObjectName(u"btnInvoices")
        self.btnInvoices.setGeometry(QRect(10, 161, 51, 41))
        self.btnInvoices.setToolTipDuration(0)
        icon10 = QIcon()
        icon10.addFile(u"../resources/assets/layout.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnInvoices.setIcon(icon10)
        self.btnInvoices.setIconSize(QSize(24, 24))
        self.btnWorksorder = QPushButton(self.frame_3)
        self.btnWorksorder.setObjectName(u"btnWorksorder")
        self.btnWorksorder.setGeometry(QRect(10, 10, 51, 41))
        self.btnWorksorder.setToolTipDuration(0)
        self.btnWorksorder.setIcon(icon6)
        self.btnWorksorder.setIconSize(QSize(24, 24))
        self.btnTimesheets = QPushButton(self.frame_3)
        self.btnTimesheets.setObjectName(u"btnTimesheets")
        self.btnTimesheets.setGeometry(QRect(10, 110, 51, 41))
        self.btnTimesheets.setToolTipDuration(0)
        icon11 = QIcon()
        icon11.addFile(u"../resources/assets/compass.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTimesheets.setIcon(icon11)
        self.btnTimesheets.setIconSize(QSize(24, 24))
        self.btnResources = QPushButton(self.frame_3)
        self.btnResources.setObjectName(u"btnResources")
        self.btnResources.setGeometry(QRect(10, 60, 51, 41))
        self.btnResources.setToolTipDuration(0)
        icon12 = QIcon()
        icon12.addFile(u"../resources/assets/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnResources.setIcon(icon12)
        self.btnResources.setIconSize(QSize(24, 24))
        self.label = QLabel(self.leftMenuSubContainer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 51, 51))
        self.label.setPixmap(QPixmap(u"../resources/assets/HCE-C.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.leftMenuSubContainer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 0, 131, 20))
        self.lbWONum = QLabel(self.leftMenuSubContainer)
        self.lbWONum.setObjectName(u"lbWONum")
        self.lbWONum.setGeometry(QRect(90, 20, 121, 31))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.lbWONum.setFont(font2)
        self.lbWONum.setAlignment(Qt.AlignCenter)
        self.btnUploadWO = QPushButton(self.leftMenuSubContainer)
        self.btnUploadWO.setObjectName(u"btnUploadWO")
        self.btnUploadWO.setEnabled(True)
        self.btnUploadWO.setGeometry(QRect(180, 60, 41, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnUploadWO.sizePolicy().hasHeightForWidth())
        self.btnUploadWO.setSizePolicy(sizePolicy1)
        self.btnUploadWO.setFont(font1)
        self.btnUploadWO.setToolTipDuration(0)
        self.btnUploadWO.setLayoutDirection(Qt.LeftToRight)
        self.btnUploadWO.setAutoFillBackground(False)
        self.btnUploadWO.setInputMethodHints(Qt.ImhNone)
        icon13 = QIcon()
        icon13.addFile(u"../resources/assets/upload-cloud.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnUploadWO.setIcon(icon13)
        self.btnUploadWO.setIconSize(QSize(24, 24))
        self.btnUploadWO.setCheckable(False)
        self.btnUploadWO.setFlat(False)

        self.verticalLayout_2.addWidget(self.leftMenuSubContainer)

        self.stwMain = QStackedWidget(self.centralwidget)
        self.stwMain.setObjectName(u"stwMain")
        self.stwMain.setGeometry(QRect(270, 10, 1251, 831))
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.label_14 = QLabel(self.dashboard)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(400, 30, 421, 21))
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.actionListContainer = QFrame(self.dashboard)
        self.actionListContainer.setObjectName(u"actionListContainer")
        self.actionListContainer.setGeometry(QRect(10, 60, 600, 771))
        self.actionListContainer.setFrameShape(QFrame.StyledPanel)
        self.actionListContainer.setFrameShadow(QFrame.Raised)
        self.tbActionList = QTableWidget(self.actionListContainer)
        self.tbActionList.setObjectName(u"tbActionList")
        self.tbActionList.setGeometry(QRect(10, 60, 581, 701))
        self.lbActionList = QLabel(self.actionListContainer)
        self.lbActionList.setObjectName(u"lbActionList")
        self.lbActionList.setGeometry(QRect(90, 20, 421, 20))
        sizePolicy2.setHeightForWidth(self.lbActionList.sizePolicy().hasHeightForWidth())
        self.lbActionList.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.lbActionList.setFont(font3)
        self.lbActionList.setAlignment(Qt.AlignCenter)
        self.openOrdersContainer = QFrame(self.dashboard)
        self.openOrdersContainer.setObjectName(u"openOrdersContainer")
        self.openOrdersContainer.setGeometry(QRect(620, 60, 600, 771))
        self.openOrdersContainer.setFrameShape(QFrame.StyledPanel)
        self.openOrdersContainer.setFrameShadow(QFrame.Raised)
        self.tbOpenOrders = QTableWidget(self.openOrdersContainer)
        self.tbOpenOrders.setObjectName(u"tbOpenOrders")
        self.tbOpenOrders.setGeometry(QRect(10, 60, 581, 701))
        self.lbOpenOrders = QLabel(self.openOrdersContainer)
        self.lbOpenOrders.setObjectName(u"lbOpenOrders")
        self.lbOpenOrders.setGeometry(QRect(90, 20, 421, 20))
        sizePolicy2.setHeightForWidth(self.lbOpenOrders.sizePolicy().hasHeightForWidth())
        self.lbOpenOrders.setSizePolicy(sizePolicy2)
        self.lbOpenOrders.setFont(font3)
        self.lbOpenOrders.setAlignment(Qt.AlignCenter)
        self.stwMain.addWidget(self.dashboard)
        self.customers = QWidget()
        self.customers.setObjectName(u"customers")
        self.lbCustomerPage = QLabel(self.customers)
        self.lbCustomerPage.setObjectName(u"lbCustomerPage")
        self.lbCustomerPage.setGeometry(QRect(220, 30, 721, 20))
        sizePolicy2.setHeightForWidth(self.lbCustomerPage.sizePolicy().hasHeightForWidth())
        self.lbCustomerPage.setSizePolicy(sizePolicy2)
        self.lbCustomerPage.setFont(font2)
        self.lbCustomerPage.setAlignment(Qt.AlignCenter)
        self.customerListContainer = QFrame(self.customers)
        self.customerListContainer.setObjectName(u"customerListContainer")
        self.customerListContainer.setGeometry(QRect(10, 60, 600, 771))
        self.customerListContainer.setFrameShape(QFrame.StyledPanel)
        self.customerListContainer.setFrameShadow(QFrame.Raised)
        self.lbCustomers = QLabel(self.customerListContainer)
        self.lbCustomers.setObjectName(u"lbCustomers")
        self.lbCustomers.setGeometry(QRect(10, 20, 151, 20))
        sizePolicy2.setHeightForWidth(self.lbCustomers.sizePolicy().hasHeightForWidth())
        self.lbCustomers.setSizePolicy(sizePolicy2)
        self.lbCustomers.setFont(font3)
        self.lbCustomers.setAlignment(Qt.AlignCenter)
        self.leSearch = QLineEdit(self.customerListContainer)
        self.leSearch.setObjectName(u"leSearch")
        self.leSearch.setGeometry(QRect(340, 20, 181, 31))
        font4 = QFont()
        font4.setPointSize(10)
        self.leSearch.setFont(font4)
        self.leSearch.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.searchBtn = QPushButton(self.customerListContainer)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setEnabled(True)
        self.searchBtn.setGeometry(QRect(540, 10, 51, 41))
        sizePolicy1.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy1)
        self.searchBtn.setFont(font1)
        self.searchBtn.setToolTipDuration(0)
        self.searchBtn.setLayoutDirection(Qt.LeftToRight)
        self.searchBtn.setAutoFillBackground(False)
        self.searchBtn.setInputMethodHints(Qt.ImhNone)
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/zoom-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon14)
        self.searchBtn.setIconSize(QSize(24, 24))
        self.searchBtn.setCheckable(False)
        self.searchBtn.setFlat(False)
        self.frame_8 = QFrame(self.customerListContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 710, 581, 51))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.btnEdit = QPushButton(self.frame_8)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setGeometry(QRect(10, 10, 75, 31))
        self.btnEdit.setStyleSheet(u"    QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(255, 255, 0));\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.btnDelete_2 = QPushButton(self.frame_8)
        self.btnDelete_2.setObjectName(u"btnDelete_2")
        self.btnDelete_2.setGeometry(QRect(130, 10, 75, 31))
        self.btnDelete_2.setStyleSheet(u"    QPushButton {\n"
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
        self.tvCustomers = QTableView(self.customerListContainer)
        self.tvCustomers.setObjectName(u"tvCustomers")
        self.tvCustomers.setGeometry(QRect(10, 60, 571, 631))
        self.customerCRUD = QFrame(self.customers)
        self.customerCRUD.setObjectName(u"customerCRUD")
        self.customerCRUD.setGeometry(QRect(620, 60, 600, 771))
        self.customerCRUD.setFrameShape(QFrame.StyledPanel)
        self.customerCRUD.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.customerCRUD)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 709, 581, 51))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.btnNew = QPushButton(self.frame_5)
        self.btnNew.setObjectName(u"btnNew")
        self.btnNew.setGeometry(QRect(10, 10, 75, 31))
        self.btnNew.setStyleSheet(u"   QPushButton {\n"
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
        self.btnClear = QPushButton(self.frame_5)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(130, 10, 75, 31))
        self.btnClear.setStyleSheet(u"   QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(145, 145, 145) );\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.leCompID = QLineEdit(self.customerCRUD)
        self.leCompID.setObjectName(u"leCompID")
        self.leCompID.setGeometry(QRect(10, 30, 101, 31))
        self.leCompID.setFont(font4)
        self.leCompID.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbCompID = QLabel(self.customerCRUD)
        self.lbCompID.setObjectName(u"lbCompID")
        self.lbCompID.setGeometry(QRect(10, 10, 121, 20))
        self.lbCompID.setFont(font)
        self.lbCompanyName = QLabel(self.customerCRUD)
        self.lbCompanyName.setObjectName(u"lbCompanyName")
        self.lbCompanyName.setGeometry(QRect(130, 10, 121, 20))
        self.lbCompanyName.setFont(font)
        self.leCompanyName = QLineEdit(self.customerCRUD)
        self.leCompanyName.setObjectName(u"leCompanyName")
        self.leCompanyName.setGeometry(QRect(130, 30, 451, 31))
        self.leCompanyName.setFont(font4)
        self.leCompanyName.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbCompStatus = QLabel(self.customerCRUD)
        self.lbCompStatus.setObjectName(u"lbCompStatus")
        self.lbCompStatus.setGeometry(QRect(10, 70, 121, 20))
        self.lbCompStatus.setFont(font)
        self.cbCompanyStatus = QComboBox(self.customerCRUD)
        self.cbCompanyStatus.setObjectName(u"cbCompanyStatus")
        self.cbCompanyStatus.setGeometry(QRect(10, 90, 101, 31))
        self.cbCompanyStatus.setStyleSheet(u"QComboBox{\n"
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
        self.frame_9 = QFrame(self.customerCRUD)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(140, 90, 431, 21))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.cboxCustomer = QCheckBox(self.frame_9)
        self.cboxCustomer.setObjectName(u"cboxCustomer")
        self.cboxCustomer.setGeometry(QRect(20, 0, 111, 17))
        self.cboxCustomer.setFont(font4)
        self.cboxSupplier = QCheckBox(self.frame_9)
        self.cboxSupplier.setObjectName(u"cboxSupplier")
        self.cboxSupplier.setGeometry(QRect(150, 0, 111, 17))
        self.cboxSupplier.setFont(font4)
        self.lbRegistrationNumber = QLabel(self.customerCRUD)
        self.lbRegistrationNumber.setObjectName(u"lbRegistrationNumber")
        self.lbRegistrationNumber.setGeometry(QRect(10, 130, 121, 20))
        self.lbRegistrationNumber.setFont(font)
        self.leRegistrationNumber = QLineEdit(self.customerCRUD)
        self.leRegistrationNumber.setObjectName(u"leRegistrationNumber")
        self.leRegistrationNumber.setGeometry(QRect(10, 150, 271, 31))
        self.leRegistrationNumber.setFont(font4)
        self.leRegistrationNumber.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbVATNumber = QLabel(self.customerCRUD)
        self.lbVATNumber.setObjectName(u"lbVATNumber")
        self.lbVATNumber.setGeometry(QRect(310, 130, 121, 20))
        self.lbVATNumber.setFont(font)
        self.leVATNumber = QLineEdit(self.customerCRUD)
        self.leVATNumber.setObjectName(u"leVATNumber")
        self.leVATNumber.setGeometry(QRect(310, 150, 271, 31))
        self.leVATNumber.setFont(font4)
        self.leVATNumber.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbWebsite = QLabel(self.customerCRUD)
        self.lbWebsite.setObjectName(u"lbWebsite")
        self.lbWebsite.setGeometry(QRect(10, 190, 121, 20))
        self.lbWebsite.setFont(font)
        self.leWebsite = QLineEdit(self.customerCRUD)
        self.leWebsite.setObjectName(u"leWebsite")
        self.leWebsite.setGeometry(QRect(10, 210, 271, 31))
        self.leWebsite.setFont(font4)
        self.leWebsite.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leAddress1 = QLineEdit(self.customerCRUD)
        self.leAddress1.setObjectName(u"leAddress1")
        self.leAddress1.setGeometry(QRect(10, 270, 571, 31))
        self.leAddress1.setFont(font4)
        self.leAddress1.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbAddress1 = QLabel(self.customerCRUD)
        self.lbAddress1.setObjectName(u"lbAddress1")
        self.lbAddress1.setGeometry(QRect(10, 250, 121, 20))
        self.lbAddress1.setFont(font)
        self.leAddress2 = QLineEdit(self.customerCRUD)
        self.leAddress2.setObjectName(u"leAddress2")
        self.leAddress2.setGeometry(QRect(10, 330, 571, 31))
        self.leAddress2.setFont(font4)
        self.leAddress2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbAddress2 = QLabel(self.customerCRUD)
        self.lbAddress2.setObjectName(u"lbAddress2")
        self.lbAddress2.setGeometry(QRect(10, 310, 121, 20))
        self.lbAddress2.setFont(font)
        self.leCity = QLineEdit(self.customerCRUD)
        self.leCity.setObjectName(u"leCity")
        self.leCity.setGeometry(QRect(10, 390, 271, 31))
        self.leCity.setFont(font4)
        self.leCity.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbCity = QLabel(self.customerCRUD)
        self.lbCity.setObjectName(u"lbCity")
        self.lbCity.setGeometry(QRect(10, 370, 121, 20))
        self.lbCity.setFont(font)
        self.lePostalCode = QLineEdit(self.customerCRUD)
        self.lePostalCode.setObjectName(u"lePostalCode")
        self.lePostalCode.setGeometry(QRect(310, 390, 271, 31))
        self.lePostalCode.setFont(font4)
        self.lePostalCode.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbPostalCode = QLabel(self.customerCRUD)
        self.lbPostalCode.setObjectName(u"lbPostalCode")
        self.lbPostalCode.setGeometry(QRect(310, 370, 121, 20))
        self.lbPostalCode.setFont(font)
        self.leProvince = QLineEdit(self.customerCRUD)
        self.leProvince.setObjectName(u"leProvince")
        self.leProvince.setGeometry(QRect(10, 450, 271, 31))
        self.leProvince.setFont(font4)
        self.leProvince.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbProvince = QLabel(self.customerCRUD)
        self.lbProvince.setObjectName(u"lbProvince")
        self.lbProvince.setGeometry(QRect(10, 430, 211, 20))
        self.lbProvince.setFont(font)
        self.lbCountry = QLabel(self.customerCRUD)
        self.lbCountry.setObjectName(u"lbCountry")
        self.lbCountry.setGeometry(QRect(310, 430, 121, 20))
        self.lbCountry.setFont(font)
        self.cbCountry = QComboBox(self.customerCRUD)
        self.cbCountry.setObjectName(u"cbCountry")
        self.cbCountry.setGeometry(QRect(310, 450, 271, 31))
        self.cbCountry.setStyleSheet(u"QComboBox{\n"
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
        self.lbBusinessPhone = QLabel(self.customerCRUD)
        self.lbBusinessPhone.setObjectName(u"lbBusinessPhone")
        self.lbBusinessPhone.setGeometry(QRect(10, 490, 211, 20))
        self.lbBusinessPhone.setFont(font)
        self.leBusinessPhone = QLineEdit(self.customerCRUD)
        self.leBusinessPhone.setObjectName(u"leBusinessPhone")
        self.leBusinessPhone.setGeometry(QRect(10, 510, 271, 31))
        self.leBusinessPhone.setFont(font4)
        self.leBusinessPhone.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbCompanyEmail = QLabel(self.customerCRUD)
        self.lbCompanyEmail.setObjectName(u"lbCompanyEmail")
        self.lbCompanyEmail.setGeometry(QRect(310, 490, 211, 20))
        self.lbCompanyEmail.setFont(font)
        self.leCompanyEmail = QLineEdit(self.customerCRUD)
        self.leCompanyEmail.setObjectName(u"leCompanyEmail")
        self.leCompanyEmail.setGeometry(QRect(310, 510, 271, 31))
        self.leCompanyEmail.setFont(font4)
        self.leCompanyEmail.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.gVLogo = QGraphicsView(self.customerCRUD)
        self.gVLogo.setObjectName(u"gVLogo")
        self.gVLogo.setGeometry(QRect(320, 570, 251, 131))
        self.stwMain.addWidget(self.customers)
        self.contacts = QWidget()
        self.contacts.setObjectName(u"contacts")
        self.label_19 = QLabel(self.contacts)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(370, 30, 421, 21))
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setFont(font2)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.contactListContainer = QFrame(self.contacts)
        self.contactListContainer.setObjectName(u"contactListContainer")
        self.contactListContainer.setGeometry(QRect(10, 60, 991, 771))
        self.contactListContainer.setFrameShape(QFrame.StyledPanel)
        self.contactListContainer.setFrameShadow(QFrame.Raised)
        self.lbContacts_2 = QLabel(self.contactListContainer)
        self.lbContacts_2.setObjectName(u"lbContacts_2")
        self.lbContacts_2.setGeometry(QRect(10, 20, 151, 20))
        sizePolicy2.setHeightForWidth(self.lbContacts_2.sizePolicy().hasHeightForWidth())
        self.lbContacts_2.setSizePolicy(sizePolicy2)
        self.lbContacts_2.setFont(font3)
        self.lbContacts_2.setAlignment(Qt.AlignCenter)
        self.leSearch_2 = QLineEdit(self.contactListContainer)
        self.leSearch_2.setObjectName(u"leSearch_2")
        self.leSearch_2.setGeometry(QRect(730, 20, 181, 31))
        self.leSearch_2.setFont(font4)
        self.leSearch_2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.searchBtn_2 = QPushButton(self.contactListContainer)
        self.searchBtn_2.setObjectName(u"searchBtn_2")
        self.searchBtn_2.setEnabled(True)
        self.searchBtn_2.setGeometry(QRect(930, 10, 51, 41))
        sizePolicy1.setHeightForWidth(self.searchBtn_2.sizePolicy().hasHeightForWidth())
        self.searchBtn_2.setSizePolicy(sizePolicy1)
        self.searchBtn_2.setFont(font1)
        self.searchBtn_2.setToolTipDuration(0)
        self.searchBtn_2.setLayoutDirection(Qt.LeftToRight)
        self.searchBtn_2.setAutoFillBackground(False)
        self.searchBtn_2.setInputMethodHints(Qt.ImhNone)
        self.searchBtn_2.setIcon(icon14)
        self.searchBtn_2.setIconSize(QSize(24, 24))
        self.searchBtn_2.setCheckable(False)
        self.searchBtn_2.setFlat(False)
        self.frame_10 = QFrame(self.contactListContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 710, 581, 51))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.btnEdit_2 = QPushButton(self.frame_10)
        self.btnEdit_2.setObjectName(u"btnEdit_2")
        self.btnEdit_2.setGeometry(QRect(10, 10, 75, 31))
        self.btnEdit_2.setStyleSheet(u"    QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(255, 255, 0));\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.btnDelete = QPushButton(self.frame_10)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(130, 10, 75, 31))
        self.btnDelete.setStyleSheet(u"    QPushButton {\n"
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
        self.tvContacts = QTableView(self.contactListContainer)
        self.tvContacts.setObjectName(u"tvContacts")
        self.tvContacts.setGeometry(QRect(10, 60, 971, 631))
        self.customerCRUD_2 = QFrame(self.contacts)
        self.customerCRUD_2.setObjectName(u"customerCRUD_2")
        self.customerCRUD_2.setGeometry(QRect(1010, 60, 241, 771))
        self.customerCRUD_2.setFrameShape(QFrame.StyledPanel)
        self.customerCRUD_2.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.customerCRUD_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 709, 221, 51))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.btnNew_2 = QPushButton(self.frame_11)
        self.btnNew_2.setObjectName(u"btnNew_2")
        self.btnNew_2.setGeometry(QRect(10, 10, 75, 31))
        self.btnNew_2.setStyleSheet(u"   QPushButton {\n"
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
        self.btnClear_2 = QPushButton(self.frame_11)
        self.btnClear_2.setObjectName(u"btnClear_2")
        self.btnClear_2.setGeometry(QRect(140, 10, 75, 31))
        self.btnClear_2.setStyleSheet(u"   QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(145, 145, 145) );\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.lbFirstName = QLabel(self.customerCRUD_2)
        self.lbFirstName.setObjectName(u"lbFirstName")
        self.lbFirstName.setGeometry(QRect(10, 10, 121, 20))
        self.lbFirstName.setFont(font)
        self.leFirstName = QLineEdit(self.customerCRUD_2)
        self.leFirstName.setObjectName(u"leFirstName")
        self.leFirstName.setGeometry(QRect(10, 30, 221, 31))
        self.leFirstName.setFont(font4)
        self.leFirstName.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbEmail = QLabel(self.customerCRUD_2)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setGeometry(QRect(10, 190, 121, 20))
        self.lbEmail.setFont(font)
        self.leEmail = QLineEdit(self.customerCRUD_2)
        self.leEmail.setObjectName(u"leEmail")
        self.leEmail.setGeometry(QRect(10, 210, 221, 31))
        self.leEmail.setFont(font4)
        self.leEmail.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lePosition = QLineEdit(self.customerCRUD_2)
        self.lePosition.setObjectName(u"lePosition")
        self.lePosition.setGeometry(QRect(10, 270, 221, 31))
        self.lePosition.setFont(font4)
        self.lePosition.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbPosition = QLabel(self.customerCRUD_2)
        self.lbPosition.setObjectName(u"lbPosition")
        self.lbPosition.setGeometry(QRect(10, 250, 121, 20))
        self.lbPosition.setFont(font)
        self.leBusPhone = QLineEdit(self.customerCRUD_2)
        self.leBusPhone.setObjectName(u"leBusPhone")
        self.leBusPhone.setGeometry(QRect(10, 330, 221, 31))
        self.leBusPhone.setFont(font4)
        self.leBusPhone.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbBusPhone = QLabel(self.customerCRUD_2)
        self.lbBusPhone.setObjectName(u"lbBusPhone")
        self.lbBusPhone.setGeometry(QRect(10, 310, 121, 20))
        self.lbBusPhone.setFont(font)
        self.leMobile = QLineEdit(self.customerCRUD_2)
        self.leMobile.setObjectName(u"leMobile")
        self.leMobile.setGeometry(QRect(10, 390, 221, 31))
        self.leMobile.setFont(font4)
        self.leMobile.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbMobile = QLabel(self.customerCRUD_2)
        self.lbMobile.setObjectName(u"lbMobile")
        self.lbMobile.setGeometry(QRect(10, 370, 121, 20))
        self.lbMobile.setFont(font)
        self.lbDOB = QLabel(self.customerCRUD_2)
        self.lbDOB.setObjectName(u"lbDOB")
        self.lbDOB.setGeometry(QRect(10, 430, 211, 20))
        self.lbDOB.setFont(font)
        self.lbLastName = QLabel(self.customerCRUD_2)
        self.lbLastName.setObjectName(u"lbLastName")
        self.lbLastName.setGeometry(QRect(10, 70, 121, 20))
        self.lbLastName.setFont(font)
        self.leLastName = QLineEdit(self.customerCRUD_2)
        self.leLastName.setObjectName(u"leLastName")
        self.leLastName.setGeometry(QRect(10, 90, 221, 31))
        self.leLastName.setFont(font4)
        self.leLastName.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.cbCompany = QComboBox(self.customerCRUD_2)
        self.cbCompany.setObjectName(u"cbCompany")
        self.cbCompany.setGeometry(QRect(10, 150, 221, 31))
        self.cbCompany.setStyleSheet(u"QComboBox{\n"
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
        self.lbCompany = QLabel(self.customerCRUD_2)
        self.lbCompany.setObjectName(u"lbCompany")
        self.lbCompany.setGeometry(QRect(10, 130, 121, 20))
        self.lbCompany.setFont(font)
        self.deDOB = QDateEdit(self.customerCRUD_2)
        self.deDOB.setObjectName(u"deDOB")
        self.deDOB.setGeometry(QRect(10, 450, 221, 31))
        self.deDOB.setStyleSheet(u"QDateEdit{\n"
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
"QDateEdit::drop-down {\n"
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
"QDateEdit::down-arrow {\n"
"     image:url(:/icons/icons/arrow-down.svg)\n"
" }\n"
"\n"
"QDateEdit::up-arrow {\n"
"     image:url(:/icons/icons/arrow-up.svg)\n"
" }\n"
"\n"
" QDateEdit::down-arrow:on { /* shift the arrow when popup is open */\n"
"     top: 1px;\n"
"     left: 1px;\n"
" }\n"
"")
        self.deDOB.setCalendarPopup(True)
        self.stwMain.addWidget(self.contacts)
        self.quotations = QWidget()
        self.quotations.setObjectName(u"quotations")
        self.label_16 = QLabel(self.quotations)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 30, 421, 21))
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.tabQuotation = QTabWidget(self.quotations)
        self.tabQuotation.setObjectName(u"tabQuotation")
        self.tabQuotation.setGeometry(QRect(10, 80, 1241, 421))
        self.register_quote = QWidget()
        self.register_quote.setObjectName(u"register_quote")
        self.tabQuotation.addTab(self.register_quote, "")
        self.scope_included = QWidget()
        self.scope_included.setObjectName(u"scope_included")
        self.tabQuotation.addTab(self.scope_included, "")
        self.scope_excluded = QWidget()
        self.scope_excluded.setObjectName(u"scope_excluded")
        self.tabQuotation.addTab(self.scope_excluded, "")
        self.design_estimate = QWidget()
        self.design_estimate.setObjectName(u"design_estimate")
        self.tabQuotation.addTab(self.design_estimate, "")
        self.supply_estimate = QWidget()
        self.supply_estimate.setObjectName(u"supply_estimate")
        self.tabQuotation.addTab(self.supply_estimate, "")
        self.service_estimate = QWidget()
        self.service_estimate.setObjectName(u"service_estimate")
        self.tabQuotation.addTab(self.service_estimate, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabQuotation.addTab(self.tab_3, "")
        self.tabWidget_2 = QTabWidget(self.quotations)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 540, 1241, 291))
        self.all_quotations = QWidget()
        self.all_quotations.setObjectName(u"all_quotations")
        self.tabWidget_2.addTab(self.all_quotations, "")
        self.open_quotations = QWidget()
        self.open_quotations.setObjectName(u"open_quotations")
        self.tabWidget_2.addTab(self.open_quotations, "")
        self.accepted_quotations = QWidget()
        self.accepted_quotations.setObjectName(u"accepted_quotations")
        self.tabWidget_2.addTab(self.accepted_quotations, "")
        self.cancelled_quotations = QWidget()
        self.cancelled_quotations.setObjectName(u"cancelled_quotations")
        self.tabWidget_2.addTab(self.cancelled_quotations, "")
        self.postponed_quotations = QWidget()
        self.postponed_quotations.setObjectName(u"postponed_quotations")
        self.tabWidget_2.addTab(self.postponed_quotations, "")
        self.lbQuotationHistory = QLabel(self.quotations)
        self.lbQuotationHistory.setObjectName(u"lbQuotationHistory")
        self.lbQuotationHistory.setGeometry(QRect(20, 520, 111, 16))
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.lbQuotationHistory.setFont(font5)
        self.lbQuotationHistory_2 = QLabel(self.quotations)
        self.lbQuotationHistory_2.setObjectName(u"lbQuotationHistory_2")
        self.lbQuotationHistory_2.setGeometry(QRect(20, 60, 111, 16))
        self.lbQuotationHistory_2.setFont(font5)
        self.stwMain.addWidget(self.quotations)
        self.worksorders = QWidget()
        self.worksorders.setObjectName(u"worksorders")
        self.label_17 = QLabel(self.worksorders)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(370, 30, 421, 20))
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.tabQuotation_2 = QTabWidget(self.worksorders)
        self.tabQuotation_2.setObjectName(u"tabQuotation_2")
        self.tabQuotation_2.setGeometry(QRect(10, 80, 1241, 421))
        self.register_quote_2 = QWidget()
        self.register_quote_2.setObjectName(u"register_quote_2")
        self.tabQuotation_2.addTab(self.register_quote_2, "")
        self.scope_included_2 = QWidget()
        self.scope_included_2.setObjectName(u"scope_included_2")
        self.tabQuotation_2.addTab(self.scope_included_2, "")
        self.scope_excluded_2 = QWidget()
        self.scope_excluded_2.setObjectName(u"scope_excluded_2")
        self.tabQuotation_2.addTab(self.scope_excluded_2, "")
        self.design_estimate_2 = QWidget()
        self.design_estimate_2.setObjectName(u"design_estimate_2")
        self.tabQuotation_2.addTab(self.design_estimate_2, "")
        self.supply_estimate_2 = QWidget()
        self.supply_estimate_2.setObjectName(u"supply_estimate_2")
        self.tabQuotation_2.addTab(self.supply_estimate_2, "")
        self.service_estimate_2 = QWidget()
        self.service_estimate_2.setObjectName(u"service_estimate_2")
        self.tabQuotation_2.addTab(self.service_estimate_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabQuotation_2.addTab(self.tab_4, "")
        self.tabWidget_3 = QTabWidget(self.worksorders)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(10, 540, 1241, 291))
        self.all_quotations_2 = QWidget()
        self.all_quotations_2.setObjectName(u"all_quotations_2")
        self.tabWidget_3.addTab(self.all_quotations_2, "")
        self.open_quotations_2 = QWidget()
        self.open_quotations_2.setObjectName(u"open_quotations_2")
        self.tabWidget_3.addTab(self.open_quotations_2, "")
        self.accepted_quotations_2 = QWidget()
        self.accepted_quotations_2.setObjectName(u"accepted_quotations_2")
        self.tabWidget_3.addTab(self.accepted_quotations_2, "")
        self.cancelled_quotations_2 = QWidget()
        self.cancelled_quotations_2.setObjectName(u"cancelled_quotations_2")
        self.tabWidget_3.addTab(self.cancelled_quotations_2, "")
        self.postponed_quotations_2 = QWidget()
        self.postponed_quotations_2.setObjectName(u"postponed_quotations_2")
        self.tabWidget_3.addTab(self.postponed_quotations_2, "")
        self.lbQuotationHistory_3 = QLabel(self.worksorders)
        self.lbQuotationHistory_3.setObjectName(u"lbQuotationHistory_3")
        self.lbQuotationHistory_3.setGeometry(QRect(20, 60, 111, 16))
        self.lbQuotationHistory_3.setFont(font5)
        self.lbQuotationHistory_4 = QLabel(self.worksorders)
        self.lbQuotationHistory_4.setObjectName(u"lbQuotationHistory_4")
        self.lbQuotationHistory_4.setGeometry(QRect(20, 520, 111, 16))
        self.lbQuotationHistory_4.setFont(font5)
        self.stwMain.addWidget(self.worksorders)
        self.resources = QWidget()
        self.resources.setObjectName(u"resources")
        self.label_18 = QLabel(self.resources)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(370, 30, 421, 20))
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.customerCRUD_3 = QFrame(self.resources)
        self.customerCRUD_3.setObjectName(u"customerCRUD_3")
        self.customerCRUD_3.setGeometry(QRect(1010, 60, 241, 771))
        self.customerCRUD_3.setFrameShape(QFrame.StyledPanel)
        self.customerCRUD_3.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.customerCRUD_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 709, 221, 51))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.btnNew_3 = QPushButton(self.frame_12)
        self.btnNew_3.setObjectName(u"btnNew_3")
        self.btnNew_3.setGeometry(QRect(10, 10, 75, 31))
        self.btnNew_3.setStyleSheet(u"   QPushButton {\n"
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
        self.btnClear_3 = QPushButton(self.frame_12)
        self.btnClear_3.setObjectName(u"btnClear_3")
        self.btnClear_3.setGeometry(QRect(140, 10, 75, 31))
        self.btnClear_3.setStyleSheet(u"   QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(145, 145, 145) );\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.lbFirstName_2 = QLabel(self.customerCRUD_3)
        self.lbFirstName_2.setObjectName(u"lbFirstName_2")
        self.lbFirstName_2.setGeometry(QRect(10, 10, 121, 20))
        self.lbFirstName_2.setFont(font)
        self.leFirstName_2 = QLineEdit(self.customerCRUD_3)
        self.leFirstName_2.setObjectName(u"leFirstName_2")
        self.leFirstName_2.setGeometry(QRect(10, 30, 221, 31))
        self.leFirstName_2.setFont(font4)
        self.leFirstName_2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbEmail_2 = QLabel(self.customerCRUD_3)
        self.lbEmail_2.setObjectName(u"lbEmail_2")
        self.lbEmail_2.setGeometry(QRect(10, 190, 121, 20))
        self.lbEmail_2.setFont(font)
        self.leEmail_2 = QLineEdit(self.customerCRUD_3)
        self.leEmail_2.setObjectName(u"leEmail_2")
        self.leEmail_2.setGeometry(QRect(10, 210, 221, 31))
        self.leEmail_2.setFont(font4)
        self.leEmail_2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leBusPhone_2 = QLineEdit(self.customerCRUD_3)
        self.leBusPhone_2.setObjectName(u"leBusPhone_2")
        self.leBusPhone_2.setGeometry(QRect(10, 330, 221, 31))
        self.leBusPhone_2.setFont(font4)
        self.leBusPhone_2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbBusPhone_2 = QLabel(self.customerCRUD_3)
        self.lbBusPhone_2.setObjectName(u"lbBusPhone_2")
        self.lbBusPhone_2.setGeometry(QRect(10, 310, 121, 20))
        self.lbBusPhone_2.setFont(font)
        self.leMobile_2 = QLineEdit(self.customerCRUD_3)
        self.leMobile_2.setObjectName(u"leMobile_2")
        self.leMobile_2.setGeometry(QRect(10, 390, 221, 31))
        self.leMobile_2.setFont(font4)
        self.leMobile_2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lbMobile_2 = QLabel(self.customerCRUD_3)
        self.lbMobile_2.setObjectName(u"lbMobile_2")
        self.lbMobile_2.setGeometry(QRect(10, 370, 121, 20))
        self.lbMobile_2.setFont(font)
        self.lbDOB_2 = QLabel(self.customerCRUD_3)
        self.lbDOB_2.setObjectName(u"lbDOB_2")
        self.lbDOB_2.setGeometry(QRect(10, 430, 211, 20))
        self.lbDOB_2.setFont(font)
        self.lbLastName_2 = QLabel(self.customerCRUD_3)
        self.lbLastName_2.setObjectName(u"lbLastName_2")
        self.lbLastName_2.setGeometry(QRect(10, 70, 121, 20))
        self.lbLastName_2.setFont(font)
        self.leLastName_2 = QLineEdit(self.customerCRUD_3)
        self.leLastName_2.setObjectName(u"leLastName_2")
        self.leLastName_2.setGeometry(QRect(10, 90, 221, 31))
        self.leLastName_2.setFont(font4)
        self.leLastName_2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.cbCompany_2 = QComboBox(self.customerCRUD_3)
        self.cbCompany_2.setObjectName(u"cbCompany_2")
        self.cbCompany_2.setGeometry(QRect(10, 150, 221, 31))
        self.cbCompany_2.setStyleSheet(u"QComboBox{\n"
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
        self.lbCompany_2 = QLabel(self.customerCRUD_3)
        self.lbCompany_2.setObjectName(u"lbCompany_2")
        self.lbCompany_2.setGeometry(QRect(10, 130, 121, 20))
        self.lbCompany_2.setFont(font)
        self.deDOB_2 = QDateEdit(self.customerCRUD_3)
        self.deDOB_2.setObjectName(u"deDOB_2")
        self.deDOB_2.setGeometry(QRect(10, 450, 221, 31))
        self.deDOB_2.setStyleSheet(u"QDateEdit{\n"
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
"QDateEdit::drop-down {\n"
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
"QDateEdit::down-arrow {\n"
"     image:url(:/icons/icons/arrow-down.svg)\n"
" }\n"
"\n"
"QDateEdit::up-arrow {\n"
"     image:url(:/icons/icons/arrow-up.svg)\n"
" }\n"
"\n"
" QDateEdit::down-arrow:on { /* shift the arrow when popup is open */\n"
"     top: 1px;\n"
"     left: 1px;\n"
" }\n"
"")
        self.deDOB_2.setCalendarPopup(True)
        self.lbPosition_2 = QLabel(self.customerCRUD_3)
        self.lbPosition_2.setObjectName(u"lbPosition_2")
        self.lbPosition_2.setGeometry(QRect(10, 250, 121, 20))
        self.lbPosition_2.setFont(font)
        self.cbPosition = QComboBox(self.customerCRUD_3)
        self.cbPosition.setObjectName(u"cbPosition")
        self.cbPosition.setGeometry(QRect(10, 270, 221, 31))
        self.cbPosition.setStyleSheet(u"QComboBox{\n"
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
        self.contactListContainer_2 = QFrame(self.resources)
        self.contactListContainer_2.setObjectName(u"contactListContainer_2")
        self.contactListContainer_2.setGeometry(QRect(10, 60, 991, 771))
        self.contactListContainer_2.setFrameShape(QFrame.StyledPanel)
        self.contactListContainer_2.setFrameShadow(QFrame.Raised)
        self.lbContacts_3 = QLabel(self.contactListContainer_2)
        self.lbContacts_3.setObjectName(u"lbContacts_3")
        self.lbContacts_3.setGeometry(QRect(10, 20, 151, 20))
        sizePolicy2.setHeightForWidth(self.lbContacts_3.sizePolicy().hasHeightForWidth())
        self.lbContacts_3.setSizePolicy(sizePolicy2)
        self.lbContacts_3.setFont(font3)
        self.lbContacts_3.setAlignment(Qt.AlignCenter)
        self.leSearch_3 = QLineEdit(self.contactListContainer_2)
        self.leSearch_3.setObjectName(u"leSearch_3")
        self.leSearch_3.setGeometry(QRect(730, 20, 181, 31))
        self.leSearch_3.setFont(font4)
        self.leSearch_3.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.searchBtn_3 = QPushButton(self.contactListContainer_2)
        self.searchBtn_3.setObjectName(u"searchBtn_3")
        self.searchBtn_3.setEnabled(True)
        self.searchBtn_3.setGeometry(QRect(930, 10, 51, 41))
        sizePolicy1.setHeightForWidth(self.searchBtn_3.sizePolicy().hasHeightForWidth())
        self.searchBtn_3.setSizePolicy(sizePolicy1)
        self.searchBtn_3.setFont(font1)
        self.searchBtn_3.setToolTipDuration(0)
        self.searchBtn_3.setLayoutDirection(Qt.LeftToRight)
        self.searchBtn_3.setAutoFillBackground(False)
        self.searchBtn_3.setInputMethodHints(Qt.ImhNone)
        self.searchBtn_3.setIcon(icon14)
        self.searchBtn_3.setIconSize(QSize(24, 24))
        self.searchBtn_3.setCheckable(False)
        self.searchBtn_3.setFlat(False)
        self.frame_13 = QFrame(self.contactListContainer_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 710, 581, 51))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.btnEdit_3 = QPushButton(self.frame_13)
        self.btnEdit_3.setObjectName(u"btnEdit_3")
        self.btnEdit_3.setGeometry(QRect(10, 10, 75, 31))
        self.btnEdit_3.setStyleSheet(u"    QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(255, 255, 0));\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.btnDelete_3 = QPushButton(self.frame_13)
        self.btnDelete_3.setObjectName(u"btnDelete_3")
        self.btnDelete_3.setGeometry(QRect(130, 10, 75, 31))
        self.btnDelete_3.setStyleSheet(u"    QPushButton {\n"
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
        self.tvContacts_2 = QTableView(self.contactListContainer_2)
        self.tvContacts_2.setObjectName(u"tvContacts_2")
        self.tvContacts_2.setGeometry(QRect(10, 60, 971, 631))
        self.stwMain.addWidget(self.resources)
        self.timesheets = QWidget()
        self.timesheets.setObjectName(u"timesheets")
        self.label_20 = QLabel(self.timesheets)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(380, 30, 421, 20))
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setFont(font2)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(self.timesheets)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 80, 1241, 751))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.stwMain.addWidget(self.timesheets)
        self.invoices = QWidget()
        self.invoices.setObjectName(u"invoices")
        self.label_21 = QLabel(self.invoices)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(300, 30, 571, 20))
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setFont(font2)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.stwMain.addWidget(self.invoices)
        self.documentControl = QWidget()
        self.documentControl.setObjectName(u"documentControl")
        self.label_22 = QLabel(self.documentControl)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(290, 30, 571, 21))
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setFont(font2)
        self.label_22.setAlignment(Qt.AlignCenter)
        self.tabDoccontrol = QTabWidget(self.documentControl)
        self.tabDoccontrol.setObjectName(u"tabDoccontrol")
        self.tabDoccontrol.setGeometry(QRect(0, 60, 1221, 761))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.lbDashborad_2 = QLabel(self.tab_5)
        self.lbDashborad_2.setObjectName(u"lbDashborad_2")
        self.lbDashborad_2.setGeometry(QRect(80, 41, 121, 20))
        self.lbDashborad_2.setFont(font)
        self.btnDesignBasis = QPushButton(self.tab_5)
        self.btnDesignBasis.setObjectName(u"btnDesignBasis")
        self.btnDesignBasis.setEnabled(True)
        self.btnDesignBasis.setGeometry(QRect(20, 30, 48, 41))
        sizePolicy.setHeightForWidth(self.btnDesignBasis.sizePolicy().hasHeightForWidth())
        self.btnDesignBasis.setSizePolicy(sizePolicy)
        self.btnDesignBasis.setFont(font1)
        self.btnDesignBasis.setToolTipDuration(0)
        self.btnDesignBasis.setLayoutDirection(Qt.LeftToRight)
        self.btnDesignBasis.setAutoFillBackground(False)
        self.btnDesignBasis.setInputMethodHints(Qt.ImhNone)
        icon15 = QIcon()
        icon15.addFile(u"../resources/assets/corner-down-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDesignBasis.setIcon(icon15)
        self.btnDesignBasis.setIconSize(QSize(24, 24))
        self.btnDesignBasis.setCheckable(False)
        self.btnDesignBasis.setFlat(False)
        self.btnProcessDescrip = QPushButton(self.tab_5)
        self.btnProcessDescrip.setObjectName(u"btnProcessDescrip")
        self.btnProcessDescrip.setEnabled(True)
        self.btnProcessDescrip.setGeometry(QRect(120, 109, 48, 41))
        sizePolicy.setHeightForWidth(self.btnProcessDescrip.sizePolicy().hasHeightForWidth())
        self.btnProcessDescrip.setSizePolicy(sizePolicy)
        self.btnProcessDescrip.setFont(font1)
        self.btnProcessDescrip.setToolTipDuration(0)
        self.btnProcessDescrip.setLayoutDirection(Qt.LeftToRight)
        self.btnProcessDescrip.setAutoFillBackground(False)
        self.btnProcessDescrip.setInputMethodHints(Qt.ImhNone)
        self.btnProcessDescrip.setIcon(icon15)
        self.btnProcessDescrip.setIconSize(QSize(24, 24))
        self.btnProcessDescrip.setCheckable(False)
        self.btnProcessDescrip.setFlat(False)
        self.lbDashborad_3 = QLabel(self.tab_5)
        self.lbDashborad_3.setObjectName(u"lbDashborad_3")
        self.lbDashborad_3.setGeometry(QRect(180, 120, 151, 20))
        self.lbDashborad_3.setFont(font)
        self.btnSiteConditions = QPushButton(self.tab_5)
        self.btnSiteConditions.setObjectName(u"btnSiteConditions")
        self.btnSiteConditions.setEnabled(True)
        self.btnSiteConditions.setGeometry(QRect(120, 69, 48, 41))
        sizePolicy.setHeightForWidth(self.btnSiteConditions.sizePolicy().hasHeightForWidth())
        self.btnSiteConditions.setSizePolicy(sizePolicy)
        self.btnSiteConditions.setFont(font1)
        self.btnSiteConditions.setToolTipDuration(0)
        self.btnSiteConditions.setLayoutDirection(Qt.LeftToRight)
        self.btnSiteConditions.setAutoFillBackground(False)
        self.btnSiteConditions.setInputMethodHints(Qt.ImhNone)
        self.btnSiteConditions.setIcon(icon15)
        self.btnSiteConditions.setIconSize(QSize(24, 24))
        self.btnSiteConditions.setCheckable(False)
        self.btnSiteConditions.setFlat(False)
        self.lbDashborad_4 = QLabel(self.tab_5)
        self.lbDashborad_4.setObjectName(u"lbDashborad_4")
        self.lbDashborad_4.setGeometry(QRect(180, 80, 121, 20))
        self.lbDashborad_4.setFont(font)
        self.btnDesignCriteria = QPushButton(self.tab_5)
        self.btnDesignCriteria.setObjectName(u"btnDesignCriteria")
        self.btnDesignCriteria.setEnabled(True)
        self.btnDesignCriteria.setGeometry(QRect(20, 159, 48, 41))
        sizePolicy.setHeightForWidth(self.btnDesignCriteria.sizePolicy().hasHeightForWidth())
        self.btnDesignCriteria.setSizePolicy(sizePolicy)
        self.btnDesignCriteria.setFont(font1)
        self.btnDesignCriteria.setToolTipDuration(0)
        self.btnDesignCriteria.setLayoutDirection(Qt.LeftToRight)
        self.btnDesignCriteria.setAutoFillBackground(False)
        self.btnDesignCriteria.setInputMethodHints(Qt.ImhNone)
        self.btnDesignCriteria.setIcon(icon15)
        self.btnDesignCriteria.setIconSize(QSize(24, 24))
        self.btnDesignCriteria.setCheckable(False)
        self.btnDesignCriteria.setFlat(False)
        self.lbDashborad_5 = QLabel(self.tab_5)
        self.lbDashborad_5.setObjectName(u"lbDashborad_5")
        self.lbDashborad_5.setGeometry(QRect(80, 170, 121, 20))
        self.lbDashborad_5.setFont(font)
        self.btnBuildinList = QPushButton(self.tab_5)
        self.btnBuildinList.setObjectName(u"btnBuildinList")
        self.btnBuildinList.setEnabled(True)
        self.btnBuildinList.setGeometry(QRect(20, 249, 48, 41))
        sizePolicy.setHeightForWidth(self.btnBuildinList.sizePolicy().hasHeightForWidth())
        self.btnBuildinList.setSizePolicy(sizePolicy)
        self.btnBuildinList.setFont(font1)
        self.btnBuildinList.setToolTipDuration(0)
        self.btnBuildinList.setLayoutDirection(Qt.LeftToRight)
        self.btnBuildinList.setAutoFillBackground(False)
        self.btnBuildinList.setInputMethodHints(Qt.ImhNone)
        self.btnBuildinList.setIcon(icon15)
        self.btnBuildinList.setIconSize(QSize(24, 24))
        self.btnBuildinList.setCheckable(False)
        self.btnBuildinList.setFlat(False)
        self.lbDashborad_6 = QLabel(self.tab_5)
        self.lbDashborad_6.setObjectName(u"lbDashborad_6")
        self.lbDashborad_6.setGeometry(QRect(80, 260, 121, 20))
        self.lbDashborad_6.setFont(font)
        self.btnStructureList = QPushButton(self.tab_5)
        self.btnStructureList.setObjectName(u"btnStructureList")
        self.btnStructureList.setEnabled(True)
        self.btnStructureList.setGeometry(QRect(20, 499, 48, 41))
        sizePolicy.setHeightForWidth(self.btnStructureList.sizePolicy().hasHeightForWidth())
        self.btnStructureList.setSizePolicy(sizePolicy)
        self.btnStructureList.setFont(font1)
        self.btnStructureList.setToolTipDuration(0)
        self.btnStructureList.setLayoutDirection(Qt.LeftToRight)
        self.btnStructureList.setAutoFillBackground(False)
        self.btnStructureList.setInputMethodHints(Qt.ImhNone)
        self.btnStructureList.setIcon(icon15)
        self.btnStructureList.setIconSize(QSize(24, 24))
        self.btnStructureList.setCheckable(False)
        self.btnStructureList.setFlat(False)
        self.lbDashborad_7 = QLabel(self.tab_5)
        self.lbDashborad_7.setObjectName(u"lbDashborad_7")
        self.lbDashborad_7.setGeometry(QRect(80, 510, 121, 20))
        self.lbDashborad_7.setFont(font)
        self.btnMEL = QPushButton(self.tab_5)
        self.btnMEL.setObjectName(u"btnMEL")
        self.btnMEL.setEnabled(True)
        self.btnMEL.setGeometry(QRect(370, 39, 48, 41))
        sizePolicy.setHeightForWidth(self.btnMEL.sizePolicy().hasHeightForWidth())
        self.btnMEL.setSizePolicy(sizePolicy)
        self.btnMEL.setFont(font1)
        self.btnMEL.setToolTipDuration(0)
        self.btnMEL.setLayoutDirection(Qt.LeftToRight)
        self.btnMEL.setAutoFillBackground(False)
        self.btnMEL.setInputMethodHints(Qt.ImhNone)
        self.btnMEL.setIcon(icon15)
        self.btnMEL.setIconSize(QSize(24, 24))
        self.btnMEL.setCheckable(False)
        self.btnMEL.setFlat(False)
        self.lbDashborad_8 = QLabel(self.tab_5)
        self.lbDashborad_8.setObjectName(u"lbDashborad_8")
        self.lbDashborad_8.setGeometry(QRect(430, 50, 181, 20))
        self.lbDashborad_8.setFont(font)
        self.lbDashborad_9 = QLabel(self.tab_5)
        self.lbDashborad_9.setObjectName(u"lbDashborad_9")
        self.lbDashborad_9.setGeometry(QRect(800, 61, 181, 20))
        self.lbDashborad_9.setFont(font)
        self.btnEEL = QPushButton(self.tab_5)
        self.btnEEL.setObjectName(u"btnEEL")
        self.btnEEL.setEnabled(True)
        self.btnEEL.setGeometry(QRect(740, 50, 48, 41))
        sizePolicy.setHeightForWidth(self.btnEEL.sizePolicy().hasHeightForWidth())
        self.btnEEL.setSizePolicy(sizePolicy)
        self.btnEEL.setFont(font1)
        self.btnEEL.setToolTipDuration(0)
        self.btnEEL.setLayoutDirection(Qt.LeftToRight)
        self.btnEEL.setAutoFillBackground(False)
        self.btnEEL.setInputMethodHints(Qt.ImhNone)
        self.btnEEL.setIcon(icon15)
        self.btnEEL.setIconSize(QSize(24, 24))
        self.btnEEL.setCheckable(False)
        self.btnEEL.setFlat(False)
        self.btnIEL = QPushButton(self.tab_5)
        self.btnIEL.setObjectName(u"btnIEL")
        self.btnIEL.setEnabled(True)
        self.btnIEL.setGeometry(QRect(740, 199, 48, 41))
        sizePolicy.setHeightForWidth(self.btnIEL.sizePolicy().hasHeightForWidth())
        self.btnIEL.setSizePolicy(sizePolicy)
        self.btnIEL.setFont(font1)
        self.btnIEL.setToolTipDuration(0)
        self.btnIEL.setLayoutDirection(Qt.LeftToRight)
        self.btnIEL.setAutoFillBackground(False)
        self.btnIEL.setInputMethodHints(Qt.ImhNone)
        self.btnIEL.setIcon(icon15)
        self.btnIEL.setIconSize(QSize(24, 24))
        self.btnIEL.setCheckable(False)
        self.btnIEL.setFlat(False)
        self.lbDashborad_10 = QLabel(self.tab_5)
        self.lbDashborad_10.setObjectName(u"lbDashborad_10")
        self.lbDashborad_10.setGeometry(QRect(800, 210, 211, 20))
        self.lbDashborad_10.setFont(font)
        self.btnGenSpec = QPushButton(self.tab_5)
        self.btnGenSpec.setObjectName(u"btnGenSpec")
        self.btnGenSpec.setEnabled(True)
        self.btnGenSpec.setGeometry(QRect(120, 199, 48, 41))
        sizePolicy.setHeightForWidth(self.btnGenSpec.sizePolicy().hasHeightForWidth())
        self.btnGenSpec.setSizePolicy(sizePolicy)
        self.btnGenSpec.setFont(font1)
        self.btnGenSpec.setToolTipDuration(0)
        self.btnGenSpec.setLayoutDirection(Qt.LeftToRight)
        self.btnGenSpec.setAutoFillBackground(False)
        self.btnGenSpec.setInputMethodHints(Qt.ImhNone)
        self.btnGenSpec.setIcon(icon15)
        self.btnGenSpec.setIconSize(QSize(24, 24))
        self.btnGenSpec.setCheckable(False)
        self.btnGenSpec.setFlat(False)
        self.lbDashborad_11 = QLabel(self.tab_5)
        self.lbDashborad_11.setObjectName(u"lbDashborad_11")
        self.lbDashborad_11.setGeometry(QRect(180, 210, 161, 20))
        self.lbDashborad_11.setFont(font)
        self.btnBuildSpec = QPushButton(self.tab_5)
        self.btnBuildSpec.setObjectName(u"btnBuildSpec")
        self.btnBuildSpec.setEnabled(True)
        self.btnBuildSpec.setGeometry(QRect(120, 289, 48, 41))
        sizePolicy.setHeightForWidth(self.btnBuildSpec.sizePolicy().hasHeightForWidth())
        self.btnBuildSpec.setSizePolicy(sizePolicy)
        self.btnBuildSpec.setFont(font1)
        self.btnBuildSpec.setToolTipDuration(0)
        self.btnBuildSpec.setLayoutDirection(Qt.LeftToRight)
        self.btnBuildSpec.setAutoFillBackground(False)
        self.btnBuildSpec.setInputMethodHints(Qt.ImhNone)
        self.btnBuildSpec.setIcon(icon15)
        self.btnBuildSpec.setIconSize(QSize(24, 24))
        self.btnBuildSpec.setCheckable(False)
        self.btnBuildSpec.setFlat(False)
        self.lbDashborad_12 = QLabel(self.tab_5)
        self.lbDashborad_12.setObjectName(u"lbDashborad_12")
        self.lbDashborad_12.setGeometry(QRect(180, 300, 121, 20))
        self.lbDashborad_12.setFont(font)
        self.lbDashborad_13 = QLabel(self.tab_5)
        self.lbDashborad_13.setObjectName(u"lbDashborad_13")
        self.lbDashborad_13.setGeometry(QRect(180, 381, 121, 20))
        self.lbDashborad_13.setFont(font)
        self.btnBuildBOM = QPushButton(self.tab_5)
        self.btnBuildBOM.setObjectName(u"btnBuildBOM")
        self.btnBuildBOM.setEnabled(True)
        self.btnBuildBOM.setGeometry(QRect(120, 370, 48, 41))
        sizePolicy.setHeightForWidth(self.btnBuildBOM.sizePolicy().hasHeightForWidth())
        self.btnBuildBOM.setSizePolicy(sizePolicy)
        self.btnBuildBOM.setFont(font1)
        self.btnBuildBOM.setToolTipDuration(0)
        self.btnBuildBOM.setLayoutDirection(Qt.LeftToRight)
        self.btnBuildBOM.setAutoFillBackground(False)
        self.btnBuildBOM.setInputMethodHints(Qt.ImhNone)
        self.btnBuildBOM.setIcon(icon15)
        self.btnBuildBOM.setIconSize(QSize(24, 24))
        self.btnBuildBOM.setCheckable(False)
        self.btnBuildBOM.setFlat(False)
        self.btnBuildBOE = QPushButton(self.tab_5)
        self.btnBuildBOE.setObjectName(u"btnBuildBOE")
        self.btnBuildBOE.setEnabled(True)
        self.btnBuildBOE.setGeometry(QRect(120, 410, 48, 41))
        sizePolicy.setHeightForWidth(self.btnBuildBOE.sizePolicy().hasHeightForWidth())
        self.btnBuildBOE.setSizePolicy(sizePolicy)
        self.btnBuildBOE.setFont(font1)
        self.btnBuildBOE.setToolTipDuration(0)
        self.btnBuildBOE.setLayoutDirection(Qt.LeftToRight)
        self.btnBuildBOE.setAutoFillBackground(False)
        self.btnBuildBOE.setInputMethodHints(Qt.ImhNone)
        self.btnBuildBOE.setIcon(icon15)
        self.btnBuildBOE.setIconSize(QSize(24, 24))
        self.btnBuildBOE.setCheckable(False)
        self.btnBuildBOE.setFlat(False)
        self.lbDashborad_14 = QLabel(self.tab_5)
        self.lbDashborad_14.setObjectName(u"lbDashborad_14")
        self.lbDashborad_14.setGeometry(QRect(180, 421, 121, 20))
        self.lbDashborad_14.setFont(font)
        self.lbDashborad_15 = QLabel(self.tab_5)
        self.lbDashborad_15.setObjectName(u"lbDashborad_15")
        self.lbDashborad_15.setGeometry(QRect(530, 211, 161, 20))
        self.lbDashborad_15.setFont(font)
        self.lbDashborad_16 = QLabel(self.tab_5)
        self.lbDashborad_16.setObjectName(u"lbDashborad_16")
        self.lbDashborad_16.setGeometry(QRect(530, 171, 171, 20))
        self.lbDashborad_16.setFont(font)
        self.btnConveyorSchedule = QPushButton(self.tab_5)
        self.btnConveyorSchedule.setObjectName(u"btnConveyorSchedule")
        self.btnConveyorSchedule.setEnabled(True)
        self.btnConveyorSchedule.setGeometry(QRect(470, 200, 48, 41))
        sizePolicy.setHeightForWidth(self.btnConveyorSchedule.sizePolicy().hasHeightForWidth())
        self.btnConveyorSchedule.setSizePolicy(sizePolicy)
        self.btnConveyorSchedule.setFont(font1)
        self.btnConveyorSchedule.setToolTipDuration(0)
        self.btnConveyorSchedule.setLayoutDirection(Qt.LeftToRight)
        self.btnConveyorSchedule.setAutoFillBackground(False)
        self.btnConveyorSchedule.setInputMethodHints(Qt.ImhNone)
        self.btnConveyorSchedule.setIcon(icon15)
        self.btnConveyorSchedule.setIconSize(QSize(24, 24))
        self.btnConveyorSchedule.setCheckable(False)
        self.btnConveyorSchedule.setFlat(False)
        self.btnMechDataSheet = QPushButton(self.tab_5)
        self.btnMechDataSheet.setObjectName(u"btnMechDataSheet")
        self.btnMechDataSheet.setEnabled(True)
        self.btnMechDataSheet.setGeometry(QRect(470, 160, 48, 41))
        sizePolicy.setHeightForWidth(self.btnMechDataSheet.sizePolicy().hasHeightForWidth())
        self.btnMechDataSheet.setSizePolicy(sizePolicy)
        self.btnMechDataSheet.setFont(font1)
        self.btnMechDataSheet.setToolTipDuration(0)
        self.btnMechDataSheet.setLayoutDirection(Qt.LeftToRight)
        self.btnMechDataSheet.setAutoFillBackground(False)
        self.btnMechDataSheet.setInputMethodHints(Qt.ImhNone)
        self.btnMechDataSheet.setIcon(icon15)
        self.btnMechDataSheet.setIconSize(QSize(24, 24))
        self.btnMechDataSheet.setCheckable(False)
        self.btnMechDataSheet.setFlat(False)
        self.lbDashborad_17 = QLabel(self.tab_5)
        self.lbDashborad_17.setObjectName(u"lbDashborad_17")
        self.lbDashborad_17.setGeometry(QRect(180, 462, 121, 20))
        self.lbDashborad_17.setFont(font)
        self.btnBuildDrg = QPushButton(self.tab_5)
        self.btnBuildDrg.setObjectName(u"btnBuildDrg")
        self.btnBuildDrg.setEnabled(True)
        self.btnBuildDrg.setGeometry(QRect(120, 451, 48, 41))
        sizePolicy.setHeightForWidth(self.btnBuildDrg.sizePolicy().hasHeightForWidth())
        self.btnBuildDrg.setSizePolicy(sizePolicy)
        self.btnBuildDrg.setFont(font1)
        self.btnBuildDrg.setToolTipDuration(0)
        self.btnBuildDrg.setLayoutDirection(Qt.LeftToRight)
        self.btnBuildDrg.setAutoFillBackground(False)
        self.btnBuildDrg.setInputMethodHints(Qt.ImhNone)
        self.btnBuildDrg.setIcon(icon15)
        self.btnBuildDrg.setIconSize(QSize(24, 24))
        self.btnBuildDrg.setCheckable(False)
        self.btnBuildDrg.setFlat(False)
        self.lbDashborad_18 = QLabel(self.tab_5)
        self.lbDashborad_18.setObjectName(u"lbDashborad_18")
        self.lbDashborad_18.setGeometry(QRect(180, 341, 121, 20))
        self.lbDashborad_18.setFont(font)
        self.btnBuildCalc = QPushButton(self.tab_5)
        self.btnBuildCalc.setObjectName(u"btnBuildCalc")
        self.btnBuildCalc.setEnabled(True)
        self.btnBuildCalc.setGeometry(QRect(120, 330, 48, 41))
        sizePolicy.setHeightForWidth(self.btnBuildCalc.sizePolicy().hasHeightForWidth())
        self.btnBuildCalc.setSizePolicy(sizePolicy)
        self.btnBuildCalc.setFont(font1)
        self.btnBuildCalc.setToolTipDuration(0)
        self.btnBuildCalc.setLayoutDirection(Qt.LeftToRight)
        self.btnBuildCalc.setAutoFillBackground(False)
        self.btnBuildCalc.setInputMethodHints(Qt.ImhNone)
        self.btnBuildCalc.setIcon(icon15)
        self.btnBuildCalc.setIconSize(QSize(24, 24))
        self.btnBuildCalc.setCheckable(False)
        self.btnBuildCalc.setFlat(False)
        self.btnStrucCalc = QPushButton(self.tab_5)
        self.btnStrucCalc.setObjectName(u"btnStrucCalc")
        self.btnStrucCalc.setEnabled(True)
        self.btnStrucCalc.setGeometry(QRect(110, 578, 48, 41))
        sizePolicy.setHeightForWidth(self.btnStrucCalc.sizePolicy().hasHeightForWidth())
        self.btnStrucCalc.setSizePolicy(sizePolicy)
        self.btnStrucCalc.setFont(font1)
        self.btnStrucCalc.setToolTipDuration(0)
        self.btnStrucCalc.setLayoutDirection(Qt.LeftToRight)
        self.btnStrucCalc.setAutoFillBackground(False)
        self.btnStrucCalc.setInputMethodHints(Qt.ImhNone)
        self.btnStrucCalc.setIcon(icon15)
        self.btnStrucCalc.setIconSize(QSize(24, 24))
        self.btnStrucCalc.setCheckable(False)
        self.btnStrucCalc.setFlat(False)
        self.lbDashborad_19 = QLabel(self.tab_5)
        self.lbDashborad_19.setObjectName(u"lbDashborad_19")
        self.lbDashborad_19.setGeometry(QRect(170, 589, 121, 20))
        self.lbDashborad_19.setFont(font)
        self.lbDashborad_21 = QLabel(self.tab_5)
        self.lbDashborad_21.setObjectName(u"lbDashborad_21")
        self.lbDashborad_21.setGeometry(QRect(170, 548, 121, 20))
        self.lbDashborad_21.setFont(font)
        self.btnStrucDrg = QPushButton(self.tab_5)
        self.btnStrucDrg.setObjectName(u"btnStrucDrg")
        self.btnStrucDrg.setEnabled(True)
        self.btnStrucDrg.setGeometry(QRect(110, 659, 48, 41))
        sizePolicy.setHeightForWidth(self.btnStrucDrg.sizePolicy().hasHeightForWidth())
        self.btnStrucDrg.setSizePolicy(sizePolicy)
        self.btnStrucDrg.setFont(font1)
        self.btnStrucDrg.setToolTipDuration(0)
        self.btnStrucDrg.setLayoutDirection(Qt.LeftToRight)
        self.btnStrucDrg.setAutoFillBackground(False)
        self.btnStrucDrg.setInputMethodHints(Qt.ImhNone)
        self.btnStrucDrg.setIcon(icon15)
        self.btnStrucDrg.setIconSize(QSize(24, 24))
        self.btnStrucDrg.setCheckable(False)
        self.btnStrucDrg.setFlat(False)
        self.btnStructCalc = QPushButton(self.tab_5)
        self.btnStructCalc.setObjectName(u"btnStructCalc")
        self.btnStructCalc.setEnabled(True)
        self.btnStructCalc.setGeometry(QRect(110, 618, 48, 41))
        sizePolicy.setHeightForWidth(self.btnStructCalc.sizePolicy().hasHeightForWidth())
        self.btnStructCalc.setSizePolicy(sizePolicy)
        self.btnStructCalc.setFont(font1)
        self.btnStructCalc.setToolTipDuration(0)
        self.btnStructCalc.setLayoutDirection(Qt.LeftToRight)
        self.btnStructCalc.setAutoFillBackground(False)
        self.btnStructCalc.setInputMethodHints(Qt.ImhNone)
        self.btnStructCalc.setIcon(icon15)
        self.btnStructCalc.setIconSize(QSize(24, 24))
        self.btnStructCalc.setCheckable(False)
        self.btnStructCalc.setFlat(False)
        self.lbDashborad_22 = QLabel(self.tab_5)
        self.lbDashborad_22.setObjectName(u"lbDashborad_22")
        self.lbDashborad_22.setGeometry(QRect(170, 629, 121, 20))
        self.lbDashborad_22.setFont(font)
        self.btnStrucSpec = QPushButton(self.tab_5)
        self.btnStrucSpec.setObjectName(u"btnStrucSpec")
        self.btnStrucSpec.setEnabled(True)
        self.btnStrucSpec.setGeometry(QRect(110, 537, 48, 41))
        sizePolicy.setHeightForWidth(self.btnStrucSpec.sizePolicy().hasHeightForWidth())
        self.btnStrucSpec.setSizePolicy(sizePolicy)
        self.btnStrucSpec.setFont(font1)
        self.btnStrucSpec.setToolTipDuration(0)
        self.btnStrucSpec.setLayoutDirection(Qt.LeftToRight)
        self.btnStrucSpec.setAutoFillBackground(False)
        self.btnStrucSpec.setInputMethodHints(Qt.ImhNone)
        self.btnStrucSpec.setIcon(icon15)
        self.btnStrucSpec.setIconSize(QSize(24, 24))
        self.btnStrucSpec.setCheckable(False)
        self.btnStrucSpec.setFlat(False)
        self.lbDashborad_23 = QLabel(self.tab_5)
        self.lbDashborad_23.setObjectName(u"lbDashborad_23")
        self.lbDashborad_23.setGeometry(QRect(170, 670, 121, 20))
        self.lbDashborad_23.setFont(font)
        self.lbDashborad_20 = QLabel(self.tab_5)
        self.lbDashborad_20.setObjectName(u"lbDashborad_20")
        self.lbDashborad_20.setGeometry(QRect(530, 131, 121, 20))
        self.lbDashborad_20.setFont(font)
        self.btnMechSpec = QPushButton(self.tab_5)
        self.btnMechSpec.setObjectName(u"btnMechSpec")
        self.btnMechSpec.setEnabled(True)
        self.btnMechSpec.setGeometry(QRect(470, 79, 48, 41))
        sizePolicy.setHeightForWidth(self.btnMechSpec.sizePolicy().hasHeightForWidth())
        self.btnMechSpec.setSizePolicy(sizePolicy)
        self.btnMechSpec.setFont(font1)
        self.btnMechSpec.setToolTipDuration(0)
        self.btnMechSpec.setLayoutDirection(Qt.LeftToRight)
        self.btnMechSpec.setAutoFillBackground(False)
        self.btnMechSpec.setInputMethodHints(Qt.ImhNone)
        self.btnMechSpec.setIcon(icon15)
        self.btnMechSpec.setIconSize(QSize(24, 24))
        self.btnMechSpec.setCheckable(False)
        self.btnMechSpec.setFlat(False)
        self.lbDashborad_24 = QLabel(self.tab_5)
        self.lbDashborad_24.setObjectName(u"lbDashborad_24")
        self.lbDashborad_24.setGeometry(QRect(530, 90, 121, 20))
        self.lbDashborad_24.setFont(font)
        self.btnMechCalc = QPushButton(self.tab_5)
        self.btnMechCalc.setObjectName(u"btnMechCalc")
        self.btnMechCalc.setEnabled(True)
        self.btnMechCalc.setGeometry(QRect(470, 120, 48, 41))
        sizePolicy.setHeightForWidth(self.btnMechCalc.sizePolicy().hasHeightForWidth())
        self.btnMechCalc.setSizePolicy(sizePolicy)
        self.btnMechCalc.setFont(font1)
        self.btnMechCalc.setToolTipDuration(0)
        self.btnMechCalc.setLayoutDirection(Qt.LeftToRight)
        self.btnMechCalc.setAutoFillBackground(False)
        self.btnMechCalc.setInputMethodHints(Qt.ImhNone)
        self.btnMechCalc.setIcon(icon15)
        self.btnMechCalc.setIconSize(QSize(24, 24))
        self.btnMechCalc.setCheckable(False)
        self.btnMechCalc.setFlat(False)
        self.lbDashborad_25 = QLabel(self.tab_5)
        self.lbDashborad_25.setObjectName(u"lbDashborad_25")
        self.lbDashborad_25.setGeometry(QRect(520, 389, 121, 20))
        self.lbDashborad_25.setFont(font)
        self.lbDashborad_26 = QLabel(self.tab_5)
        self.lbDashborad_26.setObjectName(u"lbDashborad_26")
        self.lbDashborad_26.setGeometry(QRect(520, 430, 121, 20))
        self.lbDashborad_26.setFont(font)
        self.lbDashborad_27 = QLabel(self.tab_5)
        self.lbDashborad_27.setObjectName(u"lbDashborad_27")
        self.lbDashborad_27.setGeometry(QRect(520, 349, 121, 20))
        self.lbDashborad_27.setFont(font)
        self.btnCivlDrg = QPushButton(self.tab_5)
        self.btnCivlDrg.setObjectName(u"btnCivlDrg")
        self.btnCivlDrg.setEnabled(True)
        self.btnCivlDrg.setGeometry(QRect(460, 419, 48, 41))
        sizePolicy.setHeightForWidth(self.btnCivlDrg.sizePolicy().hasHeightForWidth())
        self.btnCivlDrg.setSizePolicy(sizePolicy)
        self.btnCivlDrg.setFont(font1)
        self.btnCivlDrg.setToolTipDuration(0)
        self.btnCivlDrg.setLayoutDirection(Qt.LeftToRight)
        self.btnCivlDrg.setAutoFillBackground(False)
        self.btnCivlDrg.setInputMethodHints(Qt.ImhNone)
        self.btnCivlDrg.setIcon(icon15)
        self.btnCivlDrg.setIconSize(QSize(24, 24))
        self.btnCivlDrg.setCheckable(False)
        self.btnCivlDrg.setFlat(False)
        self.btnDCivilsList = QPushButton(self.tab_5)
        self.btnDCivilsList.setObjectName(u"btnDCivilsList")
        self.btnDCivilsList.setEnabled(True)
        self.btnDCivilsList.setGeometry(QRect(370, 259, 48, 41))
        sizePolicy.setHeightForWidth(self.btnDCivilsList.sizePolicy().hasHeightForWidth())
        self.btnDCivilsList.setSizePolicy(sizePolicy)
        self.btnDCivilsList.setFont(font1)
        self.btnDCivilsList.setToolTipDuration(0)
        self.btnDCivilsList.setLayoutDirection(Qt.LeftToRight)
        self.btnDCivilsList.setAutoFillBackground(False)
        self.btnDCivilsList.setInputMethodHints(Qt.ImhNone)
        self.btnDCivilsList.setIcon(icon15)
        self.btnDCivilsList.setIconSize(QSize(24, 24))
        self.btnDCivilsList.setCheckable(False)
        self.btnDCivilsList.setFlat(False)
        self.lbDashborad_28 = QLabel(self.tab_5)
        self.lbDashborad_28.setObjectName(u"lbDashborad_28")
        self.lbDashborad_28.setGeometry(QRect(430, 272, 121, 20))
        self.lbDashborad_28.setFont(font)
        self.btnCivilSpec = QPushButton(self.tab_5)
        self.btnCivilSpec.setObjectName(u"btnCivilSpec")
        self.btnCivilSpec.setEnabled(True)
        self.btnCivilSpec.setGeometry(QRect(460, 297, 48, 41))
        sizePolicy.setHeightForWidth(self.btnCivilSpec.sizePolicy().hasHeightForWidth())
        self.btnCivilSpec.setSizePolicy(sizePolicy)
        self.btnCivilSpec.setFont(font1)
        self.btnCivilSpec.setToolTipDuration(0)
        self.btnCivilSpec.setLayoutDirection(Qt.LeftToRight)
        self.btnCivilSpec.setAutoFillBackground(False)
        self.btnCivilSpec.setInputMethodHints(Qt.ImhNone)
        self.btnCivilSpec.setIcon(icon15)
        self.btnCivilSpec.setIconSize(QSize(24, 24))
        self.btnCivilSpec.setCheckable(False)
        self.btnCivilSpec.setFlat(False)
        self.lbDashborad_29 = QLabel(self.tab_5)
        self.lbDashborad_29.setObjectName(u"lbDashborad_29")
        self.lbDashborad_29.setGeometry(QRect(520, 310, 121, 20))
        self.lbDashborad_29.setFont(font)
        self.btnCivilBOM = QPushButton(self.tab_5)
        self.btnCivilBOM.setObjectName(u"btnCivilBOM")
        self.btnCivilBOM.setEnabled(True)
        self.btnCivilBOM.setGeometry(QRect(460, 378, 48, 41))
        sizePolicy.setHeightForWidth(self.btnCivilBOM.sizePolicy().hasHeightForWidth())
        self.btnCivilBOM.setSizePolicy(sizePolicy)
        self.btnCivilBOM.setFont(font1)
        self.btnCivilBOM.setToolTipDuration(0)
        self.btnCivilBOM.setLayoutDirection(Qt.LeftToRight)
        self.btnCivilBOM.setAutoFillBackground(False)
        self.btnCivilBOM.setInputMethodHints(Qt.ImhNone)
        self.btnCivilBOM.setIcon(icon15)
        self.btnCivilBOM.setIconSize(QSize(24, 24))
        self.btnCivilBOM.setCheckable(False)
        self.btnCivilBOM.setFlat(False)
        self.btnCivilCalc = QPushButton(self.tab_5)
        self.btnCivilCalc.setObjectName(u"btnCivilCalc")
        self.btnCivilCalc.setEnabled(True)
        self.btnCivilCalc.setGeometry(QRect(460, 338, 48, 41))
        sizePolicy.setHeightForWidth(self.btnCivilCalc.sizePolicy().hasHeightForWidth())
        self.btnCivilCalc.setSizePolicy(sizePolicy)
        self.btnCivilCalc.setFont(font1)
        self.btnCivilCalc.setToolTipDuration(0)
        self.btnCivilCalc.setLayoutDirection(Qt.LeftToRight)
        self.btnCivilCalc.setAutoFillBackground(False)
        self.btnCivilCalc.setInputMethodHints(Qt.ImhNone)
        self.btnCivilCalc.setIcon(icon15)
        self.btnCivilCalc.setIconSize(QSize(24, 24))
        self.btnCivilCalc.setCheckable(False)
        self.btnCivilCalc.setFlat(False)
        self.lbDashborad_30 = QLabel(self.tab_5)
        self.lbDashborad_30.setObjectName(u"lbDashborad_30")
        self.lbDashborad_30.setGeometry(QRect(890, 563, 121, 20))
        self.lbDashborad_30.setFont(font)
        self.btnTenderQuotes = QPushButton(self.tab_5)
        self.btnTenderQuotes.setObjectName(u"btnTenderQuotes")
        self.btnTenderQuotes.setEnabled(True)
        self.btnTenderQuotes.setGeometry(QRect(740, 512, 48, 41))
        sizePolicy.setHeightForWidth(self.btnTenderQuotes.sizePolicy().hasHeightForWidth())
        self.btnTenderQuotes.setSizePolicy(sizePolicy)
        self.btnTenderQuotes.setFont(font1)
        self.btnTenderQuotes.setToolTipDuration(0)
        self.btnTenderQuotes.setLayoutDirection(Qt.LeftToRight)
        self.btnTenderQuotes.setAutoFillBackground(False)
        self.btnTenderQuotes.setInputMethodHints(Qt.ImhNone)
        self.btnTenderQuotes.setIcon(icon15)
        self.btnTenderQuotes.setIconSize(QSize(24, 24))
        self.btnTenderQuotes.setCheckable(False)
        self.btnTenderQuotes.setFlat(False)
        self.lbDashborad_31 = QLabel(self.tab_5)
        self.lbDashborad_31.setObjectName(u"lbDashborad_31")
        self.lbDashborad_31.setGeometry(QRect(800, 525, 231, 20))
        self.lbDashborad_31.setFont(font)
        self.btnTenderSOW = QPushButton(self.tab_5)
        self.btnTenderSOW.setObjectName(u"btnTenderSOW")
        self.btnTenderSOW.setEnabled(True)
        self.btnTenderSOW.setGeometry(QRect(830, 550, 48, 41))
        sizePolicy.setHeightForWidth(self.btnTenderSOW.sizePolicy().hasHeightForWidth())
        self.btnTenderSOW.setSizePolicy(sizePolicy)
        self.btnTenderSOW.setFont(font1)
        self.btnTenderSOW.setToolTipDuration(0)
        self.btnTenderSOW.setLayoutDirection(Qt.LeftToRight)
        self.btnTenderSOW.setAutoFillBackground(False)
        self.btnTenderSOW.setInputMethodHints(Qt.ImhNone)
        self.btnTenderSOW.setIcon(icon15)
        self.btnTenderSOW.setIconSize(QSize(24, 24))
        self.btnTenderSOW.setCheckable(False)
        self.btnTenderSOW.setFlat(False)
        self.tabDoccontrol.addTab(self.tab_5, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabDoccontrol.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tabDoccontrol.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabDoccontrol.addTab(self.tab_9, "")
        self.stwMain.addWidget(self.documentControl)
        self.procurement = QWidget()
        self.procurement.setObjectName(u"procurement")
        self.label_23 = QLabel(self.procurement)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(260, 30, 571, 21))
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setFont(font2)
        self.label_23.setAlignment(Qt.AlignCenter)
        self.stwMain.addWidget(self.procurement)
        self.analysis = QWidget()
        self.analysis.setObjectName(u"analysis")
        self.label_24 = QLabel(self.analysis)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(290, 30, 571, 21))
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setFont(font2)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.stwMain.addWidget(self.analysis)
        self.techData = QWidget()
        self.techData.setObjectName(u"techData")
        self.label_25 = QLabel(self.techData)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(290, 30, 571, 21))
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setFont(font2)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.tabTechData = QTabWidget(self.techData)
        self.tabTechData.setObjectName(u"tabTechData")
        self.tabTechData.setGeometry(QRect(10, 60, 1251, 771))
        self.tabSteelSections = QWidget()
        self.tabSteelSections.setObjectName(u"tabSteelSections")
        self.tvSteelTable = QTableView(self.tabSteelSections)
        self.tvSteelTable.setObjectName(u"tvSteelTable")
        self.tvSteelTable.setGeometry(QRect(10, 280, 1221, 461))
        self.lbCompany_3 = QLabel(self.tabSteelSections)
        self.lbCompany_3.setObjectName(u"lbCompany_3")
        self.lbCompany_3.setGeometry(QRect(30, 10, 121, 20))
        self.lbCompany_3.setFont(font)
        self.leUnitMass = QLineEdit(self.tabSteelSections)
        self.leUnitMass.setObjectName(u"leUnitMass")
        self.leUnitMass.setGeometry(QRect(250, 30, 101, 31))
        self.leUnitMass.setFont(font4)
        self.leUnitMass.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leUnitMass.setReadOnly(True)
        self.lbCompID_2 = QLabel(self.tabSteelSections)
        self.lbCompID_2.setObjectName(u"lbCompID_2")
        self.lbCompID_2.setGeometry(QRect(250, 10, 121, 20))
        self.lbCompID_2.setFont(font)
        self.lbCompany_4 = QLabel(self.tabSteelSections)
        self.lbCompany_4.setObjectName(u"lbCompany_4")
        self.lbCompany_4.setGeometry(QRect(110, 10, 121, 20))
        self.lbCompany_4.setFont(font)
        self.leHeight = QLineEdit(self.tabSteelSections)
        self.leHeight.setObjectName(u"leHeight")
        self.leHeight.setGeometry(QRect(360, 30, 101, 31))
        self.leHeight.setFont(font4)
        self.leHeight.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leHeight.setReadOnly(True)
        self.lbCompID_3 = QLabel(self.tabSteelSections)
        self.lbCompID_3.setObjectName(u"lbCompID_3")
        self.lbCompID_3.setGeometry(QRect(360, 10, 121, 20))
        self.lbCompID_3.setFont(font)
        self.leDiameter = QLineEdit(self.tabSteelSections)
        self.leDiameter.setObjectName(u"leDiameter")
        self.leDiameter.setGeometry(QRect(690, 30, 101, 31))
        self.leDiameter.setFont(font4)
        self.leDiameter.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leDiameter.setReadOnly(True)
        self.lbCompID_4 = QLabel(self.tabSteelSections)
        self.lbCompID_4.setObjectName(u"lbCompID_4")
        self.lbCompID_4.setGeometry(QRect(690, 10, 101, 20))
        self.lbCompID_4.setFont(font)
        self.leLipHeight = QLineEdit(self.tabSteelSections)
        self.leLipHeight.setObjectName(u"leLipHeight")
        self.leLipHeight.setGeometry(QRect(580, 30, 101, 31))
        self.leLipHeight.setFont(font4)
        self.leLipHeight.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leLipHeight.setReadOnly(True)
        self.lbCompID_5 = QLabel(self.tabSteelSections)
        self.lbCompID_5.setObjectName(u"lbCompID_5")
        self.lbCompID_5.setGeometry(QRect(580, 10, 121, 20))
        self.lbCompID_5.setFont(font)
        self.leWidth = QLineEdit(self.tabSteelSections)
        self.leWidth.setObjectName(u"leWidth")
        self.leWidth.setGeometry(QRect(470, 30, 101, 31))
        self.leWidth.setFont(font4)
        self.leWidth.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leWidth.setReadOnly(True)
        self.lbCompID_6 = QLabel(self.tabSteelSections)
        self.lbCompID_6.setObjectName(u"lbCompID_6")
        self.lbCompID_6.setGeometry(QRect(470, 10, 121, 20))
        self.lbCompID_6.setFont(font)
        self.lbCompID_7 = QLabel(self.tabSteelSections)
        self.lbCompID_7.setObjectName(u"lbCompID_7")
        self.lbCompID_7.setGeometry(QRect(800, 10, 101, 20))
        self.lbCompID_7.setFont(font)
        self.leWebThickness = QLineEdit(self.tabSteelSections)
        self.leWebThickness.setObjectName(u"leWebThickness")
        self.leWebThickness.setGeometry(QRect(800, 30, 101, 31))
        self.leWebThickness.setFont(font4)
        self.leWebThickness.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leWebThickness.setReadOnly(True)
        self.leFlangeThickness = QLineEdit(self.tabSteelSections)
        self.leFlangeThickness.setObjectName(u"leFlangeThickness")
        self.leFlangeThickness.setGeometry(QRect(910, 30, 101, 31))
        self.leFlangeThickness.setFont(font4)
        self.leFlangeThickness.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leFlangeThickness.setReadOnly(True)
        self.lbCompID_8 = QLabel(self.tabSteelSections)
        self.lbCompID_8.setObjectName(u"lbCompID_8")
        self.lbCompID_8.setGeometry(QRect(910, 10, 101, 20))
        self.lbCompID_8.setFont(font)
        self.leWebradius = QLineEdit(self.tabSteelSections)
        self.leWebradius.setObjectName(u"leWebradius")
        self.leWebradius.setGeometry(QRect(1020, 30, 101, 31))
        self.leWebradius.setFont(font4)
        self.leWebradius.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leWebradius.setReadOnly(True)
        self.lbCompID_9 = QLabel(self.tabSteelSections)
        self.lbCompID_9.setObjectName(u"lbCompID_9")
        self.lbCompID_9.setGeometry(QRect(1020, 10, 101, 20))
        self.lbCompID_9.setFont(font)
        self.leFlangeRadius = QLineEdit(self.tabSteelSections)
        self.leFlangeRadius.setObjectName(u"leFlangeRadius")
        self.leFlangeRadius.setGeometry(QRect(1130, 30, 101, 31))
        self.leFlangeRadius.setFont(font4)
        self.leFlangeRadius.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leFlangeRadius.setReadOnly(True)
        self.lbCompID_10 = QLabel(self.tabSteelSections)
        self.lbCompID_10.setObjectName(u"lbCompID_10")
        self.lbCompID_10.setGeometry(QRect(1130, 10, 101, 20))
        self.lbCompID_10.setFont(font)
        self.lbCompID_11 = QLabel(self.tabSteelSections)
        self.lbCompID_11.setObjectName(u"lbCompID_11")
        self.lbCompID_11.setGeometry(QRect(30, 70, 101, 20))
        self.lbCompID_11.setFont(font)
        self.leTaperDistance = QLineEdit(self.tabSteelSections)
        self.leTaperDistance.setObjectName(u"leTaperDistance")
        self.leTaperDistance.setGeometry(QRect(30, 90, 101, 31))
        self.leTaperDistance.setFont(font4)
        self.leTaperDistance.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leTaperDistance.setReadOnly(True)
        self.lbCompID_12 = QLabel(self.tabSteelSections)
        self.lbCompID_12.setObjectName(u"lbCompID_12")
        self.lbCompID_12.setGeometry(QRect(250, 70, 101, 20))
        self.lbCompID_12.setFont(font)
        self.leArea = QLineEdit(self.tabSteelSections)
        self.leArea.setObjectName(u"leArea")
        self.leArea.setGeometry(QRect(250, 90, 101, 31))
        self.leArea.setFont(font4)
        self.leArea.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leArea.setReadOnly(True)
        self.leTaperAngle = QLineEdit(self.tabSteelSections)
        self.leTaperAngle.setObjectName(u"leTaperAngle")
        self.leTaperAngle.setGeometry(QRect(140, 90, 101, 31))
        self.leTaperAngle.setFont(font4)
        self.leTaperAngle.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leTaperAngle.setReadOnly(True)
        self.leIxx = QLineEdit(self.tabSteelSections)
        self.leIxx.setObjectName(u"leIxx")
        self.leIxx.setGeometry(QRect(360, 90, 101, 31))
        self.leIxx.setFont(font4)
        self.leIxx.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leIxx.setReadOnly(True)
        self.lbCompID_15 = QLabel(self.tabSteelSections)
        self.lbCompID_15.setObjectName(u"lbCompID_15")
        self.lbCompID_15.setGeometry(QRect(360, 70, 101, 20))
        self.lbCompID_15.setFont(font)
        self.leZxx = QLineEdit(self.tabSteelSections)
        self.leZxx.setObjectName(u"leZxx")
        self.leZxx.setGeometry(QRect(470, 90, 101, 31))
        self.leZxx.setFont(font4)
        self.leZxx.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leZxx.setReadOnly(True)
        self.lbCompID_16 = QLabel(self.tabSteelSections)
        self.lbCompID_16.setObjectName(u"lbCompID_16")
        self.lbCompID_16.setGeometry(QRect(470, 70, 101, 20))
        self.lbCompID_16.setFont(font)
        self.lerxx = QLineEdit(self.tabSteelSections)
        self.lerxx.setObjectName(u"lerxx")
        self.lerxx.setGeometry(QRect(580, 90, 101, 31))
        self.lerxx.setFont(font4)
        self.lerxx.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lerxx.setReadOnly(True)
        self.lbCompID_17 = QLabel(self.tabSteelSections)
        self.lbCompID_17.setObjectName(u"lbCompID_17")
        self.lbCompID_17.setGeometry(QRect(580, 70, 101, 20))
        self.lbCompID_17.setFont(font)
        self.leIyy = QLineEdit(self.tabSteelSections)
        self.leIyy.setObjectName(u"leIyy")
        self.leIyy.setGeometry(QRect(690, 90, 101, 31))
        self.leIyy.setFont(font4)
        self.leIyy.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leIyy.setReadOnly(True)
        self.lbCompID_18 = QLabel(self.tabSteelSections)
        self.lbCompID_18.setObjectName(u"lbCompID_18")
        self.lbCompID_18.setGeometry(QRect(690, 70, 101, 20))
        self.lbCompID_18.setFont(font)
        self.leZyy = QLineEdit(self.tabSteelSections)
        self.leZyy.setObjectName(u"leZyy")
        self.leZyy.setGeometry(QRect(800, 90, 101, 31))
        self.leZyy.setFont(font4)
        self.leZyy.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leZyy.setReadOnly(True)
        self.lbCompID_19 = QLabel(self.tabSteelSections)
        self.lbCompID_19.setObjectName(u"lbCompID_19")
        self.lbCompID_19.setGeometry(QRect(800, 70, 101, 20))
        self.lbCompID_19.setFont(font)
        self.leryy = QLineEdit(self.tabSteelSections)
        self.leryy.setObjectName(u"leryy")
        self.leryy.setGeometry(QRect(910, 90, 101, 31))
        self.leryy.setFont(font4)
        self.leryy.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leryy.setReadOnly(True)
        self.lbCompID_20 = QLabel(self.tabSteelSections)
        self.lbCompID_20.setObjectName(u"lbCompID_20")
        self.lbCompID_20.setGeometry(QRect(910, 70, 101, 20))
        self.lbCompID_20.setFont(font)
        self.leJ = QLineEdit(self.tabSteelSections)
        self.leJ.setObjectName(u"leJ")
        self.leJ.setGeometry(QRect(1020, 90, 101, 31))
        self.leJ.setFont(font4)
        self.leJ.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leJ.setReadOnly(True)
        self.lbCompID_21 = QLabel(self.tabSteelSections)
        self.lbCompID_21.setObjectName(u"lbCompID_21")
        self.lbCompID_21.setGeometry(QRect(1020, 70, 101, 20))
        self.lbCompID_21.setFont(font)
        self.leCw = QLineEdit(self.tabSteelSections)
        self.leCw.setObjectName(u"leCw")
        self.leCw.setGeometry(QRect(1130, 90, 101, 31))
        self.leCw.setFont(font4)
        self.leCw.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leCw.setReadOnly(True)
        self.lbCompID_22 = QLabel(self.tabSteelSections)
        self.lbCompID_22.setObjectName(u"lbCompID_22")
        self.lbCompID_22.setGeometry(QRect(1130, 70, 101, 20))
        self.lbCompID_22.setFont(font)
        self.leZplx = QLineEdit(self.tabSteelSections)
        self.leZplx.setObjectName(u"leZplx")
        self.leZplx.setGeometry(QRect(30, 150, 101, 31))
        self.leZplx.setFont(font4)
        self.leZplx.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leZplx.setReadOnly(True)
        self.lbCompID_23 = QLabel(self.tabSteelSections)
        self.lbCompID_23.setObjectName(u"lbCompID_23")
        self.lbCompID_23.setGeometry(QRect(30, 130, 101, 20))
        self.lbCompID_23.setFont(font)
        self.leZply = QLineEdit(self.tabSteelSections)
        self.leZply.setObjectName(u"leZply")
        self.leZply.setGeometry(QRect(140, 150, 101, 31))
        self.leZply.setFont(font4)
        self.leZply.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leZply.setReadOnly(True)
        self.lbCompID_24 = QLabel(self.tabSteelSections)
        self.lbCompID_24.setObjectName(u"lbCompID_24")
        self.lbCompID_24.setGeometry(QRect(140, 130, 101, 20))
        self.lbCompID_24.setFont(font)
        self.leIuu = QLineEdit(self.tabSteelSections)
        self.leIuu.setObjectName(u"leIuu")
        self.leIuu.setGeometry(QRect(250, 150, 101, 31))
        self.leIuu.setFont(font4)
        self.leIuu.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leIuu.setReadOnly(True)
        self.lbCompID_25 = QLabel(self.tabSteelSections)
        self.lbCompID_25.setObjectName(u"lbCompID_25")
        self.lbCompID_25.setGeometry(QRect(250, 130, 101, 20))
        self.lbCompID_25.setFont(font)
        self.leZuu = QLineEdit(self.tabSteelSections)
        self.leZuu.setObjectName(u"leZuu")
        self.leZuu.setGeometry(QRect(360, 150, 101, 31))
        self.leZuu.setFont(font4)
        self.leZuu.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leZuu.setReadOnly(True)
        self.lbCompID_26 = QLabel(self.tabSteelSections)
        self.lbCompID_26.setObjectName(u"lbCompID_26")
        self.lbCompID_26.setGeometry(QRect(360, 130, 101, 20))
        self.lbCompID_26.setFont(font)
        self.leruu = QLineEdit(self.tabSteelSections)
        self.leruu.setObjectName(u"leruu")
        self.leruu.setGeometry(QRect(470, 150, 101, 31))
        self.leruu.setFont(font4)
        self.leruu.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leruu.setReadOnly(True)
        self.lbCompID_27 = QLabel(self.tabSteelSections)
        self.lbCompID_27.setObjectName(u"lbCompID_27")
        self.lbCompID_27.setGeometry(QRect(470, 130, 101, 20))
        self.lbCompID_27.setFont(font)
        self.leIvv = QLineEdit(self.tabSteelSections)
        self.leIvv.setObjectName(u"leIvv")
        self.leIvv.setGeometry(QRect(580, 150, 101, 31))
        self.leIvv.setFont(font4)
        self.leIvv.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leIvv.setReadOnly(True)
        self.lbCompID_28 = QLabel(self.tabSteelSections)
        self.lbCompID_28.setObjectName(u"lbCompID_28")
        self.lbCompID_28.setGeometry(QRect(580, 130, 101, 20))
        self.lbCompID_28.setFont(font)
        self.leZvv = QLineEdit(self.tabSteelSections)
        self.leZvv.setObjectName(u"leZvv")
        self.leZvv.setGeometry(QRect(690, 150, 101, 31))
        self.leZvv.setFont(font4)
        self.leZvv.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leZvv.setReadOnly(True)
        self.lbCompID_29 = QLabel(self.tabSteelSections)
        self.lbCompID_29.setObjectName(u"lbCompID_29")
        self.lbCompID_29.setGeometry(QRect(690, 130, 101, 20))
        self.lbCompID_29.setFont(font)
        self.lervv = QLineEdit(self.tabSteelSections)
        self.lervv.setObjectName(u"lervv")
        self.lervv.setGeometry(QRect(800, 150, 101, 31))
        self.lervv.setFont(font4)
        self.lervv.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lervv.setReadOnly(True)
        self.lbCompID_30 = QLabel(self.tabSteelSections)
        self.lbCompID_30.setObjectName(u"lbCompID_30")
        self.lbCompID_30.setGeometry(QRect(800, 130, 101, 20))
        self.lbCompID_30.setFont(font)
        self.leh_tf = QLineEdit(self.tabSteelSections)
        self.leh_tf.setObjectName(u"leh_tf")
        self.leh_tf.setGeometry(QRect(910, 150, 101, 31))
        self.leh_tf.setFont(font4)
        self.leh_tf.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leh_tf.setReadOnly(True)
        self.lbCompID_31 = QLabel(self.tabSteelSections)
        self.lbCompID_31.setObjectName(u"lbCompID_31")
        self.lbCompID_31.setGeometry(QRect(910, 130, 101, 20))
        self.lbCompID_31.setFont(font)
        self.lehw = QLineEdit(self.tabSteelSections)
        self.lehw.setObjectName(u"lehw")
        self.lehw.setGeometry(QRect(1020, 150, 101, 31))
        self.lehw.setFont(font4)
        self.lehw.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lehw.setReadOnly(True)
        self.lbCompID_32 = QLabel(self.tabSteelSections)
        self.lbCompID_32.setObjectName(u"lbCompID_32")
        self.lbCompID_32.setGeometry(QRect(1020, 130, 101, 20))
        self.lbCompID_32.setFont(font)
        self.lbCompID_33 = QLabel(self.tabSteelSections)
        self.lbCompID_33.setObjectName(u"lbCompID_33")
        self.lbCompID_33.setGeometry(QRect(30, 190, 101, 20))
        self.lbCompID_33.setFont(font)
        self.leac = QLineEdit(self.tabSteelSections)
        self.leac.setObjectName(u"leac")
        self.leac.setGeometry(QRect(30, 210, 101, 31))
        self.leac.setFont(font4)
        self.leac.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leac.setReadOnly(True)
        self.lbCompID_34 = QLabel(self.tabSteelSections)
        self.lbCompID_34.setObjectName(u"lbCompID_34")
        self.lbCompID_34.setGeometry(QRect(140, 190, 101, 20))
        self.lbCompID_34.setFont(font)
        self.leax = QLineEdit(self.tabSteelSections)
        self.leax.setObjectName(u"leax")
        self.leax.setGeometry(QRect(140, 210, 101, 31))
        self.leax.setFont(font4)
        self.leax.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leax.setReadOnly(True)
        self.lbCompID_35 = QLabel(self.tabSteelSections)
        self.lbCompID_35.setObjectName(u"lbCompID_35")
        self.lbCompID_35.setGeometry(QRect(250, 190, 101, 20))
        self.lbCompID_35.setFont(font)
        self.leay = QLineEdit(self.tabSteelSections)
        self.leay.setObjectName(u"leay")
        self.leay.setGeometry(QRect(250, 210, 101, 31))
        self.leay.setFont(font4)
        self.leay.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leay.setReadOnly(True)
        self.lbCompID_36 = QLabel(self.tabSteelSections)
        self.lbCompID_36.setObjectName(u"lbCompID_36")
        self.lbCompID_36.setGeometry(QRect(1130, 130, 21, 20))
        font6 = QFont()
        font6.setFamily(u"GreekC")
        font6.setPointSize(9)
        self.lbCompID_36.setFont(font6)
        self.lealpha = QLineEdit(self.tabSteelSections)
        self.lealpha.setObjectName(u"lealpha")
        self.lealpha.setGeometry(QRect(1130, 150, 101, 31))
        font7 = QFont()
        font7.setFamily(u"GreekC")
        font7.setPointSize(10)
        self.lealpha.setFont(font7)
        self.lealpha.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lealpha.setReadOnly(True)
        self.lbCompID_37 = QLabel(self.tabSteelSections)
        self.lbCompID_37.setObjectName(u"lbCompID_37")
        self.lbCompID_37.setGeometry(QRect(1150, 130, 41, 20))
        self.lbCompID_37.setFont(font)
        self.lbCompID_38 = QLabel(self.tabSteelSections)
        self.lbCompID_38.setObjectName(u"lbCompID_38")
        self.lbCompID_38.setGeometry(QRect(160, 70, 41, 20))
        self.lbCompID_38.setFont(font)
        self.lbCompID_39 = QLabel(self.tabSteelSections)
        self.lbCompID_39.setObjectName(u"lbCompID_39")
        self.lbCompID_39.setGeometry(QRect(140, 70, 21, 20))
        font8 = QFont()
        font8.setFamily(u"GreekC")
        font8.setPointSize(9)
        font8.setItalic(True)
        self.lbCompID_39.setFont(font8)
        self.lbQuotationHistory_5 = QLabel(self.tabSteelSections)
        self.lbQuotationHistory_5.setObjectName(u"lbQuotationHistory_5")
        self.lbQuotationHistory_5.setGeometry(QRect(20, 260, 181, 16))
        self.lbQuotationHistory_5.setFont(font5)
        self.btnImportSteel = QPushButton(self.tabSteelSections)
        self.btnImportSteel.setObjectName(u"btnImportSteel")
        self.btnImportSteel.setGeometry(QRect(1150, 220, 75, 31))
        self.btnImportSteel.setStyleSheet(u"   QPushButton {\n"
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
        self.btnUpload = QPushButton(self.tabSteelSections)
        self.btnUpload.setObjectName(u"btnUpload")
        self.btnUpload.setGeometry(QRect(1060, 220, 75, 31))
        self.btnUpload.setStyleSheet(u"    QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(255, 255, 0));\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.leProfile = QLineEdit(self.tabSteelSections)
        self.leProfile.setObjectName(u"leProfile")
        self.leProfile.setGeometry(QRect(30, 30, 61, 31))
        self.leProfile.setFont(font4)
        self.leProfile.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leProfile.setReadOnly(True)
        self.leDesignation = QLineEdit(self.tabSteelSections)
        self.leDesignation.setObjectName(u"leDesignation")
        self.leDesignation.setGeometry(QRect(110, 30, 131, 31))
        self.leDesignation.setFont(font4)
        self.leDesignation.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leDesignation.setReadOnly(True)
        self.tabTechData.addTab(self.tabSteelSections, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.lbQuotationHistory_6 = QLabel(self.tab_6)
        self.lbQuotationHistory_6.setObjectName(u"lbQuotationHistory_6")
        self.lbQuotationHistory_6.setGeometry(QRect(20, 260, 181, 16))
        self.lbQuotationHistory_6.setFont(font5)
        self.tvSANSFlangeTable = QTableView(self.tab_6)
        self.tvSANSFlangeTable.setObjectName(u"tvSANSFlangeTable")
        self.tvSANSFlangeTable.setGeometry(QRect(10, 280, 1221, 461))
        self.leDesignationFlange = QLineEdit(self.tab_6)
        self.leDesignationFlange.setObjectName(u"leDesignationFlange")
        self.leDesignationFlange.setGeometry(QRect(10, 60, 131, 31))
        self.leDesignationFlange.setFont(font4)
        self.leDesignationFlange.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leDesignationFlange.setReadOnly(True)
        self.lbCompany_5 = QLabel(self.tab_6)
        self.lbCompany_5.setObjectName(u"lbCompany_5")
        self.lbCompany_5.setGeometry(QRect(10, 10, 121, 20))
        self.lbCompany_5.setFont(font)
        self.leUnitNB = QLineEdit(self.tab_6)
        self.leUnitNB.setObjectName(u"leUnitNB")
        self.leUnitNB.setGeometry(QRect(150, 60, 101, 31))
        self.leUnitNB.setFont(font4)
        self.leUnitNB.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leUnitNB.setReadOnly(True)
        self.lbCompID_13 = QLabel(self.tab_6)
        self.lbCompID_13.setObjectName(u"lbCompID_13")
        self.lbCompID_13.setGeometry(QRect(150, 10, 101, 20))
        self.lbCompID_13.setFont(font)
        self.leUnitPR = QLineEdit(self.tab_6)
        self.leUnitPR.setObjectName(u"leUnitPR")
        self.leUnitPR.setGeometry(QRect(260, 60, 101, 31))
        self.leUnitPR.setFont(font4)
        self.leUnitPR.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leUnitPR.setReadOnly(True)
        self.lbCompID_14 = QLabel(self.tab_6)
        self.lbCompID_14.setObjectName(u"lbCompID_14")
        self.lbCompID_14.setGeometry(QRect(260, 10, 101, 20))
        self.lbCompID_14.setFont(font)
        self.leUnitType = QLineEdit(self.tab_6)
        self.leUnitType.setObjectName(u"leUnitType")
        self.leUnitType.setGeometry(QRect(370, 60, 101, 31))
        self.leUnitType.setFont(font4)
        self.leUnitType.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leUnitType.setReadOnly(True)
        self.lbCompID_40 = QLabel(self.tab_6)
        self.lbCompID_40.setObjectName(u"lbCompID_40")
        self.lbCompID_40.setGeometry(QRect(370, 10, 101, 20))
        self.lbCompID_40.setFont(font)
        self.lePOD = QLineEdit(self.tab_6)
        self.lePOD.setObjectName(u"lePOD")
        self.lePOD.setGeometry(QRect(540, 60, 101, 31))
        self.lePOD.setFont(font4)
        self.lePOD.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lePOD.setReadOnly(True)
        self.lbCompID_41 = QLabel(self.tab_6)
        self.lbCompID_41.setObjectName(u"lbCompID_41")
        self.lbCompID_41.setGeometry(QRect(540, 10, 111, 20))
        self.lbCompID_41.setFont(font)
        self.leFOD = QLineEdit(self.tab_6)
        self.leFOD.setObjectName(u"leFOD")
        self.leFOD.setGeometry(QRect(650, 60, 101, 31))
        self.leFOD.setFont(font4)
        self.leFOD.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leFOD.setReadOnly(True)
        self.lbCompID_42 = QLabel(self.tab_6)
        self.lbCompID_42.setObjectName(u"lbCompID_42")
        self.lbCompID_42.setGeometry(QRect(650, 10, 111, 20))
        self.lbCompID_42.setFont(font)
        self.lbCompID_43 = QLabel(self.tab_6)
        self.lbCompID_43.setObjectName(u"lbCompID_43")
        self.lbCompID_43.setGeometry(QRect(540, 30, 111, 20))
        self.lbCompID_43.setFont(font)
        self.lbCompID_44 = QLabel(self.tab_6)
        self.lbCompID_44.setObjectName(u"lbCompID_44")
        self.lbCompID_44.setGeometry(QRect(650, 30, 101, 20))
        self.lbCompID_44.setFont(font)
        self.lbCompID_45 = QLabel(self.tab_6)
        self.lbCompID_45.setObjectName(u"lbCompID_45")
        self.lbCompID_45.setGeometry(QRect(760, 30, 61, 20))
        self.lbCompID_45.setFont(font)
        self.leFTK = QLineEdit(self.tab_6)
        self.leFTK.setObjectName(u"leFTK")
        self.leFTK.setGeometry(QRect(760, 60, 101, 31))
        self.leFTK.setFont(font4)
        self.leFTK.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leFTK.setReadOnly(True)
        self.lbCompID_46 = QLabel(self.tab_6)
        self.lbCompID_46.setObjectName(u"lbCompID_46")
        self.lbCompID_46.setGeometry(QRect(760, 10, 111, 20))
        self.lbCompID_46.setFont(font)
        self.lbCompID_47 = QLabel(self.tab_6)
        self.lbCompID_47.setObjectName(u"lbCompID_47")
        self.lbCompID_47.setGeometry(QRect(930, 30, 101, 20))
        self.lbCompID_47.setFont(font)
        self.leRFD = QLineEdit(self.tab_6)
        self.leRFD.setObjectName(u"leRFD")
        self.leRFD.setGeometry(QRect(930, 60, 101, 31))
        self.leRFD.setFont(font4)
        self.leRFD.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leRFD.setReadOnly(True)
        self.lbCompID_48 = QLabel(self.tab_6)
        self.lbCompID_48.setObjectName(u"lbCompID_48")
        self.lbCompID_48.setGeometry(QRect(930, 10, 111, 20))
        self.lbCompID_48.setFont(font)
        self.lbCompID_49 = QLabel(self.tab_6)
        self.lbCompID_49.setObjectName(u"lbCompID_49")
        self.lbCompID_49.setGeometry(QRect(1040, 30, 101, 20))
        self.lbCompID_49.setFont(font)
        self.leRFT = QLineEdit(self.tab_6)
        self.leRFT.setObjectName(u"leRFT")
        self.leRFT.setGeometry(QRect(1040, 60, 101, 31))
        self.leRFT.setFont(font4)
        self.leRFT.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leRFT.setReadOnly(True)
        self.lbCompID_50 = QLabel(self.tab_6)
        self.lbCompID_50.setObjectName(u"lbCompID_50")
        self.lbCompID_50.setGeometry(QRect(1040, 10, 111, 20))
        self.lbCompID_50.setFont(font)
        self.label_3 = QLabel(self.tab_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 341, 141))
        self.label_3.setPixmap(QPixmap(u"../resources/assets/SANS1123_plate_Flange.jpg"))
        self.label_3.setScaledContents(True)
        self.leFBOLT = QLineEdit(self.tab_6)
        self.leFBOLT.setObjectName(u"leFBOLT")
        self.leFBOLT.setGeometry(QRect(540, 170, 101, 31))
        self.leFBOLT.setFont(font4)
        self.leFBOLT.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leFBOLT.setReadOnly(True)
        self.lbCompID_51 = QLabel(self.tab_6)
        self.lbCompID_51.setObjectName(u"lbCompID_51")
        self.lbCompID_51.setGeometry(QRect(540, 120, 111, 20))
        self.lbCompID_51.setFont(font)
        self.lbCompID_52 = QLabel(self.tab_6)
        self.lbCompID_52.setObjectName(u"lbCompID_52")
        self.lbCompID_52.setGeometry(QRect(540, 140, 101, 20))
        self.lbCompID_52.setFont(font)
        self.leNOB = QLineEdit(self.tab_6)
        self.leNOB.setObjectName(u"leNOB")
        self.leNOB.setGeometry(QRect(650, 170, 101, 31))
        self.leNOB.setFont(font4)
        self.leNOB.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leNOB.setReadOnly(True)
        self.lbCompID_53 = QLabel(self.tab_6)
        self.lbCompID_53.setObjectName(u"lbCompID_53")
        self.lbCompID_53.setGeometry(QRect(650, 120, 111, 20))
        self.lbCompID_53.setFont(font)
        self.lbCompID_54 = QLabel(self.tab_6)
        self.lbCompID_54.setObjectName(u"lbCompID_54")
        self.lbCompID_54.setGeometry(QRect(650, 140, 101, 20))
        self.lbCompID_54.setFont(font)
        self.leBOS = QLineEdit(self.tab_6)
        self.leBOS.setObjectName(u"leBOS")
        self.leBOS.setGeometry(QRect(760, 170, 101, 31))
        self.leBOS.setFont(font4)
        self.leBOS.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leBOS.setReadOnly(True)
        self.lbCompID_55 = QLabel(self.tab_6)
        self.lbCompID_55.setObjectName(u"lbCompID_55")
        self.lbCompID_55.setGeometry(QRect(760, 120, 111, 20))
        self.lbCompID_55.setFont(font)
        self.lbCompID_56 = QLabel(self.tab_6)
        self.lbCompID_56.setObjectName(u"lbCompID_56")
        self.lbCompID_56.setGeometry(QRect(760, 140, 101, 20))
        self.lbCompID_56.setFont(font)
        self.lePCD = QLineEdit(self.tab_6)
        self.lePCD.setObjectName(u"lePCD")
        self.lePCD.setGeometry(QRect(870, 170, 101, 31))
        self.lePCD.setFont(font4)
        self.lePCD.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.lePCD.setReadOnly(True)
        self.lbCompID_57 = QLabel(self.tab_6)
        self.lbCompID_57.setObjectName(u"lbCompID_57")
        self.lbCompID_57.setGeometry(QRect(870, 120, 111, 20))
        self.lbCompID_57.setFont(font)
        self.lbCompID_58 = QLabel(self.tab_6)
        self.lbCompID_58.setObjectName(u"lbCompID_58")
        self.lbCompID_58.setGeometry(QRect(870, 140, 101, 20))
        self.lbCompID_58.setFont(font)
        self.btnImportFlanges = QPushButton(self.tab_6)
        self.btnImportFlanges.setObjectName(u"btnImportFlanges")
        self.btnImportFlanges.setGeometry(QRect(1150, 220, 75, 31))
        self.btnImportFlanges.setStyleSheet(u"   QPushButton {\n"
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
        self.btnUpload_2 = QPushButton(self.tab_6)
        self.btnUpload_2.setObjectName(u"btnUpload_2")
        self.btnUpload_2.setGeometry(QRect(1060, 220, 75, 31))
        self.btnUpload_2.setStyleSheet(u"    QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(255, 255, 0));\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.lbCompID_59 = QLabel(self.tab_6)
        self.lbCompID_59.setObjectName(u"lbCompID_59")
        self.lbCompID_59.setGeometry(QRect(1030, 140, 101, 20))
        self.lbCompID_59.setFont(font)
        self.lbCompID_60 = QLabel(self.tab_6)
        self.lbCompID_60.setObjectName(u"lbCompID_60")
        self.lbCompID_60.setGeometry(QRect(1030, 120, 111, 20))
        self.lbCompID_60.setFont(font)
        self.leFlangeMass = QLineEdit(self.tab_6)
        self.leFlangeMass.setObjectName(u"leFlangeMass")
        self.leFlangeMass.setGeometry(QRect(1030, 170, 101, 31))
        self.leFlangeMass.setFont(font4)
        self.leFlangeMass.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leFlangeMass.setReadOnly(True)
        self.tabTechData.addTab(self.tab_6, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabTechData.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.tabTechData.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.lbCompany_6 = QLabel(self.tab_12)
        self.lbCompany_6.setObjectName(u"lbCompany_6")
        self.lbCompany_6.setGeometry(QRect(10, 10, 121, 20))
        self.lbCompany_6.setFont(font)
        self.leDesignationFlange_2 = QLineEdit(self.tab_12)
        self.leDesignationFlange_2.setObjectName(u"leDesignationFlange_2")
        self.leDesignationFlange_2.setGeometry(QRect(10, 60, 131, 31))
        self.leDesignationFlange_2.setFont(font4)
        self.leDesignationFlange_2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leDesignationFlange_2.setReadOnly(True)
        self.leUnitNB_2 = QLineEdit(self.tab_12)
        self.leUnitNB_2.setObjectName(u"leUnitNB_2")
        self.leUnitNB_2.setGeometry(QRect(150, 60, 101, 31))
        self.leUnitNB_2.setFont(font4)
        self.leUnitNB_2.setStyleSheet(u"QLineEdit {\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
"}")
        self.leUnitNB_2.setReadOnly(True)
        self.lbCompID_61 = QLabel(self.tab_12)
        self.lbCompID_61.setObjectName(u"lbCompID_61")
        self.lbCompID_61.setGeometry(QRect(150, 10, 101, 20))
        self.lbCompID_61.setFont(font)
        self.btnImportFlanges_2 = QPushButton(self.tab_12)
        self.btnImportFlanges_2.setObjectName(u"btnImportFlanges_2")
        self.btnImportFlanges_2.setGeometry(QRect(1150, 220, 75, 31))
        self.btnImportFlanges_2.setStyleSheet(u"   QPushButton {\n"
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
        self.tvSANSFlangeTable_2 = QTableView(self.tab_12)
        self.tvSANSFlangeTable_2.setObjectName(u"tvSANSFlangeTable_2")
        self.tvSANSFlangeTable_2.setGeometry(QRect(10, 280, 1221, 461))
        self.btnUpload_3 = QPushButton(self.tab_12)
        self.btnUpload_3.setObjectName(u"btnUpload_3")
        self.btnUpload_3.setGeometry(QRect(1060, 220, 75, 31))
        self.btnUpload_3.setStyleSheet(u"    QPushButton {\n"
"         border: 1px solid gray;\n"
"         border-radius: 10px;\n"
"		 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #f6f7fa, stop: 1 rgb(255, 255, 0));\n"
"	\n"
"	\n"
"     }\n"
"\n"
" QPushButton:pressed {\n"
"         background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                           stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"     }")
        self.lbQuotationHistory_7 = QLabel(self.tab_12)
        self.lbQuotationHistory_7.setObjectName(u"lbQuotationHistory_7")
        self.lbQuotationHistory_7.setGeometry(QRect(10, 260, 181, 16))
        self.lbQuotationHistory_7.setFont(font5)
        self.label_4 = QLabel(self.tab_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 110, 341, 141))
        self.label_4.setPixmap(QPixmap(u"../resources/assets/SANS1123_plate_Flange.jpg"))
        self.label_4.setScaledContents(True)
        self.tabTechData.addTab(self.tab_12, "")
        self.stwMain.addWidget(self.techData)
        self.calculations = QWidget()
        self.calculations.setObjectName(u"calculations")
        self.label_15 = QLabel(self.calculations)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(410, 20, 421, 31))
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.stwMain.addWidget(self.calculations)
        ControlPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlPanel)

        self.stwMain.setCurrentIndex(8)
        self.tabQuotation.setCurrentIndex(6)
        self.tabWidget_2.setCurrentIndex(4)
        self.tabQuotation_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)
        self.tabDoccontrol.setCurrentIndex(0)
        self.tabTechData.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(ControlPanel)
    # setupUi

    def retranslateUi(self, ControlPanel):
        ControlPanel.setWindowTitle(QCoreApplication.translate("ControlPanel", u"Business Management", None))
        self.lbDashborad.setText(QCoreApplication.translate("ControlPanel", u"Dashboard", None))
        self.lbCustomer.setText(QCoreApplication.translate("ControlPanel", u"Customers", None))
        self.lbQuotation.setText(QCoreApplication.translate("ControlPanel", u"Quotations", None))
        self.lbContacts.setText(QCoreApplication.translate("ControlPanel", u"Contacts", None))
#if QT_CONFIG(tooltip)
        self.btnContacts.setToolTip(QCoreApplication.translate("ControlPanel", u"Go to Customer Database", None))
#endif // QT_CONFIG(tooltip)
        self.btnContacts.setText("")
#if QT_CONFIG(tooltip)
        self.btnDashboard.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnDashboard.setText("")
#if QT_CONFIG(tooltip)
        self.btnCustomer.setToolTip(QCoreApplication.translate("ControlPanel", u"Go to Customer Database", None))
#endif // QT_CONFIG(tooltip)
        self.btnCustomer.setText("")
#if QT_CONFIG(tooltip)
        self.btnQuotation.setToolTip(QCoreApplication.translate("ControlPanel", u"Generate and View Quotation", None))
#endif // QT_CONFIG(tooltip)
        self.btnQuotation.setText("")
        self.lbGeneralInfo.setText(QCoreApplication.translate("ControlPanel", u"General Technical Data", None))
        self.lbCalculations.setText(QCoreApplication.translate("ControlPanel", u"Calculations", None))
#if QT_CONFIG(tooltip)
        self.btnGeneralInfo.setToolTip(QCoreApplication.translate("ControlPanel", u"General Information Database", None))
#endif // QT_CONFIG(tooltip)
        self.btnGeneralInfo.setText("")
#if QT_CONFIG(tooltip)
        self.btnCalculation.setToolTip(QCoreApplication.translate("ControlPanel", u"Calculation Programs", None))
#endif // QT_CONFIG(tooltip)
        self.btnCalculation.setText("")
        self.lbProcurement.setText(QCoreApplication.translate("ControlPanel", u"Procurement", None))
        self.lbAnalysis.setText(QCoreApplication.translate("ControlPanel", u"Analysis and Reports", None))
#if QT_CONFIG(tooltip)
        self.btnProcurement.setToolTip(QCoreApplication.translate("ControlPanel", u"General Information Database", None))
#endif // QT_CONFIG(tooltip)
        self.btnProcurement.setText("")
#if QT_CONFIG(tooltip)
        self.btnAnalysis.setToolTip(QCoreApplication.translate("ControlPanel", u"General Information Database", None))
#endif // QT_CONFIG(tooltip)
        self.btnAnalysis.setText("")
        self.lbDocControl.setText(QCoreApplication.translate("ControlPanel", u"Document Control", None))
#if QT_CONFIG(tooltip)
        self.btnDocControl.setToolTip(QCoreApplication.translate("ControlPanel", u"General Information Database", None))
#endif // QT_CONFIG(tooltip)
        self.btnDocControl.setText("")
        self.lbWorksorder.setText(QCoreApplication.translate("ControlPanel", u"Worksorders", None))
        self.lbResources.setText(QCoreApplication.translate("ControlPanel", u"Resources", None))
        self.lbTimesheets.setText(QCoreApplication.translate("ControlPanel", u"Timesheets", None))
        self.lnInvoices.setText(QCoreApplication.translate("ControlPanel", u"Invoices and Payments", None))
#if QT_CONFIG(tooltip)
        self.btnInvoices.setToolTip(QCoreApplication.translate("ControlPanel", u"Invoice and Payments", None))
#endif // QT_CONFIG(tooltip)
        self.btnInvoices.setText("")
#if QT_CONFIG(tooltip)
        self.btnWorksorder.setToolTip(QCoreApplication.translate("ControlPanel", u"Go to WorksOrders Menu", None))
#endif // QT_CONFIG(tooltip)
        self.btnWorksorder.setText("")
#if QT_CONFIG(tooltip)
        self.btnTimesheets.setToolTip(QCoreApplication.translate("ControlPanel", u"Eneter Daily Timesheets", None))
#endif // QT_CONFIG(tooltip)
        self.btnTimesheets.setText("")
#if QT_CONFIG(tooltip)
        self.btnResources.setToolTip(QCoreApplication.translate("ControlPanel", u"Overall Resource Schedule", None))
#endif // QT_CONFIG(tooltip)
        self.btnResources.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("ControlPanel", u"Current Open Worksorder", None))
        self.lbWONum.setText("")
#if QT_CONFIG(tooltip)
        self.btnUploadWO.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnUploadWO.setText("")
        self.label_14.setText(QCoreApplication.translate("ControlPanel", u"DASHBOARD", None))
        self.lbActionList.setText(QCoreApplication.translate("ControlPanel", u"ACTION ITEMS", None))
        self.lbOpenOrders.setText(QCoreApplication.translate("ControlPanel", u"OPEN ORDERS", None))
        self.lbCustomerPage.setText(QCoreApplication.translate("ControlPanel", u"CUSTOMER MANAGEMENT SYSTEM", None))
        self.lbCustomers.setText(QCoreApplication.translate("ControlPanel", u"CUSTOMERS", None))
#if QT_CONFIG(tooltip)
        self.searchBtn.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.searchBtn.setText("")
        self.btnEdit.setText(QCoreApplication.translate("ControlPanel", u"Edit", None))
        self.btnDelete_2.setText(QCoreApplication.translate("ControlPanel", u"Delete", None))
        self.btnNew.setText(QCoreApplication.translate("ControlPanel", u"Add", None))
        self.btnClear.setText(QCoreApplication.translate("ControlPanel", u"Clear", None))
        self.lbCompID.setText(QCoreApplication.translate("ControlPanel", u"Company ID", None))
        self.lbCompanyName.setText(QCoreApplication.translate("ControlPanel", u"Company Name", None))
        self.lbCompStatus.setText(QCoreApplication.translate("ControlPanel", u"Company Status", None))
        self.cboxCustomer.setText(QCoreApplication.translate("ControlPanel", u"Customer", None))
        self.cboxSupplier.setText(QCoreApplication.translate("ControlPanel", u"Supplier", None))
        self.lbRegistrationNumber.setText(QCoreApplication.translate("ControlPanel", u"Registration Number", None))
        self.leRegistrationNumber.setText("")
        self.lbVATNumber.setText(QCoreApplication.translate("ControlPanel", u"VAT Number", None))
        self.leVATNumber.setText("")
        self.lbWebsite.setText(QCoreApplication.translate("ControlPanel", u"Website Address", None))
        self.leWebsite.setText("")
        self.leAddress1.setText("")
        self.lbAddress1.setText(QCoreApplication.translate("ControlPanel", u"Address Part 1", None))
        self.leAddress2.setText("")
        self.lbAddress2.setText(QCoreApplication.translate("ControlPanel", u"Address Part 2", None))
        self.leCity.setText("")
        self.lbCity.setText(QCoreApplication.translate("ControlPanel", u"City", None))
        self.lePostalCode.setText("")
        self.lbPostalCode.setText(QCoreApplication.translate("ControlPanel", u"Postal Code", None))
        self.leProvince.setText("")
        self.lbProvince.setText(QCoreApplication.translate("ControlPanel", u"Province / Region / State", None))
        self.lbCountry.setText(QCoreApplication.translate("ControlPanel", u"Country", None))
        self.lbBusinessPhone.setText(QCoreApplication.translate("ControlPanel", u"Business Phone", None))
        self.leBusinessPhone.setText("")
        self.lbCompanyEmail.setText(QCoreApplication.translate("ControlPanel", u"Company Email", None))
        self.leCompanyEmail.setText("")
        self.label_19.setText(QCoreApplication.translate("ControlPanel", u"CONTACT DETAILS", None))
        self.lbContacts_2.setText(QCoreApplication.translate("ControlPanel", u"CONTACTS", None))
#if QT_CONFIG(tooltip)
        self.searchBtn_2.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.searchBtn_2.setText("")
        self.btnEdit_2.setText(QCoreApplication.translate("ControlPanel", u"Edit", None))
        self.btnDelete.setText(QCoreApplication.translate("ControlPanel", u"Delete", None))
        self.btnNew_2.setText(QCoreApplication.translate("ControlPanel", u"Add", None))
        self.btnClear_2.setText(QCoreApplication.translate("ControlPanel", u"Clear", None))
        self.lbFirstName.setText(QCoreApplication.translate("ControlPanel", u"First Name", None))
        self.lbEmail.setText(QCoreApplication.translate("ControlPanel", u"Email", None))
        self.leEmail.setText("")
        self.lePosition.setText("")
        self.lbPosition.setText(QCoreApplication.translate("ControlPanel", u"Position", None))
        self.leBusPhone.setText("")
        self.lbBusPhone.setText(QCoreApplication.translate("ControlPanel", u"Business Phone", None))
        self.leMobile.setText("")
        self.lbMobile.setText(QCoreApplication.translate("ControlPanel", u"Mobile", None))
        self.lbDOB.setText(QCoreApplication.translate("ControlPanel", u"Date of Birth", None))
        self.lbLastName.setText(QCoreApplication.translate("ControlPanel", u"Last Name", None))
        self.lbCompany.setText(QCoreApplication.translate("ControlPanel", u"Company", None))
        self.label_16.setText(QCoreApplication.translate("ControlPanel", u"QUOTATIONS AND TENDERS", None))
        self.tabQuotation.setTabText(self.tabQuotation.indexOf(self.register_quote), QCoreApplication.translate("ControlPanel", u"Register Quote", None))
        self.tabQuotation.setTabText(self.tabQuotation.indexOf(self.scope_included), QCoreApplication.translate("ControlPanel", u"Scope Included", None))
        self.tabQuotation.setTabText(self.tabQuotation.indexOf(self.scope_excluded), QCoreApplication.translate("ControlPanel", u"Scope Excluded", None))
        self.tabQuotation.setTabText(self.tabQuotation.indexOf(self.design_estimate), QCoreApplication.translate("ControlPanel", u"Design Estimate", None))
        self.tabQuotation.setTabText(self.tabQuotation.indexOf(self.supply_estimate), QCoreApplication.translate("ControlPanel", u"Supply Estimate", None))
        self.tabQuotation.setTabText(self.tabQuotation.indexOf(self.service_estimate), QCoreApplication.translate("ControlPanel", u"Service Estimate", None))
        self.tabQuotation.setTabText(self.tabQuotation.indexOf(self.tab_3), QCoreApplication.translate("ControlPanel", u"Generate Quotation Document", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.all_quotations), QCoreApplication.translate("ControlPanel", u"All Quotations", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.open_quotations), QCoreApplication.translate("ControlPanel", u"Open Quotations", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.accepted_quotations), QCoreApplication.translate("ControlPanel", u"Accepted Quotations", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.cancelled_quotations), QCoreApplication.translate("ControlPanel", u"Cancelled Quotations", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.postponed_quotations), QCoreApplication.translate("ControlPanel", u"Postponed Quotations", None))
        self.lbQuotationHistory.setText(QCoreApplication.translate("ControlPanel", u"Quotation History", None))
        self.lbQuotationHistory_2.setText(QCoreApplication.translate("ControlPanel", u"Quotation Detail", None))
        self.label_17.setText(QCoreApplication.translate("ControlPanel", u"WORKSORDERS", None))
        self.tabQuotation_2.setTabText(self.tabQuotation_2.indexOf(self.register_quote_2), QCoreApplication.translate("ControlPanel", u"Register Quote", None))
        self.tabQuotation_2.setTabText(self.tabQuotation_2.indexOf(self.scope_included_2), QCoreApplication.translate("ControlPanel", u"Scope Included", None))
        self.tabQuotation_2.setTabText(self.tabQuotation_2.indexOf(self.scope_excluded_2), QCoreApplication.translate("ControlPanel", u"Scope Excluded", None))
        self.tabQuotation_2.setTabText(self.tabQuotation_2.indexOf(self.design_estimate_2), QCoreApplication.translate("ControlPanel", u"Design Estimate", None))
        self.tabQuotation_2.setTabText(self.tabQuotation_2.indexOf(self.supply_estimate_2), QCoreApplication.translate("ControlPanel", u"Supply Estimate", None))
        self.tabQuotation_2.setTabText(self.tabQuotation_2.indexOf(self.service_estimate_2), QCoreApplication.translate("ControlPanel", u"Service Estimate", None))
        self.tabQuotation_2.setTabText(self.tabQuotation_2.indexOf(self.tab_4), QCoreApplication.translate("ControlPanel", u"Generate Quotation Document", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.all_quotations_2), QCoreApplication.translate("ControlPanel", u"All Quotations", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.open_quotations_2), QCoreApplication.translate("ControlPanel", u"Open Quotations", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.accepted_quotations_2), QCoreApplication.translate("ControlPanel", u"Accepted Quotations", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.cancelled_quotations_2), QCoreApplication.translate("ControlPanel", u"Cancelled Quotations", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.postponed_quotations_2), QCoreApplication.translate("ControlPanel", u"Postponed Quotations", None))
        self.lbQuotationHistory_3.setText(QCoreApplication.translate("ControlPanel", u"Worksorder Detail", None))
        self.lbQuotationHistory_4.setText(QCoreApplication.translate("ControlPanel", u"Worksorder Detail", None))
        self.label_18.setText(QCoreApplication.translate("ControlPanel", u"RESOURCES", None))
        self.btnNew_3.setText(QCoreApplication.translate("ControlPanel", u"Add", None))
        self.btnClear_3.setText(QCoreApplication.translate("ControlPanel", u"Clear", None))
        self.lbFirstName_2.setText(QCoreApplication.translate("ControlPanel", u"First Name", None))
        self.lbEmail_2.setText(QCoreApplication.translate("ControlPanel", u"Email", None))
        self.leEmail_2.setText("")
        self.leBusPhone_2.setText("")
        self.lbBusPhone_2.setText(QCoreApplication.translate("ControlPanel", u"Business Phone", None))
        self.leMobile_2.setText("")
        self.lbMobile_2.setText(QCoreApplication.translate("ControlPanel", u"Mobile", None))
        self.lbDOB_2.setText(QCoreApplication.translate("ControlPanel", u"Date of Birth", None))
        self.lbLastName_2.setText(QCoreApplication.translate("ControlPanel", u"Last Name", None))
        self.lbCompany_2.setText(QCoreApplication.translate("ControlPanel", u"Company", None))
        self.lbPosition_2.setText(QCoreApplication.translate("ControlPanel", u"Position", None))
        self.lbContacts_3.setText(QCoreApplication.translate("ControlPanel", u"RESOURCES", None))
#if QT_CONFIG(tooltip)
        self.searchBtn_3.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.searchBtn_3.setText("")
        self.btnEdit_3.setText(QCoreApplication.translate("ControlPanel", u"Edit", None))
        self.btnDelete_3.setText(QCoreApplication.translate("ControlPanel", u"Delete", None))
        self.label_20.setText(QCoreApplication.translate("ControlPanel", u"TIMESHEETS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ControlPanel", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ControlPanel", u"Tab 2", None))
        self.label_21.setText(QCoreApplication.translate("ControlPanel", u"COMPLETION DOCUMENTS AND INVOICING", None))
        self.label_22.setText(QCoreApplication.translate("ControlPanel", u"DOCUMENT CONTROL", None))
        self.lbDashborad_2.setText(QCoreApplication.translate("ControlPanel", u"Design Basis", None))
#if QT_CONFIG(tooltip)
        self.btnDesignBasis.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnDesignBasis.setText("")
#if QT_CONFIG(tooltip)
        self.btnProcessDescrip.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnProcessDescrip.setText("")
        self.lbDashborad_3.setText(QCoreApplication.translate("ControlPanel", u"Process Description", None))
#if QT_CONFIG(tooltip)
        self.btnSiteConditions.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnSiteConditions.setText("")
        self.lbDashborad_4.setText(QCoreApplication.translate("ControlPanel", u"Site Conditions", None))
#if QT_CONFIG(tooltip)
        self.btnDesignCriteria.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnDesignCriteria.setText("")
        self.lbDashborad_5.setText(QCoreApplication.translate("ControlPanel", u"Design Criteria", None))
#if QT_CONFIG(tooltip)
        self.btnBuildinList.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnBuildinList.setText("")
        self.lbDashborad_6.setText(QCoreApplication.translate("ControlPanel", u"Building List", None))
#if QT_CONFIG(tooltip)
        self.btnStructureList.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnStructureList.setText("")
        self.lbDashborad_7.setText(QCoreApplication.translate("ControlPanel", u"Structure List", None))
#if QT_CONFIG(tooltip)
        self.btnMEL.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnMEL.setText("")
        self.lbDashborad_8.setText(QCoreApplication.translate("ControlPanel", u"Mechanical Equipment List", None))
        self.lbDashborad_9.setText(QCoreApplication.translate("ControlPanel", u"Electrical Equipment List", None))
#if QT_CONFIG(tooltip)
        self.btnEEL.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnEEL.setText("")
#if QT_CONFIG(tooltip)
        self.btnIEL.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnIEL.setText("")
        self.lbDashborad_10.setText(QCoreApplication.translate("ControlPanel", u"Instrumentation Equipment List", None))
#if QT_CONFIG(tooltip)
        self.btnGenSpec.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnGenSpec.setText("")
        self.lbDashborad_11.setText(QCoreApplication.translate("ControlPanel", u"General Specifications", None))
#if QT_CONFIG(tooltip)
        self.btnBuildSpec.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnBuildSpec.setText("")
        self.lbDashborad_12.setText(QCoreApplication.translate("ControlPanel", u"Specifications", None))
        self.lbDashborad_13.setText(QCoreApplication.translate("ControlPanel", u"Bill of Materials", None))
#if QT_CONFIG(tooltip)
        self.btnBuildBOM.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnBuildBOM.setText("")
#if QT_CONFIG(tooltip)
        self.btnBuildBOE.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnBuildBOE.setText("")
        self.lbDashborad_14.setText(QCoreApplication.translate("ControlPanel", u"Bill of Equipment", None))
        self.lbDashborad_15.setText(QCoreApplication.translate("ControlPanel", u"Conveyor Schedule", None))
        self.lbDashborad_16.setText(QCoreApplication.translate("ControlPanel", u"Equipment Datasheets", None))
#if QT_CONFIG(tooltip)
        self.btnConveyorSchedule.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnConveyorSchedule.setText("")
#if QT_CONFIG(tooltip)
        self.btnMechDataSheet.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnMechDataSheet.setText("")
        self.lbDashborad_17.setText(QCoreApplication.translate("ControlPanel", u"Drawings List", None))
#if QT_CONFIG(tooltip)
        self.btnBuildDrg.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnBuildDrg.setText("")
        self.lbDashborad_18.setText(QCoreApplication.translate("ControlPanel", u"Calculations", None))
#if QT_CONFIG(tooltip)
        self.btnBuildCalc.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnBuildCalc.setText("")
#if QT_CONFIG(tooltip)
        self.btnStrucCalc.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnStrucCalc.setText("")
        self.lbDashborad_19.setText(QCoreApplication.translate("ControlPanel", u"Calculations", None))
        self.lbDashborad_21.setText(QCoreApplication.translate("ControlPanel", u"Specifications", None))
#if QT_CONFIG(tooltip)
        self.btnStrucDrg.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnStrucDrg.setText("")
#if QT_CONFIG(tooltip)
        self.btnStructCalc.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnStructCalc.setText("")
        self.lbDashborad_22.setText(QCoreApplication.translate("ControlPanel", u"Bill of Materials", None))
#if QT_CONFIG(tooltip)
        self.btnStrucSpec.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnStrucSpec.setText("")
        self.lbDashborad_23.setText(QCoreApplication.translate("ControlPanel", u"Drawings List", None))
        self.lbDashborad_20.setText(QCoreApplication.translate("ControlPanel", u"Calculations", None))
#if QT_CONFIG(tooltip)
        self.btnMechSpec.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnMechSpec.setText("")
        self.lbDashborad_24.setText(QCoreApplication.translate("ControlPanel", u"Specifications", None))
#if QT_CONFIG(tooltip)
        self.btnMechCalc.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnMechCalc.setText("")
        self.lbDashborad_25.setText(QCoreApplication.translate("ControlPanel", u"Bill of Materials", None))
        self.lbDashborad_26.setText(QCoreApplication.translate("ControlPanel", u"Drawings List", None))
        self.lbDashborad_27.setText(QCoreApplication.translate("ControlPanel", u"Calculations", None))
#if QT_CONFIG(tooltip)
        self.btnCivlDrg.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnCivlDrg.setText("")
#if QT_CONFIG(tooltip)
        self.btnDCivilsList.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnDCivilsList.setText("")
        self.lbDashborad_28.setText(QCoreApplication.translate("ControlPanel", u"Civils List", None))
#if QT_CONFIG(tooltip)
        self.btnCivilSpec.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnCivilSpec.setText("")
        self.lbDashborad_29.setText(QCoreApplication.translate("ControlPanel", u"Specifications", None))
#if QT_CONFIG(tooltip)
        self.btnCivilBOM.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnCivilBOM.setText("")
#if QT_CONFIG(tooltip)
        self.btnCivilCalc.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnCivilCalc.setText("")
        self.lbDashborad_30.setText(QCoreApplication.translate("ControlPanel", u"Scope of Work", None))
#if QT_CONFIG(tooltip)
        self.btnTenderQuotes.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnTenderQuotes.setText("")
        self.lbDashborad_31.setText(QCoreApplication.translate("ControlPanel", u"Tender and Quotations", None))
#if QT_CONFIG(tooltip)
        self.btnTenderSOW.setToolTip(QCoreApplication.translate("ControlPanel", u"Overview of Actions and Workload", None))
#endif // QT_CONFIG(tooltip)
        self.btnTenderSOW.setText("")
        self.tabDoccontrol.setTabText(self.tabDoccontrol.indexOf(self.tab_5), QCoreApplication.translate("ControlPanel", u"General ", None))
        self.tabDoccontrol.setTabText(self.tabDoccontrol.indexOf(self.tab_7), QCoreApplication.translate("ControlPanel", u"Document Registers", None))
        self.tabDoccontrol.setTabText(self.tabDoccontrol.indexOf(self.tab_8), QCoreApplication.translate("ControlPanel", u"Document History", None))
        self.tabDoccontrol.setTabText(self.tabDoccontrol.indexOf(self.tab_9), QCoreApplication.translate("ControlPanel", u"Document Transmittal", None))
        self.label_23.setText(QCoreApplication.translate("ControlPanel", u"PROCUREMENT", None))
        self.label_24.setText(QCoreApplication.translate("ControlPanel", u"ANALYSIS AND REPORTS", None))
        self.label_25.setText(QCoreApplication.translate("ControlPanel", u"GENERAL TECHINCAL DATA DATABASE", None))
        self.lbCompany_3.setText(QCoreApplication.translate("ControlPanel", u"Steel Profile", None))
        self.lbCompID_2.setText(QCoreApplication.translate("ControlPanel", u"m (kg/m)", None))
        self.lbCompany_4.setText(QCoreApplication.translate("ControlPanel", u"Designation", None))
        self.lbCompID_3.setText(QCoreApplication.translate("ControlPanel", u"h (mm)", None))
        self.lbCompID_4.setText(QCoreApplication.translate("ControlPanel", u"d (mm)", None))
        self.lbCompID_5.setText(QCoreApplication.translate("ControlPanel", u"c (mm)", None))
        self.lbCompID_6.setText(QCoreApplication.translate("ControlPanel", u"b (mm)", None))
        self.lbCompID_7.setText(QCoreApplication.translate("ControlPanel", u"tw (mm)", None))
        self.lbCompID_8.setText(QCoreApplication.translate("ControlPanel", u"tf (mm)", None))
        self.lbCompID_9.setText(QCoreApplication.translate("ControlPanel", u"r1 (mm)", None))
        self.lbCompID_10.setText(QCoreApplication.translate("ControlPanel", u"r2 (mm)", None))
        self.lbCompID_11.setText(QCoreApplication.translate("ControlPanel", u"b1 (mm)", None))
        self.lbCompID_12.setText(QCoreApplication.translate("ControlPanel", u"A  (mm2)", None))
        self.leTaperAngle.setText("")
        self.lbCompID_15.setText(QCoreApplication.translate("ControlPanel", u"Ix  (mm4)", None))
        self.lbCompID_16.setText(QCoreApplication.translate("ControlPanel", u"Zx  (mm3)", None))
        self.lbCompID_17.setText(QCoreApplication.translate("ControlPanel", u"rx  (mm)", None))
        self.lbCompID_18.setText(QCoreApplication.translate("ControlPanel", u"Iy  (mm4)", None))
        self.lbCompID_19.setText(QCoreApplication.translate("ControlPanel", u"Zy  (mm3)", None))
        self.lbCompID_20.setText(QCoreApplication.translate("ControlPanel", u"ry  (mm)", None))
        self.lbCompID_21.setText(QCoreApplication.translate("ControlPanel", u"J  (mm4)", None))
        self.lbCompID_22.setText(QCoreApplication.translate("ControlPanel", u"Cw  (mm6)", None))
        self.lbCompID_23.setText(QCoreApplication.translate("ControlPanel", u"Zplx  (mm3)", None))
        self.lbCompID_24.setText(QCoreApplication.translate("ControlPanel", u"Zply (mm3)", None))
        self.lbCompID_25.setText(QCoreApplication.translate("ControlPanel", u"Iu  (mm4)", None))
        self.lbCompID_26.setText(QCoreApplication.translate("ControlPanel", u"Zu  (mm3)", None))
        self.lbCompID_27.setText(QCoreApplication.translate("ControlPanel", u"ru (mm)", None))
        self.lbCompID_28.setText(QCoreApplication.translate("ControlPanel", u"Iv (mm4))", None))
        self.lbCompID_29.setText(QCoreApplication.translate("ControlPanel", u"Zv  (mm3)", None))
        self.lbCompID_30.setText(QCoreApplication.translate("ControlPanel", u"rv  (mm)", None))
        self.lbCompID_31.setText(QCoreApplication.translate("ControlPanel", u"h/tf", None))
        self.lbCompID_32.setText(QCoreApplication.translate("ControlPanel", u"hw  (mm)", None))
        self.lbCompID_33.setText(QCoreApplication.translate("ControlPanel", u"ac  (mm)", None))
        self.lbCompID_34.setText(QCoreApplication.translate("ControlPanel", u"ax  (mm)", None))
        self.lbCompID_35.setText(QCoreApplication.translate("ControlPanel", u"ay  (mm)", None))
        self.lbCompID_36.setText(QCoreApplication.translate("ControlPanel", u"a", None))
        self.lealpha.setText("")
        self.lbCompID_37.setText(QCoreApplication.translate("ControlPanel", u"deg", None))
        self.lbCompID_38.setText(QCoreApplication.translate("ControlPanel", u"deg", None))
        self.lbCompID_39.setText(QCoreApplication.translate("ControlPanel", u"B", None))
        self.lbQuotationHistory_5.setText(QCoreApplication.translate("ControlPanel", u"Steel Sections Table", None))
        self.btnImportSteel.setText(QCoreApplication.translate("ControlPanel", u"Import", None))
        self.btnUpload.setText(QCoreApplication.translate("ControlPanel", u"Upload Detail", None))
        self.tabTechData.setTabText(self.tabTechData.indexOf(self.tabSteelSections), QCoreApplication.translate("ControlPanel", u"SANS 50025-Steel Sections", None))
        self.lbQuotationHistory_6.setText(QCoreApplication.translate("ControlPanel", u"SANS 1123 Plate Flange Tables", None))
        self.lbCompany_5.setText(QCoreApplication.translate("ControlPanel", u"Designation", None))
        self.lbCompID_13.setText(QCoreApplication.translate("ControlPanel", u"Nominal Bore", None))
        self.lbCompID_14.setText(QCoreApplication.translate("ControlPanel", u"Pressure Rating", None))
        self.lbCompID_40.setText(QCoreApplication.translate("ControlPanel", u"Type", None))
        self.lbCompID_41.setText(QCoreApplication.translate("ControlPanel", u"Pipe Outside Dia.", None))
        self.lbCompID_42.setText(QCoreApplication.translate("ControlPanel", u"Flange Outside Dia.", None))
        self.lbCompID_43.setText(QCoreApplication.translate("ControlPanel", u"d1 (mm)", None))
        self.lbCompID_44.setText(QCoreApplication.translate("ControlPanel", u"D (mm)", None))
        self.lbCompID_45.setText(QCoreApplication.translate("ControlPanel", u"b1 (mm)", None))
        self.lbCompID_46.setText(QCoreApplication.translate("ControlPanel", u"Flange Thickness", None))
        self.lbCompID_47.setText(QCoreApplication.translate("ControlPanel", u"d3 (mm)", None))
        self.lbCompID_48.setText(QCoreApplication.translate("ControlPanel", u"Raised Face Dia.", None))
        self.lbCompID_49.setText(QCoreApplication.translate("ControlPanel", u"f (mm)", None))
        self.lbCompID_50.setText(QCoreApplication.translate("ControlPanel", u"Rasied Face Thick.", None))
        self.label_3.setText("")
        self.lbCompID_51.setText(QCoreApplication.translate("ControlPanel", u"Bolt Size", None))
        self.lbCompID_52.setText("")
        self.lbCompID_53.setText(QCoreApplication.translate("ControlPanel", u"Number of Bolts", None))
        self.lbCompID_54.setText("")
        self.lbCompID_55.setText(QCoreApplication.translate("ControlPanel", u"Bolt Holes Size", None))
        self.lbCompID_56.setText(QCoreApplication.translate("ControlPanel", u"d1 (mm)", None))
        self.lbCompID_57.setText(QCoreApplication.translate("ControlPanel", u"Bolt Holes Centres", None))
        self.lbCompID_58.setText(QCoreApplication.translate("ControlPanel", u"PCD (mm)", None))
        self.btnImportFlanges.setText(QCoreApplication.translate("ControlPanel", u"Import", None))
        self.btnUpload_2.setText(QCoreApplication.translate("ControlPanel", u"Upload Detail", None))
        self.lbCompID_59.setText(QCoreApplication.translate("ControlPanel", u"m (kg)", None))
        self.lbCompID_60.setText(QCoreApplication.translate("ControlPanel", u"Flange Mass", None))
        self.tabTechData.setTabText(self.tabTechData.indexOf(self.tab_6), QCoreApplication.translate("ControlPanel", u"SANS 1123 Pipe Flanges", None))
        self.tabTechData.setTabText(self.tabTechData.indexOf(self.tab_10), QCoreApplication.translate("ControlPanel", u"SANS 62 and SANS 719 Pipe Sizes", None))
        self.tabTechData.setTabText(self.tabTechData.indexOf(self.tab_11), QCoreApplication.translate("ControlPanel", u"SANS 1313 Conveyor Idlers", None))
        self.lbCompany_6.setText(QCoreApplication.translate("ControlPanel", u"Designation", None))
        self.lbCompID_61.setText(QCoreApplication.translate("ControlPanel", u"Nominal Bore", None))
        self.btnImportFlanges_2.setText(QCoreApplication.translate("ControlPanel", u"Import", None))
        self.btnUpload_3.setText(QCoreApplication.translate("ControlPanel", u"Upload Detail", None))
        self.lbQuotationHistory_7.setText(QCoreApplication.translate("ControlPanel", u"SANS 1123 Plate Flange Tables", None))
        self.label_4.setText("")
        self.tabTechData.setTabText(self.tabTechData.indexOf(self.tab_12), QCoreApplication.translate("ControlPanel", u"IEC Electric Motors", None))
        self.label_15.setText(QCoreApplication.translate("ControlPanel", u"CALCULATIONS", None))
    # retranslateUi

