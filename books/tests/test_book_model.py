from django.urls import reverse

from books import models

import pytest
from pytest_django.asserts import assertContains, assertTemplateUsed


class BookTest():
    """This class is for test Book model."""

    @pytest.fixture
    def book(self):
        """This function is for create book object."""
        book = models.Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='39.99'
        )
        return book
    
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
        assertTemplateUsed(response, 'books/book_detail.html')
        