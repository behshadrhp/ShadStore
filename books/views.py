from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from django.db.models import Q

from . import models


class BookListView(LoginRequiredMixin, ListView):
    """This class is for list books."""

    model = models.Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """This class is for detail book view."""

    model = models.Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
    queryset = models.Book.objects.all().prefetch_related('reviews__author')


class SearchResultsListView(ListView):
    """This class is for return search results."""

    model = models.Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        results = models.Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return results
