# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P3.ui'
#
# Created: Sun Nov 12 19:10:52 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(609, 556)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../Project1-EID/pi.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.request_button = QtGui.QPushButton(self.centralwidget)
        self.request_button.setGeometry(QtCore.QRect(10, 30, 101, 41))
        self.request_button.setObjectName(_fromUtf8("request_button"))
        self.text_window = QtGui.QTextEdit(self.centralwidget)
        self.text_window.setGeometry(QtCore.QRect(120, 10, 461, 71))
        self.text_window.setObjectName(_fromUtf8("text_window"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 160, 591, 231))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Humgraph_button = QtGui.QPushButton(self.centralwidget)
        self.Humgraph_button.setGeometry(QtCore.QRect(180, 100, 121, 31))
        self.Humgraph_button.setObjectName(_fromUtf8("Humgraph_button"))
        self.Tempgraph_button = QtGui.QPushButton(self.centralwidget)
        self.Tempgraph_button.setGeometry(QtCore.QRect(380, 100, 151, 31))
        self.Tempgraph_button.setObjectName(_fromUtf8("Tempgraph_button"))
        self.CtoF_button = QtGui.QPushButton(self.centralwidget)
        self.CtoF_button.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.CtoF_button.setObjectName(_fromUtf8("CtoF_button"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 410, 161, 121))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Project1", None))
        self.request_button.setText(_translate("MainWindow", "Request Data", None))
        self.Humgraph_button.setText(_translate("MainWindow", "Humidity Graph", None))
        self.Tempgraph_button.setText(_translate("MainWindow", "Temperature Graph", None))
        self.CtoF_button.setText(_translate("MainWindow", "C <-> F", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">Average</span></p><p><span style=\" color:#ff0000;\">Maximum</span></p><p><span style=\" color:#ffff00;\">Minimum</span></p><p><span style=\" color:#00aa00;\">Latest</span></p><p><br/></p></body></html>", None))

