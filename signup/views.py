from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import userDetails
from .models import SaveUserDetails

def showSignupPage(request):
    template = loader.get_template('signup/signupTemplate.html')
    
    if request.method == 'POST':
        form = userDetails(request.POST)
        if form.is_valid():
            enteredEmail = form.cleaned_data['email']
            enteredUsername = form.cleaned_data['username']
            enteredPassword = form.cleaned_data['password']
            saveuserdetails = SaveUserDetails()
            saveuserdetails.email = enteredEmail
            saveuserdetails.username = enteredUsername
            saveuserdetails.password = enteredPassword

            #Check if same username or email already exists
            try:
                checkUserDetails = SaveUserDetails.objects.get(username=enteredUsername)   #Exception arises when username doesn't exist in database, as get can not find it.
                hit = True
            except Exception as e:
                hit = False
            if hit:
                context={
                    'form': form,
                    'result': "Username already exists"
                }
                return HttpResponse(template.render(context,request))
            else:
                saveuserdetails.save()
                context={
                    'form': form,
                    'result': "Details saved"
                }
                return HttpResponse(template.render(context,request))
    else:
        form = userDetails()
    context={
        'form': form,
    }
    return HttpResponse(template.render(context, request))

