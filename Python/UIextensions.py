from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

def browsefiles(self):
    filename = QtWidgets.QFileDialog.getOpenFileName(filter="*.csv")
    print(filename)