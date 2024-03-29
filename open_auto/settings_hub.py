from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import mysql.connector

class Ui_Form(object):

    def upload_shop_logo(self):
        file_filter = "Image Files(*.jpg *.png *.svg)"
        logo_select = QFileDialog.getOpenFileName(
            caption="Select Image",
            filter=file_filter,
            initialFilter="Image Files(*.jpg *.png *.svg)"
        )

        shop_logo_image = QtGui.QPixmap(logo_select[0])
        if logo_select:
            self.label.setPixmap(shop_logo_image)
            self.label.move(1, 42)
            self.label.setScaledContents(True)
            
    def show_estimate_terms(self):
        self.estimate_terms_edit.show()
        self.invoice_terms_edit.hide()
        self.warranty_terms_edit.hide()

    def show_invoice_terms(self):
        self.invoice_terms_edit.show()
        self.estimate_terms_edit.hide()
        self.warranty_terms_edit.hide()

    def show_warranty_terms(self):
        self.warranty_terms_edit.show()
        self.estimate_terms_edit.hide()
        self.invoice_terms_edit.hide()
        self.warranty_checkbox.show()

    def save_settings(self):
        settings = (self.shop_name_edit.text(), self.facility_number_edit.text(), self.address_edit.text(),
                    self.city_edit.text(), self.state_edit.text(), self.zip_edit.text(),
                    self.estimate_terms_edit.toPlainText(), self.invoice_terms_edit.toPlainText(),
                    self.warranty_terms_edit.toPlainText(), self.labor_rate_edit.text(), self.parts_markup_edit.text(),
                    self.oem_markup_edit.text(), self.tire_markup_edit.text())
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="OpenAuto1",
            database="CUSTOMERS"
        )
        conn = my_db.cursor()
        save_to_db = """INSERT OR REPLACE INTO settings (shop_name, facility_number, address, city, state, zip,
                        estimate_terms, invoice_terms, warranty_terms, labor_rate, parts_markup, oem_markup, 
                        tire_markup) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
       # conn.execute(save_to_db, settings)
      #  my_db.commit()
       # my_db.close()
        print(self.estimate_terms_edit.toPlainText())

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1134, 719)
        Form.setMinimumSize(QtCore.QSize(0, 30))
#        Form.setStyleSheet("background-color: #504F4F;")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
 #       self.tabWidget.setStyleSheet("background-color: #504F4F;")
        self.tabWidget.setObjectName("tabWidget")
        self.shop_info_tab = QtWidgets.QWidget()
        self.shop_info_tab.setObjectName("shop_info_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.shop_info_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(248, 611, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 2, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.abort_button = QtWidgets.QPushButton(parent=self.shop_info_tab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.abort_button.setIcon(icon)
        self.abort_button.setIconSize(QtCore.QSize(30, 30))
        self.abort_button.setFlat(True)
        self.abort_button.setObjectName("abort_button")
        self.abort_button.clicked.connect(Form.close)
        self.horizontalLayout_7.addWidget(self.abort_button)
        self.save_button = QtWidgets.QPushButton(parent=self.shop_info_tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.save_button.setIcon(icon1)
        self.save_button.setIconSize(QtCore.QSize(30, 30))
        self.save_button.setFlat(True)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_7.addWidget(self.save_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(909, 38, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(238, 301, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.shop_logo_label = QtWidgets.QLabel(parent=self.shop_info_tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.shop_logo_label.setFont(font)
        self.shop_logo_label.setObjectName("shop_logo_label")
        self.horizontalLayout_8.addWidget(self.shop_logo_label)
        self.upload_button = QtWidgets.QPushButton(parent=self.shop_info_tab)
        self.upload_button.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.upload_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.upload_button.setIcon(icon2)
        self.upload_button.setIconSize(QtCore.QSize(30, 30))
        self.upload_button.setObjectName("upload_button")
        self.upload_button.clicked.connect(self.upload_shop_logo)
        self.horizontalLayout_8.addWidget(self.upload_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.label = QtWidgets.QLabel(parent=self.shop_info_tab)
        self.label.setMinimumSize(QtCore.QSize(236, 254))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.shop_name_label = QtWidgets.QLabel(parent=self.shop_info_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.shop_name_label.setFont(font)
        self.shop_name_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.shop_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.shop_name_label.setObjectName("shop_name_label")
        self.verticalLayout.addWidget(self.shop_name_label)
        self.shop_name_edit = QtWidgets.QLineEdit(parent=self.shop_info_tab)
        self.shop_name_edit.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.shop_name_edit.setFont(font)
        self.shop_name_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.shop_name_edit.setObjectName("shop_name_edit")
        self.verticalLayout.addWidget(self.shop_name_edit)
        self.facility_number_label = QtWidgets.QLabel(parent=self.shop_info_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.facility_number_label.setFont(font)
        self.facility_number_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.facility_number_label.setObjectName("facility_number_label")
        self.verticalLayout.addWidget(self.facility_number_label)
        self.facility_number_edit = QtWidgets.QLineEdit(parent=self.shop_info_tab)
        self.facility_number_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.facility_number_edit.setFont(font)
        self.facility_number_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.facility_number_edit.setObjectName("facility_number_edit")
        self.verticalLayout.addWidget(self.facility_number_edit)
        self.address_label = QtWidgets.QLabel(parent=self.shop_info_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.address_label.setFont(font)
        self.address_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.address_label.setObjectName("address_label")
        self.verticalLayout.addWidget(self.address_label)
        self.address_edit = QtWidgets.QLineEdit(parent=self.shop_info_tab)
        self.address_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.address_edit.setFont(font)
        self.address_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.address_edit.setObjectName("address_edit")
        self.verticalLayout.addWidget(self.address_edit)
        self.city_label = QtWidgets.QLabel(parent=self.shop_info_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.city_label.setFont(font)
        self.city_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.city_label.setObjectName("city_label")
        self.verticalLayout.addWidget(self.city_label)
        self.city_edit = QtWidgets.QLineEdit(parent=self.shop_info_tab)
        self.city_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.city_edit.setFont(font)
        self.city_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.city_edit.setObjectName("city_edit")
        self.verticalLayout.addWidget(self.city_edit)
        self.state_label = QtWidgets.QLabel(parent=self.shop_info_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.state_label.setFont(font)
        self.state_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.state_label.setObjectName("state_label")
        self.verticalLayout.addWidget(self.state_label)
        self.state_edit = QtWidgets.QLineEdit(parent=self.shop_info_tab)
        self.state_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.state_edit.setFont(font)
        self.state_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.state_edit.setObjectName("state_edit")
        self.verticalLayout.addWidget(self.state_edit)
        self.zip_label = QtWidgets.QLabel(parent=self.shop_info_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.zip_label.setFont(font)
        self.zip_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.zip_label.setObjectName("zip_label")
        self.verticalLayout.addWidget(self.zip_label)
        self.zip_edit = QtWidgets.QLineEdit(parent=self.shop_info_tab)
        self.zip_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.zip_edit.setFont(font)
        self.zip_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.zip_edit.setObjectName("zip_edit")
        self.verticalLayout.addWidget(self.zip_edit)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.tabWidget.addTab(self.shop_info_tab, "")
        self.terms_tab = QtWidgets.QWidget()
        self.terms_tab.setObjectName("terms_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.terms_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.terms_buttons_tab = QtWidgets.QTabWidget(parent=self.terms_tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.terms_buttons_tab.setFont(font)
        self.terms_buttons_tab.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.terms_buttons_tab.setStyleSheet("background-color: #929191;")
        self.terms_buttons_tab.setTabBarAutoHide(True)
        self.terms_buttons_tab.setObjectName("terms_buttons_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 169, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.estimate_term_button = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.estimate_term_button.setMinimumSize(QtCore.QSize(0, 50))
        self.estimate_term_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.estimate_term_button.setChecked(True)
        self.estimate_term_button.clicked.connect(self.show_estimate_terms)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/add-document.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.estimate_term_button.setIcon(icon3)
        self.estimate_term_button.setIconSize(QtCore.QSize(30, 30))
        self.estimate_term_button.setObjectName("estimate_term_button")
        self.verticalLayout_3.addWidget(self.estimate_term_button)
        self.invoice_term_button = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.invoice_term_button.setMinimumSize(QtCore.QSize(0, 50))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/document.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.invoice_term_button.setIcon(icon4)
        self.invoice_term_button.setIconSize(QtCore.QSize(30, 30))
        self.invoice_term_button.setObjectName("invoice_term_button")
        self.invoice_term_button.clicked.connect(self.show_invoice_terms)
        self.verticalLayout_3.addWidget(self.invoice_term_button)
        self.warranty_term_button = QtWidgets.QRadioButton(parent=self.layoutWidget)
        self.warranty_term_button.setMinimumSize(QtCore.QSize(0, 50))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.warranty_term_button.setIcon(icon5)
        self.warranty_term_button.setIconSize(QtCore.QSize(30, 30))
        self.warranty_term_button.setObjectName("warranty_term_button")
        self.verticalLayout_3.addWidget(self.warranty_term_button)
        self.terms_buttons_tab.addTab(self.tab, "")
        self.warranty_term_button.clicked.connect(self.show_warranty_terms)
        self.gridLayout_3.addWidget(self.terms_buttons_tab, 0, 0, 1, 1)
        self.invoice_terms_edit = QtWidgets.QTextEdit(parent=self.terms_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoice_terms_edit.sizePolicy().hasHeightForWidth())
        self.invoice_terms_edit.setSizePolicy(sizePolicy)
        self.invoice_terms_edit.setMinimumSize(QtCore.QSize(911, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.invoice_terms_edit.setFont(font)
        self.invoice_terms_edit.setObjectName("invoice_terms_edit")
        self.gridLayout_3.addWidget(self.invoice_terms_edit, 0, 1, 2, 2)
        spacerItem3 = QtWidgets.QSpacerItem(174, 249, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 4, 1)
        spacerItem4 = QtWidgets.QSpacerItem(732, 238, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 1, 3, 1)
        self.warranty_checkbox = QtWidgets.QCheckBox(parent=self.terms_tab)
        self.warranty_checkbox.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.warranty_checkbox.setFont(font)
        self.warranty_checkbox.setObjectName("warranty_checkbox")
        self.gridLayout_3.addWidget(self.warranty_checkbox, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(158, 149, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.abort_button_2 = QtWidgets.QPushButton(parent=self.terms_tab)
        self.abort_button_2.setMinimumSize(QtCore.QSize(0, 30))
        self.abort_button_2.setIcon(icon)
        self.abort_button_2.setIconSize(QtCore.QSize(30, 30))
        self.abort_button_2.setFlat(True)
        self.abort_button_2.setObjectName("abort_button_2")
        self.abort_button_2.clicked.connect(Form.close)
        self.horizontalLayout.addWidget(self.abort_button_2)
        self.save_button_2 = QtWidgets.QPushButton(parent=self.terms_tab)
        self.save_button_2.setMinimumSize(QtCore.QSize(0, 30))
        self.save_button_2.setIcon(icon1)
        self.save_button_2.setIconSize(QtCore.QSize(30, 30))
        self.save_button_2.setFlat(True)
        self.save_button_2.setObjectName("save_button_2")
        self.horizontalLayout.addWidget(self.save_button_2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.warranty_terms_edit = QtWidgets.QTextEdit(parent=self.terms_tab)
        self.warranty_terms_edit.setGeometry(QtCore.QRect(190, 10, 911, 400))
        self.warranty_terms_edit.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.warranty_terms_edit.setFont(font)
        self.warranty_terms_edit.setObjectName("warranty_terms_edit")
        self.estimate_terms_edit = QtWidgets.QTextEdit(parent=self.terms_tab)
        self.estimate_terms_edit.setGeometry(QtCore.QRect(190, 10, 911, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.estimate_terms_edit.setFont(font)
        self.estimate_terms_edit.setObjectName("estimate_terms_edit")
        self.tabWidget.addTab(self.terms_tab, "")
        self.taxes_tab = QtWidgets.QWidget()
        self.taxes_tab.setObjectName("taxes_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.taxes_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labor_rate_label = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.labor_rate_label.setFont(font)
        self.labor_rate_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labor_rate_label.setObjectName("labor_rate_label")
        self.verticalLayout_4.addWidget(self.labor_rate_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labor_rate_edit = QtWidgets.QLineEdit(parent=self.taxes_tab)
        self.labor_rate_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labor_rate_edit.setFont(font)
        self.labor_rate_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labor_rate_edit.setObjectName("labor_rate_edit")
        self.horizontalLayout_2.addWidget(self.labor_rate_edit)
        self.labor_rate_symbol = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.labor_rate_symbol.setFont(font)
        self.labor_rate_symbol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labor_rate_symbol.setObjectName("labor_rate_symbol")
        self.horizontalLayout_2.addWidget(self.labor_rate_symbol)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.parts_markup_label = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.parts_markup_label.setFont(font)
        self.parts_markup_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.parts_markup_label.setObjectName("parts_markup_label")
        self.verticalLayout_4.addWidget(self.parts_markup_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.parts_markup_edit = QtWidgets.QLineEdit(parent=self.taxes_tab)
        self.parts_markup_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.parts_markup_edit.setFont(font)
        self.parts_markup_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.parts_markup_edit.setObjectName("parts_markup_edit")
        self.horizontalLayout_3.addWidget(self.parts_markup_edit)
        self.parts_markup_symbol = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.parts_markup_symbol.setFont(font)
        self.parts_markup_symbol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.parts_markup_symbol.setObjectName("parts_markup_symbol")
        self.horizontalLayout_3.addWidget(self.parts_markup_symbol)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.oem_markup_label = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.oem_markup_label.setFont(font)
        self.oem_markup_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oem_markup_label.setObjectName("oem_markup_label")
        self.verticalLayout_4.addWidget(self.oem_markup_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.oem_markup_edit = QtWidgets.QLineEdit(parent=self.taxes_tab)
        self.oem_markup_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.oem_markup_edit.setFont(font)
        self.oem_markup_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oem_markup_edit.setObjectName("oem_markup_edit")
        self.horizontalLayout_4.addWidget(self.oem_markup_edit)
        self.oem_markup_symbol = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.oem_markup_symbol.setFont(font)
        self.oem_markup_symbol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oem_markup_symbol.setObjectName("oem_markup_symbol")
        self.horizontalLayout_4.addWidget(self.oem_markup_symbol)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tire_markup_label = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.tire_markup_label.setFont(font)
        self.tire_markup_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tire_markup_label.setObjectName("tire_markup_label")
        self.verticalLayout_4.addWidget(self.tire_markup_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tire_markup_edit = QtWidgets.QLineEdit(parent=self.taxes_tab)
        self.tire_markup_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tire_markup_edit.setFont(font)
        self.tire_markup_edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tire_markup_edit.setObjectName("tire_markup_edit")
        self.horizontalLayout_5.addWidget(self.tire_markup_edit)
        self.tire_markup_symbol = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.tire_markup_symbol.setFont(font)
        self.tire_markup_symbol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tire_markup_symbol.setObjectName("tire_markup_symbol")
        self.horizontalLayout_5.addWidget(self.tire_markup_symbol)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 3, 1)
        spacerItem6 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.low_markup_checkbox = QtWidgets.QCheckBox(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.low_markup_checkbox.setFont(font)
        self.low_markup_checkbox.setIconSize(QtCore.QSize(30, 30))
        self.low_markup_checkbox.setTristate(False)
        self.low_markup_checkbox.setObjectName("low_markup_checkbox")
        self.verticalLayout_5.addWidget(self.low_markup_checkbox)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.under_markup_amount = QtWidgets.QLineEdit(parent=self.taxes_tab)
        self.under_markup_amount.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.under_markup_amount.setFont(font)
        self.under_markup_amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.under_markup_amount.setObjectName("under_markup_amount")
        self.horizontalLayout_9.addWidget(self.under_markup_amount)
        self.under_markup_amount_symbol = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.under_markup_amount_symbol.setFont(font)
        self.under_markup_amount_symbol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.under_markup_amount_symbol.setObjectName("under_markup_amount_symbol")
        self.horizontalLayout_9.addWidget(self.under_markup_amount_symbol)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.under_markup_percent = QtWidgets.QLineEdit(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.under_markup_percent.setFont(font)
        self.under_markup_percent.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.under_markup_percent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.under_markup_percent.setObjectName("under_markup_percent")
        self.horizontalLayout_10.addWidget(self.under_markup_percent)
        self.under_markup_percent_symbol = QtWidgets.QLabel(parent=self.taxes_tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.under_markup_percent_symbol.setFont(font)
        self.under_markup_percent_symbol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.under_markup_percent_symbol.setObjectName("under_markup_percent_symbol")
        self.horizontalLayout_10.addWidget(self.under_markup_percent_symbol)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 2, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(228, 494, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 1, 2, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(506, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 2, 1, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.abort_button_3 = QtWidgets.QPushButton(parent=self.taxes_tab)
        self.abort_button_3.setIcon(icon)
        self.abort_button_3.setIconSize(QtCore.QSize(30, 30))
        self.abort_button_3.setFlat(True)
        self.abort_button_3.setObjectName("abort_button_3")
        self.abort_button_3.clicked.connect(Form.close)
        self.horizontalLayout_6.addWidget(self.abort_button_3)
        self.save_button_3 = QtWidgets.QPushButton(parent=self.taxes_tab)
        self.save_button_3.setIcon(icon1)
        self.save_button_3.setIconSize(QtCore.QSize(30, 30))
        self.save_button_3.setFlat(True)
        self.save_button_3.setObjectName("save_button_3")
        self.horizontalLayout_6.addWidget(self.save_button_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 2, 3, 1, 1)
        self.tabWidget.addTab(self.taxes_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.save_button.clicked.connect(self.save_settings)
        self.save_button_2.clicked.connect(self.save_settings)
        self.save_button_3.clicked.connect(self.save_settings)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.terms_buttons_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.abort_button.setText(_translate("Form", "Abort"))
        self.save_button.setText(_translate("Form", "Save"))
        self.shop_logo_label.setText(_translate("Form", "Shops Logo"))
        self.upload_button.setText(_translate("Form", "Upload"))
        self.shop_name_label.setText(_translate("Form", "Shop Name"))
        self.facility_number_label.setText(_translate("Form", "Facility #"))
        self.address_label.setText(_translate("Form", "Address"))
        self.city_label.setText(_translate("Form", "City"))
        self.state_label.setText(_translate("Form", "State"))
        self.zip_label.setText(_translate("Form", "Zip"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shop_info_tab), _translate("Form", "Shop\'s Info"))
        self.estimate_term_button.setText(_translate("Form", "Estimates"))
        self.invoice_term_button.setText(_translate("Form", "Invoices"))
        self.warranty_term_button.setText(_translate("Form", "Warranty"))
        self.terms_buttons_tab.setTabText(self.terms_buttons_tab.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.warranty_checkbox.setText(_translate("Form", "Warranty On Invoice"))
        self.abort_button_2.setText(_translate("Form", "Abort"))
        self.save_button_2.setText(_translate("Form", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.terms_tab), _translate("Form", "Estimate And Invoice Terms"))
        self.labor_rate_label.setText(_translate("Form", "Shops Labor Rate"))
        self.labor_rate_symbol.setText(_translate("Form", "$"))
        self.parts_markup_label.setText(_translate("Form", "Parts Markup"))
        self.parts_markup_symbol.setText(_translate("Form", "%"))
        self.oem_markup_label.setText(_translate("Form", "OEM Markup"))
        self.oem_markup_symbol.setText(_translate("Form", "%"))
        self.tire_markup_label.setText(_translate("Form", "Tire Markup"))
        self.tire_markup_symbol.setText(_translate("Form", "%"))
        self.low_markup_checkbox.setText(_translate("Form", "Markup For Parts Under "))
        self.under_markup_amount_symbol.setText(_translate("Form", "$"))
        self.under_markup_percent_symbol.setText(_translate("Form", "%"))
        self.abort_button_3.setText(_translate("Form", "Abort"))
        self.save_button_3.setText(_translate("Form", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.taxes_tab), _translate("Form", "Parts and Labor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
