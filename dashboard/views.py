from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import chatDatabase

def loadDashboard(request):
    template = loader.get_template('dashboard/dashboardTemplate.html')
    message = ''
    allMessages = chatDatabase.objects.all()
    if request.method == 'POST':
        message = request.POST.get('msgbox', 'default message')     #my_var = dict.get(<key>, <default>). Without MultiValueDict's get method request.POST['msgbox'] gives MultiValueDictKeyError.
        noOfMessages = chatDatabase.objects.filter().count()
        msgToSave = chatDatabase()
        msgToSave.serialNo = noOfMessages+1
        msgToSave.username = request.session['loggedInUsername']
        msgToSave.message = message
        msgToSave.save()
    
    context={
        'user': request.session['loggedInUsername'],
        'message': message,
        'allMessages': allMessages,
    }
    return HttpResponse(template.render(context, request))
