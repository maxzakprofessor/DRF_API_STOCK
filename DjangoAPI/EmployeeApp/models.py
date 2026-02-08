from django.db import models

# Create your models here.

class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    nameGood = models.CharField(max_length=500)

class Stocks(models.Model):
    id = models.AutoField(primary_key=True)
    nameStock = models.CharField(max_length=500)

class Goodincomes(models.Model):
    id = models.AutoField(primary_key=True)
    idStock = models.IntegerField(default=0)
    nameStock = models.CharField(max_length=500)
    idGood = models.IntegerField(default=0)
    nameGood = models.CharField(max_length=500)
    qty = models.IntegerField(default=0)
    datetime = models.DateTimeField()

class Goodmoves(models.Model):
    id = models.AutoField(primary_key=True)
    nameStockFrom = models.CharField(max_length=500)
    nameStockTowhere = models.CharField(max_length=500)
    nameGood = models.CharField(max_length=500)
    qty = models.IntegerField(default=0)
    datetime = models.DateTimeField()  

class Goodrests(models.Model):
    id = models.AutoField(primary_key=True)
    nameStock = models.CharField(max_length=500)
    nameGood = models.CharField(max_length=500)
    qty = models.IntegerField(default=0)

#commit test
