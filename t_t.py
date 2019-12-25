from functools import reduce
from itertools import chain, product

import django
from django.db.models import Max, Count, Min, Sum

django.setup()
from db_cases.models import CaseModel

if __name__ == '__main__':

    # casemodel = CaseModel()
    # type(casemodel).objects.filter()
    # pass
    #
    # a = [1,2,3]
    # b = [4,5,6]
    # for i in product(a,b):
    #     print(i)
    #
    # CaseModel.objects.using().filter().exclude().delete()
    # CaseModel.objects.update_or_create()
    # CaseModel.objects.aggregate(Max("c1"), Sum())
    # CaseModel.objects.bulk_create()
    # CaseModel.objects.first()
    # CaseModel.objects.last()
    # CaseModel.objects.filter().values()

    a = [1,2,3,4,5,6]
    k = reduce(lambda x,y:x*y, a)
    print(k)
