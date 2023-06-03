from IIndividual import IIndividual
from Individual import Individual
from IIndividualCreator import IIndividualCreator

class IndividualCreator(IIndividualCreator):
    def createItem(self, solution, size) -> IIndividual:
        return Individual(solution, size)