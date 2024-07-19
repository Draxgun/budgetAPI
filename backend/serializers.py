from rest_framework import serializers 
from .models import Person,Expense

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['person_id','name','budget']
        read_only_fields = ['person_id']
        

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['expense_id','name','person','amount']
        read_only_fields = ['expense_id']

