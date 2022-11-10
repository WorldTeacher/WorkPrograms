# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFrame,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QTextBrowser, QTextEdit, QToolButton, QWidget)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(800, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings.sizePolicy().hasHeightForWidth())
        settings.setSizePolicy(sizePolicy)
        settings.setMinimumSize(QSize(800, 500))
        settings.setMaximumSize(QSize(800, 500))
        settings.setMouseTracking(True)
        settings.setAcceptDrops(False)
        self.buttonBox = QDialogButtonBox(settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(529, 460, 261, 39))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Discard|QDialogButtonBox.RestoreDefaults|QDialogButtonBox.Save)
        self.label_red = QLabel(settings)
        self.label_red.setObjectName(u"label_red")
        self.label_red.setGeometry(QRect(630, 20, 31, 21))
        self.label_green = QLabel(settings)
        self.label_green.setObjectName(u"label_green")
        self.label_green.setGeometry(QRect(630, 50, 31, 21))
        self.label_blue = QLabel(settings)
        self.label_blue.setObjectName(u"label_blue")
        self.label_blue.setGeometry(QRect(630, 80, 31, 21))
        self.value_red = QSpinBox(settings)
        self.value_red.setObjectName(u"value_red")
        self.value_red.setGeometry(QRect(660, 20, 80, 22))
        self.value_red.setMouseTracking(True)
        self.value_red.setMaximum(255)
        self.value_green = QSpinBox(settings)
        self.value_green.setObjectName(u"value_green")
        self.value_green.setGeometry(QRect(660, 50, 80, 22))
        self.value_green.setMouseTracking(True)
        self.value_green.setMaximum(255)
        self.value_blue = QSpinBox(settings)
        self.value_blue.setObjectName(u"value_blue")
        self.value_blue.setGeometry(QRect(660, 80, 80, 22))
        self.value_blue.setMouseTracking(True)
        self.value_blue.setMaximum(255)
        self.textEdit = QTextEdit(settings)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(620, 110, 121, 21))
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_color = QLineEdit(settings)
        self.search_color.setObjectName(u"search_color")
        self.search_color.setGeometry(QRect(70, 10, 113, 21))
        self.search_color.setMaxLength(11)
        self.search_color_label = QLabel(settings)
        self.search_color_label.setObjectName(u"search_color_label")
        self.search_color_label.setGeometry(QRect(20, 10, 55, 21))
        self.title_color_label = QLabel(settings)
        self.title_color_label.setObjectName(u"title_color_label")
        self.title_color_label.setGeometry(QRect(20, 40, 55, 21))
        self.title_color = QLineEdit(settings)
        self.title_color.setObjectName(u"title_color")
        self.title_color.setGeometry(QRect(70, 40, 113, 21))
        self.title_color.setMaxLength(11)
        self.save_directory_label = QLabel(settings)
        self.save_directory_label.setObjectName(u"save_directory_label")
        self.save_directory_label.setGeometry(QRect(20, 370, 61, 21))
        self.save_directory_auto = QLineEdit(settings)
        self.save_directory_auto.setObjectName(u"save_directory_auto")
        self.save_directory_auto.setGeometry(QRect(120, 370, 113, 20))
        self.browse_ = QToolButton(settings)
        self.browse_.setObjectName(u"browse_")
        self.browse_.setGeometry(QRect(230, 370, 25, 21))
        self.line = QFrame(settings)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 130, 791, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(settings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 320, 771, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_bwl = QLabel(settings)
        self.label_bwl.setObjectName(u"label_bwl")
        self.label_bwl.setGeometry(QRect(20, 340, 91, 21))
        self.label = QLabel(settings)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 370, 51, 21))
        self.csv_name_auto = QLineEdit(settings)
        self.csv_name_auto.setObjectName(u"csv_name_auto")
        self.csv_name_auto.setGeometry(QRect(390, 370, 113, 20))
        self.label_auto = QLabel(settings)
        self.label_auto.setObjectName(u"label_auto")
        self.label_auto.setGeometry(QRect(90, 370, 31, 21))
        self.label_auto_2 = QLabel(settings)
        self.label_auto_2.setObjectName(u"label_auto_2")
        self.label_auto_2.setGeometry(QRect(360, 370, 31, 21))
        self.save_directory_manual = QLineEdit(settings)
        self.save_directory_manual.setObjectName(u"save_directory_manual")
        self.save_directory_manual.setGeometry(QRect(120, 400, 113, 20))
        self.browse_1 = QToolButton(settings)
        self.browse_1.setObjectName(u"browse_1")
        self.browse_1.setGeometry(QRect(230, 400, 25, 21))
        self.csv_name_manual = QLineEdit(settings)
        self.csv_name_manual.setObjectName(u"csv_name_manual")
        self.csv_name_manual.setGeometry(QRect(390, 400, 113, 20))
        self.label_manual = QLabel(settings)
        self.label_manual.setObjectName(u"label_manual")
        self.label_manual.setGeometry(QRect(80, 400, 41, 21))
        self.labe_manual = QLabel(settings)
        self.labe_manual.setObjectName(u"labe_manual")
        self.labe_manual.setGeometry(QRect(350, 400, 41, 21))
        self.textBrowser = QTextBrowser(settings)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(540, 340, 231, 111))

        self.retranslateUi(settings)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Settings", None))
        self.label_red.setText(QCoreApplication.translate("settings", u"Rot", None))
        self.label_green.setText(QCoreApplication.translate("settings", u"Gr\u00fcn", None))
        self.label_blue.setText(QCoreApplication.translate("settings", u"Blau", None))
