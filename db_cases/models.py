from db_cases.db_managers import MyManager
from django.db import models

# Create your models here.

class CaseModel(models.Model):

    c1 = models.CharField(max_length=255, default="")
    c2 = models.CharField(max_length=255, default="")
    c3 = models.CharField(max_length=255, default="")


    class Meta:
        # abstract = False #  抽象与否
        # ordering = ("c1", "-c2") #  默认排序规则
        # managed = True #  是否同意django对此模型的管理
        # 这些选项是哪里来的？
        db_table = "db_cases"
