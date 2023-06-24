from django.views.generic import ListView, DetailView

from . import models


class BookListView(ListView):
    """This class is for list books."""

    model = models.Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    """This class is for detail book view."""

    model = models.Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'