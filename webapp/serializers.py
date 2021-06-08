from rest_framework import serializers as Serializers
from . models import *


class employeesSerializer(Serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'

'''using redis method'''
'''from employees.models import employee


def get_employee():
    
    return list(Employee.objects.prefetch_related('employees'))'''
