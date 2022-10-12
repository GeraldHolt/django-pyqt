import os
import csv
from views.mainWindow import Ui_ControlPanel
from views.login import Ui_LoginForm
from views.signup import Ui_SignupForm
from views.welcome import Ui_WelcomeForm
from views.worksorder_selector import Ui_SelectWorksorder
import settings
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlRelationalTableModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from apps.accounts.models import *
from apps.techdata.models import *

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
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

class WorkorderSelectorWindow(QDialog, Ui_SelectWorksorder):
    def __init__(self):
        super(WorkorderSelectorWindow, self).__init__()
        self.setupUi(self)
        self.cbWorksorders.addItem('Tset1')
        self.btnConfirm.clicked.connect


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

    def create_db(self):
        pass
        # self.db = QSqlDatabase.addDatabase('QSQLITE')
        # db_name = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        # self.db.setDatabaseName(db_name)

        # if not self.db.open():
        #     print("Qt failed to open database")
        #     return False
        # else :
        #     print('Success')
        #     return True
        # hostname = settings.DATABASES['default']['HOST']
        # username = settings.DATABASES['default']['NAME']
        # database = settings.DATABASES['default']['ENGINE']
        # password = settings.DATABASES['default']['PASSWORD']
        # db = QSqlDatabase.addDatabase('QMYSQL')
        # db.setHostName(hostname)
        # db.setDatabaseName(database)
        # db.setUserName(username)
        # db.setPassword(password)
        # ok = db.open()
        # self.db = ok
        # if ok:
        #     print('Success')
        # else:
        #     print(self.db.lastError().text())

        

    def goto_dashboard(self):
        self.stwMain.setCurrentWidget(self.dashboard)
        

    def goto_customers(self):
        self.stwMain.setCurrentWidget(self.customers)
        
        # Load Companies
        data = Company.objects.all().values_list('compID', 'companyName')
        if data:
            self.tableModel = TableModel(data)
            self.tableModel.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            self.tableModel.setHeaderData(1, QtCore.Qt.Horizontal, "Company Name")
            self.tvCustomers.setModel(self.tableModel)

            # header = self.tvCustomers.horizontalHeader()       
            # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.tvCustomers.show()   
        else:
            print("No data yet")

        self.btnNew.clicked.connect(self.createNewCustomer)
        
    def goto_contacts(self):
        self.stwMain.setCurrentWidget(self.contacts)

         # Load Contacts
        data = Contact.objects.all().values_list('firstName', 'lastName', 'companyName', 'contactEmail')
        if data:
            self.tableModel = TableModel(data)
            self.tableModel.setHeaderData(0, QtCore.Qt.Horizontal, "First Name")
            self.tableModel.setHeaderData(1, QtCore.Qt.Horizontal, "Last Name")
            self.tableModel.setHeaderData(2, QtCore.Qt.Horizontal, "Company Name")
            self.tableModel.setHeaderData(3, QtCore.Qt.Horizontal, "Contact Email")
            self.tvContacts.setModel(self.tableModel)

            # header = self.tvContacts.horizontalHeader()       
            # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.tvContacts.show()    
        
        else:
            print("No data yet")       

        self.btnNew_2.clicked.connect(self.createNewContact)
    
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

    def goto_generalinfo(self):
        self.stwMain.setCurrentWidget(self.techData)

        # Load Steel Tables
        data = SAISCSteelSections.objects.all().values_list('designation', 'unit_mass', 'A', 'h', 'b', 'd', 'tw', 'tf','Ix','Iy','rx','ry','J','Cw', 'Zplx', 'Zply')
        print(data)
        if data:
            self.tableModel = TableModel(data)
            self.tableModel.setHeaderData(0, QtCore.Qt.Horizontal, "Designation")
            self.tableModel.setHeaderData(1, QtCore.Qt.Horizontal, "Unit Mass")
            self.tableModel.setHeaderData(2, QtCore.Qt.Horizontal, "Area")
            self.tableModel.setHeaderData(3, QtCore.Qt.Horizontal, "h")
            self.tableModel.setHeaderData(4, QtCore.Qt.Horizontal, "b")
            self.tableModel.setHeaderData(5, QtCore.Qt.Horizontal, "d")
            self.tableModel.setHeaderData(6, QtCore.Qt.Horizontal, "tw")
            self.tableModel.setHeaderData(7, QtCore.Qt.Horizontal, "tf")
            self.tableModel.setHeaderData(8, QtCore.Qt.Horizontal, "Ix")
            self.tableModel.setHeaderData(9, QtCore.Qt.Horizontal, "Iy")
            self.tableModel.setHeaderData(10, QtCore.Qt.Horizontal, "rx")
            self.tableModel.setHeaderData(11, QtCore.Qt.Horizontal, "ry")
            self.tableModel.setHeaderData(12, QtCore.Qt.Horizontal, "J")
            self.tableModel.setHeaderData(13, QtCore.Qt.Horizontal, "Cw")
            self.tableModel.setHeaderData(14, QtCore.Qt.Horizontal, "Zplx")
            self.tableModel.setHeaderData(15, QtCore.Qt.Horizontal, "Zply")
            self.tvSteelTable.setModel(self.tableModel)

            # header = self.tvSteelTable.horizontalHeader()       
            # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.tvSteelTable.show()
        else:
            print("No data yet")   
           
        
        self.btnImportSteel.clicked.connect(self.importSteelSections)


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
        print(data)
        if data: 
            self.tableModel2 = TableModel(data)
            self.tableModel2.setHeaderData(0, QtCore.Qt.Horizontal, "Designation")
            self.tableModel2.setHeaderData(1, QtCore.Qt.Horizontal, "Nominal Bore")
            self.tableModel2.setHeaderData(2, QtCore.Qt.Horizontal, "Pressure Rating")
            self.tableModel2.setHeaderData(3, QtCore.Qt.Horizontal, "Type")
            self.tableModel2.setHeaderData(4, QtCore.Qt.Horizontal, "Pipe OD")
            self.tableModel2.setHeaderData(5, QtCore.Qt.Horizontal, "Flange OD")
            self.tableModel2.setHeaderData(6, QtCore.Qt.Horizontal, "Thickness")
            self.tableModel2.setHeaderData(7, QtCore.Qt.Horizontal, "Raised Face OD")
            self.tableModel2.setHeaderData(8, QtCore.Qt.Horizontal, "Raised Face Thk")
            self.tableModel2.setHeaderData(9, QtCore.Qt.Horizontal, "Bolt Size")
            self.tableModel2.setHeaderData(10, QtCore.Qt.Horizontal, "No. of Bolts")
            self.tableModel2.setHeaderData(11, QtCore.Qt.Horizontal, "Bolt Hole Dia")
            self.tableModel2.setHeaderData(12, QtCore.Qt.Horizontal, "PCD")
            self.tableModel2.setHeaderData(13, QtCore.Qt.Horizontal, "Flange Mass")
        
            self.tvSANSFlangeTable.setModel(self.tableModel2)

            # header = self.tvSteelTable.horizontalHeader()       
            # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

            self.tvSANSFlangeTable.show()
        
        else:
            print("No data yet")  

        self.btnImportFlanges.clicked.connect(self.importSANSPlateFlanges)



    def goto_calculations(self):
        self.stwMain.setCurrentWidget(self.calculations)

    def createNewCustomer(self):
        pass

    def createNewContact(self):
        pass


    def importSteelSections(self):
        fname = QFileDialog.getOpenFileName(self, "Import File", "", "(*.csv)")
        if fname:
            with open(fname[0]) as file:
                data = csv.reader(file, delimiter=",")
                next(data)
                counter = 0
                for row in data:
                    counter +=1
                    print(counter)
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

    def importSANSPlateFlanges(self):
        fname = QFileDialog.getOpenFileName(self, "Import File", "", "(*.csv)")
        if fname:
            with open(fname[0]) as file:
                data = csv.reader(file, delimiter=",")
                next(data)
                counter = 0
                for row in data:
                    counter +=1
                    print(counter)
                    print(row[0])
                    print(row[1])
                    
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



