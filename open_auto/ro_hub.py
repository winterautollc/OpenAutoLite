from PyQt6 import QtCore, QtGui, QtWidgets
import home, login, new_ro, settings_hub


class Ui_ROs(object):

    def open_home_page(self):
        self.show_home_page = QtWidgets.QMainWindow()
        self.home_page_ui = home.Ui_MainWindow()
        self.home_page_ui.setupUi(self.show_home_page)
        self.show_home_page.show()
        self.show_home_page.showMaximized()

    def create_ro(self):
        self.new_ro_page = QtWidgets.QWidget()
        self.new_ro_page_ui = new_ro.Ui_create_ro()
        self.new_ro_page_ui.setupUi(self.new_ro_page)
        self.new_ro_page.show()

    def show_all(self):
        self.ro_lists.setColumnCount(9)
        self.ro_lists.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        header_names = ("RO Number", "Date", "Name", "Year", "Make", "Model", "Tech", "Total", "Status")
        self.ro_lists.setHorizontalHeaderLabels(header_names)

    def show_estimates(self):
        self.ro_lists.setColumnCount(8)
        self.ro_lists.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def show_approved(self):
        self.ro_lists.setColumnCount(8)
        self.ro_lists.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def show_working(self):
        self.ro_lists.setColumnCount(8)
        self.ro_lists.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def open_settings(self):
        self.settings_window = QtWidgets.QWidget()
        self.settings_ui = settings_hub.Ui_Form()
        self.settings_ui.setupUi(self.settings_window)
        self.settings_window.show()



    def setupUi(self, ROs):
        ROs.setObjectName("ROs")
        ROs.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/list-check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ROs.setWindowIcon(icon)
