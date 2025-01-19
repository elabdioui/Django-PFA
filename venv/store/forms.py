from django import forms
from .models import Product, CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'type']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'type']

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Password',
            'class': 'placeholder pass',
            'id': 'password',
            'onchange': 'psw_tester()',
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'placeholder user',
                'id': 'name',
                'onchange': 'combined_tester()',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'placeholder email',
                'id': 'email',
                'onchange': 'mail_tester()',
                'required': 'required'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'username',
            'class': 'placeholder user',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Password',
            'class': 'placeholder pass',
            'id': 'login_password',
            'required': 'required'
        })
    )

class FilterProduits(forms.Form):
    name = forms.CharField(required=False)
    price = forms.DecimalField(required=False)
    category = forms.CharField(required=False)
    type = forms.CharField(required=False)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)