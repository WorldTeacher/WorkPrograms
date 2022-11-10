# -*- coding: utf-8 -*-


from platform import system
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import urlsearch,os, json, manualsearch,  search_db
import atexit
from make_csv import Csv
from settings_data import Settings
from settings import Ui_settings
from PySide6.QtCore import QRunnable, QThreadPool, QThread, Signal, Slot

# class Ui_settings(object):
#     def setupUi(self, settings):
#         settings.setObjectName("settings")
#         settings.resize(800, 500)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(settings.sizePolicy().hasHeightForWidth())
#         settings.setSizePolicy(sizePolicy)
#         settings.setMinimumSize(QtCore.QSize(800, 500))
#         settings.setMaximumSize(QtCore.QSize(800, 500))
#         settings.setMouseTracking(True)
#         settings.setAcceptDrops(False)
#         self.buttonBox = QtWidgets.QDialogButtonBox(settings)
#         self.buttonBox.setGeometry(QtCore.QRect(529, 460, 261, 39))
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Discard|QtWidgets.QDialogButtonBox.StandardButton.RestoreDefaults|QtWidgets.QDialogButtonBox.StandardButton.Save)
#         self.buttonBox.setObjectName("buttonBox")
#         self.label = QtWidgets.QLabel(settings)
#         self.label.setGeometry(QtCore.QRect(630, 30, 21, 16))
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(settings)
#         self.label_2.setGeometry(QtCore.QRect(660, 30, 31, 16))
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(settings)
#         self.label_3.setGeometry(QtCore.QRect(700, 30, 21, 16))
#         self.label_3.setObjectName("label_3")
#         self.value_red = QtWidgets.QSpinBox(settings)
#         self.value_red.setGeometry(QtCore.QRect(620, 50, 42, 22))
#         self.value_red.setMaximum(255)
#         self.value_red.setObjectName("value_red")
#         self.value_green = QtWidgets.QSpinBox(settings)
#         self.value_green.setGeometry(QtCore.QRect(660, 50, 42, 22))
#         self.value_green.setMaximum(255)
#         self.value_green.setObjectName("value_green")
#         self.value_blue = QtWidgets.QSpinBox(settings)
#         self.value_blue.setGeometry(QtCore.QRect(700, 50, 42, 22))
#         self.value_blue.setMaximum(255)
#         self.value_blue.setObjectName("value_blue")
#         self.textEdit = QtWidgets.QTextEdit(settings)
#         self.textEdit.setGeometry(QtCore.QRect(620, 80, 121, 21))
#         self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.textEdit.setObjectName("textEdit")
#         self.label_search = QtWidgets.QLabel(settings)
#         self.label_search.setGeometry(QtCore.QRect(20, 20, 40, 16))
#         self.label_search.setObjectName("label_search")
#         #if value of spinbox changes, update color
#         self.value_red.valueChanged.connect(self.updateColor)
#         self.value_green.valueChanged.connect(self.updateColor)
#         self.value_blue.valueChanged.connect(self.updateColor)
#         self.retranslateUi(settings)
#         QtCore.QMetaObject.connectSlotsByName(settings)

#     def retranslateUi(self, settings):
#         _translate = QtCore.QCoreApplication.translate
#         settings.setWindowTitle(_translate("settings", "Settings"))
#         self.label.setText(_translate("settings", "Rot"))
#         self.label_2.setText(_translate("settings", "Grün"))
#         self.label_3.setText(_translate("settings", "Blau"))
#         self.textEdit.setHtml(_translate("settings", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Farbe</p></body></html>"))
        
#     def getValues(self):
#         return self.value_red.value(), self.value_green.value(), self.value_blue.value()
#     def updateColor(self):
#         self.textEdit.setStyleSheet("background-color: rgb({}, {}, {});".format(self.value_red.value(), self.value_green.value(), self.value_blue.value()))
#     def write_to_settings(self, field, value):
#         import json 
#         with open("gui-settings.json", "r") as f:
#             settings = json.load(f)
#         data={field:value}
#         settings.update(data)
#         with open("gui-settings.json", "w") as f:
#             json.dump(settings, f)

