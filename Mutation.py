from IMutable import IMutable
from IIndividual import IIndividual
import random, copy

class Mutation(IMutable):
    def __init__(self):
        super().__init__()

    def mutation(self, mutationProb, individual: IIndividual):
        for i in range(len(individual.getGenotype)):
            #random numer [0;1]
            generateNumer = random.uniform(0, 1)
            newGenotype = copy.deepcopy(individual.getGenotype)
            #if generate numer isnt higher than probability
            if generateNumer <= mutationProb:
                if individual.getGenotype[i] == 0:
                    newGenotype[i] = 1
                else:
                    newGenotype[i] = 0
            individual.setGenotype = newGenotype
