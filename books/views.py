from django.views.generic import ListView

from . import models


class BookListView(ListView):
    """This class is for list books."""

    model = models.Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
