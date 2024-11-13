from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import GaetaUser


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = GaetaUser
        

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = GaetaUser
        fields = (
            'username',
            'email',
            'phone_number',
            'date_of_birth',
            'password1',
            'password2',
        )


class UserProfileForm(UserChangeForm):
    class Meta:
        model = GaetaUser
        fields = (
            'image',
            'username',
            'email',
            'phone_number',
            'date_of_birth',
            'password',
        )