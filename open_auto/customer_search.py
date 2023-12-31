from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
import mysql.connector
import confirm_delete
import customer_info
from database.customers import customers_db


class Ui_Form(object):
    def search_customer(self):
        search_name = self.search_edit.text()
        for row in range(self.ro_search_list.rowCount()):
            item = self.ro_search_list.item(row, 0)
            self.ro_search_list.setRowHidden(row, search_name not in item.text())

    def delete_prompt(self):
        self.delete_page = QtWidgets.QWidget()
        self.delete_page_ui = confirm_delete.Ui_confirm_delete()
        self.delete_page_ui.setupUi(self.delete_page)
        selected_row = self.ro_search_list.currentRow()
        selected_column = self.ro_search_list.currentColumn()
        selected_data = []
        selected_name = self.ro_search_list.itemAt(selected_row, selected_column)
        for column in range(self.ro_search_list.model().columnCount()):
            index = self.ro_search_list.model().index(selected_row, column)
            selected_data.append(index.data())
        self.delete_page_ui.customer_label.setText("Delete %s From Database?" % selected_data[0])
        self.delete_page.show()
        self.delete_page_ui.yes_delete.clicked.connect(self.delete_customer)

    def delete_customer(self):
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        selected_row = self.ro_search_list.currentRow()
        selected_column = self.ro_search_list.currentColumn()
        selected_data = []
        selected_name = self.ro_search_list.itemAt(selected_row, selected_column)
        for column in range(self.ro_search_list.model().columnCount()):
            index = self.ro_search_list.model().index(selected_row, column)
            selected_data.append(index.data())
        conn = my_db.cursor()
        delete_customer_row = "DELETE FROM customers WHERE name = %s AND address = %s"
        conn.execute(delete_customer_row, (selected_data[0], selected_data[1]))
        my_db.commit()
        my_db.close()
        self.ro_search_list.removeRow(selected_row)

    def highlight_row(self):
        self.ro_search_list.selectRow(self.ro_search_list.currentRow())
    def update_customer_credentials(self):
        self.show_new_customer_page = QtWidgets.QWidget()
        self.show_new_customer_page_ui = customer_info.Ui_Form()
        self.show_new_customer_page_ui.setupUi(self.show_new_customer_page)
        self.show_new_customer_page.show()
        if self.ro_search_list.cellDoubleClicked:
            self.show_new_customer_page.setWindowTitle("Edit Customer")
            self.show_new_customer_page_ui.save_create_button.hide()
        selected_row = self.ro_search_list.currentRow()
        selected_column = self.ro_search_list.currentColumn()
        selected_data = []
        for column in range(self.ro_search_list.model().columnCount()):
            index = self.ro_search_list.model().index(selected_row, column)
            selected_data.append(index.data())
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()
        query = """SELECT * FROM customers WHERE(name = %s and phone = %s)"""
        name_data = [selected_data[0], selected_data[5]]
        conn.execute(query, name_data)
        result = conn.fetchall()
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





    def setupUi(self, Form):
        Form.setObjectName("Find Customer")
        Form.resize(1280, 720)
#        Form.setStyleSheet("  background-color: #504F4F;")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(903, 68, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 2)
        self.winter_auto_logo = QtWidgets.QLabel(parent=Form)
        self.winter_auto_logo.setText("")
        self.winter_auto_logo.setPixmap(QtGui.QPixmap("/home/fred/PycharmProjects/OpenAuto/ui_files/designer_files/../winter_auto.png"))
        self.winter_auto_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.winter_auto_logo.setObjectName("winter_auto_logo")
        self.gridLayout.addWidget(self.winter_auto_logo, 0, 2, 2, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_label = QtWidgets.QLabel(parent=Form)
        self.search_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search_label.setFont(font)
        self.search_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.search_label.setObjectName("search_label")
        self.verticalLayout.addWidget(self.search_label)
        self.search_edit = QtWidgets.QLineEdit(parent=Form)
        self.search_edit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search_edit.setFont(font)
        self.search_edit.setStyleSheet("background-color: #929191;")
        self.search_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.search_edit.setObjectName("search_edit")
        self.search_edit.setPlaceholderText("Search Name... Case Sensitive")
        self.search_edit.textChanged.connect(self.search_customer)
        self.verticalLayout.addWidget(self.search_edit)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(447, 68, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.ro_search_list = QtWidgets.QTableWidget(parent=Form)
        self.ro_search_list.setColumnCount(8)
        header_names = ("Name", "Address", "City", "State", "Zip", "Phone", "Alt", "Email")
        self.ro_search_list.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ro_search_list.setHorizontalHeaderLabels(header_names)
        self.ro_search_list.setObjectName("ro_search_list")
        self.ro_search_list.setRowCount(customers_db.row_count(self))
        self.ro_search_list.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.ro_search_list.setShowGrid(False)
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
            self.ro_search_list.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ro_search_list.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ro_search_list.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ro_search_list.setItem(table_row, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ro_search_list.setItem(table_row, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ro_search_list.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ro_search_list.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ro_search_list.setItem(table_row, 7, QtWidgets.QTableWidgetItem(row[7]))

            table_row += 1
        self.ro_search_list.cellDoubleClicked.connect(self.update_customer_credentials)
        self.ro_search_list.cellClicked.connect(self.highlight_row)
        Form.setFocus()
        self.gridLayout.addWidget(self.ro_search_list, 2, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(1081, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.abort_button = QtWidgets.QPushButton(parent=Form)
        self.abort_button.setStyleSheet("text-align: center;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.abort_button.setIcon(icon)
        self.abort_button.setIconSize(QtCore.QSize(30, 30))
        self.abort_button.setAutoRepeatDelay(100)
        self.abort_button.setFlat(True)
        self.abort_button.setObjectName("abort_button")
        self.abort_button.clicked.connect(self.delete_prompt)
        self.horizontalLayout.addWidget(self.abort_button)
        self.ok_button = QtWidgets.QPushButton(parent=Form)
        self.ok_button.setStyleSheet("text-align: center;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ok_button.setIcon(icon1)
        self.ok_button.setIconSize(QtCore.QSize(30, 30))
        self.ok_button.setFlat(True)
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(self.update_customer_credentials)
        self.horizontalLayout.addWidget(self.ok_button)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Find Customer"))
        self.search_label.setText(_translate("Form", "Search Name"))
        self.abort_button.setText(_translate("Form", "Delete"))
        self.ok_button.setText(_translate("Form", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
