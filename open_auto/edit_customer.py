from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
import cannot_delete_warning


class Ui_create_customer_form(object):

    def edit_customer(self):
        self.show_cant_edit = QtWidgets.QWidget()
        self.show_cant_edit_ui = cannot_delete_warning.Ui_cant_delete()
        self.show_cant_edit_ui.setupUi(self.show_cant_edit)
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()

        customers_attributes = (self.name_line.text(), self.address_line.text(), self.city_line.text(),
                                self.state_line.text(), self.zipcode_line.text(), self.phone_line.text(),
                                self.alt_line.text(), self.alt_name.currentText(), self.email_line.text())
        print(customers_attributes)
        add_options = """UPDATE CUSTOMERS.customers SET name= %s, address = %s, city = %s, state = %s, zip = %s, 
                         phone = %s, alt_phone = %s, alt_name = %s, email = %s WHERE(name = %s and phone = %s)"""

        conn.execute(add_options, (customers_attributes[0], customers_attributes[1],
                                       customers_attributes[2], customers_attributes[3], customers_attributes[4],
                                       customers_attributes[5], customers_attributes[6], customers_attributes[7],
                                        customers_attributes[8], customers_attributes[0], customers_attributes[5]))

        my_db.commit()
        my_db.close()






    def setupUi(self, create_customer_form):
        create_customer_form.setObjectName("create_customer_form")
        create_customer_form.resize(606, 663)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/fred/PycharmProjects/OpenAuto/ui_files/designer_files/Images/winter_auto.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("/home/fred/PycharmProjects/OpenAuto/ui_files/designer_files/Images/winter_auto.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        create_customer_form.setWindowIcon(icon)
        create_customer_form.setStyleSheet("")
        self.formLayout = QtWidgets.QFormLayout(create_customer_form)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.address_line = QtWidgets.QLineEdit(parent=create_customer_form)
        self.address_line.setMinimumSize(QtCore.QSize(0, 40))
        self.address_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.address_line.setFont(font)
        self.address_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.address_line.setObjectName("address_line")
        self.gridLayout.addWidget(self.address_line, 1, 3, 1, 1)
        self.phone_label = QtWidgets.QLabel(parent=create_customer_form)
        self.phone_label.setObjectName("phone_label")
        self.gridLayout.addWidget(self.phone_label, 5, 0, 1, 1)
        self.email_line = QtWidgets.QLineEdit(parent=create_customer_form)
        self.email_line.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.email_line.setFont(font)
        self.email_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.email_line.setObjectName("email_line")
        self.gridLayout.addWidget(self.email_line, 7, 3, 1, 1)
        self.email_label = QtWidgets.QLabel(parent=create_customer_form)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 7, 0, 1, 1)
        self.state_line = QtWidgets.QLineEdit(parent=create_customer_form)
        self.state_line.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.state_line.setFont(font)
        self.state_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.state_line.setObjectName("state_line")
        self.state_line.setMaxLength(2)
        self.gridLayout.addWidget(self.state_line, 3, 3, 1, 1)
        self.name_label = QtWidgets.QLabel(parent=create_customer_form)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.name_line = QtWidgets.QLineEdit(parent=create_customer_form)
        self.name_line.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_line.setFont(font)
        self.name_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_line.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.name_line, 0, 3, 1, 1)
        self.city_label = QtWidgets.QLabel(parent=create_customer_form)
        self.city_label.setObjectName("city_label")
        self.gridLayout.addWidget(self.city_label, 2, 0, 1, 1)
        self.address_label = QtWidgets.QLabel(parent=create_customer_form)
        self.address_label.setMinimumSize(QtCore.QSize(60, 0))
        self.address_label.setStyleSheet("text-align: left;")
        self.address_label.setObjectName("address_label")
        self.gridLayout.addWidget(self.address_label, 1, 0, 1, 1)
        self.zipcode_line = QtWidgets.QLineEdit(parent=create_customer_form)
        self.zipcode_line.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.zipcode_line.setFont(font)
        self.zipcode_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.zipcode_line.setObjectName("zipcode_line")
        self.gridLayout.addWidget(self.zipcode_line, 4, 3, 1, 1)
        self.phone_line = QtWidgets.QLineEdit(parent=create_customer_form)
        self.phone_line.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.phone_line.setFont(font)
        self.phone_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.phone_line.setObjectName("phone_line")
        self.gridLayout.addWidget(self.phone_line, 5, 3, 1, 1)
        self.alt_label = QtWidgets.QLabel(parent=create_customer_form)
        self.alt_label.setObjectName("alt_label")
        self.gridLayout.addWidget(self.alt_label, 6, 0, 1, 1)
        self.city_line = QtWidgets.QLineEdit(parent=create_customer_form)
        self.city_line.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.city_line.setFont(font)
        self.city_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.city_line.setObjectName("city_line")
        self.gridLayout.addWidget(self.city_line, 2, 3, 1, 1)
        self.state_label = QtWidgets.QLabel(parent=create_customer_form)
        self.state_label.setObjectName("state_label")
        self.gridLayout.addWidget(self.state_label, 3, 0, 1, 1)
        self.zipcode_label = QtWidgets.QLabel(parent=create_customer_form)
        self.zipcode_label.setObjectName("zipcode_label")
        self.gridLayout.addWidget(self.zipcode_label, 4, 0, 1, 1)
        self.alt_name = QtWidgets.QComboBox(parent=create_customer_form)
        self.alt_name.setMinimumSize(QtCore.QSize(120, 40))
        self.alt_name.setObjectName("alt_name")
        self.alt_name.setEditable(True)
        name_items = ["Work", "Cell", "Home", "Relative"]
        self.alt_name.addItems(name_items)
        self.gridLayout.addWidget(self.alt_name, 6, 1, 1, 1)
        self.alt_line = QtWidgets.QLineEdit(parent=create_customer_form)
        self.alt_line.setMinimumSize(QtCore.QSize(0, 40))
        self.alt_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.alt_line.setFont(font)
        self.alt_line.setObjectName("alt_line")
        self.gridLayout.addWidget(self.alt_line, 6, 3, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.abort_button = QtWidgets.QPushButton(parent=create_customer_form)
        self.abort_button.setStyleSheet("text-align: left;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/fred/PycharmProjects/OpenAuto/ui_files/designer_files/../Images/Icons/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.abort_button.setIcon(icon1)
        self.abort_button.setIconSize(QtCore.QSize(30, 30))
        self.abort_button.setFlat(True)
        self.abort_button.setObjectName("abort_button")
        self.abort_button.clicked.connect(create_customer_form.close)
        self.horizontalLayout.addWidget(self.abort_button)
        self.save_button = QtWidgets.QPushButton(parent=create_customer_form)
        self.save_button.setStyleSheet("text-align: left;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/fred/PycharmProjects/OpenAuto/ui_files/designer_files/../Images/Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setIconSize(QtCore.QSize(30, 30))
        self.save_button.setAutoRepeatDelay(100)
        self.save_button.setFlat(True)
        self.save_button.clicked.connect(self.edit_customer)
        self.save_button.clicked.connect(create_customer_form.close)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.label_8 = QtWidgets.QLabel(parent=create_customer_form)
        self.label_8.setEnabled(True)
        self.label_8.setMaximumSize(QtCore.QSize(200, 50))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("/home/fred/PycharmProjects/OpenAuto/ui_files/designer_files/Images/winter_auto.png"))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 125, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 125, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(120, 125, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem2)

        self.retranslateUi(create_customer_form)
        QtCore.QMetaObject.connectSlotsByName(create_customer_form)

    def retranslateUi(self, create_customer_form):
        _translate = QtCore.QCoreApplication.translate
        create_customer_form.setWindowTitle(_translate("create_customer_form", "Edit Customer"))
        self.phone_label.setText(_translate("create_customer_form", "Phone"))
        self.email_label.setText(_translate("create_customer_form", "Email"))
        self.name_label.setText(_translate("create_customer_form", "Name"))
        self.city_label.setText(_translate("create_customer_form", "City"))
        self.address_label.setText(_translate("create_customer_form", "Address"))
        self.alt_label.setText(_translate("create_customer_form", "Alt"))
        self.state_label.setText(_translate("create_customer_form", "State"))
        self.zipcode_label.setText(_translate("create_customer_form", "Zip"))
        self.abort_button.setText(_translate("create_customer_form", "Abort"))
        self.save_button.setText(_translate("create_customer_form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_customer_form = QtWidgets.QWidget()
    ui = Ui_create_customer_form()
    ui.setupUi(create_customer_form)
    create_customer_form.show()
    create_customer_form.setFocus()
    sys.exit(app.exec())
