from IGeneticAlgorithm import IGeneticAlgorithm
from IKnapsackProblem import IKnapsackProblem
from ISolutionCounter import ISolutionCounter
from IIndividual import IIndividual
from IMutable import IMutable
from ICrossable import ICrossable
from ILogger import ILogger
from IIndividualCreator import IIndividualCreator
import random, copy, logging

class GeneticAlgorithm(IGeneticAlgorithm):
    def __init__(self, knapsack: IKnapsackProblem, solution: ISolutionCounter, individualCreator: IIndividualCreator,
                 mutation: IMutable, crosser: ICrossable, logger: ILogger):
        super().__init__()
        self._knapsack = knapsack
        self._solution = solution
        self._mutation = mutation
        self._crosser = crosser
        self._logger = logger
        self._individualCreator = individualCreator

    def runAlgorithm(self, numberOfIteration: int, numberOfIndividuals: int, 
                     crossProb: float, mutationProb: float) -> IIndividual | None | int:
        @self._logger.log(logging.INFO)
        def Algorithm(numberOfIteration) -> IIndividual | None:
            #check if algorithm can run
            if numberOfIteration < 1:
                return None
            if numberOfIndividuals < 2:
                return None
            
            self._createIndividuals(numberOfIndividuals)

            bestIndividual = copy.deepcopy(self._individuals[0])
            for _ in range(numberOfIteration):
                #quality check of individuals
                bestIndividual = self._qualityCheck(bestIndividual)
                #cross
                self._cross(crossProb)
                #mutation
                self._mutate(mutationProb)
            #check if solucion was find
            bestIndividual.countFitness(self._knapsack)
            if bestIndividual.fitness < 0:
                return 0
            return bestIndividual
        return Algorithm(numberOfIteration)

    def _mutate(self, mutationProb):
        @self._logger.log(logging.DEBUG)
        def mutate():
            for i in self._individuals:
                self._mutation.mutation(mutationProb, i)

            return self._returnerForLogger()
        mutate()

    def _cross(self, crossProb):
        @self._logger.log(logging.DEBUG)
        def cross():
            childrensGenotypes = []
            while(len(childrensGenotypes) != len(self._individuals)):
                parentsID = self._getParentsID()
                #random numer [0;1]
                generateNumer = random.uniform(0, 1)
                #check if cross have to be done
                if generateNumer <= crossProb:
                    self._makeCross(parentsID, childrensGenotypes)
                else:
                    self._dontMakeCross(parentsID, childrensGenotypes)
            self._setGenotypesToChildrens(childrensGenotypes)
            return self._returnerForLogger()
        cross()

    def _returnerForLogger(self):
        #create list of new genotypes
        #it is only for logger
        returner = []
        for i in self._individuals:
            returner.append(i._genotype)
        return returner

    def _qualityCheck(self, bestIndividual: IIndividual):
        @self._logger.log(logging.DEBUG)
        def qualityCheck(bestIndividual):
            for i in self._individuals:
                #count fitness
                i.countFitness(self._knapsack)
                #check if it is better then best
                if i.fitness > bestIndividual.fitness:
                    bestIndividual = copy.deepcopy(i)
            return bestIndividual
        return qualityCheck(bestIndividual)
    
    def _getParentsID(self):
        for i in range(2):
            ID1 = int(random.randint(0, len(self._individuals) - 1))
            ID2 = int(random.randint(0, len(self._individuals) - 1))
            IDs = [0, 0]

            if self._individuals[ID1].fitness > self._individuals[ID2].fitness:
                IDs[i] = ID1
            else:
                IDs[i] = ID2

            return IDs
        
    def _makeCross(self, parentsID:list, newChildrens:list):
        childrens = self._crosser.cross(self._individuals[parentsID[0]], self._individuals[parentsID[1]])
        for i in range(len(childrens)):
            if len(newChildrens) != len(self._individuals):
                newChildrens.append(childrens[i])

    def _dontMakeCross(self, parentsID:list, newChildrens:list):
        for i in range(2):
            if len(newChildrens) != len(self._individuals):
                newChildrens.append(self._individuals[parentsID[i]].getGenotype)
        
    def _setGenotypesToChildrens(self, genotypes):
        for i in range(len(self._individuals)):
            self._individuals[i].setGenotype = copy.deepcopy(genotypes[i])

    def _createIndividuals(self, numerOfIndividuals):
        newIndividuals = []
        size = len(self._knapsack.items)
        for _ in range(numerOfIndividuals):
            newIndividuals.append(self._individualCreator.createItem(self._solution, size))
        self._individuals = newIndividuals
