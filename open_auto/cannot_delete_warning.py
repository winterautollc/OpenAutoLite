from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_cant_delete(object):
    def setupUi(self, cant_delete):
        cant_delete.setObjectName("cant_delete")
        cant_delete.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/info.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        cant_delete.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(cant_delete)
        self.gridLayout.setObjectName("gridLayout")
        self.warning_label = QtWidgets.QLabel(parent=cant_delete)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.warning_label.setFont(font)
        self.warning_label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.warning_label.setScaledContents(False)
        self.warning_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.warning_label.setWordWrap(True)
        self.warning_label.setObjectName("warning_label")
        self.gridLayout.addWidget(self.warning_label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=cant_delete)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui_files/Images/Icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(cant_delete.close)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.retranslateUi(cant_delete)
        QtCore.QMetaObject.connectSlotsByName(cant_delete)

    def retranslateUi(self, cant_delete):
        _translate = QtCore.QCoreApplication.translate
        cant_delete.setWindowTitle(_translate("cant_delete", "Cannot Delete Names"))
        self.warning_label.setText(_translate("cant_delete", "Names cannot be changed. Please delete and create new if necessary."))
        self.pushButton.setText(_translate("cant_delete", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cant_delete = QtWidgets.QWidget()
    ui = Ui_cant_delete()
    ui.setupUi(cant_delete)
    cant_delete.show()
    sys.exit(app.exec())
