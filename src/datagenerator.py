import datetime
import random

from candidate import Candidate
from project import Project


class DataGenerator:
    __first_names = ['Alene', 'Alison', 'Alessandra', 'Aleta', 'Alethea', 'Alex', 'Alexa', 'Alexandra', 'Anastasia',
                     'Bob', 'Deedee', 'Denna', 'Deerdre', 'Deeyn', 'Dehlia', 'Deidre', 'Deina', 'Duke', 'Dom', 'Jane',
                     'John', 'Jennifer', 'Scott', 'Greg']
    __last_names = ['Aaronson', 'Ab', 'Aba', 'Abagael', 'Benil', 'Benilda', 'Benildas', 'Benildis', 'White', 'Red',
                    'Green', 'Carpenter', 'Wittrock', 'Black', 'Bandidas', 'Horseshoe', 'Lane']
    __domains = ['IT', 'Household', 'Agriculture', 'Health', 'Insurance', 'Construction', 'Transport', 'Politics',
                 'Human Resources', 'Management', 'Security', 'Banking', 'Investment']

    def __init__(self):
        pass

    def generate_candidates(self, nr):
        rnd_fn = self.generate_first_names(nr)
        rnd_ln = self.generate_last_names(nr)
        result = []

        for x in range(nr):
            experience = self.generate_experience(random.randint(1, 4), False)
            candidate = Candidate(rnd_fn[x], rnd_ln[x], experience)
            result.append(candidate)

        return [cand.serialize() for cand in result]

    def generate_names(self, nr):
        rnd_fn = self.generate_first_names(nr)
        rnd_ln = self.generate_last_names(nr)
        result = [{'first_name': rnd_fn[x], 'last_name': rnd_ln[x]} for x in range(nr)]

        return result

    def generate_first_names(self, nr):
        fn_length = len(self.__first_names)
        result = [self.__first_names[random.randint(0, fn_length - 1)] for x in range(nr)]
        return result

    def generate_last_names(self, nr):
        ln_length = len(self.__last_names)
        result = [self.__last_names[random.randint(0, ln_length - 1)] for x in range(nr)]
        return result

    def generate_experience(self, nr, serialize=False):
        result = []
        for x in range(nr):
            if random.randint(0, 1244) % 2 == 0:
                project_name = '[New] Project ' + self.__first_names[random.randint(0, len(self.__first_names) - 1)]
            else:
                project_name = 'Project ' + self.__last_names[random.randint(0, len(self.__last_names) - 1)]

            start_date = datetime.datetime(random.randint(1990, 2018), random.randint(1, 12), random.randint(1, 28))
            end_date = start_date + datetime.timedelta(days=random.randint(2, 432))
            prj = Project(project_name, start_date, end_date, 'Description for project ' + project_name)
            result.append(prj)

        if serialize:
            return [res.serialize() for res in result]
        else:
            return result
