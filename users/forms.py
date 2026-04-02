from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    # Ограничиваем выбор роли для обычной регистрации
    ROLE_CHOICES = (
        ('buyer', 'Покупатель'),
        ('seller', 'Продавец'),
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        initial='buyer',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if password != confirm_password:
            self.add_error('confirm_password', 'Пароли не совпадают')

        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Такой username уже используется')

        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Такой email уже используется')
