from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListCreateAPIView):
    """
    Get info
    """

    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Conduct CRUD operations to `books/{id}`
    """

    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
