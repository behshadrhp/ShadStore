from django.urls import reverse, resolve

from store import views

from pytest_django.asserts import assertTemplateUsed, assertContains
import pytest


class TestAboutPage():
    """This class is for test about page."""

    @pytest.fixture
    def response(self, client):
        """This function is for response fixture --> SetUp"""
        url = reverse('about')
        response = client.get(url)
        return response
    
    def test_about_page(self, response):
        "This function is for test url exists at correct location."
        assert response.status_code == 200

    def test_about_page_template(self, response):
         """This class is for test template at about page."""
        assertTemplateUsed(response, 'about.html')

    def test_about_page_contains_correct_html(self, response):
        """This function is for test content html at about page."""
        assertContains(response, "About Page")

    def test_about_page_url_resolve(self):
        """This function is for test resolve url about pate at views."""
        view = resolve('/about/')
        assert view.func.__name__ == views.AboutView.as_view().__name__
