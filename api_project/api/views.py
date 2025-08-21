from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing books.

    Authentication:
    - Uses Token Authentication. Clients must send `Authorization: Token <token>` header.
    
    Permissions:
    - Only authenticated users can access.
    - Change `permission_classes` to restrict further (e.g., IsAdminUser).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]