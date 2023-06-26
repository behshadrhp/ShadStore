from django.contrib.auth import get_user_model
from django.urls import reverse

from books import models

import pytest
from pytest_django.asserts import assertContains, assertTemplateUsed



User = get_user_model()

class BookTest():
    """This class is for test Book model."""

    @pytest.fixture
    def book(self):
        """This function is for create book object."""
        user = User.objects.create_user(
            username='user1',
            email='user1@gmail.com',
            password='12345678'
        )
        book = models.Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='39.99'
        )
        reviews = models.Review.objects.create(
            book=book,
            author=user,
            reviews='hello world'
        )
        
    
    @pytest.fixture
    def response(self, client):
        """This class is for return response to get page."""
        url = reverse('book-list')
        return client.get(url)

    @pytest.mark.django_db
    def test_book_listing(self, book):
        """This function is for test list book."""
        assert book.title == 'Harry Potter'
        assert book.author == 'JK Rowling'
        assert book.price == '39.99'

    @pytest.mark.django_db
    def test_book_list_view(self, response):
        """This function is for test list view."""
        assert response.status_code == 200
        assertContains(response, "Harry Potter")
        assertTemplateUsed(response, 'books/book_list.html')

    @pytest.mark.django_db
    def test_book_detail_view(self, client):
        """This function is for test detail view."""
        response = client.get(self.book.get_absolute_url())
        no_response =  client.get('/books/12345/')
        assert response.status_code == 200
        assert no_response.status_code == 404
        assertContains(response, "Harry Potter")
        assertContains(response, "hello world")
        assertTemplateUsed(response, 'books/book_detail.html')
        