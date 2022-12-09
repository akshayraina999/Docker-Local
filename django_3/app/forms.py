from django import forms
from .models import Posts
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['blog_by_author', 'title', 'body', 'category']
        # fields = "__all__"


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

