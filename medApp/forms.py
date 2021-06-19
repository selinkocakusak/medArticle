from django import forms
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.models import User
from .models import UserInfo
# from dal import autocomplete


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'password')


# class WiForm(forms.Form):
#     dataLabel = autocomplete.Select2ListChoiceField(
#         widget=autocomplete.ListSelect2(url='tag'),
#         label="Choose the tag"

#     )

# class CommentForm(forms.ModelForm):
#
#     class Meta:
#         model = Comment
#         fields = ["comment"]

# from django.core import validators
# from medApp.models import User
#
# class newUserForm(forms.ModelForm):
#     class Meta():
#         model=User
#         fields = '__all__'


# class Form_Name(forms.Form):
#     formname=forms.CharField()
#     formemail=forms.EmailField()
#     verifyEmail = forms.EmailField(label="Please re-enter your email: ")
#
#
#     def clean(self):
#         cleanAllData = super().clean()
#         email=cleanAllData['formemail']
#         verEmail=cleanAllData['verifyEmail']
#
#         if formemail != verifyEmail:
#             raise forms.ValidationError("Please make sure if the email addresses match")
