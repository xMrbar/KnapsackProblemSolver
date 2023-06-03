from MyGUI import Ui_knapsackProblem
from IGeneticAlgorithm import IGeneticAlgorithm
from IKnapsackProblem import IKnapsackProblem
from IItemCreator import IItemCreator
from IReader import IReader
from IWritableKnapsack import IWritableKnapsack
from IWritableSolution import IWritableSolution
from IIndividual import IIndividual
from IValidator import IValidator
import PySide6.QtWidgets as ps6
from PySide6.QtCore import QStringListModel
from tkinter.filedialog import askopenfilename

class GUILogic(ps6.QMainWindow, Ui_knapsackProblem):
    def __init__(self, itemCreator: IItemCreator, knapsack: IKnapsackProblem, genAlgorithm: IGeneticAlgorithm, 
                 validator: IValidator, solutionWriter: IWritableSolution, knapsackWriter: IWritableKnapsack, 
                 knapsackReader: IReader):
        super(GUILogic, self).__init__()
        self.setupUi(self)
        #add methods to GUI elements
        self.buttonAddItem.clicked.connect(self.addItem)
        self.buttonDeleteItem.clicked.connect(self.removeItem)
        self.buttonRun.clicked.connect(self.runAlgorithm)
        self.buttonWriteSolution.clicked.connect(self.writeSolutionToFile)
        self.buttonWriteFileKnapsack.clicked.connect(self.writeKnapsackToFile)
        self.buttonReadFileKnapsack.clicked.connect(self.readKnapsackFromFile)
        #fields
        self._model = QStringListModel()
        self._itemsStr = []
        self._model.setStringList(self._itemsStr)
        self.listOfItems.setModel(self._model)

        self._itemCreator: IItemCreator = itemCreator
        self._knapsack: IKnapsackProblem = knapsack
        self._genAlgorthm: IGeneticAlgorithm = genAlgorithm
        self.validator: IValidator = validator
        self.solutionWriter: IWritableSolution = solutionWriter
        self.knapsackWriter: IWritableKnapsack = knapsackWriter
        self.knapsackReader: IReader = knapsackReader

        #Must be like this
        self.filetypes = (("Text files", "*.txt"), ("Text files", "*.txt"))

    def addItem(self):
        self.buttonDeleteItem.setEnabled(True)
        self.buttonWriteFileKnapsack.setEnabled(True)
        self.buttonRun.setEnabled(True)
        #create item
        newItem = self._itemCreator.createItem(self.spinValue.value(), self.spinSize.value())
        newItemStr = f"Size: {self.spinSize.value()};  Value: {self.spinValue.value()}"
        #add it to collections
        self._knapsack.addItem(newItem)
        self._itemsStr.append(newItemStr)
        self._model.setStringList(self._itemsStr)
        #set to first index
        first_index = self.listOfItems.model().index(0, 0)
        self.listOfItems.setCurrentIndex(first_index)

    def removeItem(self):
        #there has to be at least one item
        if len(self._itemsStr) != 0:
            index = self.listOfItems.currentIndex().row()
            self._knapsack.deleteItem(index)
            self._itemsStr.pop(index)
            self._model.setStringList(self._itemsStr)
            first_index = self.listOfItems.model().index(0, 0)
            self.listOfItems.setCurrentIndex(first_index)
        
        #check if no item left
        if len(self._itemsStr) == 0:
            self.buttonDeleteItem.setEnabled(False)
            self.buttonWriteFileKnapsack.setEnabled(False)
            self.buttonRun.setEnabled(False)

    def runAlgorithm(self):
        result = self._genAlgorthm.runAlgorithm(self.spinIterations.value(), self.spinIndividuals.value(),
                                                self.spinCrossProbab.value(), self.spinMutProbab.value())
        if result == None:
            self.msgBoxRunAlg.exec()
            return
        if result == 0:
            self.msgBoxRunAlg1.exec()
            return
        self.buttonWriteSolution.setEnabled(True)
        self._writeResult(result)
        
    def _writeResult(self, result: IIndividual):
        self.solutionTextOutput.clear()
        self._knapsack.setSize = self.spinKnapsackSize.value()
        self.solutionTextOutput.append(f"For knapsack of size: {self._knapsack.size}\nAnd items:\n")
        for i in self._knapsack.items:
            toWrite = f"Size: {i.size} | Value: {i.value}"
            self.solutionTextOutput.append(toWrite)

        self.solutionTextOutput.append(f"The solution is:")
        self.solutionTextOutput.append(str(result))

        self.solutionTextOutput.append(f"\nWe should take items (Value; Size): ")
        for i in range(len(self._knapsack.items)):
            if result.getGenotype[i] == 1:
                item = self._knapsack.items[i]
                toWrite = f"({item.value};{item.size})"
                self.solutionTextOutput.append(toWrite)

    def writeSolutionToFile(self):
        filename = askopenfilename(filetypes=self.filetypes)
        if filename != '':
            self.solutionWriter.writeToFile(filename, self.solutionTextOutput.toPlainText(), 'a')
            self.msgBoxWrietSol.exec()

    def writeKnapsackToFile(self):
        filename = askopenfilename(filetypes=self.filetypes)
        self._knapsack.setSize = int(self.spinKnapsackSize.value())
        if filename != '':
            self.knapsackWriter.writeToFile(filename, self._knapsack, 'w')
            self.msgBoxWriteKnap.exec()

    def readKnapsackFromFile(self):
        filename = askopenfilename(filetypes=self.filetypes)
        if filename != '':
            items = self.knapsackReader.read(filename)

            if items == None:
                self.msgBoxReadKnap.exec()
                return
            if not self.validator.validate(items):
                self.msgBoxReadKnap1.exec()
                return
            #remove all items
            self._removeAllItems()
            #add items
            self.spinKnapsackSize.setValue(int(items[0][0]))
            self._knapsack.setSize = int(items[0][0])
            for i in range (1, len(items)):
                self.spinValue.setValue(int(items[i][0]))
                self.spinSize.setValue(int(items[i][1]))
                self.addItem()

    def _removeAllItems(self):
        length = len(self._itemsStr)
        for i in range (0, length):
            first_index = self.listOfItems.model().index(0, 0)
            self.listOfItems.setCurrentIndex(first_index)
            self.removeItem()