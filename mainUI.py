# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 20, 391, 201))
        self.listView.setObjectName("listView")
        self.addProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.addProfileButton.setGeometry(QtCore.QRect(440, 20, 141, 41))
        self.addProfileButton.setObjectName("addProfileButton")
        self.removeProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeProfileButton.setGeometry(QtCore.QRect(440, 100, 141, 41))
        self.removeProfileButton.setObjectName("removeProfileButton")
        self.updateConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateConfigButton.setGeometry(QtCore.QRect(440, 180, 141, 41))
        self.updateConfigButton.setObjectName("updateConfigButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translpushButtonate("MainWindow", "MainWindow"))
        self.addProfileButton.setText(_translate("MainWindow", "Add Profile"))
        self.removeProfileButton.setText(_translate("MainWindow", "Remove Profile"))
        self.updateConfigButton.setText(_translate("MainWindow", "Update Config"))
