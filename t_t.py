from itertools import chain, product

import django
django.setup()
from db_cases.models import CaseModel

if __name__ == '__main__':

    # casemodel = CaseModel()
    # type(casemodel).objects.filter()
    # pass

    a = [1,2,3]
    b = [4,5,6]
    for i in product(a,b):
        print(i)
