from django.contrib import admin
from . import models



class ReviewInLine(admin.TabularInline):
    model = models.Review

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    inlines = [
        ReviewInLine,
    ]
