# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'N:\My Settings\Downloads\Transfer project v3\GUI\Seats.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Seating(object):
    def setupUi(self, Seating):
        Seating.setObjectName("Seating")
        Seating.resize(1059, 735)
        Seating.setMinimumSize(QtCore.QSize(1059, 735))
        Seating.setMaximumSize(QtCore.QSize(1059, 735))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Seating.setPalette(palette)
        self.lblTicket = QtWidgets.QLabel(Seating)
        self.lblTicket.setGeometry(QtCore.QRect(10, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblTicket.setFont(font)
        self.lblTicket.setObjectName("lblTicket")
        self.lblRegular = QtWidgets.QLabel(Seating)
        self.lblRegular.setGeometry(QtCore.QRect(10, 210, 51, 13))
        self.lblRegular.setObjectName("lblRegular")
        self.lblReduced = QtWidgets.QLabel(Seating)
        self.lblReduced.setGeometry(QtCore.QRect(60, 210, 81, 13))
        self.lblReduced.setObjectName("lblReduced")
        self.lblReduced_2 = QtWidgets.QLabel(Seating)
        self.lblReduced_2.setGeometry(QtCore.QRect(150, 210, 41, 13))
        self.lblReduced_2.setObjectName("lblReduced_2")
        self.comboRegular = QtWidgets.QComboBox(Seating)
        self.comboRegular.setGeometry(QtCore.QRect(10, 230, 41, 16))
        self.comboRegular.setObjectName("comboRegular")
        self.comboRegular.addItem("")
        self.comboRegular.addItem("")
        self.comboRegular.addItem("")
        self.comboRegular.addItem("")
        self.comboRegular.addItem("")
        self.comboRegular.addItem("")
        self.comboReduced = QtWidgets.QComboBox(Seating)
        self.comboReduced.setGeometry(QtCore.QRect(80, 230, 41, 16))
        self.comboReduced.setObjectName("comboReduced")
        self.comboReduced.addItem("")
        self.comboReduced.addItem("")
        self.comboReduced.addItem("")
        self.comboReduced.addItem("")
        self.comboReduced.addItem("")
        self.comboReduced.addItem("")
        self.comboSpecial = QtWidgets.QComboBox(Seating)
        self.comboSpecial.setGeometry(QtCore.QRect(150, 230, 41, 16))
        self.comboSpecial.setObjectName("comboSpecial")
        self.comboSpecial.addItem("")
        self.comboSpecial.addItem("")
        self.comboSpecial.addItem("")
        self.comboSpecial.addItem("")
        self.comboSpecial.addItem("")
        self.comboSpecial.addItem("")
        self.lblTotal = QtWidgets.QLabel(Seating)
        self.lblTotal.setGeometry(QtCore.QRect(10, 480, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotal.setFont(font)
        self.lblTotal.setObjectName("lblTotal")
        self.lblCost = QtWidgets.QLabel(Seating)
        self.lblCost.setGeometry(QtCore.QRect(130, 480, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblCost.setFont(font)
        self.lblCost.setObjectName("lblCost")
        self.lblSeats = QtWidgets.QLabel(Seating)
        self.lblSeats.setGeometry(QtCore.QRect(10, 270, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblSeats.setFont(font)
        self.lblSeats.setObjectName("lblSeats")
        self.lblSelected = QtWidgets.QLabel(Seating)
        self.lblSelected.setGeometry(QtCore.QRect(10, 290, 281, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblSelected.setFont(font)
        self.lblSelected.setText("")
        self.lblSelected.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblSelected.setWordWrap(True)
        self.lblSelected.setObjectName("lblSelected")

        self.retranslateUi(Seating)
        QtCore.QMetaObject.connectSlotsByName(Seating)

    def retranslateUi(self, Seating):
        _translate = QtCore.QCoreApplication.translate
        Seating.setWindowTitle(_translate("Seating", "Dialog"))
        self.lblTicket.setText(_translate("Seating", "Ticket"))
        self.lblRegular.setText(_translate("Seating", "Regular"))
        self.lblReduced.setText(_translate("Seating", "Under18/Over65"))
        self.lblReduced_2.setText(_translate("Seating", "Special"))
        self.comboRegular.setItemText(0, _translate("Seating", "0"))
        self.comboRegular.setItemText(1, _translate("Seating", "1"))
        self.comboRegular.setItemText(2, _translate("Seating", "2"))
        self.comboRegular.setItemText(3, _translate("Seating", "3"))
        self.comboRegular.setItemText(4, _translate("Seating", "4"))
        self.comboRegular.setItemText(5, _translate("Seating", "5"))
        self.comboReduced.setItemText(0, _translate("Seating", "0"))
        self.comboReduced.setItemText(1, _translate("Seating", "1"))
        self.comboReduced.setItemText(2, _translate("Seating", "2"))
        self.comboReduced.setItemText(3, _translate("Seating", "3"))
        self.comboReduced.setItemText(4, _translate("Seating", "4"))
        self.comboReduced.setItemText(5, _translate("Seating", "5"))
        self.comboSpecial.setItemText(0, _translate("Seating", "0"))
        self.comboSpecial.setItemText(1, _translate("Seating", "1"))
        self.comboSpecial.setItemText(2, _translate("Seating", "2"))
        self.comboSpecial.setItemText(3, _translate("Seating", "3"))
        self.comboSpecial.setItemText(4, _translate("Seating", "4"))
        self.comboSpecial.setItemText(5, _translate("Seating", "5"))
        self.lblTotal.setText(_translate("Seating", "Total Cost"))
        self.lblCost.setText(_translate("Seating", "£0.00"))
        self.lblSeats.setText(_translate("Seating", "Seats Selected"))
import Seats_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Seating = QtWidgets.QDialog()
    ui = Ui_Seating()
    ui.setupUi(Seating)
    Seating.show()
    sys.exit(app.exec_())
