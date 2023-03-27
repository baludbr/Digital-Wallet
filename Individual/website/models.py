from django.db import models
import datetime
# Create your models here.
class Register_Login(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    balance=models.IntegerField()
    role=models.CharField(max_length=7, default='user', editable=False)
class Transaction_History(models.Model):
    timestamp_1=models.DateTimeField(default=str(datetime.datetime.now())
    id1=models.IntegerField()
    category=models.CharField(max_length=100)
    type_amount=models.CharField(max_length=100,default=None)
    amount=models.IntegerField()
    balance=models.IntegerField()
class Query(models.Model):
    query=models.CharField(max_length=100)
    problem=models.CharField(max_length=1000)
    