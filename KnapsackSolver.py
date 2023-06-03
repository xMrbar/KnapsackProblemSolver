import sys
from KnapsackItem import KnapsackItem
from KnapsackProblem import KnapsackProblem
from SolutionCounter import SolutionCounter
from Individual import Individual
from GeneticAlgorithm import GeneticAlgorithm
from Crosser import Crosser
from Mutation import Mutation
from Validator import Validator
from Logger import Logger
from ItemCreator import ItemCreator
from Reader import Reader
from WriteKnapsack import WriteKnapsack
from WriteSolution import WriteSolution
from IndividualCreator import IndividualCreator
import logging, traceback
import PySide6.QtWidgets as ps6
from GUILogic import GUILogic

class App():
    def __init__(self):
        self.app = ps6.QApplication(sys.argv)
        self.knapsack = KnapsackProblem(1)
        self.logger = Logger(logging.DEBUG)
        self.solutionCount = SolutionCounter()
        self.individualCreator = IndividualCreator()
        self.crosser = Crosser(self.solutionCount)
        self.mutator = Mutation()
        self.genAlgorithm = GeneticAlgorithm(self.knapsack, self.solutionCount, self.individualCreator,
                                             self.mutator, self.crosser, self.logger)
        self.itemCrator = ItemCreator()
        self.solutoinWriter = WriteSolution(self.logger)
        self.knapsackWriter = WriteKnapsack(self.logger)
        self.knapsackReader = Reader(self.logger)
        self.validator = Validator(self.logger)
        self.window = GUILogic(self.itemCrator, self.knapsack, self.genAlgorithm, self.validator, 
                               self.solutoinWriter, self.knapsackWriter, self.knapsackReader)

    def run(self):
        self.window.show()
        self.app.exec()
    
def main():
    app = App()
    app.run()
    return 0

if __name__ == '__main__':
    sys.exit(main())