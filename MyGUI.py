# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiProj.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QLabel, QLayout, QListView, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget, QMessageBox)

from tkinter import Tk

class Ui_knapsackProblem(object):
    def setupUi(self, knapsackProblem):
        if not knapsackProblem.objectName():
            knapsackProblem.setObjectName(u"knapsackProblem")
        knapsackProblem.resize(935, 594)
        knapsackProblem.setContextMenuPolicy(Qt.NoContextMenu)
        knapsackProblem.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(knapsackProblem)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.itemSizeText = QLabel(self.centralwidget)
        self.itemSizeText.setObjectName(u"itemSizeText")
        font = QFont()
        font.setPointSize(14)
        self.itemSizeText.setFont(font)

        self.gridLayout_2.addWidget(self.itemSizeText, 1, 0, 1, 1)

        self.itemValueText = QLabel(self.centralwidget)
        self.itemValueText.setObjectName(u"itemValueText")
        self.itemValueText.setFont(font)

        self.gridLayout_2.addWidget(self.itemValueText, 0, 0, 1, 1)

        self.spinSize = QSpinBox(self.centralwidget)
        self.spinSize.setObjectName(u"spinSize")
        self.spinSize.setMinimum(1)
        self.spinSize.setMaximum(9999999)

        self.gridLayout_2.addWidget(self.spinSize, 1, 1, 1, 1)

        self.spinValue = QSpinBox(self.centralwidget)
        self.spinValue.setObjectName(u"spinValue")
        self.spinValue.setMinimum(1)
        self.spinValue.setMaximum(9999999)

        self.gridLayout_2.addWidget(self.spinValue, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.buttonDeleteItem = QPushButton(self.centralwidget)
        self.buttonDeleteItem.setObjectName(u"buttonDeleteItem")

        self.verticalLayout_2.addWidget(self.buttonDeleteItem)

        self.buttonWriteFileKnapsack = QPushButton(self.centralwidget)
        self.buttonWriteFileKnapsack.setObjectName(u"buttonWriteFileKnapsack")

        self.verticalLayout_2.addWidget(self.buttonWriteFileKnapsack)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 7, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.buttonRun = QPushButton(self.centralwidget)
        self.buttonRun.setObjectName(u"buttonRun")

        self.gridLayout_5.addWidget(self.buttonRun, 0, 0, 1, 1)

        self.solutionText = QLabel(self.centralwidget)
        self.solutionText.setObjectName(u"solutionText")
        self.solutionText.setFont(font)
        self.solutionText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.solutionText, 1, 0, 1, 1)

        self.solutionTextOutput = QTextEdit(self.centralwidget)
        self.solutionTextOutput.setObjectName(u"solutionTextOutput")
        font1 = QFont()
        font1.setPointSize(11)
        self.solutionTextOutput.setFont(font1)
        self.solutionTextOutput.setReadOnly(True)

        self.gridLayout_5.addWidget(self.solutionTextOutput, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 2, 2, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ListOfItemsText = QLabel(self.centralwidget)
        self.ListOfItemsText.setObjectName(u"ListOfItemsText")
        self.ListOfItemsText.setFont(font)

        self.gridLayout_4.addWidget(self.ListOfItemsText, 2, 0, 1, 1)

        self.listOfItems = QListView(self.centralwidget)
        self.listOfItems.setObjectName(u"listOfItems")

        self.gridLayout_4.addWidget(self.listOfItems, 3, 0, 1, 1)

        self.buttonAddItem = QPushButton(self.centralwidget)
        self.buttonAddItem.setObjectName(u"buttonAddItem")

        self.gridLayout_4.addWidget(self.buttonAddItem, 0, 0, 1, 1)

        self.buttonReadFileKnapsack = QPushButton(self.centralwidget)
        self.buttonReadFileKnapsack.setObjectName(u"buttonReadFileKnapsack")

        self.gridLayout_4.addWidget(self.buttonReadFileKnapsack, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 1, 12, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.mutableText = QLabel(self.centralwidget)
        self.mutableText.setObjectName(u"mutableText")
        self.mutableText.setFont(font)

        self.gridLayout.addWidget(self.mutableText, 4, 0, 1, 1)

        self.crossText = QLabel(self.centralwidget)
        self.crossText.setObjectName(u"crossText")
        self.crossText.setFont(font)

        self.gridLayout.addWidget(self.crossText, 3, 0, 1, 1)

        self.knapsackSizeText = QLabel(self.centralwidget)
        self.knapsackSizeText.setObjectName(u"knapsackSizeText")
        self.knapsackSizeText.setFont(font)

        self.gridLayout.addWidget(self.knapsackSizeText, 0, 0, 1, 1)

        self.algorithmIterationsText = QLabel(self.centralwidget)
        self.algorithmIterationsText.setObjectName(u"algorithmIterationsText")
        self.algorithmIterationsText.setFont(font)

        self.gridLayout.addWidget(self.algorithmIterationsText, 1, 0, 1, 1)

        self.individualsText = QLabel(self.centralwidget)
        self.individualsText.setObjectName(u"individualsText")
        self.individualsText.setFont(font)

        self.gridLayout.addWidget(self.individualsText, 2, 0, 1, 1)

        self.spinKnapsackSize = QSpinBox(self.centralwidget)
        self.spinKnapsackSize.setObjectName(u"spinKnapsackSize")
        self.spinKnapsackSize.setMinimum(1)
        self.spinKnapsackSize.setMaximum(999999999)

        self.gridLayout.addWidget(self.spinKnapsackSize, 0, 1, 1, 1)

        self.spinIterations = QSpinBox(self.centralwidget)
        self.spinIterations.setObjectName(u"spinIterations")
        self.spinIterations.setMinimum(1)
        self.spinIterations.setMaximum(9999)

        self.gridLayout.addWidget(self.spinIterations, 1, 1, 1, 1)

        self.spinIndividuals = QSpinBox(self.centralwidget)
        self.spinIndividuals.setObjectName(u"spinIndividuals")
        self.spinIndividuals.setMinimum(2)
        self.spinIndividuals.setMaximum(99)

        self.gridLayout.addWidget(self.spinIndividuals, 2, 1, 1, 1)

        self.spinCrossProbab = QDoubleSpinBox(self.centralwidget)
        self.spinCrossProbab.setObjectName(u"spinCrossProbab")
        self.spinCrossProbab.setMaximum(1.000000000000000)
        self.spinCrossProbab.setSingleStep(0.010000000000000)
        self.spinCrossProbab.setValue(0.200000000000000)

        self.gridLayout.addWidget(self.spinCrossProbab, 3, 1, 1, 1)

        self.spinMutProbab = QDoubleSpinBox(self.centralwidget)
        self.spinMutProbab.setObjectName(u"spinMutProbab")
        self.spinMutProbab.setMaximum(1.000000000000000)
        self.spinMutProbab.setSingleStep(0.010000000000000)
        self.spinMutProbab.setValue(0.200000000000000)

        self.gridLayout.addWidget(self.spinMutProbab, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.buttonWriteSolution = QPushButton(self.centralwidget)
        self.buttonWriteSolution.setObjectName(u"buttonWriteSolution")

        self.verticalLayout_4.addWidget(self.buttonWriteSolution)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 7, 2, 1, 1)

        knapsackProblem.setCentralWidget(self.centralwidget)

        self.msgBoxRunAlg = QMessageBox()
        self.msgBoxRunAlg.setWindowTitle("Algorithm run error!")
        self.msgBoxRunAlg.setDefaultButton(QMessageBox.Ignore)
        self.msgBoxRunAlg1 = QMessageBox()
        self.msgBoxRunAlg1.setWindowTitle("Algorithm no solution found!")
        self.msgBoxRunAlg1.setDefaultButton(QMessageBox.Ignore)
        self.msgBoxWrietSol = QMessageBox()
        self.msgBoxWrietSol.setWindowTitle("Solution saved!")
        self.msgBoxWrietSol.setDefaultButton(QMessageBox.Ignore)
        self.msgBoxWriteKnap = QMessageBox()
        self.msgBoxWriteKnap.setWindowTitle("Knapsack saved!")
        self.msgBoxWriteKnap.setDefaultButton(QMessageBox.Ignore)
        self.msgBoxReadKnap = QMessageBox()
        self.msgBoxReadKnap.setWindowTitle("Read error!")
        self.msgBoxReadKnap.setDefaultButton(QMessageBox.Ignore)
        self.msgBoxReadKnap1 = QMessageBox()
        self.msgBoxReadKnap1.setWindowTitle("Read error!")
        self.msgBoxReadKnap1.setDefaultButton(QMessageBox.Ignore)

        self.pathReader = Tk()
        self.pathReader.withdraw()

        self.retranslateUi(knapsackProblem)

        QMetaObject.connectSlotsByName(knapsackProblem)
    # setupUi

    def retranslateUi(self, knapsackProblem):
        knapsackProblem.setWindowTitle(QCoreApplication.translate("knapsackProblem", u"Knapsack Problem", None))
        self.itemSizeText.setText(QCoreApplication.translate("knapsackProblem", u"Item's Size:", None))
        self.itemValueText.setText(QCoreApplication.translate("knapsackProblem", u"Item's Value:", None))
        self.buttonDeleteItem.setText(QCoreApplication.translate("knapsackProblem", u"Delete selected item from knapsack", None))
        self.buttonWriteFileKnapsack.setText(QCoreApplication.translate("knapsackProblem", u"Save knapsack to file", None))
        self.buttonRun.setText(QCoreApplication.translate("knapsackProblem", u"Run algorithm", None))
        self.solutionText.setText(QCoreApplication.translate("knapsackProblem", u"Solution Found:", None))
        self.ListOfItemsText.setText(QCoreApplication.translate("knapsackProblem", u"Items:", None))
        self.buttonAddItem.setText(QCoreApplication.translate("knapsackProblem", u"Add item to knapsack", None))
        self.buttonReadFileKnapsack.setText(QCoreApplication.translate("knapsackProblem", u"Read knapsack from file", None))
        self.mutableText.setText(QCoreApplication.translate("knapsackProblem", u"Probability Of Mutation:", None))
        self.crossText.setText(QCoreApplication.translate("knapsackProblem", u"Probability Of Cross:", None))
        self.knapsackSizeText.setText(QCoreApplication.translate("knapsackProblem", u"Knapsack Size:", None))
        self.algorithmIterationsText.setText(QCoreApplication.translate("knapsackProblem", u"Numers Of Algorithm Iterations:", None))
        self.individualsText.setText(QCoreApplication.translate("knapsackProblem", u"Numers Of Individuals:", None))
        self.buttonWriteSolution.setText(QCoreApplication.translate("knapsackProblem", u"Write solution to file", None))

        self.buttonRun.setEnabled(False)
        self.buttonWriteSolution.setEnabled(False)
        self.buttonWriteFileKnapsack.setEnabled(False)
        self.buttonDeleteItem.setEnabled(False)
        self.msgBoxRunAlg.setText("Algorithm runtime error!\nCheck algorithm params!")
        self.msgBoxRunAlg1.setText("Algorithm error!\nNo solution found!\nTry change items sizes or knapsack size")
        self.msgBoxWrietSol.setText("Your solution has been\nsuccessfully saved to file!")
        self.msgBoxWriteKnap.setText("Your knapsack has been\nsuccessfully saved to file!")
        self.msgBoxReadKnap.setText("Check if your file is exists!")
        self.msgBoxReadKnap1.setText("Check if data in your file is correct!")
    # retranslateUi
