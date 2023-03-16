from django.db import models

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
    id1=models.IntegerField()
    category=models.CharField(max_length=100)
    credit_amount=models.IntegerField()
    debit_amount=models.IntegerField()
    balance=models.IntegerField()
class Query(models.Model):
    query=models.CharField(max_length=100)
    problem=models.CharField(max_length=1000)
    