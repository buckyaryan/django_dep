from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from start_app.models import Topic, Webpage, Access
from start_app.forms import NewUserForm, UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     webpages_list = Access.objects.order_by('date')
#     my_dict = {'access_records':webpages_list}
#     return render(request,'start_app/index.html', context=my_dict)

# def user_details(request):
#     form = NewUserForm()
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("Invalid Form")
#     return render(request,'start_app/users.html', {'form' : form})

# def form_name_view(request):
#     form = FormName()

#     if request.method == 'POST':
#         form = forms.FormName(request.POST)

#         if form.is_valid():
#             print("Validation Success")
#             print("Name :"+ form.cleaned_data['name'])
#             print("Email :"+ form.cleaned_data['email'])
#             print("Text :"+ form.cleaned_data['text'])

#     return render(request,'start_app/form_page.html', {'form':form})

def index(request):
    context_dict = {'text':'Hello World', 'number':100}
    return render(request, 'start_app/index.html', context_dict)

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('start_app:index'))

def other(request):
    return render(request, 'start_app/other.html')

def relative(request):
    return render(request, 'start_app/relative_url.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'start_app/register.html', {'user_form':user_form, 
                                                        'profile_form':profile_form,
                                                        'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('start_app:index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'start_app/login.html',{})    