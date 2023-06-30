from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm


User = get_user_model()

class UserCreationForm(BaseUserCreationForm):
    """This class is for user create form."""
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )

class UserChangeForm(BaseUserChangeForm):
    """This class is for user change form."""
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )
