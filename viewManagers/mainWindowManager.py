import os
import sys
import csv
from apps.accounts.list_of_countries import COUNTRIES
from forms.ui_massbalance import Ui_MassBalance
from views.mainWindow import Ui_ControlPanel
from views.login import Ui_LoginForm
from views.signup import Ui_SignupForm
from views.welcome import Ui_WelcomeForm
from views.worksorder_selector import Ui_SelectWorksorder
from views.massbalance import Ui_MassBalance
from views.pop_up_message import Ui_PopUpMessage
import settings
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlRelationalTableModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from apps.accounts.models import *
from apps.accounts.gen_look_up import *
from apps.techdata.models import *
from distutils.util import strtobool
import datetime
import comtypes.client


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, headers):
        self.columns = headers
        super(TableModel, self).__init__()
        self._data = data
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            # return f"Column {section + 1}"
            return self.columns[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f"{section + 1}"

class WorkorderSelectorWindow(QDialog, Ui_SelectWorksorder):
    def __init__(self):
        super(WorkorderSelectorWindow, self).__init__()
        self.setupUi(self)
        self.cbWorksorders.addItem('Tset1')
        self.btnConfirm.clicked.connect

class MassBalanceWindow(QDialog, Ui_MassBalance):
    def __init__(self):
        super(MassBalanceWindow, self).__init__()
        self.setupUi(self)
        

class PopUpMessageWindow(QDialog, Ui_PopUpMessage):
    def __init__(self):
        super(PopUpMessageWindow, self).__init__()
        self.setupUi(self)
        self.btnConfirm.clicked.connect(self.closeIt)
    
    def message(self, text):
        self.lbPopUpMessage.setText(text)

    def closeIt(self):
        self.close()

class WelcomeWindow(QMainWindow, Ui_WelcomeForm):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
   

class LoginWindow(QMainWindow, Ui_LoginForm):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

class SignupWindow(QMainWindow, Ui_SignupForm):
    def __init__(self):
        super(SignupWindow, self).__init__()
        self.setupUi(self)

class ControlPanel(QMainWindow, Ui_ControlPanel):
    def __init__(self):
        super(ControlPanel, self).__init__()
        self.setupUi(self)
        self.btnDashboard.clicked.connect(self.goto_dashboard)
        self.btnCustomer.clicked.connect(self.goto_customers)  
        self.btnContacts.clicked.connect(self.goto_contacts)
        self.btnQuotation.clicked.connect(self.goto_quotations) 
        self.btnWorksorder.clicked.connect(self.goto_select_workorder)    
        self.btnResources.clicked.connect(self.goto_resources) 
        self.btnTimesheets.clicked.connect(self.goto_timesheets) 
        self.btnInvoices.clicked.connect(self.goto_invoices) 
        self.btnDocControl.clicked.connect(self.goto_doccontrol) 
        self.btnProcurement.clicked.connect(self.goto_procurement) 
        self.btnAnalysis.clicked.connect(self.goto_analysis) 
        self.btnGeneralInfo.clicked.connect(self.goto_generalinfo) 
        self.btnCalculation.clicked.connect(self.goto_calculations) 
        self.btnUploadWO.clicked.connect(self.goto_select_workorder)
        self.btnMassBalance.clicked.connect(self.goto_massbalance)

    def goto_dashboard(self):
        self.stwMain.setCurrentWidget(self.dashboard)

# Customers ============================================================================#   
    def goto_customers(self):
        self.stwMain.setCurrentWidget(self.customers)
        
        # Load Companies
        data = Company.objects.all().values_list('compID', 'companyName')
        if data:
            headers = ["ID", "Company Name"]
            self.tableModel = TableModel(data, headers)
            self.tvCustomers.setModel(self.tableModel)
            self.tvCustomers.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    
            self.tvCustomers.show()   
        else:
            print("No data yet")

        # Load Comboboxes
        self.status = COMPANY_OPERATION_STATUS
        self.country = COUNTRIES

        company_status = []
        countries_names = []
        for ct in self.country:
            countries_names.append(ct[1])
        for st in self.status:
            company_status.append(st[1])

        self.cbCompanyStatus.addItems(company_status)
        self.cbCountry.addItems(countries_names)
        self.cbCountry.setCurrentIndex(countries_names.index('South Africa'))

        # Allocate Buttons
        self.btnNewCustomer.clicked.connect(self.createNewUpdateCustomer)
        self.btnClearCustomerCells.clicked.connect(self.clearCustomerCells)
        self.btnEditCustomer.clicked.connect(self.editCustomer)
        # self.btnDeleteCustomer.clicked.connect(self.deleteCustomer)

    def clearCustomerCells(self):
        self.leCompID.clear()
        self.leCompanyName.clear()
        self.cbCompanyStatus.clear()
        self.leRegistrationNumber.clear()
        self.leVATNumber.clear()
        self.leWebsite.clear()
        self.leAddress1.clear()
        self.leAddress2.clear()
        self.leCity.clear()
        self.lePostalCode.clear()
        self.leProvince.clear()
        self.cbCountry.clear()
        self.leBusinessPhone.clear()
        self.leCompanyEmail.clear()

    def createNewUpdateCustomer(self):

        compID  =  self.leCompID.text()
        companyName = self.leCompanyName.text()
        company_status = self.cbCompanyStatus.currentText()
        company_reg_no = self.leRegistrationNumber.text()
        VAT_no = self.leVATNumber.text()
        companyWeb =  self.leWebsite.text()
        address1 = self.leAddress1.text()
        address2 = self.leAddress2.text()
        city = self.leCity.text()
        postalCode = self.lePostalCode.text()
        province = self.leProvince.text()
        country = self.cbCountry.currentText()
        businessPhone = self.leBusinessPhone.text()
        companyEmail = self.leCompanyEmail.text()
        customer = self.cboxCustomer.isChecked()
        supplier = self.cboxSupplier.isChecked()

        try:
            if compID:
                company = Company.objects.filter(compID  =  compID)
            
                if company:
                    company.update(
                                    companyName = companyName,                         
                                    company_status = company_status,
                                    company_reg_no = company_reg_no,
                                    VAT_no = VAT_no,
                                    companyWeb = companyWeb,
                                    address1 = address1,
                                    address2 = address2,
                                    city = city,
                                    postalCode = postalCode,
                                    province = province,
                                    country = country,
                                    businessPhone = businessPhone,
                                    companyEmail = companyEmail,
                                    customer = customer,
                                    supplier = supplier
                    )
                    self.clearCustomerCells()
                    self.leCompID.setReadOnly(False)
                    message = 'Customer Data Updated'
                    pop_up = PopUpMessageWindow()
                    pop_up.message(message)
                    pop_up.exec_()

                else:
                    company.create(
                                    companyName = companyName,                         
                                    company_status = company_status,
                                    company_reg_no = company_reg_no,
                                    VAT_no = VAT_no,
                                    companyWeb = companyWeb,
                                    address1 = address1,
                                    address2 = address2,
                                    city = city,
                                    postalCode = postalCode,
                                    province = province,
                                    country = country,
                                    businessPhone = businessPhone,
                                    companyEmail = companyEmail,
                                    customer = customer,
                                    supplier = supplier
                    )
                    self.leCompID.setReadOnly(False)
                    self.clearCustomerCells()
                    self.leCompID.setReadOnly(False)
                    message = 'New Customer Added'
                    pop_up = PopUpMessageWindow()
                    pop_up.message(message)
                    pop_up.exec_()
            else:
                message = 'Cannot Upload Empty Cells'
                pop_up = PopUpMessageWindow()
                pop_up.message(message)
                pop_up.exec_()

        except Exception as e:
            print(e)
            message = 'Something went wrong!!!'
            pop_up = PopUpMessageWindow()
            pop_up.message(message)
            pop_up.exec_()

    def editCustomer(self):
        index = self.tvCustomers.selectionModel().selectedIndexes()[0]
        row_index = {index.row() for index in self.tvCustomers.selectionModel().selectedIndexes()}
        if len(row_index)>1:
            message = 'Select only a single line'
            pop_up = PopUpMessageWindow()
            pop_up.message(message)
            pop_up.exec_()
        else:
            
            column = 0
            row = list(row_index)[0]
            index = self.tvCustomers.model().index(row, column)  
            company = Company.objects.get(compID = str(index.data()))
            self.leCompID.setText(company.compID)
            self.leCompanyName.setText(company.companyName)
            self.cbCompanyStatus.setCurrentText(company.company_status)
            self.leRegistrationNumber.setText(company.company_reg_no)
            self.leVATNumber.setText(company.VAT_no)
            self.leWebsite.setText(company.companyWeb)
            self.leAddress1.setText(company.address1)
            self.leAddress2.setText(company.address2)
            self.leCity.setText(company.city)
            self.lePostalCode.setText(company.postalCode)
            self.leProvince.setText(company.province)
            self.cbCountry.setCurrentText(company.country)
            self.leBusinessPhone.setText(company.businessPhone)
            self.leCompanyEmail.setText(company.companyEmail)
            # self.cboxCustomer.setChecked(bool(strtobool(company.customer)))
            # self.cboxSupplier.setChecked(bool(strtobool(company.supplier)))
            self.leCompID.setReadOnly(True)

    

# Contacts ============================================================================#   
    def goto_contacts(self):
        self.stwMain.setCurrentWidget(self.contacts)

         # Load Contacts
        data = Contact.objects.all().values_list('contID','firstName', 'lastName', 'companyName', 'contactEmail')
        companies = list(Company.objects.all().values_list('id', 'companyName'))
        temp_data = []
        for group in data:
            temp=[]
            for item in group:
                temp.append(item)
            temp_data.append(temp)
        
        for item in temp_data:  
            for comp in companies:
                if item[3] == comp[0]:
                    item[3]=(comp[1])
        if data:
            headers = ["Contact ID","First Name", "Last Name", "Company Name","Contact Email"]
            self.tableModel = TableModel(temp_data, headers)
            self.tvContacts.setModel(self.tableModel)
            self.tvContacts.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    
            self.tvContacts.show()    
        
        else:
            print("No data yet")       

        # Load Comboboxes
        self.companies = Company.objects.all()
        company_names = []
        for cn in self.companies:
            company_names.append(cn.companyName)

        self.cbCompany.addItems(company_names)

        # Allocate Buttons
        self.btnNewContact.clicked.connect(self.createNewUpdateContact)
        self.btnClearContactCells.clicked.connect(self.clearContactCells)
        self.btnEditContact.clicked.connect(self.editContact)
        # self.btnDeleteContact.clicked.connect(self.deleteContact)

    def clearContactCells(self):
        self.leContactID.clear()
        self.leFirstName.clear()
        self.leLastName.clear()
        self.cbCompany.clear()
        self.leEmail.clear()
        self.lePosition.clear()
        self.leBusPhone.clear()
        self.leMobile.clear()
        self.deDOB.clear()

    def createNewUpdateContact(self):
        contID = self.leContactID.text()
        firstName  =  self.leFirstName.text()
        lastName = self.leLastName.text()
        companyName = self.cbCompany.currentText()
        contactEmail = self.leEmail.text()
        jobTitle = self.lePosition.text()
        contactBusPhone =  self.leBusPhone.text()
        contactMobile = self.leMobile.text()
        date_of_birth = self.deDOB.text()

        try:
            if firstName:
                contact = Contact.objects.filter(contID  =  contID)
                company = Company.objects.get(companyName = companyName)
                if contact:
                    contact.update(
                                    contID = contID,
                                    firstName = firstName,                         
                                    lastName = lastName,
                                    companyName = company.id,
                                    contactEmail = contactEmail,
                                    jobTitle = jobTitle,
                                    contactBusPhone = contactBusPhone,
                                    contactMobile = contactMobile,
                                    date_of_birth = date_of_birth,
                    )
                    self.clearContactCells()
                    self.leContactID.setReadOnly(False)
                    message = 'Contact Details Updated'
                    pop_up = PopUpMessageWindow()
                    pop_up.message(message)
                    pop_up.exec_()

                else:
                    contact.create(
                                    contID = contID,
                                    firstName = firstName,                         
                                    lastName = lastName,
                                    companyName = company.id,
                                    contactEmail = contactEmail,
                                    jobTitle = jobTitle,
                                    contactBusPhone = contactBusPhone,
                                    contactMobile = contactMobile,
                                    date_of_birth = date_of_birth,
                    )
                    self.clearContactCells()
                    self.leContactID.setReadOnly(False)
                    message = 'New Contact Added'
                    pop_up = PopUpMessageWindow()
                    pop_up.message(message)
                    pop_up.exec_()

            else:
                message = 'Cannot Upload Empty Cells'
                pop_up = PopUpMessageWindow()
                pop_up.message(message)
                pop_up.exec_()

        except Exception as e:
            print(e)
            message = 'Something went wrong!!!'
            pop_up = PopUpMessageWindow()
            pop_up.message(message)
            pop_up.exec_()

    def editContact(self):
        index = self.tvContacts.selectionModel().selectedIndexes()[0]
        row_index = {index.row() for index in self.tvContacts.selectionModel().selectedIndexes()}
        if len(row_index)>1:
            message = 'Select only a single line'
            pop_up = PopUpMessageWindow()
            pop_up.message(message)
            pop_up.exec_()
        else:
            
            column = 0
            row = list(row_index)[0]
            index = self.tvContacts.model().index(row, column)  
            contact = Contact.objects.get(contID = str(index.data()))
            company = Company.objects.get(companyName = contact.companyName)
            comp = company.companyName
            self.leContactID.setText(contact.contID)
            self.leFirstName.setText(contact.firstName)
            self.leLastName.setText(contact.lastName)
            self.cbCompany.setCurrentText(comp)
            self.leEmail.setText(contact.contactEmail)
            self.lePosition.setText(contact.jobTitle)
            self.leBusPhone.setText(contact.contactBusPhone)
            self.leMobile.setText(contact.contactMobile)
            # self.deDOB.setDate(DOB)
            self.leContactID.setReadOnly(True)

            self.companies = Company.objects.all()
            company_names = []
            for cn in self.companies:
                company_names.append(cn.companyName)
                self.cbCompany.addItems(company_names)


    
    def goto_quotations(self):
        self.stwMain.setCurrentWidget(self.quotations)

    def goto_select_workorder(self):
        work_order_select = WorkorderSelectorWindow()
        work_order_select.exec_()
        
    def goto_workorders(self):
        self.stwMain.setCurrentWidget(self.worksorders)

    def goto_resources(self):
        self.stwMain.setCurrentWidget(self.resources)
        
    def goto_timesheets(self):
        self.stwMain.setCurrentWidget(self.timesheets)
    
    def goto_invoices(self):
        self.stwMain.setCurrentWidget(self.invoices)

    def goto_doccontrol(self):
        self.stwMain.setCurrentWidget(self.documentControl)

    def goto_procurement(self):
        self.stwMain.setCurrentWidget(self.procurement)

    def goto_analysis(self):
        self.stwMain.setCurrentWidget(self.analysis)

# General Information =====================================================================#
    def goto_generalinfo(self):
        self.stwMain.setCurrentWidget(self.techData)

    # Load Steel Tables
        data = SAISCSteelSections.objects.all().values_list('designation', 'unit_mass', 'A', 'h', 'b', 'd', 'tw', 'tf','Ix','Iy','rx','ry','J','Cw', 'Zplx', 'Zply')
        headers = ["Designation", "Unit Mass", "Area", "h", "b", "d", "tw", "tf", "Ix", "Iy", "rx", "ry", "J", "Cw", "Zplx", "Zply"]
        if data:
            self.tableModel = TableModel(data, headers)
            self.tvSteelTable.setModel(self.tableModel)
            self.header = self.tvSteelTable.horizontalHeader()
            self.tvSteelTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    

            self.tvSteelTable.show()
        else:
            print("No data yet")   
           
        
        self.btnUploadSteelData.clicked.connect(self.uploadSteelSections)


    # Load SANS 1123 Pipe Flanges
        data = SANSPlateFlanges.objects.all().values_list(
                                                        'designation',
                                                        'nom_bore',
                                                        'pressureRating',
                                                        'flange_type', 
                                                        'pipeOutsideDia',
                                                        'flangeOutsideDia', 
                                                        'flangeThickness',
                                                        'raisedFaceDia', 
                                                        'raisedFaceThick', 
                                                        'boltSize', 
                                                        'NOB',
                                                        'boltHoleSize',
                                                        'PCD',
                                                     'flange_mass', )

        headers = ["Designation", "Nominal Bore", "Pressure Rating", "Type", "Pipe OD", "Flange OD", "Thickness", "Raised Face OD", "Raised Face Thk","Bolt Size", "No. of Bolts", "Bolt Hole Dia", "PCD", "Flange Mass"]
        if data: 
            self.tableModel2 = TableModel(data, headers)
            self.tvSANSFlangeTable.setModel(self.tableModel2)
            self.header = self.tvSteelTable.horizontalHeader()
            self.tvSteelTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    
            self.tvSANSFlangeTable.show()
        
        else:
            print("No data yet")  

        self.btnImportFlanges.clicked.connect(self.importSANSPlateFlanges)
        
    # Load IED Motor Flanges
        data = IECElectricalMotors.objects.all().values_list(
                                                        'designation',
                                                        'motorPower',
                                                        'motorSpeed',
                                                        'poles', 
                                                        'frame',
                                                        'shaft', 
                                                        'keywaywidth',
                                                        'keywayheight', 
                                                        'shaftkeydepth', 
                                                        'shaft_height', 
                                                        'full_load_torque',
                                                        'lock_rotor_torque',
                                                        'break_torque',
                                                        'mounting', )

        headers = ["Designation", "Motor Power", "Motor Speed", "Poles", "Frame", "Shaft", "Key Width", "Key Height", "Shaft Key Depth","Weight", "Shaft Height", "Full Torque", "Lock Torque", "Break Torque", "Mounting"]
        if data: 
            self.tableModel3 = TableModel(data, headers)
            self.tvIECMotors.setModel(self.tableModel3)
            self.header = self.tvSteelTable.horizontalHeader()
            self.tvSteelTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    
            self.tvIECMotors.show()
        
        else:
            print("No data yet")  

        self.btnImportFlanges.clicked.connect(self.importIECMotorDetails)

    # Load ConveyorSolePlatesBearings
        data = SolePLatePlummerBlock.objects.all().values_list('designation', 'bearShaftDia','plumBlock','bearing','adapterSleeve','lockRing','seal','dimA','dimC','dimD', 'dimE','dimF', 'dimF1','dimG','dimH','dimJ','dimK','dimL','dimM', 'dimN', 'dimS', 'dimT', 'dimU')
        headers = ["Designation", "Shaft Dia.", "Plummer", "Bearing", "Adapter", "Lock Ring", "Seals", "A", "C", "D", "E", "F", "F1", "G", "H", "J", "K", "L", "M", "N", "S", "T", "U"]
        if data:
            self.tableModel4 = TableModel(data, headers)
            self.tvConSolePlatBearings.setModel(self.tableModel4)
            self.header = self.tvConSolePlatBearings.horizontalHeader()
            self.tvConSolePlatBearings.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    
            self.tvConSolePlatBearings.show()
        else:
            print("No data yet")   
           
        
        # self.btnUploadSole.clicked.connect(self.uploadSolePlatedate)
        # self.btnPrintSole.clicked.connect(self.uploadSolePlatedate)

    def uploadSteelSections(self):
        index = self.tvSteelTable.selectionModel().selectedIndexes()[0]
        row_index = {index.row() for index in self.tvSteelTable.selectionModel().selectedIndexes()}
        if len(row_index)>1:
            message = 'Select only a single line'
            pop_up = PopUpMessageWindow()
            pop_up.message(message)
            pop_up.exec_()
        else:
            
            column = 0
            row = list(row_index)[0]
            index = self.tvSteelTable.model().index(row, column)  
            steel = SAISCSteelSections.objects.get(designation = str(index.data()))
            self.leProfile.setText(steel.profile)
            self.leDesignation.setText(steel.designation)
            self.leUnitMass.setText(steel.unit_mass)
            self.leHeight.setText(steel.h)
            self.leWidth.setText(steel.b)
            self.leLipHeight.setText(steel.c)
            self.leDiameter.setText(steel.d)
            self.leWebThickness.setText(steel.tw)
            self.leFlangeThickness.setText(steel.tf)
            self.leWebradius.setText(steel.r1)
            self.leFlangeRadius.setText(steel.r2)
            self.leTaperDistance.setText(steel.b1)
            self.leTaperAngle.setText(steel.Beta)
            self.leArea.setText(steel.A)
            self.leIxx.setText(steel.Ix)
            self.leZxx.setText(steel.Zx)
            self.lerxx.setText(steel.rx)
            self.leIyy.setText(steel.Iy)
            self.leZyy.setText(steel.Zy)
            self.leryy.setText(steel.ry)
            self.leJ.setText(steel.J)
            self.leCw.setText(steel.Cw)
            self.leZplx.setText(steel.Zplx)
            self.leZply.setText(steel.Zply)
            self.leIuu.setText(steel.Iu)
            self.leZuu.setText(steel.Zu)
            self.leruu.setText(steel.ru)
            self.leIvv.setText(steel.Iv)
            self.leZvv.setText(steel.Zv)
            self.lervv.setText(steel.rv)
            self.leIuu.setText(steel.Iu)
            self.leZuu.setText(steel.Zu)
            self.leh_tf.setText(steel.h_tf)
            self.lehw.setText(steel.hw)
            self.lealpha.setText(steel.alpha)
            self.leac.setText(steel.ac)
            self.leax.setText(steel.ax)
            self.leay.setText(steel.ay)
            
    def goto_massbalance(self):
        massbalance = MassBalanceWindow()
        massbalance.exec_()

# Calculations and Tools =====================================================================#
    def goto_calculations(self):
        self.stwMain.setCurrentWidget(self.calculations)
        self.btnUploadFiles.clicked.connect(self.uploadFilestoConverttoPDF)



# Import Steel Sections =============================================================#
    def importSteelSections(self):
        fname = QFileDialog.getOpenFileName(self, "Import File", "", "(*.csv)")
        if fname:
            with open(fname[0]) as file:
                data = csv.reader(file, delimiter=",")
                next(data)
                counter = 0
                for row in data:
                    counter +=1
                    try:
                        obj, created = SANSPlateFlanges.objects.update_or_create(                                                                                
                                                                designation         = row[0],
                                                                profile             = row[1],
                                                                unit_mass           = row[2],
                                                                h                   = row[3],
                                                                b                   = row[4],
                                                                c                   = row[5],
                                                                d                   = row[6],
                                                                tw                  = row[7],
                                                                tf                  = row[8],
                                                                r1                  = row[9],
                                                                r2                  = row[10],
                                                                b1                  = row[11],
                                                                Beta                = row[12],
                                                                A                   = row[13],
                                                                Ix                  = row[14],
                                                                Zx                  = row[15],
                                                                rx                  = row[16],
                                                                Iy                  = row[17],
                                                                Zy                  = row[18],
                                                                ry                  = row[19],
                                                                Iu                  = row[24],
                                                                Zu                  = row[25],
                                                                ru                  = row[26],
                                                                Iv                  = row[27],
                                                                Zv                  = row[28],
                                                                rv                  = row[29],
                                                                J                   = row[20],
                                                                Cw                  = row[21],
                                                                Zplx                = row[22],
                                                                Zply                = row[23],
                                                                h_tf                = row[30],
                                                                hw                  = row[31],
                                                                ac                  = row[32],
                                                                ax                  = row[33],
                                                                ay                  = row[34],
                                                                alpha               = row[35]
                                                                )
                    except Exception as e:
                        print(e)	
            file.close()
            self.goto_generalinfo
        else:
            self.goto_generalinfo
# Import Steel Flanges =============================================================#
    def importSANSPlateFlanges(self):
        fname = QFileDialog.getOpenFileName(self, "Import File", "", "(*.csv)")
        if fname:
            with open(fname[0]) as file:
                data = csv.reader(file, delimiter=",")
                next(data)
                counter = 0
                for row in data:
                    counter +=1
                    obj, created = SANSPlateFlanges.objects.update_or_create(                                                                                
                                                            designation         = row[0],
                                                            nom_bore            = row[1],
                                                            pressureRating      = row[2],
                                                            flange_type         = row[3],
                                                            pipeOutsideDia      = row[4],
                                                            flangeOutsideDia    = row[5],
                                                            flangeThickness     = row[6],
                                                            raisedFaceDia       = row[7],
                                                            raisedFaceThick     = row[8],
                                                            boltSize            = row[9],
                                                            NOB                 = row[10],
                                                            boltHoleSize        = row[11],
                                                            PCD                 = row[12],
                                                            flange_mass         = row[13],
                    )
                                             
            file.close()
            self.goto_generalinfo
        else:
            self.goto_generalinfo
# Import IEC Motors =============================================================#
    def importIECMotorDetails(self):
        fname = QFileDialog.getOpenFileName(self, "Import File", "", "(*.csv)")
        if fname:
            with open(fname[0]) as file:
                data = csv.reader(file, delimiter=",")
                next(data)
                counter = 0
                for row in data:
                    counter +=1
                    try:
                        obj, created = IECElectricalMotors.objects.update_or_create(                                                                                
                                                                designation      = row[0],
                                                                motorPower       = row[1],
                                                                motorSpeed       = row[2],
                                                                poles            = row[3],
                                                                frame            = row[4],
                                                                shaft            = row[5],
                                                                keywaywidth      = row[6],
                                                                keywayheight     = row[7],
                                                                shaftkeydept     = row[8],
                                                                weight           = row[9],
                                                                shaft_height     = row[10],
                                                                full_load_torque = row[11],
                                                                lock_rotor_torque= row[12],
                                                                break_torque     = row[13],
                                                                mounting         = row[14],
                                                                                    )
                    except Exception as e:
                        print(e)	
            file.close()
            self.goto_generalinfo
        else:
            self.goto_generalinfo

# Upload  =============================================================#
    def uploadFilestoConverttoPDF(self):
        filenames, _ = QFileDialog.getOpenFileNames(
                    None,
                    "QFileDialog.getOpenFileNames()",
                    "",
                    "Word Files(*.docx);;Excel Files (*.xlsx)",
                )
        if filenames:
            for filename in filenames:
                item = QtGui.QStandardItem(filename)
                self.lvBulkFilesLoad.appendRow(item)


# =========================================================================================#
# Main Window  Block ======================================================================#
# =========================================================================================#

class MainWindow(QtWidgets.QStackedWidget):

    def __init__(self):
        super().__init__()
        self.welcome_screen = WelcomeWindow()
        self.login_screen = LoginWindow()
        self.signup_screen = SignupWindow()
        self.control_screen = ControlPanel()
        self.work_orders_selector = WorkorderSelectorWindow()
        self.pop_up_message = PopUpMessageWindow()
        self.massbalance = MassBalanceWindow()

        self.addWidget(self.welcome_screen)
        self.addWidget(self.login_screen)
        self.addWidget(self.signup_screen)
        self.addWidget(self.control_screen)
        self.addWidget(self.work_orders_selector)
        self.addWidget(self.pop_up_message)

        self.setFixedSize(980, 570)
        self.center()
        
        self.welcome_screen.btnLogin.clicked.connect(self.goto_login)
        self.welcome_screen.btnRegister.clicked.connect(self.goto_signup)
 
        self.goto_welcome()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def goto_login(self):
        self.setFixedSize(410, 644)
        self.center()
        self.setCurrentIndex(self.indexOf(self.login_screen))
        self.login_screen.btnLogin.clicked.connect(self.login)
        self.login_screen.btnForgotpass.clicked.connect(self.forgotPass)
        self.login_screen.btnRegister.clicked.connect(self.goto_signup)
        
    def goto_welcome(self):
        self.center() 
        self.setCurrentIndex(self.indexOf(self.welcome_screen))

    def goto_signup(self):
        self.setFixedSize(410, 644)
        self.signup_screen.lbInvalid.setHidden(True)
        self.center()
        self.setCurrentIndex(self.indexOf(self.signup_screen))
        self.signup_screen.btnRegister.clicked.connect(self.signup)
        
    def goto_control_panel(self): 
        # self.setFixedSize(1540, 963)
        self.setCurrentIndex(self.indexOf(self.control_screen)) 


    def login(self):
        username = self.login_screen.leUserName.text()
        password = self.login_screen.lePassword.text()
        
        if len(username) == 0 or len(password) == 0:
            self.login_screen.lbInvalid.setText("Please enter in all fields")
        else:
            user = authenticate(username = username, password = password)
            if user is not None:
                self.login_screen.lbInvalid.setText("ACCESS GRANTED")
                controlPanel = ControlPanel()
                self.addWidget(controlPanel)
                self.setFixedSize(1550, 850)
                self.setCurrentIndex(self.indexOf(self.control_screen)) 
            else:
                self.login_screen.lbInvalid.setText("NO ACCESS")
                self.login_screen.btnForgotpass.clicked.connect(self.forgotPass)
                self.login_screen.btnRegister.clicked.connect(self.goto_signup)
    
    
    def signup(self):
        username = self.signup_screen.leUserName.text()
        email = self.signup_screen.leEmail.text()
        password = self.signup_screen.lePassword.text()
        confirmPass = self.signup_screen.leConfirmpass.text()

        if password != confirmPass:
            self.signup_screen.lbInvalid.setText("Passwords are no the same")
        else:
            user = User.objects.create_user(username, email, password)
            user.save()

    def forgotPass(self):
        print("----UNDER CONSTRUCTION ---")





    # Activate Menu Buttons
    def showDashboard(self):
        self.stwMain.setCurrentWidget(self.dashboard)

    def showCustomer(self):
        self.stwMain.setCurrentWidget(self.customers)
        print("gggggggggggggggggggggg")



    # Activate Customer Buttons
