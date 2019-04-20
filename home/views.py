from django.shortcuts import render
from django.http import HttpResponse

def showHome(request):
    html = '<CENTER><H2>Welcome to the chat. Please login to continue</H2><BR><BR><a href="/login"><button style="border: 3px solid #47476b; color: #fff; background-color: #47476b;">Login</button></a></CENTER>'
    return HttpResponse(html)    #When function is called it returns a HttpResponse
