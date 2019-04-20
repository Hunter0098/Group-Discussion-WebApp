from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import usernamePassword     #Access usernamePassword function from forms.py
from signup.models import SaveUserDetails

def showLoginPage(request):
    template = loader.get_template('login/loginTemplate.html')  #had to add 'templates' in settings.py dir[]

    if request.method == 'POST':
        if 'login' in request.POST:     #Check which one of login or signup buttons is clicked
            form = usernamePassword(request.POST)
            if form.is_valid():
                enteredUsername = form.cleaned_data['username']     #After form.is_valid() data is accessed using form.cleaned_data['']
                enteredPassword = form.cleaned_data['password']

                #Check if same username and password are correct
                try:
                    checkUserDetails = SaveUserDetails.objects.get(username=enteredUsername)   #Exception arises when username doesn't exist in database, as get can not find it.
                    if checkUserDetails.password == enteredPassword:    #Check if password entered by user is correct
                        hit = True
                    else:
                        hit = False
                except:
                    hit= False

                if hit:
                    request.session['loggedInUsername'] = checkUserDetails.username     #To access data between views https://stackoverflow.com/questions/32787838/how-to-pass-data-between-django-views
                    context={
                        'form': form,
                        'result': "Login Successful",
                        'welcomeUser': "Welcome back, " + checkUserDetails.username,
                    }
                    return HttpResponseRedirect('/dashboard')   #Redirects to /dashboard page
                else:
                    context={
                        'form': form,
                        'result': "Login failed. Please recheck your username and password.",
                    }
                    return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect('/signup')    #Redirects to /signup page
    else:
        form = usernamePassword()
        username = 'empty'
        context={
            'form': form,
            'username': username,
        }
        return HttpResponse(template.render(context, request))
