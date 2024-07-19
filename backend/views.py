from django.http import JsonResponse
from .models import Person,Expense
from .serializers import PersonSerializer,ExpenseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def person_list(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many= True)
    return JsonResponse({'Persons':serializer.data})

@api_view(['GET'])
def person_get_by_id(request,id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PersonSerializer(person)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def person_add(request):
    serializer = PersonSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def person_update_by_id(request,id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = PersonSerializer(person, data =request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def person_delete_by_id(request,id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    person.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)    

@api_view(['GET'])
def expense_list(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many= True)
    return JsonResponse({'Expenses':serializer.data})

@api_view(['GET'])
def expense_get_by_id(request,id):
    try:
        expense = Expense.objects.get(pk=id)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ExpenseSerializer(expense)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def expense_get_list_by_person_id(request,person_id):
    try:
        expenses = Expense.objects.filter(person_id=person_id)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ExpenseSerializer(expenses, many=True)
    return JsonResponse({'Expenses':serializer.data})

@api_view(['POST'])
def expense_add(request):
    serializer = ExpenseSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def expense_update_by_id(request,id):
    try:
        expense = Expense.objects.get(pk=id)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ExpenseSerializer(expense, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def expense_delete_by_id(request,id):
    try:
        expense = Expense.objects.get(pk=id)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    expense.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)    