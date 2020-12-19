from django.shortcuts import render
from django.http import HttpResponse
from index_app.models import User
from index_app import forms

# Create your views here.

def index(request):
  return render(request, 'index/index.html', context={"index_page": "Jaha detta är startsidan"})

def help(request):
  my_dict = {'help_page': 'Det här är help page, denna text kommer ifrån index-funktionen i index_app/views'}
  return render(request, 'help/index.html', context=my_dict)

def bild(request):
  my_dict = {'bild_page': 'Det här är bildsidan'}
  return render(request, 'bild/index.html', context=my_dict)

def users(request):
  users_list = User.objects.order_by('first_name')
  my_dict = {'users' : users_list}
  return render(request, 'users/index.html', context=my_dict)

def create_user(request):
  form = forms.UserForm()
  my_dict = {'form' : form}

  if request.method == 'POST':
    user_form_input = forms.UserForm(request.POST)

    if user_form_input.is_valid():
      print("Username: " + user_form_input.cleaned_data['user'])
      print("First name: " + user_form_input.cleaned_data['first_name'])
      print("Last name: " + user_form_input.cleaned_data['last_name'])
      print("Email: " + user_form_input.cleaned_data['email'])
      user_form_input.save()

      #denna länkar om till views.users efter att formuläret skickats
      return users(request)

  return render(request, 'create_user/index.html', context=my_dict)



# def help(request):
#   my_dict = {'help_page': 'Det här är help page, denna text kommer ifrån index-funktionen i index_app/views'}
#   return render(request, 'help/index.html', context=my_dict)
