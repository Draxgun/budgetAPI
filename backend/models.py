from django.db import models

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    budget= models.IntegerField()
    
    def __str__(self):
        return self.name + ' ' + str(self.budget)
    

class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='Tacos')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    amount = models.IntegerField()
    
    def __str__(self):
        return self.person.name + ' ' + self.name + ' ' + str(self.amount)
    