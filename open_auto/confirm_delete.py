from PyQt6 import QtCore, QtGui, QtWidgets
import customer_hub

class Ui_confirm_delete(object):
    def setupUi(self, confirm_delete):
        confirm_delete.setObjectName("confirm_delete")
        confirm_delete.resize(572, 207)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/winter_auto.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        confirm_delete.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(confirm_delete)
        self.gridLayout.setObjectName("gridLayout")
        self.customer_label = QtWidgets.QLabel(parent=confirm_delete)
        self.customer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.customer_label.setObjectName("customer_label")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.customer_label.setFont(font)
        self.gridLayout.addWidget(self.customer_label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.no_delete = QtWidgets.QPushButton(parent=confirm_delete)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.no_delete.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/cross.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.no_delete.setIcon(icon1)
        self.no_delete.setIconSize(QtCore.QSize(30, 30))
        self.no_delete.setObjectName("no_delete")
        self.no_delete.clicked.connect(confirm_delete.close)
        self.horizontalLayout.addWidget(self.no_delete)
        self.yes_delete = QtWidgets.QPushButton(parent=confirm_delete)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yes_delete.setFont(font)
        self.yes_delete.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.yes_delete.setIcon(icon2)
        self.yes_delete.setIconSize(QtCore.QSize(30, 30))
        self.yes_delete.setObjectName("yes_delete")
        self.yes_delete.clicked.connect(confirm_delete.close)
        self.horizontalLayout.addWidget(self.yes_delete)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(confirm_delete)
        QtCore.QMetaObject.connectSlotsByName(confirm_delete)

    def retranslateUi(self, confirm_delete):
        _translate = QtCore.QCoreApplication.translate
        confirm_delete.setWindowTitle(_translate("confirm_delete", "Confirm Delete"))
        self.customer_label.setText(_translate("confirm_delete", "TextLabel"))
        self.no_delete.setText(_translate("confirm_delete", "NO"))
        self.yes_delete.setText(_translate("confirm_delete", "YES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirm_delete = QtWidgets.QWidget()
    ui = Ui_confirm_delete()
    ui.setupUi(confirm_delete)
    confirm_delete.show()
    sys.exit(app.exec())
