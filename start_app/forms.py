from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import UserInfo, UserProfileInfo


# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     confirm_email = forms.EmailField(label='Enter your email again:')
#     text = forms.CharField(widget=forms.Textarea)
#     # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, 
#     #                             validators=[validators.MaxLengthValidator(0)])

#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         cemail = all_clean_data['confirm_email']

#         if email != cemail:
#             raise forms.ValidationError("Make sure Emails Match!")

class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
