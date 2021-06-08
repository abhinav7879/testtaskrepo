from rest_framework.views import APIView
import requests
from django.http import JsonResponse
import urllib.request,json
from functools import lru_cache


class searchList(APIView):
    @lru_cache(maxsize=None)
    def get (self, request):
        with urllib.request.urlopen("https://sandbox.musement.com/api/v3/activities") as url:
            data = json.loads(url.read().decode())
            print(data)
            return JsonResponse(data, safe=False)


'''commented code showing redis method using form method'''
'''we can set the live time of cache using cache_TTL'''
'''from django.shortcuts import render
from employees.services import get_cache


def recipes_view(request):
    return render(request, 'employees.html', {
        'employees': get_employees()
    })'''
