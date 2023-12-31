from PyQt6 import QtCore, QtGui, QtWidgets
import home
import new_ro
import customer_search
import mysql.connector
import confirm_delete
import sys
import customer_info
from database.customers import customers_db
class Ui_MainWindow(object):

# Closes customer hub and opens home page
    def open_home_page(self):
        self.show_home_page = QtWidgets.QMainWindow()
        self.home_page_ui = home.Ui_MainWindow()
        self.home_page_ui.setupUi(self.show_home_page)
        self.show_home_page.show()

# Opens customer search window to find name and associated vehicle to create repair order
    def open_customer_search(self):
        self.show_customer_search = QtWidgets.QWidget()
        self.show_customer_search_ui = customer_search.Ui_Form()
        self.show_customer_search_ui.setupUi(self.show_customer_search)
        self.show_customer_search.show()


# Opens new customer window for adding customer into database
    def open_new_customer(self):
        self.show_new_customer_page = QtWidgets.QWidget()
        self.show_new_customer_page_ui = customer_info.Ui_Form()
        self.show_new_customer_page_ui.setupUi(self.show_new_customer_page)
        self.show_new_customer_page.show()
        self.show_new_customer_page_ui.edit_button.hide()
        self.show_new_customer_page.setWindowTitle("New Customer")



# Opens window for creating repair order by selecting data and customer concern
    def create_ro(self):
        self.new_ro_page = QtWidgets.QWidget()
        self.new_ro_page_ui = new_ro.Ui_create_ro()
        self.new_ro_page_ui.setupUi(self.new_ro_page)
        self.new_ro_page.show()

# Delete selected customer row in table data
    def delete_customer(self):
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        selected_row = self.customer_table.currentRow()
        selected_column = self.customer_table.currentColumn()
        selected_data = []
        selected_name = self.customer_table.itemAt(selected_row, selected_column)
        for column in range(self.customer_table.model().columnCount()):
            index = self.customer_table.model().index(selected_row, column)
            selected_data.append(index.data())
        conn = my_db.cursor()
        delete_customer_row = "DELETE FROM customers WHERE name = %s AND address = %s"
        conn.execute(delete_customer_row, (selected_data[0], selected_data[1]))
        my_db.commit()
        my_db.close()
        self.customer_table.removeRow(selected_row)


# Shows "are you sure prompt before deleting customer and vehicle form database
    def delete_prompt(self):
        self.delete_page = QtWidgets.QWidget()
        self.delete_page_ui = confirm_delete.Ui_confirm_delete()
        self.delete_page_ui.setupUi(self.delete_page)
        selected_row = self.customer_table.currentRow()
        selected_column = self.customer_table.currentColumn()
        selected_data = []
        selected_name = self.customer_table.itemAt(selected_row, selected_column)
        for column in range(self.customer_table.model().columnCount()):
            index = self.customer_table.model().index(selected_row, column)
            selected_data.append(index.data())
        self.delete_page_ui.customer_label.setText("Delete %s From Database?" % selected_data[0])
        self.delete_page.show()
        self.delete_page_ui.yes_delete.clicked.connect(self.delete_customer)

    # populate customer line edits with data from selected row and change save button to edit button
    def update_customer_credentials(self):
        self.show_new_customer_page = QtWidgets.QWidget()
        self.show_new_customer_page_ui = customer_info.Ui_Form()
        self.show_new_customer_page_ui.setupUi(self.show_new_customer_page)
        self.show_new_customer_page.show()
        self.show_new_customer_page_ui.save_create_button.hide()
        if self.customer_table.cellDoubleClicked:
            self.show_new_customer_page.setWindowTitle("Edit Customer")
        selected_row = self.customer_table.currentRow()
        selected_column = self.customer_table.currentColumn()
        selected_data = []
        selected_name = self.customer_table.itemAt(selected_row, selected_column)
        for column in range(self.customer_table.model().columnCount()):
            index = self.customer_table.model().index(selected_row, column)
            selected_data.append(index.data())
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()
        query = """SELECT * FROM customers WHERE(name = %s and phone = %s)"""
        name_phone = [selected_data[0], selected_data[5]]
        conn.execute(query, name_phone)
        result = conn.fetchall()

        print(selected_data)
        for row in result:
            self.show_new_customer_page_ui.name_line.setText(row[0])
            self.show_new_customer_page_ui.address_line.setText(row[1])
            self.show_new_customer_page_ui.city_line.setText(row[2])
            self.show_new_customer_page_ui.state_line.setText(row[3])
            self.show_new_customer_page_ui.zip_line.setText(row[4])
            self.show_new_customer_page_ui.phone_line.setText(row[5])
            self.show_new_customer_page_ui.alt_phone_line.setText(row[6])
            self.show_new_customer_page_ui.email_line.setText(row[7])
            self.show_new_customer_page_ui.vin_line.setText(row[9])
            self.show_new_customer_page_ui.year_line.setText(row[10])
            self.show_new_customer_page_ui.make_line.setText(row[11])
            self.show_new_customer_page_ui.model_line.setText(row[12])
            self.show_new_customer_page_ui.engine_line.setText(row[13])
            self.show_new_customer_page_ui.trim_line.setText(row[14])
        my_db.close()

