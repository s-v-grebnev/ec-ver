# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Sep  7 18:28:26 2017
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
        MainWindow.resize(900, 687)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 250, 80, 21))
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralWidget)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 280, 861, 341))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(9, 19, 881, 221))
        self.frame.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 21, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 21, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 21, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 21, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 841, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 40, 841, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 70, 841, 22))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 100, 841, 22))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 130, 841, 22))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 160, 841, 22))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(60, 190, 811, 22))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 21, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 55, 14))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 900, 19))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTest = QtGui.QMenu(self.menuBar)
        self.menuTest.setObjectName(_fromUtf8("menuTest"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionLoad_Test_256 = QtGui.QAction(MainWindow)
        self.actionLoad_Test_256.setObjectName(_fromUtf8("actionLoad_Test_256"))
        self.actionLoad_Test_512 = QtGui.QAction(MainWindow)
        self.actionLoad_Test_512.setObjectName(_fromUtf8("actionLoad_Test_512"))
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionClear_2 = QtGui.QAction(MainWindow)
        self.actionClear_2.setObjectName(_fromUtf8("actionClear_2"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionCheck = QtGui.QAction(MainWindow)
        self.actionCheck.setObjectName(_fromUtf8("actionCheck"))
        self.actionCop_y_Log = QtGui.QAction(MainWindow)
        self.actionCop_y_Log.setObjectName(_fromUtf8("actionCop_y_Log"))
        self.actionCopy_Cu_rve = QtGui.QAction(MainWindow)
        self.actionCopy_Cu_rve.setObjectName(_fromUtf8("actionCopy_Cu_rve"))
        self.actionClear_output = QtGui.QAction(MainWindow)
        self.actionClear_output.setObjectName(_fromUtf8("actionClear_output"))
        self.action_Run_self_test = QtGui.QAction(MainWindow)
        self.action_Run_self_test.setObjectName(_fromUtf8("action_Run_self_test"))
        self.actionRun_Atkin = QtGui.QAction(MainWindow)
        self.actionRun_Atkin.setObjectName(_fromUtf8("actionRun_Atkin"))
        self.action_Options = QtGui.QAction(MainWindow)
        self.action_Options.setObjectName(_fromUtf8("action_Options"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.action_Options)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCheck)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuTest.addAction(self.actionLoad_Test_256)
        self.menuTest.addAction(self.actionLoad_Test_512)
        self.menuTest.addAction(self.action_Run_self_test)
        self.menuTest.addAction(self.actionRun_Atkin)
        self.menuHelp.addAction(self.actionHelp)
        self.menuEdit.addAction(self.actionClear_2)
        self.menuEdit.addAction(self.actionClear_output)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuTest.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.label.setBuddy(self.lineEdit)
        self.label_6.setBuddy(self.lineEdit_6)
        self.label_5.setBuddy(self.lineEdit_5)
        self.label_3.setBuddy(self.lineEdit_3)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_4.setBuddy(self.lineEdit_4)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "The Mighty EC Verifier", None))
        self.pushButton.setText(_translate("MainWindow", "&Check!", None))
        self.label.setText(_translate("MainWindow", "&P=", None))
        self.label_6.setText(_translate("MainWindow", "&Y=", None))
        self.label_5.setText(_translate("MainWindow", "&X=", None))
        self.label_3.setText(_translate("MainWindow", "&A=", None))
        self.label_2.setText(_translate("MainWindow", "&Q=", None))
        self.label_4.setText(_translate("MainWindow", "&B=", None))
        self.label_7.setText(_translate("MainWindow", "Name=", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuTest.setTitle(_translate("MainWindow", "&Test", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit", None))
        self.actionOpen.setText(_translate("MainWindow", "&Load", None))
        self.actionSave.setText(_translate("MainWindow", "&Save", None))
        self.actionQuit.setText(_translate("MainWindow", "&Quit", None))
        self.actionLoad_Test_256.setText(_translate("MainWindow", "Load Test-256", None))
        self.actionLoad_Test_512.setText(_translate("MainWindow", "Load Test-512", None))
        self.actionClear.setText(_translate("MainWindow", "Clear", None))
        self.actionClear_2.setText(_translate("MainWindow", "C&lear input", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionCheck.setText(_translate("MainWindow", "&Check", None))
        self.actionCop_y_Log.setText(_translate("MainWindow", "Cop&y Log", None))
        self.actionCopy_Cu_rve.setText(_translate("MainWindow", "Copy Cu&rve", None))
        self.actionClear_output.setText(_translate("MainWindow", "Clear &output", None))
        self.action_Run_self_test.setText(_translate("MainWindow", "&Run self-test", None))
        self.actionRun_Atkin.setText(_translate("MainWindow", "Run &Atkin for p,q", None))
        self.action_Options.setText(_translate("MainWindow", "&Options", None))