#if QT_CONFIG(tooltip)
        self.value_red.setToolTip(QCoreApplication.translate("settings", u"Hier kann ein numerischer Wert von 0 - 255 eingetragen werden, das \"Farbe\" Feld stellt die Farbe dar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.value_green.setToolTip(QCoreApplication.translate("settings", u"Hier kann ein numerischer Wert von 0 - 255 eingetragen werden, das \"Farbe\" Feld stellt die Farbe dar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.value_blue.setToolTip(QCoreApplication.translate("settings", u"Hier kann ein numerischer Wert von 0 - 255 eingetragen werden, das \"Farbe\" Feld stellt die Farbe dar", None))
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Farbe</p></body></html>", None))
        self.search_color_label.setText(QCoreApplication.translate("settings", u"Search", None))
        self.title_color_label.setText(QCoreApplication.translate("settings", u"Title", None))
#if QT_CONFIG(tooltip)
        self.save_directory_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.save_directory_label.setText(QCoreApplication.translate("settings", u"Speicherort", None))
#if QT_CONFIG(tooltip)
        self.save_directory_auto.setToolTip(QCoreApplication.translate("settings", u"Hier kann ein Speicherort entweder eingetragen werden, oder mithilfe des \"...\" festlegen", None))
#endif // QT_CONFIG(tooltip)
        self.browse_.setText(QCoreApplication.translate("settings", u"...", None))
        self.label_bwl.setText(QCoreApplication.translate("settings", u"BW LastCopies", None))
        self.label.setText(QCoreApplication.translate("settings", u"CSV-Name", None))
#if QT_CONFIG(tooltip)
        self.csv_name_auto.setToolTip(QCoreApplication.translate("settings", u"Hier kann ein Speicherort entweder eingetragen werden, oder mithilfe des \"...\" festlegen", None))
#endif // QT_CONFIG(tooltip)
        self.label_auto.setText(QCoreApplication.translate("settings", u"auto", None))
        self.label_auto_2.setText(QCoreApplication.translate("settings", u"auto", None))
#if QT_CONFIG(tooltip)
        self.save_directory_manual.setToolTip(QCoreApplication.translate("settings", u"Hier kann ein Speicherort entweder eingetragen werden, oder mithilfe des \"...\" festlegen", None))
#endif // QT_CONFIG(tooltip)
        self.browse_1.setText(QCoreApplication.translate("settings", u"...", None))
#if QT_CONFIG(tooltip)
        self.csv_name_manual.setToolTip(QCoreApplication.translate("settings", u"Hier kann ein Speicherort entweder eingetragen werden, oder mithilfe des \"...\" festlegen", None))
#endif // QT_CONFIG(tooltip)
        self.label_manual.setText(QCoreApplication.translate("settings", u"manuell", None))
        self.labe_manual.setText(QCoreApplication.translate("settings", u"manuell", None))
        self.textBrowser.setHtml(QCoreApplication.translate("settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">F\u00fcr die CSV-Dateien kann manuell ein Speicherort festgelegt werden. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Standard ist: C://Benutzer/Desktop/BWLastCopies/{dateiname}.csv</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Der"
                        " Name kann konfiguriert werden, wird aber immer ein &quot;auto_&quot; bzw. &quot;manual_&quot; am Anfang haben, um die Dateien zu unterscheiden.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Standard ist hier: &quot;auto_{Datum[JJJJ.MM.TT]}.csv&quot;</p></body></html>", None))
    # retranslateUi

