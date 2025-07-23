from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters in the sidebar
    list_filter = ('author', 'publication_year')

    # Enable search box for these fields
    search_fields = ('title', 'author')