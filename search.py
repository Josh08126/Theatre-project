# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Josh\OneDrive\Documents\Transfer project\GUI\Search.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(1059, 735)
        Search.setMinimumSize(QtCore.QSize(1059, 735))
        Search.setMaximumSize(QtCore.QSize(1059, 735))
        self.twViewers = QtWidgets.QTableWidget(Search)
        self.twViewers.setGeometry(QtCore.QRect(60, 320, 601, 192))
        self.twViewers.setObjectName("twViewers")
        self.twViewers.setColumnCount(11)
        self.twViewers.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.twViewers.setHorizontalHeaderItem(10, item)
        self.lename = QtWidgets.QLineEdit(Search)
        self.lename.setGeometry(QtCore.QRect(70, 20, 113, 20))
        self.lename.setObjectName("lename")
        self.pbsearch = QtWidgets.QPushButton(Search)
        self.pbsearch.setGeometry(QtCore.QRect(470, 280, 121, 23))
        self.pbsearch.setObjectName("pbsearch")

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "Dialog"))
        self.pbsearch.setText(_translate("Search", "search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search = QtWidgets.QDialog()
    ui = Ui_Search()
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec_())
