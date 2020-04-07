from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm, ProductForm
from django.shortcuts import redirect


from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView

# Create your views here.



class Index(TemplateView):
    template_name = 'index.html'


class Invalid_p(TemplateView):
   template_name = 'invalid_page.html'

class Succes_Product_page(TemplateView):
    template_name = 'basic_app/product_succes_adding.html'


def registration(request):
    registerd = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        user_profile = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

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


def Login_View(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        print('username: {}, password: {}'.format(username, password))
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('Index_page'))
            # return HttpResponseRedirect('/basic_app/login_page/')
        else:
            return HttpResponseRedirect(reverse('basic_app:Invalid'))
            # return redirect('/basic_app/login_failed/')  it worked
    else:
        return render(request, 'basic_app/login.html')

@login_required
def LogOut_View(request):
    logout(request)
    return HttpResponseRedirect(reverse('Index_page'))

@login_required
def Product_Adder_View(request):
    
    if request.method == 'POST':
        Prdct_form = ProductForm(request.POST, request.FILES)
        if Prdct_form.is_valid():
            Prdct_form.save()
            return HttpResponseRedirect(reverse('basic_app:Product_added'))
        else:
            raise('Not Valid Form')
    else:
        Prdct_form = ProductForm()
    return render(request, 'basic_app/product_adding.html', context={'Prdct_form':Prdct_form})
