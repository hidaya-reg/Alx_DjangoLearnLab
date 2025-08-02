from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Library
from .models import Book
from .models import Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_add_book')
def add_book(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        error = None
        if title and author_id:
            try:
                author = Author.objects.get(id=author_id)
                Book.objects.create(title=title, author=author)
                return redirect('list_books')
            except Author.DoesNotExist:
                error = "Invalid author selected."
        else:
            error = "Please provide both title and author."
        return render(request, 'relationship_app/add_book.html', {'authors': authors, 'error': error})
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    authors = Author.objects.all()
    error = None
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            try:
                author = Author.objects.get(id=author_id)
                book.title = title
                book.author = author
                book.save()
                return redirect('list_books')
            except Author.DoesNotExist:
                error = "Invalid author selected."
        else:
            error = "Please provide both title and author."
        return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors, 'error': error})
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})