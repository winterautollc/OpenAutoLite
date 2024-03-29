import io
import json
from PyQt6 import QtCore, QtGui, QtWidgets
from pyvin import VIN
import mysql.connector
import new_ro

class Ui_Form(object):


    def save_vehicle(self):
        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()

        with open('../database/customers/cid.json', 'r') as outfile:
            customer_id = json.load(outfile)

        find_cid = """SELECT customer_id from customers where name = %s and phone = %s"""
        conn.execute(find_cid, customer_id)
        result = conn.fetchone()
        print(result)
        vehicle_attributes = (self.vin_line.text(), self.year_line.text(), self.make_line.text(),
                              self.model_line.text(), self.engine_line.text(), self.trim_line.text(), result[0])
        new_vehicle = """INSERT INTO vehicles ( vin, year, make, model, engine, trim, customer_id)
                                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        conn.execute(new_vehicle, vehicle_attributes)
        my_db.commit()
        my_db.close()
    def update_vehicle(self):


        my_db = mysql.connector.connect(

            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()
        with open('../database/vehicles/vid.json', 'r') as outfile:
            vehicle_id = json.load(outfile)
        find_id = """SELECT vehicle_id, customer_id from vehicles where vin = %s and year = %s and make = %s 
                and model = %s"""
        conn.execute(find_id, vehicle_id)
        result = conn.fetchone()
        print(result)
        change_vehicle = """UPDATE vehicles SET vin = %s, year = %s, make = %s, model = %s, engine = %s, trim = %s
                            WHERE(vehicle_id = %s and customer_id = %s)"""
        vehicle_attributes = [self.vin_line.text(), self.year_line.text(), self.make_line.text(),
                              self.model_line.text(), self.engine_line.text(), self.trim_line.text()]
        conn.execute(change_vehicle, (vehicle_attributes[0], vehicle_attributes[1], vehicle_attributes[2],
                                      vehicle_attributes[3],
                                      vehicle_attributes[4], vehicle_attributes[5], result[0], result[1]))
        my_db.commit()
        my_db.close()

    def vin_search(self):
        try:
            self.vin = VIN(self.vin_line.text())
            self.year_line.setText(self.vin.ModelYear)
            self.make_line.setText(self.vin.Make)
            self.model_line.setText(self.vin.Model)
            self.engine_line.setText(self.vin.DisplacementL)
            self.trim_line.setText(self.vin.Trim)
        except:
            self.vin_line.setText("Please choose a proper vin number")


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/car.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.vin_label = QtWidgets.QLabel(parent=Form)
        self.vin_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vin_label.setFont(font)
        self.vin_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vin_label.setObjectName("vin_label")
        self.gridLayout.addWidget(self.vin_label, 0, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.year_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.year_label.setFont(font)
        self.year_label.setStyleSheet("text-align: center;")
        self.year_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.year_label.setObjectName("year_label")
        self.horizontalLayout_4.addWidget(self.year_label)
        self.year_line = QtWidgets.QLineEdit(parent=Form)
        self.year_line.setMinimumSize(QtCore.QSize(50, 30))
        self.year_line.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.year_line.setFont(font)
        self.year_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.year_line.setObjectName("year_line")
        self.horizontalLayout_4.addWidget(self.year_line)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.make_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.make_label.setFont(font)
        self.make_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.make_label.setObjectName("make_label")
        self.horizontalLayout_5.addWidget(self.make_label)
        self.make_line = QtWidgets.QLineEdit(parent=Form)
        self.make_line.setMinimumSize(QtCore.QSize(0, 30))
        self.make_line.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.make_line.setFont(font)
        self.make_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.make_line.setObjectName("make_line")
        self.horizontalLayout_5.addWidget(self.make_line)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.model_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.model_label.setFont(font)
        self.model_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.model_label.setObjectName("model_label")
        self.horizontalLayout_6.addWidget(self.model_label)
        self.model_line = QtWidgets.QLineEdit(parent=Form)
        self.model_line.setMinimumSize(QtCore.QSize(0, 30))
        self.model_line.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.model_line.setFont(font)
        self.model_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.model_line.setObjectName("model_line")
        self.horizontalLayout_6.addWidget(self.model_line)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.engine_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.engine_label.setFont(font)
        self.engine_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.engine_label.setObjectName("engine_label")
        self.horizontalLayout_3.addWidget(self.engine_label)
        self.engine_line = QtWidgets.QLineEdit(parent=Form)
        self.engine_line.setMinimumSize(QtCore.QSize(0, 30))
        self.engine_line.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.engine_line.setFont(font)
        self.engine_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.engine_line.setObjectName("engine_line")
        self.horizontalLayout_3.addWidget(self.engine_line)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.trim_label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.trim_label.setFont(font)
        self.trim_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trim_label.setObjectName("trim_label")
        self.horizontalLayout_7.addWidget(self.trim_label)
        self.trim_line = QtWidgets.QLineEdit(parent=Form)
        self.trim_line.setMinimumSize(QtCore.QSize(0, 30))
        self.trim_line.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.trim_line.setFont(font)
        self.trim_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.trim_line.setObjectName("trim_line")
        self.horizontalLayout_7.addWidget(self.trim_line)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vin_search_button = QtWidgets.QPushButton(parent=Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.vin_search_button.setIcon(icon1)
        self.vin_search_button.setIconSize(QtCore.QSize(30, 30))
        self.vin_search_button.setFlat(True)
        self.vin_search_button.setObjectName("vin_search_button")
        self.vin_search_button.clicked.connect(self.vin_search)
        self.horizontalLayout_2.addWidget(self.vin_search_button)
        self.vin_line = QtWidgets.QLineEdit(parent=Form)
        self.vin_line.setMinimumSize(QtCore.QSize(0, 35))
        self.vin_line.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.vin_line.setFont(font)
        self.vin_line.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vin_line.setObjectName("vin_line")
        self.horizontalLayout_2.addWidget(self.vin_line)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.winter_auto_logo = QtWidgets.QLabel(parent=Form)
        self.winter_auto_logo.setMaximumSize(QtCore.QSize(16777215, 200))
        self.winter_auto_logo.setText("")
        self.winter_auto_logo.setPixmap(QtGui.QPixmap("../ui_files/Images/winter_auto.png"))
        self.winter_auto_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.winter_auto_logo.setObjectName("winter_auto_logo")
        self.gridLayout.addWidget(self.winter_auto_logo, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 150, -1, 9)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.abort_button = QtWidgets.QPushButton(parent=Form)
        self.abort_button.setStyleSheet("text-align: center;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.abort_button.setIcon(icon2)
        self.abort_button.setIconSize(QtCore.QSize(30, 30))
        self.abort_button.setAutoRepeatDelay(100)
        self.abort_button.setFlat(True)
        self.abort_button.setObjectName("abort_button")
        self.abort_button.clicked.connect(Form.close)
        self.horizontalLayout.addWidget(self.abort_button)
        self.save_create_button = QtWidgets.QPushButton(parent=Form)
        self.save_create_button.setStyleSheet("text-align: center;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.save_create_button.setIcon(icon3)
        self.save_create_button.setIconSize(QtCore.QSize(30, 30))
        self.save_create_button.setFlat(True)
        self.save_create_button.clicked.connect(self.save_vehicle)
        self.save_create_button.clicked.connect(Form.close)
        self.edit_button = QtWidgets.QPushButton(parent=Form)
        self.edit_button.setStyleSheet("text-align: center;")
        self.edit_button.setIcon(icon3)
        self.edit_button.setFlat(True)
        self.edit_button.setObjectName("edit_button")
        self.edit_button.setIconSize(QtCore.QSize(30, 30))
        self.edit_button.clicked.connect(self.update_vehicle)
        self.edit_button.clicked.connect(Form.close)
        self.horizontalLayout.addWidget(self.edit_button)
        self.save_create_button.setObjectName("save_create_button")
        self.horizontalLayout.addWidget(self.save_create_button)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 800, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vehicle Search"))
        self.vin_label.setText(_translate("Form", "Search By VIN"))
        self.year_label.setText(_translate("Form", "Year"))
        self.make_label.setText(_translate("Form", "Make"))
        self.model_label.setText(_translate("Form", "Model"))
        self.engine_label.setText(_translate("Form", "Engine"))
        self.trim_label.setText(_translate("Form", "Trim"))
        self.vin_search_button.setText(_translate("Form", "VIN Search"))
        self.abort_button.setText(_translate("Form", "Abort"))
        self.save_create_button.setText(_translate("Form", "Save Vehicle"))
        self.edit_button.setText(_translate("Form", "Save Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