# Find row id to be able to edit or delete data from database
    def row_id_find(self):
        selected_row = self.customer_table.currentRow()
        selected_column = self.customer_table.currentColumn()
        selected_data = []
        selected_name = self.customer_table.itemAt(selected_row, selected_column)
        for column in range(self.customer_table.model().columnCount()):
            index = self.customer_table.model().index(selected_row, column)
            selected_data.append(index.data())
        print(selected_data)

# Refresh Window To Update Table Data
    def restart_app(self):

        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
# Highlights entire row instead of single cell
    def highlight_row(self):
        self.customer_table.selectRow(self.customer_table.currentRow())


    def setupUi(self, Customers):
        Customers.setObjectName("Customers")
        Customers.resize(1243, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/user.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        Customers.setWindowIcon(icon)
#        Customers.setStyleSheet("  background-color: #504F4F;")
        self.centralwidget = QtWidgets.QWidget(parent=Customers)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.customer_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        header_names = ("Name", "Address", "City", "State", "Zip", "Phone", "Alt Phone", "Email")
      #  self.customer_table.setStyleSheet("border: 20px;")
        self.customer_table.setColumnCount(8)
        self.customer_table.setObjectName("customer_table")
        self.customer_table.setRowCount(customers_db.row_count(self))
        self.customer_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.customer_table.setHorizontalHeaderLabels(header_names)
        self.customer_table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.customer_table.setShowGrid(False)
     #   self.customer_table.setStyleSheet('QtableView::item {border-bottom: 10px solid #d6d9dc;}')
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()
        conn.execute("SELECT * FROM customers ORDER BY name")
        table_row = 0
        result = conn.fetchall()

        for row in result:
            self.customer_table.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.customer_table.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.customer_table.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.customer_table.setItem(table_row, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.customer_table.setItem(table_row, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.customer_table.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.customer_table.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.customer_table.setItem(table_row, 7, QtWidgets.QTableWidgetItem(row[7]))
            table_row += 1
        my_db.close()
        self.gridLayout.addWidget(self.customer_table, 0, 1, 2, 1)
        self.customer_table.cellDoubleClicked.connect(self.update_customer_credentials)
        self.customer_table.cellDoubleClicked.connect(self.customer_table.repaint)
        self.customer_table.cellClicked.connect(self.highlight_row)
        self.winter_auto_logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.winter_auto_logo.setMaximumSize(QtCore.QSize(130, 16777215))
        self.winter_auto_logo.setText("")
        self.winter_auto_logo.setPixmap(QtGui.QPixmap("../ui_files/winter_auto.png"))
        self.winter_auto_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.winter_auto_logo.setObjectName("winter_auto_logo")
        self.winter_auto_logo.setMinimumSize(QtCore.QSize(0, 100))
        self.winter_auto_logo.setMaximumSize(QtCore.QSize(130, 200))
        self.gridLayout.addWidget(self.winter_auto_logo, 1, 0, 1, 1)
        self.sidebar = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.sidebar.setMaximumSize(QtCore.QSize(130, 500))
        self.sidebar.setStyleSheet("background-color: #929191;")
        self.sidebar.setIconSize(QtCore.QSize(30, 30))
        self.sidebar.setTabBarAutoHide(True)
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setMinimumSize(QtCore.QSize(130, 500))
        self.sidebar.setMaximumSize(QtCore.QSize(90, 800))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(parent=self.tab)
        self.widget.setGeometry(QtCore.QRect(3, 4, 121, 461))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.new_customer_button = QtWidgets.QPushButton(parent=self.widget)
        self.new_customer_button.setMinimumSize(QtCore.QSize(90, 30))
        self.new_customer_button.setStyleSheet("text-align: left;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/user-add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.new_customer_button.setIcon(icon1)
        self.new_customer_button.setIconSize(QtCore.QSize(30, 30))
        self.new_customer_button.setFlat(True)
        self.new_customer_button.setObjectName("new_customer_button")
        self.new_customer_button.clicked.connect(self.open_new_customer)
        self.verticalLayout.addWidget(self.new_customer_button)
        self.create_ro_button = QtWidgets.QPushButton(parent=self.widget)
        self.create_ro_button.setMinimumSize(QtCore.QSize(0, 30))
        self.create_ro_button.setStyleSheet("text-align: left;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/add-document.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.create_ro_button.setIcon(icon2)
        self.create_ro_button.setIconSize(QtCore.QSize(30, 30))
        self.create_ro_button.setFlat(True)
        self.create_ro_button.clicked.connect(self.create_ro)
        self.create_ro_button.setObjectName("create_ro_button")
        self.verticalLayout.addWidget(self.create_ro_button)
        self.search_button = QtWidgets.QPushButton(parent=self.widget)
        self.search_button.setMinimumSize(QtCore.QSize(30, 30))
        self.search_button.setStyleSheet("text-align: left;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_button.setIcon(icon3)
        self.search_button.setIconSize(QtCore.QSize(30, 30))
        self.search_button.setFlat(True)
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(self.open_customer_search)
        self.verticalLayout.addWidget(self.search_button)
        self.print_button = QtWidgets.QPushButton(parent=self.widget)
        self.print_button.setMinimumSize(QtCore.QSize(0, 30))
        self.print_button.setStyleSheet("text-align: left;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/print.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.print_button.setIcon(icon4)
        self.print_button.setIconSize(QtCore.QSize(30, 30))
        self.print_button.setFlat(True)
        self.print_button.setObjectName("print_button")
        self.verticalLayout.addWidget(self.print_button)
        self.refresh_button = QtWidgets.QPushButton(parent=self.widget)
        self.refresh_button.setMinimumSize(QtCore.QSize(0, 30))
        self.refresh_button.setStyleSheet("text-align: left;\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.refresh_button.setIcon(icon5)
        self.refresh_button.setIconSize(QtCore.QSize(30, 30))
        self.refresh_button.setFlat(True)
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.clicked.connect(self.restart_app)
       # self.refresh_button.hide()
        self.verticalLayout.addWidget(self.refresh_button)
        self.delete_button = QtWidgets.QPushButton(parent=self.widget)
        self.delete_button.setMinimumSize(QtCore.QSize(90, 30))
        self.delete_button.setStyleSheet("text-align: left;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/trash.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delete_button.setIcon(icon6)
        self.delete_button.setIconSize(QtCore.QSize(30, 30))
        self.delete_button.setFlat(True)
        self.delete_button.setObjectName("delete_button")
        self.delete_button.clicked.connect(self.delete_prompt)
        self.verticalLayout.addWidget(self.delete_button)
        self.home_button = QtWidgets.QPushButton(parent=self.widget)
        self.home_button.setMinimumSize(QtCore.QSize(0, 30))
        self.home_button.setStyleSheet("text-align: left;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.home_button.setIcon(icon7)
        self.home_button.setIconSize(QtCore.QSize(30, 30))
        self.home_button.setFlat(True)
        self.home_button.setObjectName("home_button")
        self.home_button.clicked.connect(self.open_home_page)
        self.home_button.clicked.connect(Customers.close)
        self.verticalLayout.addWidget(self.home_button)
        self.sidebar.addTab(self.tab, "")
        self.gridLayout.addWidget(self.sidebar, 0, 0, 1, 1)
        Customers.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Customers)
        self.statusbar.setObjectName("statusbar")
        Customers.setStatusBar(self.statusbar)

        self.retranslateUi(Customers)
        self.sidebar.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Customers)

    def retranslateUi(self, Customers):
        _translate = QtCore.QCoreApplication.translate
        Customers.setWindowTitle(_translate("Customers", "Customers"))
        self.new_customer_button.setText(_translate("Customers", "New "))
        self.create_ro_button.setText(_translate("Customers", "Create RO"))
        self.search_button.setText(_translate("Customers", "Search"))
        self.print_button.setText(_translate("Customers", "Print"))
        self.refresh_button.setText(_translate("Customers", "Refresh"))
        self.delete_button.setText(_translate("Customers", "Delete"))
        self.home_button.setText(_translate("Customers", "Home"))
        self.sidebar.setTabText(self.sidebar.indexOf(self.tab), _translate("Customers", "Tab 1"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Customers = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Customers)
    Customers.show()
    sys.exit(app.exec())