#     def set_search_text_color(self, color:tuple):
#         red=color[0]
#         green=color[1]
#         blue=color[2]
#         rgb="rgb({}, {}, {})".format(red, green, blue)
#         self.write_to_settings("search_text_color", rgb)

#     def launch(self):
#         import sys
#         app = QtWidgets.QApplication(sys.argv)
#         settings = QtWidgets.QWidget()
#         ui = Ui_settings()
#         ui.setupUi(settings)
#         settings.show()
#         sys.exit(app.exec())
# class Worker(QRunnable):
#     '''
#     Worker thread

#     Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

#     :param callback: The function callback to run on this worker thread. Supplied args and
#                      kwargs will be passed through to the runner.
#     :type callback: function
#     :param args: Arguments to pass to the callback function
#     :param kwargs: Keywords to pass to the callback function

#     '''

#     def __init__(self, fn, *args, **kwargs):
#         super(Worker, self).__init__()
#         # Store constructor arguments (re-used for processing)
#         self.fn = fn
#         self.args = args
#         self.kwargs = kwargs

#     #@pyqtSlot()
#     def run(self):
#         '''
#         Initialise the runner function with passed args, kwargs.
#         '''
#         self.fn(*self.args, **self.kwargs)  
        
class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.threadpool = QThreadPool()
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ReiheA_BWL = QtWidgets.QTabWidget(self.centralwidget)
        self.ReiheA_BWL.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReiheA_BWL.sizePolicy().hasHeightForWidth())
        self.ReiheA_BWL.setSizePolicy(sizePolicy)
        self.ReiheA_BWL.setMinimumSize(QtCore.QSize(1280, 720))
        self.ReiheA_BWL.setMaximumSize(QtCore.QSize(1280, 720))
        self.ReiheA_BWL.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.ReiheA_BWL.setWhatsThis("")
        self.ReiheA_BWL.setObjectName("ReiheA_BWL")
        self.tab_reihe_a = QtWidgets.QWidget()
        self.tab_reihe_a.setObjectName("tab_reihe_a")
        self.pushButton = QtWidgets.QPushButton(self.tab_reihe_a)
        self.pushButton.setGeometry(QtCore.QRect(1180, 620, 75, 23))
        self.pushButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.tab_reihe_a)
        self.progressBar.setGeometry(QtCore.QRect(10, 620, 1141, 23))
        self.progressBar.setToolTip("")
        self.progressBar.setToolTipDuration(2)
        self.progressBar.setWhatsThis("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.name = QtWidgets.QCheckBox(self.tab_reihe_a)
        self.name.setGeometry(QtCore.QRect(10, 590, 70, 17))
        self.name.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.name.setObjectName("name")
        self.testloginfo = QtWidgets.QPlainTextEdit(self.tab_reihe_a)
        self.testloginfo.setEnabled(True)
        self.testloginfo.setGeometry(QtCore.QRect(30, 510, 891, 71))
        self.testloginfo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.testloginfo.setAcceptDrops(True)
        self.testloginfo.setObjectName("testloginfo")
        self.loglabel = QtWidgets.QLabel(self.tab_reihe_a)
        self.loglabel.setGeometry(QtCore.QRect(30, 490, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loglabel.setFont(font)
        self.loglabel.setObjectName("loglabel")
        self.ReiheA_BWL.addTab(self.tab_reihe_a, "")
        self.tab_bwl = QtWidgets.QWidget()
        self.tab_bwl.setObjectName("tab_bwl")
        self.tabwidget_auto_manual = QtWidgets.QTabWidget(self.tab_bwl)
        self.tabwidget_auto_manual.setGeometry(QtCore.QRect(0, 0, 1271, 671))
        self.tabwidget_auto_manual.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.tabwidget_auto_manual.setToolTip("")
        self.tabwidget_auto_manual.setObjectName("tabwidget_auto_manual")
        self.Automatic = QtWidgets.QWidget()
        self.Automatic.setObjectName("Automatic")
        self.do_run_bwlastcopies = QtWidgets.QPushButton(self.Automatic)
        self.do_run_bwlastcopies.setGeometry(QtCore.QRect(1180, 610, 75, 23))
        self.do_run_bwlastcopies.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.do_run_bwlastcopies.setObjectName("do_run_bwlastcopies")
        self.progressbar_lastcopies = QtWidgets.QProgressBar(self.Automatic)
        self.progressbar_lastcopies.setGeometry(QtCore.QRect(10, 610, 1141, 23))
        self.progressbar_lastcopies.setToolTip("")
        self.progressbar_lastcopies.setToolTipDuration(2)
        self.progressbar_lastcopies.setWhatsThis("")
        self.progressbar_lastcopies.setProperty("value", 0)
        self.progressbar_lastcopies.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressbar_lastcopies.setObjectName("progressbar_lastcopies")
        self.loginfo_bwl = QtWidgets.QPlainTextEdit(self.Automatic)
        self.loginfo_bwl.setEnabled(True)
        self.loginfo_bwl.setGeometry(QtCore.QRect(30, 500, 891, 71))
        self.loginfo_bwl.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.loginfo_bwl.setAcceptDrops(True)
        self.loginfo_bwl.setObjectName("loginfo_bwl")
        self.xml_path = QtWidgets.QLineEdit(self.Automatic)
        self.xml_path.setEnabled(False)
        self.xml_path.setGeometry(QtCore.QRect(100, 30, 113, 19))
        self.xml_path.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.xml_path.setObjectName("xml_path")
        self.save_json = QtWidgets.QPushButton(self.Automatic)
        self.save_json.setGeometry(QtCore.QRect(440, 10, 75, 23))
        self.save_json.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.save_json.setObjectName("save_json")
        self.show_url = QtWidgets.QCheckBox(self.Automatic)
        self.show_url.setGeometry(QtCore.QRect(120, 240, 70, 17))
        self.show_url.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.show_url.setObjectName("show_url")
        self.loglabel_bwlastcopies = QtWidgets.QLabel(self.Automatic)
        self.loglabel_bwlastcopies.setGeometry(QtCore.QRect(30, 480, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loglabel_bwlastcopies.setFont(font)
        self.loglabel_bwlastcopies.setObjectName("loglabel_bwlastcopies")
        self.import_xml_label = QtWidgets.QLabel(self.Automatic)
        self.import_xml_label.setGeometry(QtCore.QRect(20, 20, 71, 40))
        self.import_xml_label.setObjectName("import_xml_label")
        self.log_url = QtWidgets.QCheckBox(self.Automatic)
        self.log_url.setGeometry(QtCore.QRect(120, 260, 70, 17))
        self.log_url.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.log_url.setObjectName("log_url")
        self.import_xml_buton = QtWidgets.QToolButton(self.Automatic)
        self.import_xml_buton.setGeometry(QtCore.QRect(210, 30, 25, 21))
        self.import_xml_buton.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.import_xml_buton.setObjectName("import_xml_buton")
        self.tabwidget_auto_manual.addTab(self.Automatic, "")
        self.manual = QtWidgets.QWidget()
        self.manual.setObjectName("manual")
        self.check_bwlastcopies_manual = QtWidgets.QPushButton(self.manual)
        self.check_bwlastcopies_manual.setGeometry(QtCore.QRect(460, 210, 81, 23))
        self.check_bwlastcopies_manual.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.check_bwlastcopies_manual.setToolTip("")
        self.check_bwlastcopies_manual.setToolTipDuration(-1)
        self.check_bwlastcopies_manual.setWhatsThis("")
        self.check_bwlastcopies_manual.setAutoDefault(False)
        self.check_bwlastcopies_manual.setDefault(False)
        self.check_bwlastcopies_manual.setFlat(False)
        self.check_bwlastcopies_manual.setObjectName("check_bwlastcopies_manual")
        self.label_result = QtWidgets.QLabel(self.manual)
        self.label_result.setGeometry(QtCore.QRect(20, 260, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.description_manual = QtWidgets.QLabel(self.manual)
        self.description_manual.setGeometry(QtCore.QRect(20, 10, 1191, 101))
        self.description_manual.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.description_manual.setScaledContents(False)
        self.description_manual.setWordWrap(True)
        self.description_manual.setObjectName("description_manual")
        self.label_author = QtWidgets.QLabel(self.manual)
        self.label_author.setGeometry(QtCore.QRect(20, 110, 41, 21))
        self.label_author.setStatusTip("")
        self.label_author.setWhatsThis("")
        self.label_author.setAccessibleName("")
        self.label_author.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_author.setAutoFillBackground(False)
        self.label_author.setIndent(-1)
        self.label_author.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.label_author.setObjectName("label_author")
        self.label_title = QtWidgets.QLabel(self.manual)
        self.label_title.setGeometry(QtCore.QRect(300, 110, 41, 21))
        self.label_title.setStatusTip("")
        self.label_title.setWhatsThis("")
        self.label_title.setAccessibleName("")
        self.label_title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_title.setAutoFillBackground(False)
        self.label_title.setIndent(-1)
        self.label_title.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_title.setObjectName("label_title")
        self.bibid = QtWidgets.QLabel(self.manual)
        self.bibid.setGeometry(QtCore.QRect(20, 150, 81, 21))
        self.bibid.setObjectName("bibid")
        self.bib_id_input = QtWidgets.QLineEdit(self.manual)
        self.bib_id_input.setGeometry(QtCore.QRect(100, 150, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bib_id_input.sizePolicy().hasHeightForWidth())
        self.bib_id_input.setSizePolicy(sizePolicy)
        self.bib_id_input.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.bib_id_input.setAutoFillBackground(False)
        self.bib_id_input.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.bib_id_input.setInputMask("")
        self.bib_id_input.setText("")
        self.bib_id_input.setMaxLength(10)
        self.bib_id_input.setObjectName("bib_id_input")
        self.label_sigil = QtWidgets.QLabel(self.manual)
        self.label_sigil.setGeometry(QtCore.QRect(170, 150, 31, 21))
        self.label_sigil.setStatusTip("")
        self.label_sigil.setWhatsThis("")
        self.label_sigil.setAccessibleName("")
        self.label_sigil.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_sigil.setAutoFillBackground(False)
        self.label_sigil.setIndent(-1)
        self.label_sigil.setObjectName("label_sigil")
        self.sigi_input = QtWidgets.QLineEdit(self.manual)
        self.sigi_input.setGeometry(QtCore.QRect(200, 150, 81, 20))
        self.sigi_input.setMaxLength(20)
        self.sigi_input.setObjectName("sigi_input")
        self.validate_sigil = QtWidgets.QToolButton(self.manual)
        self.validate_sigil.setGeometry(QtCore.QRect(280, 150, 25, 20))
        self.validate_sigil.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.validate_sigil.setObjectName("validate_sigil")
        self.author_input = QtWidgets.QLineEdit(self.manual)
        self.author_input.setGeometry(QtCore.QRect(60, 110, 211, 20))
        self.author_input.setInputMask("")
        self.author_input.setText("")
        self.author_input.setMaxLength(32767)
        self.author_input.setClearButtonEnabled(True)
        self.author_input.setObjectName("author_input")
        self.title_input = QtWidgets.QLineEdit(self.manual)
        self.title_input.setGeometry(QtCore.QRect(330, 110, 211, 20))
        self.title_input.setInputMask("")
        self.title_input.setText("")
        self.title_input.setMaxLength(32767)
        self.title_input.setClearButtonEnabled(True)
        self.title_input.setObjectName("title_input")
        self.pass_issue = QtWidgets.QLabel(self.manual)
        self.pass_issue.setGeometry(QtCore.QRect(320, 150, 51, 21))
        self.pass_issue.setObjectName("pass_issue")
        self.pass_issue_input = QtWidgets.QLineEdit(self.manual)
        self.pass_issue_input.setGeometry(QtCore.QRect(370, 150, 113, 20))
        self.pass_issue_input.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.pass_issue_input.setClearButtonEnabled(True)
        self.pass_issue_input.setObjectName("pass_issue_input")
        self.result_bwl_manual = QtWidgets.QTextEdit(self.manual)
        self.result_bwl_manual.setEnabled(True)
        self.result_bwl_manual.setGeometry(QtCore.QRect(20, 290, 1171, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_bwl_manual.sizePolicy().hasHeightForWidth())
        self.result_bwl_manual.setSizePolicy(sizePolicy)
        self.result_bwl_manual.setMouseTracking(False)
        self.result_bwl_manual.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.result_bwl_manual.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.result_bwl_manual.setTabChangesFocus(True)
        self.result_bwl_manual.setDocumentTitle("")
        self.result_bwl_manual.setUndoRedoEnabled(True)
        self.result_bwl_manual.setReadOnly(True)
        self.result_bwl_manual.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.result_bwl_manual.setObjectName("result_bwl_manual")
        self.savecsv = QtWidgets.QCheckBox(self.manual)
        self.savecsv.setGeometry(QtCore.QRect(20, 210, 81, 21))
        self.savecsv.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.savecsv.setObjectName("savecsv")
        self.chec_status = QtWidgets.QLabel(self.manual)
        self.chec_status.setGeometry(QtCore.QRect(390, 210, 51, 21))
        self.chec_status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.chec_status.setWordWrap(False)
        self.chec_status.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.chec_status.setObjectName("chec_status")
        self.frame = QtWidgets.QFrame(self.manual)
        self.frame.setGeometry(QtCore.QRect(630, 110, 541, 161))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setLineWidth(10)
        self.frame.setObjectName("frame")
        self.label_isil = QtWidgets.QLabel(self.frame)
        self.label_isil.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label_isil.setObjectName("label_isil")
        self.isil_input = QtWidgets.QLineEdit(self.frame)
        self.isil_input.setGeometry(QtCore.QRect(50, 10, 71, 21))
        self.isil_input.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.isil_input.setObjectName("isil_input")
        self.search_isil = QtWidgets.QToolButton(self.frame)
        self.search_isil.setGeometry(QtCore.QRect(120, 10, 25, 21))
        self.search_isil.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.search_isil.setObjectName("search_isil")
        self.organame = QtWidgets.QLabel(self.frame)
        self.organame.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.organame.setObjectName("organame")
        self.tel_nr = QtWidgets.QLabel(self.frame)
        self.tel_nr.setGeometry(QtCore.QRect(320, 70, 47, 21))
        self.tel_nr.setObjectName("tel_nr")
        self.mail = QtWidgets.QLabel(self.frame)
        self.mail.setGeometry(QtCore.QRect(10, 70, 47, 21))
        self.mail.setObjectName("mail")
        self.adress = QtWidgets.QLabel(self.frame)
        self.adress.setGeometry(QtCore.QRect(10, 90, 47, 21))
        self.adress.setObjectName("adress")
        self.notification = QtWidgets.QLabel(self.frame)
        self.notification.setGeometry(QtCore.QRect(300, 90, 71, 21))
        self.notification.setObjectName("notification")
        self.organame_line = QtWidgets.QLineEdit(self.frame)
        self.organame_line.setGeometry(QtCore.QRect(70, 50, 423, 20))
        self.organame_line.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.organame_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.organame_line.setCursorPosition(0)
        self.organame_line.setObjectName("organame_line")
        self.mailto = QtWidgets.QLineEdit(self.frame)
        self.mailto.setGeometry(QtCore.QRect(70, 70, 211, 20))
        self.mailto.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.mailto.setObjectName("mailto")
        self.telnr = QtWidgets.QLineEdit(self.frame)
        self.telnr.setGeometry(QtCore.QRect(380, 70, 113, 20))
        self.telnr.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.telnr.setObjectName("telnr")
        self.noti_out = QtWidgets.QLineEdit(self.frame)
        self.noti_out.setGeometry(QtCore.QRect(380, 90, 113, 20))
        self.noti_out.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.noti_out.setObjectName("noti_out")
        self.adress_out = QtWidgets.QTextEdit(self.frame)
        self.adress_out.setGeometry(QtCore.QRect(70, 90, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.adress_out.setFont(font)
        self.adress_out.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.adress_out.setObjectName("adress_out")
        self.tabwidget_auto_manual.addTab(self.manual, "")
        self.ReiheA_BWL.addTab(self.tab_bwl, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuDatei = QtWidgets.QMenu(self.menuBar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuEinstellungen = QtWidgets.QMenu(self.menuBar)
        self.menuEinstellungen.setObjectName("menuEinstellungen")
        MainWindow.setMenuBar(self.menuBar)
        self.actionReihe_A = QtGui.QAction(MainWindow)
        self.actionReihe_A.setObjectName("actionReihe_A")
        self.actionBW_LastCopies = QtGui.QAction(MainWindow)
        self.actionBW_LastCopies.setObjectName("actionBW_LastCopies")
        self.actionbearbeiten = QtGui.QAction(MainWindow)
        self.actionbearbeiten.setCheckable(False)
        self.actionbearbeiten.setShortcutVisibleInContextMenu(True)
        self.actionbearbeiten.setObjectName("actionbearbeiten")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setMenuRole(QtGui.QAction.MenuRole.QuitRole)
        self.actionExit.setObjectName("actionExit")
        self.menuDatei.addAction(self.actionExit)
        self.menuEinstellungen.addAction(self.actionbearbeiten)
        self.menuBar.addAction(self.menuDatei.menuAction())
        self.menuBar.addAction(self.menuEinstellungen.menuAction())
        
    	
        self.retranslateUi(MainWindow)
        self.get_data_from_settings()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.author_input, self.title_input)
        MainWindow.setTabOrder(self.title_input, self.bib_id_input)
        MainWindow.setTabOrder(self.bib_id_input, self.sigi_input)
        MainWindow.setTabOrder(self.sigi_input, self.pass_issue_input)
        MainWindow.setTabOrder(self.pass_issue_input, self.search_isil)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UniversalUI"))
        self.pushButton.setText(_translate("MainWindow", "ClickMe"))
        self.name.setText(_translate("MainWindow", "name"))
        self.testloginfo.setPlainText(_translate("MainWindow", "fsd fsd sdfsdfsdfefsd "))
        self.loglabel.setText(_translate("MainWindow", "Logs:"))
        self.ReiheA_BWL.setTabText(self.ReiheA_BWL.indexOf(self.tab_reihe_a), _translate("MainWindow", "Reihe A"))
        self.do_run_bwlastcopies.setText(_translate("MainWindow", "ClickMe"))
        self.save_json.setText(_translate("MainWindow", "save config"))
        self.show_url.setText(_translate("MainWindow", "show url"))
        self.loglabel_bwlastcopies.setText(_translate("MainWindow", "Logs:"))
        self.import_xml_label.setText(_translate("MainWindow", "Import XML:"))
        self.log_url.setText(_translate("MainWindow", "log url"))
        self.import_xml_buton.setText(_translate("MainWindow", "..."))
        self.tabwidget_auto_manual.setTabText(self.tabwidget_auto_manual.indexOf(self.Automatic), _translate("MainWindow", "Automatisch"))
        self.check_bwlastcopies_manual.setStatusTip(_translate("MainWindow", "Prüft den Titel auf BW-LastCopies-Status"))
        self.check_bwlastcopies_manual.setText(_translate("MainWindow", "Prüfen"))
        self.label_result.setText(_translate("MainWindow", "Ergebnis:"))
        self.description_manual.setText(_translate("MainWindow", "<html><head/><body><p>Dieser Tab dient dazu, selbst kleine suchen durchzuführen. Um ein Medium auf BW-LastCopies-Status zu prüfen, wird mindestens der Titel benötigt; der Autor kann ergänzt werden. Nachdem der Titel und ggf. Autor in die unte stehenden Felder eingegeben wurde, auf &quot;Prüfen&quot; klicken und das Ergebnis aus dem unten stehenden Feld ablesen.</p><p><br/></p></body></html>"))
        self.label_author.setText(_translate("MainWindow", "Autor:"))
        self.label_title.setText(_translate("MainWindow", "Titel:"))
        self.bibid.setText(_translate("MainWindow", "Bibliotheks-ID:"))
        self.bib_id_input.setToolTip(_translate("MainWindow", "Die Bibliotheks-ID kann über winIBW mithilfe des Befehls \"s bib\" ermittelt werden."))
        self.bib_id_input.setPlaceholderText(_translate("MainWindow", "20735"))
        self.label_sigil.setText(_translate("MainWindow", "Sigel:"))
        self.sigi_input.setPlaceholderText(_translate("MainWindow", "DE-Frei129"))
        self.validate_sigil.setToolTip(_translate("MainWindow", "WIP: This will test the entered Sigil using the ISIL Database and return an error if the sigil was not found"))
        self.validate_sigil.setText(_translate("MainWindow", "?"))
        self.author_input.setToolTip(_translate("MainWindow", "Wenn kein Autor vorhanden ist, eine 0 (Null) eintragen"))
        self.author_input.setPlaceholderText(_translate("MainWindow", "Nachname, Vorname"))
        self.title_input.setToolTip(_translate("MainWindow", "Der Vollständige Titel des Werkes, z.B Java ist auch eine Insel"))
        self.title_input.setPlaceholderText(_translate("MainWindow", "Vollständiger Titel"))
        self.pass_issue.setText(_translate("MainWindow", "Auflage:"))
        self.pass_issue_input.setPlaceholderText(_translate("MainWindow", "3 / 3. Aufl. etc"))
        self.result_bwl_manual.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.savecsv.setText(_translate("MainWindow", "Save CSV?"))
        self.chec_status.setText(_translate("MainWindow", "Loading"))
        self.label_isil.setText(_translate("MainWindow", "Sigel: "))
        self.search_isil.setText(_translate("MainWindow", "Go!"))
        self.organame.setText(_translate("MainWindow", "OrgaName"))
        self.tel_nr.setText(_translate("MainWindow", "Tel. Nr"))
        self.mail.setText(_translate("MainWindow", "Mail"))
        self.adress.setText(_translate("MainWindow", "Adress"))
        self.notification.setText(_translate("MainWindow", "Anmerkung"))
        self.tabwidget_auto_manual.setTabText(self.tabwidget_auto_manual.indexOf(self.manual), _translate("MainWindow", "Manuell"))
        self.tabwidget_auto_manual.setTabToolTip(self.tabwidget_auto_manual.indexOf(self.manual), _translate("MainWindow", "Hier kann ein einzelner Titel gesucht werden"))
        self.ReiheA_BWL.setTabText(self.ReiheA_BWL.indexOf(self.tab_bwl), _translate("MainWindow", "BW LastCopies"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.menuEinstellungen.setTitle(_translate("MainWindow", "Einstellungen"))
        self.actionReihe_A.setText(_translate("MainWindow", "Reihe A"))
        self.actionBW_LastCopies.setText(_translate("MainWindow", "BW LastCopies"))
        self.actionbearbeiten.setText(_translate("MainWindow", "Formatierung bearbeiten"))
        self.actionbearbeiten.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.check_bwlastcopies_manual.clicked.connect(self.is_pressed)
        self.actionbearbeiten.triggered.connect(self.edit_config)
        self.search_isil.clicked.connect(self.get_data_isil)
        #open filedialog if button is pressed

        self.import_xml_buton.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self): 
        #get os name
        # platform = sys.platform
        os_name = system()
        print(os_name)
        if os_name == 'Windows':
            direct='C:\\'
            direct=os.path.expanduser('~')
        elif os_name == 'Linux':
            direct='/home'
            direct=os.path.expanduser('~')
        elif os_name== 'Darwin':
            direct='/home'
            direct=os.path.expanduser('~')
        else:
            self.xml_path.setText("OS not supported")

        self.file_path = QFileDialog.getOpenFileName(caption="XML-Datei auswählen", filter="XML-Dateien (*.xml)",directory=direct)
        self.file_path = self.file_path[0]
        self.xml_path.setText(self.file_path)
        self.import_xml_buton.setStyleSheet("background-color: green")
        self.import_xml_buton.setToolTip("XML-Datei wurde ausgewählt")
        self.import_xml_buton.setDisabled(False)
    def is_pressed(self):

        author,title,issue=self.get_input()
        
        result=manualsearch.search(author,title,issue)
        title=result['title']
        our_issues=result['our_issues']
        our_signature=result['signature']
        our_count=result['our_count']
        all_issues=result['issue_count']
        all_issues_raw=result['all_issues']
        all_count=result['all_count']
        ppn=result['ppn']
        series=result['series']
        if author=="0": author="ohne Angabe"
        notification_1=f'Die Suche nach Titel:  {title}, Autor: {author} ergab folgendes Ergebnis:'
        notification_manual=f'Lokal: Auflage(n): {our_issues}, Signatur(en): {our_signature}, PPN: {ppn}, Serie: {series}, BWLastCopies: '
        notification_3=f'Gesamt: Anzahl: {all_count}, Auflage(n):\n{all_issues}'
        self.result_bwl_manual.setText(f' {notification_1}\n\n{notification_manual}\n\n{notification_3}')
        if self.savecsv.isChecked():
            #make csv file with the data
            data={'title':title,'author':author,'our_issues':our_issues,'our_signature':our_signature,'our_count':our_count,'all_issues':all_issues_raw,'all_count':all_count,'ppn':ppn,'series':series}
            csv_data=[title,author,our_issues,our_signature,ppn,series,all_count,all_issues_raw]
            csv_data=[str(x) for x in csv_data]
            csv_data=";".join(csv_data)
            #make csv file with the data
            self.save_csv(csv_data)
            with open('results.csv','a') as f:
                f.write(data+"\n")
                f.close()
            
    def edit_config(self):
        #start settings.py
        self.settings = QtWidgets.QWidget()
        self.ui = Ui_settings()
        self.ui.setupUi(self.settings)
        self.settings.show()
    def get_data_isil(self):
        #check if self.isil_input is empty
        isil=self.isil_input.text()
        try:
            data=search_db.search_database(isil)
            self.organame_line.setText(data['name'])
            self.telnr.setText(data['phone'])
            self.mailto.setText(data['mail'])
            adress_notification=self.adress_notification(data['adress'])
            self.adress_out.setText(adress_notification)
        except Exception as e:
            print(e)
            self.isil_input.setText('Fehler')
    def adress_notification(self,adress):
        adress_notification=f'{adress[0]}\n{adress[2]} {adress[1]}\n{adress[3]}'
        return adress_notification
    def get_input(self):
        author=self.author_input.text()
        title=self.title_input.text()
        issue=self.pass_issue_input.text()
        self.chec_status.setText("Searching")
        #print(f'author: {author}, title: {title}')
        return author,title,issue  

    def get_data_from_settings(self):
        f=Settings().load_settings()
        self.bib_id_input.setText(f['Bibliotheks-ID'])
        self.sigi_input.setText(f['Sigel'])
        self.ReiheA_BWL.setCurrentIndex(f['Index_ReiheA_BWL'])
        self.tabwidget_auto_manual.setCurrentIndex(f['Index_Automatic_Manual'])
    
    def save_data_to_settings(self):
        a=Settings()
        bibid=self.bib_id_input.text()
        sigel=self.sigi_input.text()
        tab_bwl_man_auto=self.tabwidget_auto_manual.currentIndex()
        tab_ra_bwlastcopies=self.ReiheA_BWL.currentIndex()
        data = {
            "Bibliotheks-ID": bibid,
            "Sigel": sigel,
            "Index_Automatic_Manual": tab_bwl_man_auto,
            "Index_ReiheA_BWL":tab_ra_bwlastcopies,
            "csv_safe_location":"default"
            }
        a.save_settings(data,"gui-settings.jsonc")
    
    def save_csv(self,data:dict):
        Csv("result_01").add_row(data)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    atexit.register(ui.save_data_to_settings)
    sys.exit(app.exec())

