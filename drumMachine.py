# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drumMachine.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(818, 350)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        Dialog.setPalette(palette)
        Dialog.setAutoFillBackground(True)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(110, 300, 681, 23))
        self.progressBar.setMaximum(16)
        self.progressBar.setProperty("value", 16)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.lcdnumberBeat = QtGui.QLCDNumber(Dialog)
        self.lcdnumberBeat.setGeometry(QtCore.QRect(400, 40, 31, 23))
        self.lcdnumberBeat.setLineWidth(2)
        self.lcdnumberBeat.setNumDigits(1)
        self.lcdnumberBeat.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdnumberBeat.setProperty("intValue", 1)
        self.lcdnumberBeat.setObjectName(_fromUtf8("lcdnumberBeat"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(100, 100, 20, 201))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.labelBassDrum = QtGui.QLabel(Dialog)
        self.labelBassDrum.setGeometry(QtCore.QRect(20, 270, 81, 20))
        self.labelBassDrum.setObjectName(_fromUtf8("labelBassDrum"))
        self.labelSnare = QtGui.QLabel(Dialog)
        self.labelSnare.setGeometry(QtCore.QRect(40, 230, 68, 17))
        self.labelSnare.setObjectName(_fromUtf8("labelSnare"))
        self.labelHiHat = QtGui.QLabel(Dialog)
        self.labelHiHat.setGeometry(QtCore.QRect(40, 150, 68, 17))
        self.labelHiHat.setObjectName(_fromUtf8("labelHiHat"))
        self.push_1_1 = QtGui.QPushButton(Dialog)
        self.push_1_1.setGeometry(QtCore.QRect(120, 260, 31, 27))
        self.push_1_1.setText(_fromUtf8(""))
        self.push_1_1.setObjectName(_fromUtf8("push_1_1"))
        self.push_1_2 = QtGui.QPushButton(Dialog)
        self.push_1_2.setGeometry(QtCore.QRect(160, 260, 31, 27))
        self.push_1_2.setText(_fromUtf8(""))
        self.push_1_2.setObjectName(_fromUtf8("push_1_2"))
        self.push_1_3 = QtGui.QPushButton(Dialog)
        self.push_1_3.setGeometry(QtCore.QRect(200, 260, 31, 27))
        self.push_1_3.setText(_fromUtf8(""))
        self.push_1_3.setObjectName(_fromUtf8("push_1_3"))
        self.push_1_4 = QtGui.QPushButton(Dialog)
        self.push_1_4.setGeometry(QtCore.QRect(240, 260, 31, 27))
        self.push_1_4.setText(_fromUtf8(""))
        self.push_1_4.setObjectName(_fromUtf8("push_1_4"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(270, 100, 20, 201))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(440, 100, 20, 201))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(610, 100, 20, 201))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(780, 100, 20, 201))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.push_1_6 = QtGui.QPushButton(Dialog)
        self.push_1_6.setGeometry(QtCore.QRect(330, 260, 31, 27))
        self.push_1_6.setText(_fromUtf8(""))
        self.push_1_6.setObjectName(_fromUtf8("push_1_6"))
        self.push_1_5 = QtGui.QPushButton(Dialog)
        self.push_1_5.setGeometry(QtCore.QRect(290, 260, 31, 27))
        self.push_1_5.setText(_fromUtf8(""))
        self.push_1_5.setObjectName(_fromUtf8("push_1_5"))
        self.push_1_7 = QtGui.QPushButton(Dialog)
        self.push_1_7.setGeometry(QtCore.QRect(370, 260, 31, 27))
        self.push_1_7.setText(_fromUtf8(""))
        self.push_1_7.setObjectName(_fromUtf8("push_1_7"))
        self.push_1_8 = QtGui.QPushButton(Dialog)
        self.push_1_8.setGeometry(QtCore.QRect(410, 260, 31, 27))
        self.push_1_8.setText(_fromUtf8(""))
        self.push_1_8.setObjectName(_fromUtf8("push_1_8"))
        self.push_1_10 = QtGui.QPushButton(Dialog)
        self.push_1_10.setGeometry(QtCore.QRect(500, 260, 31, 27))
        self.push_1_10.setText(_fromUtf8(""))
        self.push_1_10.setObjectName(_fromUtf8("push_1_10"))
        self.push_1_9 = QtGui.QPushButton(Dialog)
        self.push_1_9.setGeometry(QtCore.QRect(460, 260, 31, 27))
        self.push_1_9.setText(_fromUtf8(""))
        self.push_1_9.setObjectName(_fromUtf8("push_1_9"))
        self.push_1_11 = QtGui.QPushButton(Dialog)
        self.push_1_11.setGeometry(QtCore.QRect(540, 260, 31, 27))
        self.push_1_11.setText(_fromUtf8(""))
        self.push_1_11.setObjectName(_fromUtf8("push_1_11"))
        self.push_1_12 = QtGui.QPushButton(Dialog)
        self.push_1_12.setGeometry(QtCore.QRect(580, 260, 31, 27))
        self.push_1_12.setText(_fromUtf8(""))
        self.push_1_12.setObjectName(_fromUtf8("push_1_12"))
        self.push_1_14 = QtGui.QPushButton(Dialog)
        self.push_1_14.setGeometry(QtCore.QRect(670, 260, 31, 27))
        self.push_1_14.setText(_fromUtf8(""))
        self.push_1_14.setObjectName(_fromUtf8("push_1_14"))
        self.push_1_13 = QtGui.QPushButton(Dialog)
        self.push_1_13.setGeometry(QtCore.QRect(630, 260, 31, 27))
        self.push_1_13.setText(_fromUtf8(""))
        self.push_1_13.setObjectName(_fromUtf8("push_1_13"))
        self.push_1_15 = QtGui.QPushButton(Dialog)
        self.push_1_15.setGeometry(QtCore.QRect(710, 260, 31, 27))
        self.push_1_15.setText(_fromUtf8(""))
        self.push_1_15.setObjectName(_fromUtf8("push_1_15"))
        self.push_1_16 = QtGui.QPushButton(Dialog)
        self.push_1_16.setGeometry(QtCore.QRect(750, 260, 31, 27))
        self.push_1_16.setText(_fromUtf8(""))
        self.push_1_16.setDefault(False)
        self.push_1_16.setFlat(False)
        self.push_1_16.setObjectName(_fromUtf8("push_1_16"))
        self.push_2_4 = QtGui.QPushButton(Dialog)
        self.push_2_4.setGeometry(QtCore.QRect(240, 220, 31, 27))
        self.push_2_4.setText(_fromUtf8(""))
        self.push_2_4.setObjectName(_fromUtf8("push_2_4"))
        self.push_2_15 = QtGui.QPushButton(Dialog)
        self.push_2_15.setGeometry(QtCore.QRect(710, 220, 31, 27))
        self.push_2_15.setText(_fromUtf8(""))
        self.push_2_15.setObjectName(_fromUtf8("push_2_15"))
        self.push_2_3 = QtGui.QPushButton(Dialog)
        self.push_2_3.setGeometry(QtCore.QRect(200, 220, 31, 27))
        self.push_2_3.setText(_fromUtf8(""))
        self.push_2_3.setObjectName(_fromUtf8("push_2_3"))
        self.push_2_10 = QtGui.QPushButton(Dialog)
        self.push_2_10.setGeometry(QtCore.QRect(500, 220, 31, 27))
        self.push_2_10.setText(_fromUtf8(""))
        self.push_2_10.setObjectName(_fromUtf8("push_2_10"))
        self.push_2_16 = QtGui.QPushButton(Dialog)
        self.push_2_16.setGeometry(QtCore.QRect(750, 220, 31, 27))
        self.push_2_16.setText(_fromUtf8(""))
        self.push_2_16.setObjectName(_fromUtf8("push_2_16"))
        self.push_2_8 = QtGui.QPushButton(Dialog)
        self.push_2_8.setGeometry(QtCore.QRect(410, 220, 31, 27))
        self.push_2_8.setText(_fromUtf8(""))
        self.push_2_8.setObjectName(_fromUtf8("push_2_8"))
        self.push_2_12 = QtGui.QPushButton(Dialog)
        self.push_2_12.setGeometry(QtCore.QRect(580, 220, 31, 27))
        self.push_2_12.setText(_fromUtf8(""))
        self.push_2_12.setObjectName(_fromUtf8("push_2_12"))
        self.push_2_11 = QtGui.QPushButton(Dialog)
        self.push_2_11.setGeometry(QtCore.QRect(540, 220, 31, 27))
        self.push_2_11.setText(_fromUtf8(""))
        self.push_2_11.setObjectName(_fromUtf8("push_2_11"))
        self.push_2_13 = QtGui.QPushButton(Dialog)
        self.push_2_13.setGeometry(QtCore.QRect(630, 220, 31, 27))
        self.push_2_13.setText(_fromUtf8(""))
        self.push_2_13.setObjectName(_fromUtf8("push_2_13"))
        self.push_2_5 = QtGui.QPushButton(Dialog)
        self.push_2_5.setGeometry(QtCore.QRect(290, 220, 31, 27))
        self.push_2_5.setText(_fromUtf8(""))
        self.push_2_5.setObjectName(_fromUtf8("push_2_5"))
        self.push_2_2 = QtGui.QPushButton(Dialog)
        self.push_2_2.setGeometry(QtCore.QRect(160, 220, 31, 27))
        self.push_2_2.setText(_fromUtf8(""))
        self.push_2_2.setObjectName(_fromUtf8("push_2_2"))
        self.push_2_7 = QtGui.QPushButton(Dialog)
        self.push_2_7.setGeometry(QtCore.QRect(370, 220, 31, 27))
        self.push_2_7.setText(_fromUtf8(""))
        self.push_2_7.setObjectName(_fromUtf8("push_2_7"))
        self.push_2_9 = QtGui.QPushButton(Dialog)
        self.push_2_9.setGeometry(QtCore.QRect(460, 220, 31, 27))
        self.push_2_9.setText(_fromUtf8(""))
        self.push_2_9.setObjectName(_fromUtf8("push_2_9"))
        self.push_2_1 = QtGui.QPushButton(Dialog)
        self.push_2_1.setGeometry(QtCore.QRect(120, 220, 31, 27))
        self.push_2_1.setText(_fromUtf8(""))
        self.push_2_1.setObjectName(_fromUtf8("push_2_1"))
        self.push_2_14 = QtGui.QPushButton(Dialog)
        self.push_2_14.setGeometry(QtCore.QRect(670, 220, 31, 27))
        self.push_2_14.setText(_fromUtf8(""))
        self.push_2_14.setObjectName(_fromUtf8("push_2_14"))
        self.push_2_6 = QtGui.QPushButton(Dialog)
        self.push_2_6.setGeometry(QtCore.QRect(330, 220, 31, 27))
        self.push_2_6.setText(_fromUtf8(""))
        self.push_2_6.setObjectName(_fromUtf8("push_2_6"))
        self.push_3_4 = QtGui.QPushButton(Dialog)
        self.push_3_4.setGeometry(QtCore.QRect(240, 180, 31, 27))
        self.push_3_4.setText(_fromUtf8(""))
        self.push_3_4.setObjectName(_fromUtf8("push_3_4"))
        self.push_3_15 = QtGui.QPushButton(Dialog)
        self.push_3_15.setGeometry(QtCore.QRect(710, 180, 31, 27))
        self.push_3_15.setText(_fromUtf8(""))
        self.push_3_15.setObjectName(_fromUtf8("push_3_15"))
        self.push_3_3 = QtGui.QPushButton(Dialog)
        self.push_3_3.setGeometry(QtCore.QRect(200, 180, 31, 27))
        self.push_3_3.setText(_fromUtf8(""))
        self.push_3_3.setObjectName(_fromUtf8("push_3_3"))
        self.push_3_10 = QtGui.QPushButton(Dialog)
        self.push_3_10.setGeometry(QtCore.QRect(500, 180, 31, 27))
        self.push_3_10.setText(_fromUtf8(""))
        self.push_3_10.setObjectName(_fromUtf8("push_3_10"))
        self.push_3_16 = QtGui.QPushButton(Dialog)
        self.push_3_16.setGeometry(QtCore.QRect(750, 180, 31, 27))
        self.push_3_16.setText(_fromUtf8(""))
        self.push_3_16.setObjectName(_fromUtf8("push_3_16"))
        self.push_3_8 = QtGui.QPushButton(Dialog)
        self.push_3_8.setGeometry(QtCore.QRect(410, 180, 31, 27))
        self.push_3_8.setText(_fromUtf8(""))
        self.push_3_8.setObjectName(_fromUtf8("push_3_8"))
        self.push_3_12 = QtGui.QPushButton(Dialog)
        self.push_3_12.setGeometry(QtCore.QRect(580, 180, 31, 27))
        self.push_3_12.setText(_fromUtf8(""))
        self.push_3_12.setObjectName(_fromUtf8("push_3_12"))
        self.push_3_11 = QtGui.QPushButton(Dialog)
        self.push_3_11.setGeometry(QtCore.QRect(540, 180, 31, 27))
        self.push_3_11.setText(_fromUtf8(""))
        self.push_3_11.setObjectName(_fromUtf8("push_3_11"))
        self.push_3_13 = QtGui.QPushButton(Dialog)
        self.push_3_13.setGeometry(QtCore.QRect(630, 180, 31, 27))
        self.push_3_13.setText(_fromUtf8(""))
        self.push_3_13.setObjectName(_fromUtf8("push_3_13"))
        self.push_3_5 = QtGui.QPushButton(Dialog)
        self.push_3_5.setGeometry(QtCore.QRect(290, 180, 31, 27))
        self.push_3_5.setText(_fromUtf8(""))
        self.push_3_5.setObjectName(_fromUtf8("push_3_5"))
        self.push_3_2 = QtGui.QPushButton(Dialog)
        self.push_3_2.setGeometry(QtCore.QRect(160, 180, 31, 27))
        self.push_3_2.setText(_fromUtf8(""))
        self.push_3_2.setObjectName(_fromUtf8("push_3_2"))
        self.push_3_7 = QtGui.QPushButton(Dialog)
        self.push_3_7.setGeometry(QtCore.QRect(370, 180, 31, 27))
        self.push_3_7.setText(_fromUtf8(""))
        self.push_3_7.setObjectName(_fromUtf8("push_3_7"))
        self.push_3_9 = QtGui.QPushButton(Dialog)
        self.push_3_9.setGeometry(QtCore.QRect(460, 180, 31, 27))
        self.push_3_9.setText(_fromUtf8(""))
        self.push_3_9.setObjectName(_fromUtf8("push_3_9"))
        self.push_3_1 = QtGui.QPushButton(Dialog)
        self.push_3_1.setGeometry(QtCore.QRect(120, 180, 31, 27))
        self.push_3_1.setText(_fromUtf8(""))
        self.push_3_1.setDefault(False)
        self.push_3_1.setObjectName(_fromUtf8("push_3_1"))
        self.push_3_14 = QtGui.QPushButton(Dialog)
        self.push_3_14.setGeometry(QtCore.QRect(670, 180, 31, 27))
        self.push_3_14.setText(_fromUtf8(""))
        self.push_3_14.setObjectName(_fromUtf8("push_3_14"))
        self.push_3_6 = QtGui.QPushButton(Dialog)
        self.push_3_6.setGeometry(QtCore.QRect(330, 180, 31, 27))
        self.push_3_6.setText(_fromUtf8(""))
        self.push_3_6.setObjectName(_fromUtf8("push_3_6"))
        self.push_4_4 = QtGui.QPushButton(Dialog)
        self.push_4_4.setGeometry(QtCore.QRect(240, 140, 31, 27))
        self.push_4_4.setText(_fromUtf8(""))
        self.push_4_4.setObjectName(_fromUtf8("push_4_4"))
        self.push_4_15 = QtGui.QPushButton(Dialog)
        self.push_4_15.setGeometry(QtCore.QRect(710, 140, 31, 27))
        self.push_4_15.setText(_fromUtf8(""))
        self.push_4_15.setObjectName(_fromUtf8("push_4_15"))
        self.push_4_3 = QtGui.QPushButton(Dialog)
        self.push_4_3.setGeometry(QtCore.QRect(200, 140, 31, 27))
        self.push_4_3.setText(_fromUtf8(""))
        self.push_4_3.setObjectName(_fromUtf8("push_4_3"))
        self.push_4_10 = QtGui.QPushButton(Dialog)
        self.push_4_10.setGeometry(QtCore.QRect(500, 140, 31, 27))
        self.push_4_10.setText(_fromUtf8(""))
        self.push_4_10.setObjectName(_fromUtf8("push_4_10"))
        self.push_4_16 = QtGui.QPushButton(Dialog)
        self.push_4_16.setGeometry(QtCore.QRect(750, 140, 31, 27))
        self.push_4_16.setText(_fromUtf8(""))
        self.push_4_16.setObjectName(_fromUtf8("push_4_16"))
        self.push_4_8 = QtGui.QPushButton(Dialog)
        self.push_4_8.setGeometry(QtCore.QRect(410, 140, 31, 27))
        self.push_4_8.setText(_fromUtf8(""))
        self.push_4_8.setObjectName(_fromUtf8("push_4_8"))
        self.push_4_12 = QtGui.QPushButton(Dialog)
        self.push_4_12.setGeometry(QtCore.QRect(580, 140, 31, 27))
        self.push_4_12.setText(_fromUtf8(""))
        self.push_4_12.setObjectName(_fromUtf8("push_4_12"))
        self.push_4_11 = QtGui.QPushButton(Dialog)
        self.push_4_11.setGeometry(QtCore.QRect(540, 140, 31, 27))
        self.push_4_11.setText(_fromUtf8(""))
        self.push_4_11.setObjectName(_fromUtf8("push_4_11"))
        self.push_4_13 = QtGui.QPushButton(Dialog)
        self.push_4_13.setGeometry(QtCore.QRect(630, 140, 31, 27))
        self.push_4_13.setText(_fromUtf8(""))
        self.push_4_13.setObjectName(_fromUtf8("push_4_13"))
        self.push_4_5 = QtGui.QPushButton(Dialog)
        self.push_4_5.setGeometry(QtCore.QRect(290, 140, 31, 27))
        self.push_4_5.setText(_fromUtf8(""))
        self.push_4_5.setObjectName(_fromUtf8("push_4_5"))
        self.push_4_2 = QtGui.QPushButton(Dialog)
        self.push_4_2.setGeometry(QtCore.QRect(160, 140, 31, 27))
        self.push_4_2.setText(_fromUtf8(""))
        self.push_4_2.setObjectName(_fromUtf8("push_4_2"))
        self.push_4_7 = QtGui.QPushButton(Dialog)
        self.push_4_7.setGeometry(QtCore.QRect(370, 140, 31, 27))
        self.push_4_7.setText(_fromUtf8(""))
        self.push_4_7.setObjectName(_fromUtf8("push_4_7"))
        self.push_4_9 = QtGui.QPushButton(Dialog)
        self.push_4_9.setGeometry(QtCore.QRect(460, 140, 31, 27))
        self.push_4_9.setText(_fromUtf8(""))
        self.push_4_9.setObjectName(_fromUtf8("push_4_9"))
        self.push_4_1 = QtGui.QPushButton(Dialog)
        self.push_4_1.setEnabled(True)
        self.push_4_1.setGeometry(QtCore.QRect(120, 140, 31, 27))
        self.push_4_1.setText(_fromUtf8(""))
        self.push_4_1.setObjectName(_fromUtf8("push_4_1"))
        self.push_4_14 = QtGui.QPushButton(Dialog)
        self.push_4_14.setGeometry(QtCore.QRect(670, 140, 31, 27))
        self.push_4_14.setText(_fromUtf8(""))
        self.push_4_14.setObjectName(_fromUtf8("push_4_14"))
        self.push_4_6 = QtGui.QPushButton(Dialog)
        self.push_4_6.setGeometry(QtCore.QRect(330, 140, 31, 27))
        self.push_4_6.setText(_fromUtf8(""))
        self.push_4_6.setObjectName(_fromUtf8("push_4_6"))
        self.push_5_4 = QtGui.QPushButton(Dialog)
        self.push_5_4.setGeometry(QtCore.QRect(240, 100, 31, 27))
        self.push_5_4.setText(_fromUtf8(""))
        self.push_5_4.setObjectName(_fromUtf8("push_5_4"))
        self.push_5_15 = QtGui.QPushButton(Dialog)
        self.push_5_15.setGeometry(QtCore.QRect(710, 100, 31, 27))
        self.push_5_15.setText(_fromUtf8(""))
        self.push_5_15.setObjectName(_fromUtf8("push_5_15"))
        self.push_5_3 = QtGui.QPushButton(Dialog)
        self.push_5_3.setGeometry(QtCore.QRect(200, 100, 31, 27))
        self.push_5_3.setText(_fromUtf8(""))
        self.push_5_3.setObjectName(_fromUtf8("push_5_3"))
        self.push_5_10 = QtGui.QPushButton(Dialog)
        self.push_5_10.setGeometry(QtCore.QRect(500, 100, 31, 27))
        self.push_5_10.setText(_fromUtf8(""))
        self.push_5_10.setObjectName(_fromUtf8("push_5_10"))
        self.push_5_16 = QtGui.QPushButton(Dialog)
        self.push_5_16.setGeometry(QtCore.QRect(750, 100, 31, 27))
        self.push_5_16.setText(_fromUtf8(""))
        self.push_5_16.setObjectName(_fromUtf8("push_5_16"))
        self.push_5_8 = QtGui.QPushButton(Dialog)
        self.push_5_8.setGeometry(QtCore.QRect(410, 100, 31, 27))
        self.push_5_8.setText(_fromUtf8(""))
        self.push_5_8.setObjectName(_fromUtf8("push_5_8"))
        self.push_5_12 = QtGui.QPushButton(Dialog)
        self.push_5_12.setGeometry(QtCore.QRect(580, 100, 31, 27))
        self.push_5_12.setText(_fromUtf8(""))
        self.push_5_12.setObjectName(_fromUtf8("push_5_12"))
        self.push_5_11 = QtGui.QPushButton(Dialog)
        self.push_5_11.setGeometry(QtCore.QRect(540, 100, 31, 27))
        self.push_5_11.setText(_fromUtf8(""))
        self.push_5_11.setObjectName(_fromUtf8("push_5_11"))
        self.push_5_13 = QtGui.QPushButton(Dialog)
        self.push_5_13.setGeometry(QtCore.QRect(630, 100, 31, 27))
        self.push_5_13.setText(_fromUtf8(""))
        self.push_5_13.setObjectName(_fromUtf8("push_5_13"))
        self.push_5_5 = QtGui.QPushButton(Dialog)
        self.push_5_5.setGeometry(QtCore.QRect(290, 100, 31, 27))
        self.push_5_5.setText(_fromUtf8(""))
        self.push_5_5.setObjectName(_fromUtf8("push_5_5"))
        self.push_5_2 = QtGui.QPushButton(Dialog)
        self.push_5_2.setGeometry(QtCore.QRect(160, 100, 31, 27))
        self.push_5_2.setText(_fromUtf8(""))
        self.push_5_2.setObjectName(_fromUtf8("push_5_2"))
        self.push_5_7 = QtGui.QPushButton(Dialog)
        self.push_5_7.setGeometry(QtCore.QRect(370, 100, 31, 27))
        self.push_5_7.setText(_fromUtf8(""))
        self.push_5_7.setObjectName(_fromUtf8("push_5_7"))
        self.push_5_9 = QtGui.QPushButton(Dialog)
        self.push_5_9.setGeometry(QtCore.QRect(460, 100, 31, 27))
        self.push_5_9.setText(_fromUtf8(""))
        self.push_5_9.setObjectName(_fromUtf8("push_5_9"))
        self.push_5_1 = QtGui.QPushButton(Dialog)
        self.push_5_1.setGeometry(QtCore.QRect(120, 100, 31, 27))
        self.push_5_1.setText(_fromUtf8(""))
        self.push_5_1.setObjectName(_fromUtf8("push_5_1"))
        self.push_5_14 = QtGui.QPushButton(Dialog)
        self.push_5_14.setGeometry(QtCore.QRect(670, 100, 31, 27))
        self.push_5_14.setText(_fromUtf8(""))
        self.push_5_14.setObjectName(_fromUtf8("push_5_14"))
        self.push_5_6 = QtGui.QPushButton(Dialog)
        self.push_5_6.setGeometry(QtCore.QRect(330, 100, 31, 27))
        self.push_5_6.setAutoFillBackground(False)
        self.push_5_6.setText(_fromUtf8(""))
        self.push_5_6.setObjectName(_fromUtf8("push_5_6"))
        self.labelBeat = QtGui.QLabel(Dialog)
        self.labelBeat.setGeometry(QtCore.QRect(350, 40, 41, 17))
        self.labelBeat.setObjectName(_fromUtf8("labelBeat"))
        self.labelBPM = QtGui.QLabel(Dialog)
        self.labelBPM.setGeometry(QtCore.QRect(100, 40, 41, 20))
        self.labelBPM.setObjectName(_fromUtf8("labelBPM"))
        self.lineEditTempo = QtGui.QLineEdit(Dialog)
        self.lineEditTempo.setGeometry(QtCore.QRect(152, 40, 51, 27))
        self.lineEditTempo.setObjectName(_fromUtf8("lineEditTempo"))
        self.pushDownTempo = QtGui.QPushButton(Dialog)
        self.pushDownTempo.setGeometry(QtCore.QRect(210, 40, 31, 27))
        self.pushDownTempo.setObjectName(_fromUtf8("pushDownTempo"))
        self.pushUpTempo = QtGui.QPushButton(Dialog)
        self.pushUpTempo.setGeometry(QtCore.QRect(240, 40, 31, 27))
        self.pushUpTempo.setObjectName(_fromUtf8("pushUpTempo"))
        self.labelRim = QtGui.QLabel(Dialog)
        self.labelRim.setGeometry(QtCore.QRect(50, 190, 41, 17))
        self.labelRim.setObjectName(_fromUtf8("labelRim"))
        self.labelCymbal = QtGui.QLabel(Dialog)
        self.labelCymbal.setGeometry(QtCore.QRect(30, 110, 68, 17))
        self.labelCymbal.setObjectName(_fromUtf8("labelCymbal"))
        self.pushPlay = QtGui.QPushButton(Dialog)
        self.pushPlay.setGeometry(QtCore.QRect(460, 40, 99, 27))
        self.pushPlay.setAutoFillBackground(False)
        self.pushPlay.setObjectName(_fromUtf8("pushPlay"))
        self.pushReset = QtGui.QPushButton(Dialog)
        self.pushReset.setGeometry(QtCore.QRect(560, 40, 99, 27))
        self.pushReset.setObjectName(_fromUtf8("pushReset"))
        self.pushStop = QtGui.QPushButton(Dialog)
        self.pushStop.setGeometry(QtCore.QRect(660, 40, 99, 27))
        self.pushStop.setObjectName(_fromUtf8("pushStop"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Tom\'s Drum Machine!", None))
        self.labelBassDrum.setText(_translate("Dialog", "Bass Drum", None))
        self.labelSnare.setText(_translate("Dialog", "Snare", None))
        self.labelHiHat.setText(_translate("Dialog", "Hi Hat", None))
        self.labelBeat.setText(_translate("Dialog", "Beat:", None))
        self.labelBPM.setText(_translate("Dialog", "BPM:", None))
        self.lineEditTempo.setText(_translate("Dialog", "120", None))
        self.pushDownTempo.setText(_translate("Dialog", "<", None))
        self.pushUpTempo.setText(_translate("Dialog", ">", None))
        self.labelRim.setText(_translate("Dialog", "Rim", None))
        self.labelCymbal.setText(_translate("Dialog", "Cymbal", None))
        self.pushPlay.setText(_translate("Dialog", "Play", None))
        self.pushReset.setText(_translate("Dialog", "Reset", None))
        self.pushStop.setText(_translate("Dialog", "Stop", None))

