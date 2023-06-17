from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed, assertContains

import pytest

from accounts.forms import UserCreationForm
from accounts.views import SignUpView

class TestSignUpPage():
    """This class is for test signup page template."""

    @pytest.fixture
    def signup(self, client):
        url = reverse('signup')
        response = client.get(url)
        return response
    
    def test_signup_template(self, signup):
        """This function is for test template response."""
        assert signup.status_code == 200
        assertTemplateUsed(signup, 'registration/signup.html')
        assertContains(signup, 'Sign Up')

    def test_signup_form(self, signup):
        """This function is for test form registration."""
        form = signup.context.get('form')
        assert form.__class__ == UserCreationForm
        assertContains(signup, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        """This function is for signup url path."""
        view = resolve('/accounts/signup/')
        assert view.func.__name__ == SignUpView.as_view().__name__
