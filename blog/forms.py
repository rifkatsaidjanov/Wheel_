# Admin paneldan to'ldiriladigan malumotlarni foydalanuvchi xam to'ldira olishi uchun
from django import forms
from .models import Article
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Maqola kiritish uchun
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'year',
            'transmitter',
            'fuel_type',
            'phone',
            'kilometers',
            'color',
            'price',
            'engine_capacity',
            'photo1',
            'photo2',
            'photo3',
            'photo4',
            'photo5',
            'category',
            'content'
        ]

        widgets = {
            # 'title': forms.TextInput(attrs={
            #     'placeholder': 'Название',
            #     'class': 'form-control'
            # }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Описание',
                'class': 'form-control'
            }),
            # 'is_published': forms.CheckboxInput(attrs={
            #     'class': 'form-chek-input'
            # }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            })
        }


# Bu yog'i voyti yani kirish saxifasi uchun form ochish uchun'
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваш username'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваш пароль'
    }))


# Bu yog'i registratsiya saxifasi uchun'
class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))

    # last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Фамилия'
    # }))
    #
    # first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Имя'
    # }))
    #
    # email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Имя пользователя'
    # }))

    password1 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль пользователя'
    }))

    password2 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль'
    }))

    class Meta:
        model = User
        fields = ('username',
                  # 'last_name', 'first_name', 'email',
                  'password1', 'password2')



