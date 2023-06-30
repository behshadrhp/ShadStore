from django.urls import reverse, resolve

from store import views

from pytest_django.asserts import assertTemplateUsed, assertContains
import pytest

class TestHomePage():
    """This class is for test home page."""

    @pytest.fixture
    def response(self, client):
        """This function is for response fixture --> SetUp"""
        url = reverse('home')
        response = client.get(url)
        return response

    def test_url_response(self, response):
        "This function is for test url exists at correct location."
        assert response.status_code == 200

    def test_url_name(self, response):
        """This function is for test url name at home page."""
        assert response.status_code == 200

    def test_template(self, response):
        """This class is for test template at home page."""
        assertTemplateUsed(response, 'home.html')

    def test_home_page_content(self, response):
        """This function is for test content html at home page."""
        assertContains(response, 'Home')

    def test_resolve_url_home_page(self, response):
        """This function is for test resolve url home pate at views."""
        view = resolve('/')
        assert view.func.__name__ == views.HomeView.as_view().__name__
