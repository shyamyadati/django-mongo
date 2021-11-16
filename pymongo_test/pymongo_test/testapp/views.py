from django.shortcuts import render
from django.views import View
from utils import get_db_handle
from django.http import HttpResponse, HttpRequest

# Create your views here.
def my_test_view(request: HttpRequest) -> HttpResponse:
    
