from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from database.customers.customers_db import row_count

import vehicle_add
import edit_customer




class Ui_create_ro(object):
    def search_vehicle(self):
        search_vehicle = self.vehicle_line_edit.text()
        for row in range(self.vehicle_table.rowCount()):
            item = self.vehicle_table.item(row, 0)
            self.vehicle_table.setRowHidden(row, search_vehicle not in item.text())
            self.customer_table.setRowHidden(row, search_vehicle not in item.text())

    def customer_search(self):
        search_customer = self.customer_line_edit.text()
        for row in range(self.customer_table.rowCount()):
            item = self.customer_table.item(row, 0) or self.customer_table.item(row, 1)
            self.customer_table.setRowHidden(row, search_customer not in item.text())
            self.vehicle_table.setRowHidden(row, search_customer not in item.text())

    def update_customer_credentials(self):
            self.show_edit_customer_page = QtWidgets.QWidget()
            self.show_edit_customer_page_ui = edit_customer.Ui_create_customer_form()
            self.show_edit_customer_page_ui.setupUi(self.show_edit_customer_page)
            self.show_edit_customer_page.show()
            if self.customer_table.cellDoubleClicked:
                self.show_edit_customer_page.setWindowTitle("Edit Customer")
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
            name_phone = [selected_data[0], selected_data[1]]
            conn.execute(query, name_phone)
            result = conn.fetchall()

            print(selected_data)
            for row in result:
                self.show_edit_customer_page_ui.name_line.setText(row[0])
                self.show_edit_customer_page_ui.address_line.setText(row[1])
                self.show_edit_customer_page_ui.city_line.setText(row[2])
                self.show_edit_customer_page_ui.state_line.setText(row[3])
                self.show_edit_customer_page_ui.zipcode_line.setText(row[4])
                self.show_edit_customer_page_ui.phone_line.setText(row[5])
                self.show_edit_customer_page_ui.alt_name.setItemText(0, row[7])
                self.show_edit_customer_page_ui.alt_line.setText(row[6])
                self.show_edit_customer_page_ui.email_line.setText(row[8])
                print(self.show_edit_customer_page_ui.alt_name.currentText())
            my_db.close()
    def update_vehicle(self):
        self.change_vehicle = QtWidgets.QWidget()
        self.change_vehicle_ui = vehicle_add.Ui_Form()
        self.change_vehicle_ui.setupUi(self.change_vehicle)
        self.change_vehicle.show()
        self.change_vehicle.setWindowTitle("Edit Vehicle")
        selected_row = self.vehicle_table.currentRow()
        selected_column = self.vehicle_table.currentColumn()
        selected_data = []
        selected_vehicle = self.vehicle_table.itemAt(selected_row, selected_column)
        for column in range(self.vehicle_table.model().columnCount()):
            index = self.vehicle_table.model().index(selected_row, column)
            selected_data.append(index.data())
        year = int(selected_data[0])
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()
        find_vehicle = """SELECT * FROM vehicles WHERE year = %s and make = %s and model = %s"""
        vh_data = [selected_data[0], selected_data[1], selected_data[2]]
        conn.execute(find_vehicle, vh_data)
        result = conn.fetchall()
        for row in result:
            self.change_vehicle_ui.vin_line.setText(row[1])
            self.change_vehicle_ui.year_line.setText(row[2])
            self.change_vehicle_ui.make_line.setText(row[3])
            self.change_vehicle_ui.model_line.setText(row[4])
            self.change_vehicle_ui.engine_line.setText(row[5])
            self.change_vehicle_ui.trim_line.setText(row[6])
        my_db.close()


    def highlight_vehicle(self):
        self.vehicle_table.selectRow(self.vehicle_table.currentRow())
        self.customer_table.selectRow(self.vehicle_table.currentRow())

    def highlight_customer(self):
        self.customer_table.selectRow(self.customer_table.currentRow())
        self.vehicle_table.selectRow(self.customer_table.currentRow())
        self.new_vehicle_button.show()

    def scroll_bars(self, index):
        self.customer_table.verticalScrollBar().setValue(index)
        self.vehicle_table.verticalScrollBar().setValue(index)

    def open_vehicle_add(self):
        self.show_vehicle_add = QtWidgets.QWidget()
        self.show_vehicle_add_ui = vehicle_add.Ui_Form()
        self.show_vehicle_add_ui.setupUi(self.show_vehicle_add)
        self.show_vehicle_add.show()




    def setupUi(self, create_ro):
        create_ro.setObjectName("create_ro")
        create_ro.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        create_ro.setWindowIcon(icon)
