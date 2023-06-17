from django.contrib.auth import get_user_model

import pytest


User = get_user_model()

class TestUserModel():
    """This class is for Test User Model."""

    @pytest.fixture
    def user(self):
        """This function is for user fixture."""
        return User.objects.create_user('john', 'john@gmail.com', '12345678')
    
    @pytest.fixture
    def superuser(self):
        """This function is for superuser fixture."""
        return User.objects.create_superuser('tom', 'tom@gmail.com', '87654321')
    
    @pytest.mark.django_db
    def test_create_user(self, user):
        """This function is for test simple user model."""
        assert user.username == 'john'
        assert user.email == 'john@gmail.com'
        assert user.is_active == True
        assert user.is_staff == False
        assert user.is_superuser == False

    @pytest.mark.django_db
    def test_create_superuser(self, superuser):
        """This function is for test superuser model."""
        assert superuser.username == 'tom'
        assert superuser.email == 'tom@gmail.com'
        assert superuser.is_active == True
        assert superuser.is_staff == True
        assert superuser.is_superuser == True
