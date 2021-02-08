# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 600, 400))
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setText("")
        self.label.setObjectName("label")
        self.map_view = QtWidgets.QComboBox(self.centralwidget)
        self.map_view.setGeometry(QtCore.QRect(640, 10, 131, 21))
        self.map_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.map_view.setObjectName("map_view")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(10, 470, 131, 41))
        self.search.setObjectName("search")
        self.text_query = QtWidgets.QLineEdit(self.centralwidget)
        self.text_query.setGeometry(QtCore.QRect(10, 430, 271, 31))
        self.text_query.setObjectName("text_query")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setGeometry(QtCore.QRect(630, 530, 141, 61))
        self.reset_btn.setObjectName("reset_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Большая задача по Maps API"))
        self.search.setText(_translate("MainWindow", "Искать"))
        self.reset_btn.setText(_translate("MainWindow", "Сбросить"))