#        create_ro.setStyleSheet("background-color: #504F4F;\n"
#"")
        self.gridLayout = QtWidgets.QGridLayout(create_ro)
        self.gridLayout.setObjectName("gridLayout")
        self.customer_states_label = QtWidgets.QLabel(parent=create_ro)
        self.customer_states_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customer_states_label.setFont(font)
        self.customer_states_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_states_label.setObjectName("customer_states_label")
        self.gridLayout.addWidget(self.customer_states_label, 1, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.customer_button = QtWidgets.QPushButton(parent=create_ro)
        self.customer_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.customer_button.setIcon(icon1)
        self.customer_button.setIconSize(QtCore.QSize(30, 30))
        self.customer_button.setFlat(True)
        self.customer_button.setObjectName("customer_button")
        self.verticalLayout.addWidget(self.customer_button)
        self.customer_label = QtWidgets.QLabel(parent=create_ro)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customer_label.setFont(font)
        self.customer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_label.setObjectName("customer_label")
        self.verticalLayout.addWidget(self.customer_label)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.customer_line_edit = QtWidgets.QLineEdit(parent=create_ro)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.customer_line_edit.setFont(font)
        self.customer_line_edit.setStyleSheet("text-align: center;")
        self.customer_line_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_line_edit.setObjectName("customer_line_edit")
        self.customer_line_edit.textChanged.connect(self.customer_search)
        self.customer_line_edit.setPlaceholderText("Search Name... Case Sensitive")
        self.verticalLayout_3.addWidget(self.customer_line_edit)
        header_names = ("People", "Phone")
        self.customer_table = QtWidgets.QTableWidget(parent=create_ro)
        self.customer_table.setMinimumSize(QtCore.QSize(500, 265))
        self.customer_table.setObjectName("customer_table")
        self.customer_table.setColumnCount(2)
        self.customer_table.setRowCount(row_count(self))
        self.customer_table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.customer_table.setHorizontalHeaderLabels(header_names)
        self.customer_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()
        tables_populate = """SELECT * FROM customers INNER JOIN vehicles ON
                    customers.customer_id = vehicles.vehicle_id ORDER BY customers.name"""
        conn.execute(tables_populate)
        table_row = 0
        result = conn.fetchall()

        for row in result:
            self.customer_table.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.customer_table.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[5]))
            table_row += 1
        self.customer_table.cellClicked.connect(self.highlight_customer)
        self.customer_table.cellDoubleClicked.connect(self.update_customer_credentials)
        self.customer_table.verticalScrollBar().valueChanged.connect(self.scroll_bars)
        self.verticalLayout_3.addWidget(self.customer_table)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.new_vehicle_button = QtWidgets.QPushButton(parent=create_ro)
        self.new_vehicle_button.setText("Add New Vehicle")
        self.new_vehicle_button.hide()
        self.vehicle_button = QtWidgets.QPushButton(parent=create_ro)
        self.new_vehicle_button.clicked.connect(self.open_vehicle_add)
        self.vehicle_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/car.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.vehicle_button.setIcon(icon2)
        self.vehicle_button.setIconSize(QtCore.QSize(30, 30))
        self.vehicle_button.setFlat(True)
        self.vehicle_button.setObjectName("vehicle_button")
        self.verticalLayout_2.addWidget(self.new_vehicle_button)
        self.verticalLayout_2.addWidget(self.vehicle_button)
        self.vehicle_label = QtWidgets.QLabel(parent=create_ro)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vehicle_label.setFont(font)
        self.vehicle_label.setStyleSheet("align: center;")
        self.vehicle_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vehicle_label.setObjectName("vehicle_label")
        self.verticalLayout_2.addWidget(self.vehicle_label)
        self.vehicle_line_edit = QtWidgets.QLineEdit(parent=create_ro)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.vehicle_line_edit.setFont(font)
        self.vehicle_line_edit.setStyleSheet("text-align: center;")
        self.vehicle_line_edit.setObjectName("vehicle_line_edit")
        self.vehicle_line_edit.textChanged.connect(self.search_vehicle)
        self.vehicle_line_edit.setPlaceholderText("Search Year")
        self.verticalLayout_2.addWidget(self.vehicle_line_edit)
        self.vehicle_table = QtWidgets.QTableWidget(parent=create_ro)
        self.vehicle_table.setMinimumSize(QtCore.QSize(500, 265))
        self.vehicle_table.setObjectName("vehicle_table")
        self.vehicle_table.setColumnCount(3)
        self.vehicle_table.setRowCount(row_count(self))
        self.vehicle_table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.vehicle_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.vehicle_table.cellDoubleClicked.connect(self.update_vehicle)
        self.vehicle_table.verticalScrollBar().valueChanged.connect(self.scroll_bars)
        header_names = ("Year", "Make", "Model")
        self.vehicle_table.setHorizontalHeaderLabels(header_names)
        vehicle_table_row = 0
        for row in result:
            self.vehicle_table.setItem(vehicle_table_row, 0, QtWidgets.QTableWidgetItem(row[12]))
            self.vehicle_table.setItem(vehicle_table_row, 1, QtWidgets.QTableWidgetItem(row[13]))
            self.vehicle_table.setItem(vehicle_table_row, 2, QtWidgets.QTableWidgetItem(row[14]))
            vehicle_table_row += 1
        self.verticalLayout_2.addWidget(self.vehicle_table)
        self.vehicle_table.cellClicked.connect(self.highlight_vehicle)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 219, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 2, 2, 1)
        self.customer_states = QtWidgets.QTextEdit(parent=create_ro)
        self.customer_states.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.customer_states.setFont(font)
        self.customer_states.setObjectName("customer_states")
        self.gridLayout.addWidget(self.customer_states, 2, 0, 2, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.abort_button = QtWidgets.QPushButton(parent=create_ro)
        self.abort_button.setMinimumSize(QtCore.QSize(30, 30))
        self.abort_button.setStyleSheet("text-align: center;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.abort_button.setIcon(icon3)
        self.abort_button.setIconSize(QtCore.QSize(30, 30))
        self.abort_button.setFlat(True)
        self.abort_button.setObjectName("abort_button")
        self.abort_button.clicked.connect(create_ro.close)
        self.horizontalLayout.addWidget(self.abort_button)
        self.save_button = QtWidgets.QPushButton(parent=create_ro)
        self.save_button.setMinimumSize(QtCore.QSize(30, 30))
        self.save_button.setStyleSheet("text-align: center;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.save_button.setIcon(icon4)
        self.save_button.setIconSize(QtCore.QSize(30, 30))
        self.save_button.setFlat(True)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.winter_auto_logo = QtWidgets.QLabel(parent=create_ro)
        self.winter_auto_logo.setMinimumSize(QtCore.QSize(150, 0))
        self.winter_auto_logo.setText("")
        self.winter_auto_logo.setPixmap(QtGui.QPixmap("../ui_files/winter_auto.png"))
        self.winter_auto_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.winter_auto_logo.setObjectName("winter_auto_logo")
        self.gridLayout.addWidget(self.winter_auto_logo, 0, 2, 1, 1)

        self.retranslateUi(create_ro)
        QtCore.QMetaObject.connectSlotsByName(create_ro)

    def retranslateUi(self, create_ro):
        _translate = QtCore.QCoreApplication.translate
        create_ro.setWindowTitle(_translate("create_ro", "Create Ro"))
        self.customer_states_label.setText(_translate("create_ro", "Customer States"))
        self.customer_label.setText(_translate("create_ro", "Customer"))
        self.vehicle_label.setText(_translate("create_ro", "Vehicle"))
        self.abort_button.setText(_translate("create_ro", "Abort"))
        self.save_button.setText(_translate("create_ro", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_ro = QtWidgets.QWidget()
    ui = Ui_create_ro()
    ui.setupUi(create_ro)
    create_ro.show()
    sys.exit(app.exec())
