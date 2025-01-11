from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from orm import *



class Ui_MainWindow(object):
    def __init__(self):
        self.session_db = create_session(setup_database())
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnshow_dir = QtWidgets.QPushButton(self.centralwidget)
        self.btnshow_dir.setGeometry(QtCore.QRect(10, 510, 100, 50))
        self.btnshow_dir.setObjectName("btnDir")
        self.btnshow_dir.clicked.connect(self.showDirBtn)

        self.btnshow_mov = QtWidgets.QPushButton(self.centralwidget)
        self.btnshow_mov.setGeometry(QtCore.QRect(110, 510, 100, 50))
        self.btnshow_mov.setObjectName("btnMov")
        self.btnshow_mov.clicked.connect(self.showMoviesBtn)

        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(60,570,100,50))
        self.btn_clear.setObjectName("btnClear")
        self.btn_clear.clicked.connect(self.btn_Clear)

        self.label_overview = QtWidgets.QLabel(self.centralwidget)
        self.label_overview.setGeometry(QtCore.QRect(240, 0, 460, 261))
        self.label_overview.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_overview.setObjectName("label")
        self.label_overview.setWordWrap(True)
        self.label_overview.setAlignment(Qt.AlignTop)
        self.label_overview.setFont(QFont('Helvetica', 10))

        self.label_director = QtWidgets.QLabel(self.centralwidget)
        self.label_director.setGeometry(QtCore.QRect(240, 260, 460, 81))
        self.label_director.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_director.setObjectName("label_director")
        self.label_director.setFont(QFont('Helvetica',10))

        self.label_mark = QtWidgets.QLabel(self.centralwidget)
        self.label_mark.setGeometry(QtCore.QRect(240, 340, 460, 91))
        self.label_mark.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.label_mark.setObjectName("label_mark")
        self.label_mark.setFont(QFont('Helvetica',10))

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(1, 0, 240, 500))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.clicked.connect(self.movielist_clicked)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showMoviesBtn (self):
        movie_set = self.session_db.query(Movies)
        for movie in movie_set:
            self.listWidget.addItem(movie.original_title)
        self.label_overview.setText("Overview")
        self.label_director.setText("Director")
        self.label_mark.setText("Average mark")
    def showDirBtn(self):
        dir_set = self.session_db.query(Directors)
        for director in dir_set:
            self.listWidget.addItem(director.name)
        self.label_overview.setText("Films")
        self.label_director.setText("Department")

    def btn_Clear(self):
        self.listWidget.clear()
        self.label_overview.setText(None)
        self.label_director.setText(None)
        self.label_mark.setText(None)


    def movielist_clicked(self):
        selectedmoviename = self.listWidget.currentItem().text()
        selecteddirname = self.listWidget.currentItem().text()
        try:
            selectedmovieobject = self.session_db.query(Movies).filter_by(original_title=selectedmoviename).first()
            self.label_overview.setText(selectedmovieobject.overview)
            selectedMovieMark = self.session_db.query(Movies).filter_by(original_title=selectedmoviename).first()
            self.label_mark.setText(str(selectedMovieMark.vote_average))
            selectedMovieDir = self.session_db.query(Movies).filter_by(original_title=selectedmoviename).first()
            self.label_director.setText(selectedMovieDir.director.name)
        except:
            selecteddirobject = self.session_db.query(Directors).filter_by(name = selecteddirname).first()
            films = ''
            for i in range(len(selecteddirobject.movies)):
                films += '"' + selecteddirobject.movies[i].original_title + '"' + ' '
            self.label_overview.setText(films)
            selecteddirdepartment = self.session_db.query(Directors).filter_by(name = selecteddirname).first()
            self.label_director.setText(selecteddirdepartment.department)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ordinary app"))
        self.btnshow_dir.setText(_translate("MainWindow", "Directors"))
        self.btnshow_mov.setText(_translate("MainWindow", "Movies"))
        self.btn_clear.setText(_translate("MainWindow","Clear"))



import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())