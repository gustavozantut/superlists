from email.policy import default
from django.db import models

class List(models.Model):
	pass

class Item(models.Model):
	text = models.TextField(default='')
	priority = models.CharField(choices=[("sem prioridade","sem prioridade"),("alta","alta"),("média","média"),("baixa","baixa")], default="sem prioridade", max_length=20)
	list = models.ForeignKey(List,on_delete=models.SET_DEFAULT,default=None)