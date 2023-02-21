from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QApplication
from game import Gamecheck
from stylehelp import Stleship


class Ui_MainWindow(QMainWindow):
    def restart(self):
        for btn in self.btn_lst:
            btn.setText("")
            btn.setEnabled(True)
        self.cur_play = 1
        self.lbl_x.setStyleSheet(Stleship.activate())
        self.lbl_o.setStyleSheet(Stleship.not_activate())      
    def click_btn(self, num:int):
        if self.cur_play == 1:
            self.btn_lst[num].setStyleSheet("color: brown;font-size:35px;")
            self.btn_lst[num].setText("X")
            self.btn_lst[num].setEnabled(False)
            self.cur_play = 0
            self.lbl_o.setStyleSheet(Stleship.activate())
            self.lbl_x.setStyleSheet(Stleship.not_activate())
            
        else:
            self.btn_lst[num].setStyleSheet("color: green;font-size:35px;")
            self.btn_lst[num].setText("O")
            self.btn_lst[num].setEnabled(False)
            self.cur_play = 1
            self.lbl_x.setStyleSheet(Stleship.activate())
            self.lbl_o.setStyleSheet(Stleship.not_activate())
            
        ans = self.gm_check.check_winner()
        if ans != None:
            QMessageBox.information(None,"TABRIKLAYMIZ",ans+"  \n"+"SIZ GOLIBSIZ")
            self.restart()
    def exit(self):
        QApplication.quit()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 631)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(100, 31, 351, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_x = QtWidgets.QLabel(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_x.setFont(font)
        self.lbl_x.setScaledContents(True)
        self.lbl_x.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_x.setObjectName("lbl_x")
        self.horizontalLayout.addWidget(self.lbl_x)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_1 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_1.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_4.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_9.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_3.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_8.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 2, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_5.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_2.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_7.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 2, 0, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_6.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.lbl_o = QtWidgets.QLabel(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_o.setFont(font)
        self.lbl_o.setScaledContents(True)
        self.lbl_o.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_o.setObjectName("lbl_o")
        self.horizontalLayout.addWidget(self.lbl_o)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 40))
        self.cur_play = 1
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(12, 16, 255);\n"
"border:none;\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(12, 16, 255);\n"
"border:none;\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(12, 16, 255);\n"
"border:none;\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);")
        
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.exit)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 26))
        self.menubar.setObjectName("menubar")
        self.menuX_O_O_yini = QtWidgets.QMenu(parent=self.menubar)
        self.menuX_O_O_yini.setObjectName("menuX_O_O_yini")
        self.menuHammaga_omad = QtWidgets.QMenu(parent=self.menubar)
        self.menuHammaga_omad.setObjectName("menuHammaga_omad")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuX_O_O_yini.menuAction())
        self.menubar.addAction(self.menuHammaga_omad.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.btn_lst = [
            self.btn_1,
            self.btn_2,
            self.btn_3,
            self.btn_4,
            self.btn_5,
            self.btn_6,
            self.btn_7,
            self.btn_8,
            self.btn_9
        ]
        self.btn_1.clicked.connect(lambda: self.click_btn(0))
        self.btn_2.clicked.connect(lambda: self.click_btn(1))
        self.btn_3.clicked.connect(lambda: self.click_btn(2))
        self.btn_4.clicked.connect(lambda: self.click_btn(3))
        self.btn_5.clicked.connect(lambda: self.click_btn(4))
        self.btn_6.clicked.connect(lambda: self.click_btn(5))
        self.btn_7.clicked.connect(lambda: self.click_btn(6))
        self.btn_8.clicked.connect(lambda: self.click_btn(7))
        self.btn_9.clicked.connect(lambda: self.click_btn(8))
        self.pushButton.clicked.connect(self.restart)
        self.gm_check = Gamecheck(self.btn_lst)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Bu mening birinchi o\'yinim.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">O\'yin muallifi:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Botirov</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Muhammadumar</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "O\'yin haqida"))
        self.lbl_x.setText(_translate("MainWindow", "X"))
        self.lbl_o.setText(_translate("MainWindow", "O"))
        self.pushButton.setText(_translate("MainWindow", "Restart"))
        self.pushButton_3.setText(_translate("MainWindow", "O\'yin haqida"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "O\'yin"))
        self.menuX_O_O_yini.setTitle(_translate("MainWindow", "X  O O\'yini"))
        self.menuHammaga_omad.setTitle(_translate("MainWindow", "Hammaga omad"))
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
