from django.db import models

# Create your models here.

class info(models.Model):                #Model for user info
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    city=models.CharField(max_length=10)
    Phone_No=models.IntegerField()
    created_at=models.DateTimeField( auto_now_add=True)

class question(models.Model):                       #Model for questions
    Enter_your_question=models.CharField(max_length=100)

