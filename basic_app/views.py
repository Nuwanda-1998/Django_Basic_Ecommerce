from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm


from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView

# Create your views here.



class Index(TemplateView):
    template_name = 'index.html'




def registration(request):
    registerd = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        user_profile = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)

            profile = user_profile.save(commit= False)
            profile.user = user
            profile.save()

            registerd = True
        else:
            print(user_form.errors, user_profile.errors)

    else:
        user_form = UserForm()
        user_profile = UserProfileInfoForm()
    
    return render(request, 'registration.html', context={'registerd':registerd, 'user_form':user_form, 'user_profile':user_profile})


