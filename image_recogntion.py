# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_recogntion.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(894, 829)
        dialog.setSizeGripEnabled(False)
        dialog.setModal(False)
        self.textBrowser = QtWidgets.QTextBrowser(dialog)
        self.textBrowser.setGeometry(QtCore.QRect(50, 70, 371, 411))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 371, 411))
        self.label.setText("")
        self.label.setObjectName("label")
        # self.label.setScaledContents(True) # 设置图片自适应大小
        self.textBrowser_2 = QtWidgets.QTextBrowser(dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(480, 70, 371, 411))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 161, 51))
        self.label_3.setStyleSheet("font: 20pt \"华文新魏\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(600, 10, 161, 51))
        self.label_4.setStyleSheet("font: 20pt \"华文新魏\";")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(480, 70, 371, 411))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        # self.label.setScaledContents(True)  # 设置图片自适应大小
        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 510, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(dialog)
        self.groupBox.setGeometry(QtCore.QRect(480, 490, 371, 91))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 30, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 30, 181, 41))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 45, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(dialog)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 590, 801, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 761, 161))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(670, 10, 111, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 273, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(320, 10, 340, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_2.addWidget(self.textBrowser_3)
        self.groupBox_3 = QtWidgets.QGroupBox(dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 490, 371, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(50, 20, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.textBrowser_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "人脸识别"))
        self.label_3.setText(_translate("dialog", "原始图片"))
        self.label_4.setText(_translate("dialog", "识别结果"))
        self.pushButton_3.setText(_translate("dialog", "清空图片"))
        self.groupBox.setTitle(_translate("dialog", "识别操作"))
        self.pushButton_2.setText(_translate("dialog", "识别"))
        self.pushButton_6.setText(_translate("dialog", "保存人脸"))
        self.label_5.setText(_translate("dialog", "备注："))
        self.groupBox_2.setTitle(_translate("dialog", "选择保存地址"))
        self.pushButton_5.setText(_translate("dialog", "保存头像"))
        self.pushButton_4.setText(_translate("dialog", "按名字搜索"))
        self.label_6.setText(_translate("dialog", "存储位置："))
        self.groupBox_3.setTitle(_translate("dialog", "原图操作"))
        self.pushButton.setText(_translate("dialog", "选择图片"))

