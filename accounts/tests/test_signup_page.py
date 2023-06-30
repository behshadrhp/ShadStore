from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed, assertContains

import pytest


from accounts.views import SignUpView

class TestSignUpPage():
    """This class is for test signup page template."""

    username = "ted"
    email = "ted@email.com"

    @pytest.fixture
    def response(self, client):
        url = reverse('account_signup')
        return client.get(url)
    
    @pytest.mark.django_db
    def test_signup_template(self, response):
        """This function is for test template response."""
        assert response.status_code == 200
        assertTemplateUsed(response, 'account/signup.html')
        assertContains(response, 'Sign Up')

    @pytest.mark.django_db
    def test_signup_form(self):
        """This function is for test form registration."""
        user = get_user_model().objects.create_user(self.username, self.email)
        assert get_user_model().objects.all().count() == 1
        assert get_user_model().objects.all()[0].username == self.username
        assert get_user_model().objects.all()[0].email == self.email

    def test_signup_view(self):
        """This function is for signup url path."""
        view = resolve('/accounts/signup/')
        assert view.func.__name__ == SignUpView.as_view().__name__