class MainWindow(QtWidgets.QStackedWidget):

    def __init__(self):
        super().__init__()
        self.welcome_screen = WelcomeWindow()
        self.login_screen = LoginWindow()
        self.signup_screen = SignupWindow()
        self.control_screen = ControlPanel()
        self.work_orders_selector = WorkorderSelectorWindow()

        self.addWidget(self.welcome_screen)
        self.addWidget(self.login_screen)
        self.addWidget(self.signup_screen)
        self.addWidget(self.control_screen)
        self.addWidget(self.work_orders_selector)

        self.setFixedSize(980, 570)
        
        self.welcome_screen.btnLogin.clicked.connect(self.goto_login)
        self.welcome_screen.btnRegister.clicked.connect(self.goto_signup)
        self.goto_welcome()

    def goto_login(self):
        self.setFixedSize(410, 644)
        self.setCurrentIndex(self.indexOf(self.login_screen))
        self.login_screen.btnLogin.clicked.connect(self.login)
        self.login_screen.btnForgotpass.clicked.connect(self.forgotPass)
        self.login_screen.btnRegister.clicked.connect(self.goto_signup)

    def goto_welcome(self):
        self.setCurrentIndex(self.indexOf(self.welcome_screen))

    def goto_signup(self):
        self.setFixedSize(410, 644)
        self.signup_screen.lbInvalid.setHidden(True)
        self.setCurrentIndex(self.indexOf(self.signup_screen))
        self.signup_screen.btnRegister.clicked.connect(self.signup)

    def goto_control_panel(self): 
        self.setFixedSize(1260, 835)
        self.setCurrentIndex(self.indexOf(self.control_screen)) 

    def login(self):
        username = self.login_screen.leUserName.text()
        password = self.login_screen.lePassword.text()
        print("------------------------------")
        
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
