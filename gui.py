from translator import main, save, LANGUAGES

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton,
                               QSizePolicy, QSpacerItem, QStatusBar,
                               QTextBrowser, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Translator")
        MainWindow.resize(304, 406)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_4.addWidget(self.comboBox, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_4.addWidget(self.comboBox_2, 1, 2, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 1, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        self.label_2.setFont(font)

        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1, Qt.AlignHCenter)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 2, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        self.label.setFont(font1)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 2, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 0, 1, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei Light"])
        self.textBrowser.setFont(font2)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_8.addWidget(self.textBrowser, 2, 0, 1, 3)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI Light"])
        self.lineEdit.setFont(font3)

        self.gridLayout_8.addWidget(self.lineEdit, 0, 0, 1, 3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.gridLayout_8.addWidget(self.pushButton, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum,
                                          QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        self.gridLayout_8.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setFont(font2)
        self.textBrowser_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_8.addWidget(self.textBrowser_2, 3, 0, 1, 3)

        self.gridLayout.addLayout(self.gridLayout_8, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.setEnabled(False)

        for l in LANGUAGES:
            self.comboBox.addItem(l)
            self.comboBox_2.addItem(l)
        self.comboBox.setCurrentIndex(2)
        self.comboBox_2.setCurrentIndex(3)

        self.pushButton.clicked.connect(self.translate)
        self.pushButton_2.clicked.connect(self.save_button)

    def translate(self):
        """
        Функция, запускающаяся при нажатии на кнопку "Translate"
        """

        words, sentences = main(self.comboBox_2.currentText(),
                                self.comboBox.currentText(), self.lineEdit.text())
        self.update_text_browsers()
        self.textBrowser.append(words)
        self.textBrowser_2.append(sentences)
        self.filename = self.lineEdit.text()
        self.pushButton_2.setEnabled(True)

    def update_text_browsers(self):
        """
        Перед каждым новым введённым словом обновляет textBrowser'ы,
        чтобы у "Word Translations" и "Usage Examples" осталось оформление.
        """

        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'Microsoft YaHei Light'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Word translations:</span></p>\n"
                                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>",
                                                            None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'Microsoft YaHei Light'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Usage examples:</span></p>\n"
                                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                              None))

    def save_button(self):
        """
        Сохраняет результаты перевода в файл при нажатии кнопки.
        """

        output = [f"{self.comboBox_2.currentText()} Word Translations:\n",
                  self.textBrowser.toPlainText(),
                  "\n\n",
                  f"{self.comboBox.currentText()} - {self.comboBox_2.currentText()} Sentence Examples:\n",
                  self.textBrowser_2.toPlainText()]
        output = "".join(output)
        save(self.filename, output)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Target language:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Source language:", None))
        self.update_text_browsers()
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save results to .txt file", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Enter the word you want to translate...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Translate", None))


if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    mw = Ui_MainWindow()
    mw.setupUi(window)
    window.show()
    app.exec()
