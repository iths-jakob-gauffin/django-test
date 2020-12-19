from django import forms
from index_app.models import User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    # fields = ['user', 'first_name', 'last_name', 'email'] 
    fields = '__all__'

# class UserForm(forms.Form):
#   username = forms.CharField()
#   first_name = forms.CharField()
#   last_name = forms.CharField()
#   email = forms.EmailField()