#        ROs.setStyleSheet("background-color: #504F4F;")
        self.gridLayout = QtWidgets.QGridLayout(ROs)
        self.gridLayout.setObjectName("gridLayout")
        self.side_menu = QtWidgets.QTabWidget(parent=ROs)
        self.side_menu.setMinimumSize(QtCore.QSize(130, 500))
        self.side_menu.setMaximumSize(QtCore.QSize(90, 800))
        self.side_menu.setStyleSheet("background-color: #929191;")
        self.side_menu.setTabBarAutoHide(True)
        self.side_menu.setObjectName("side_menu")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 125, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_all_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.show_all_button.setStyleSheet("text-align: left;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/apps.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.show_all_button.setIcon(icon1)
        self.show_all_button.setIconSize(QtCore.QSize(30, 30))
        self.show_all_button.setFlat(True)
        self.show_all_button.setObjectName("show_all_button")
        self.show_all_button.clicked.connect(self.show_all)
        self.verticalLayout.addWidget(self.show_all_button)
        self.new_ro_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.new_ro_button.setStyleSheet("text-align: left;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/add-document.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.new_ro_button.setIcon(icon2)
        self.new_ro_button.setIconSize(QtCore.QSize(30, 30))
        self.new_ro_button.setFlat(True)
        self.new_ro_button.setObjectName("new_ro_button")
        self.new_ro_button.clicked.connect(self.create_ro)
        self.verticalLayout.addWidget(self.new_ro_button)
        self.estimates_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.estimates_button.setStyleSheet("text-align: left;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/ballot.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.estimates_button.setIcon(icon3)
        self.estimates_button.setIconSize(QtCore.QSize(30, 30))
        self.estimates_button.setFlat(True)
        self.estimates_button.setObjectName("estimates_button")
        self.estimates_button.clicked.connect(self.show_estimates)
        self.verticalLayout.addWidget(self.estimates_button)
        self.approved_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.approved_button.setStyleSheet("text-align: left;")
        self.approved_button.setIcon(icon)
        self.approved_button.setIconSize(QtCore.QSize(30, 30))
        self.approved_button.setFlat(True)
        self.approved_button.setObjectName("approved_button")
        self.approved_button.clicked.connect(self.show_approved)
        self.verticalLayout.addWidget(self.approved_button)
        self.in_progress_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.in_progress_button.setStyleSheet("text-align: left;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/document.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.in_progress_button.setIcon(icon4)
        self.in_progress_button.setIconSize(QtCore.QSize(30, 30))
        self.in_progress_button.setFlat(True)
        self.in_progress_button.setObjectName("in_progress_button")
        self.in_progress_button.clicked.connect(self.show_working)
        self.verticalLayout.addWidget(self.in_progress_button)
        self.checckout_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.checckout_button.setStyleSheet("text-align: left;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/shopping-cart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.checckout_button.setIcon(icon5)
        self.checckout_button.setIconSize(QtCore.QSize(30, 30))
        self.checckout_button.setFlat(True)
        self.checckout_button.setObjectName("checkout_button")
        self.verticalLayout.addWidget(self.checckout_button)
        self.settings_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.settings_button.setStyleSheet("text-align: left;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settings_button.setIcon(icon6)
        self.settings_button.setIconSize(QtCore.QSize(30, 30))
        self.settings_button.setFlat(True)
        self.settings_button.setObjectName("settings_button")
        self.settings_button.clicked.connect(self.open_settings)
        self.verticalLayout.addWidget(self.settings_button)
        self.home_button = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.home_button.setStyleSheet("text-align: left;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.home_button.setIcon(icon7)
        self.home_button.setIconSize(QtCore.QSize(30, 30))
        self.home_button.setFlat(True)
        self.home_button.setObjectName("home_button")
        self.home_button.clicked.connect(self.open_home_page)
        self.home_button.clicked.connect(ROs.close)

        self.verticalLayout.addWidget(self.home_button)
        self.side_menu.addTab(self.tab, "")
        self.gridLayout.addWidget(self.side_menu, 0, 0, 1, 1)
        self.ro_lists = QtWidgets.QTableWidget(parent=ROs)
        header_names = ("RO Number", "Date", "Name", "Year", "Make", "Model", "Tech", "Total", "Status")
        self.ro_lists.setMinimumSize(QtCore.QSize(0, 720))
#        self.ro_lists.setStyleSheet("background-color: #504F4F;\n"
#"border: none;")
        self.ro_lists.setGridStyle(QtCore.Qt.PenStyle.DashDotLine)
        self.ro_lists.setRowCount(0)
        self.ro_lists.setColumnCount(9)
        self.ro_lists.setObjectName("ro_lists")
        self.ro_lists.horizontalHeader().setCascadingSectionResizes(True)
        self.ro_lists.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ro_lists.setHorizontalHeaderLabels(header_names)
        self.gridLayout.addWidget(self.ro_lists, 0, 1, 2, 1)
        self.label_2 = QtWidgets.QLabel(parent=ROs)
        self.label_2.setMinimumSize(QtCore.QSize(0, 100))
        self.label_2.setMaximumSize(QtCore.QSize(130, 200))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../ui_files/winter_auto.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(ROs)
        self.side_menu.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ROs)

    def retranslateUi(self, ROs):
        _translate = QtCore.QCoreApplication.translate
        ROs.setWindowTitle(_translate("ROs", "Repair Orders"))
        self.show_all_button.setText(_translate("ROs", "Show All"))
        self.new_ro_button.setText(_translate("ROs", "Create New"))
        self.estimates_button.setText(_translate("ROs", "Estimates"))
        self.approved_button.setText(_translate("ROs", "Approved"))
        self.in_progress_button.setText(_translate("ROs", "Working"))
        self.checckout_button.setText(_translate("ROs", "Checkout"))
        self.settings_button.setText(_translate("ROs", "Settings"))
        self.home_button.setText(_translate("ROs", "Home"))
        self.side_menu.setTabText(self.side_menu.indexOf(self.tab), _translate("ROs", "Tab 1"))
        self.ro_lists.setSortingEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ROs = QtWidgets.QWidget()
    ui = Ui_ROs()
    ui.setupUi(ROs)
    ROs.show()
    ROs.showMaximized()
    sys.exit(app.exec())
